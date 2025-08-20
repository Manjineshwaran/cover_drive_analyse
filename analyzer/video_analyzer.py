import cv2
import mediapipe as mp
import os
from utils.math_utils import angle
from .drawing import draw_landmarks, put_metrics, put_checks
from .scoring import compute_scores
from .data_logger import save_evaluation, save_frame_data
from recommendation_ai_agent.agent import get_recomendation

mp_pose = mp.solutions.pose

def analyze_video(path, out_dir="output"):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w, h = int(cap.get(3)), int(cap.get(4))

    out = cv2.VideoWriter(f"{out_dir}/annotated_video.mp4",
                          cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    metrics_log, checks_log, all_frame_values = [], [], []

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = pose.process(rgb)

            if res.pose_landmarks:
                lm = res.pose_landmarks.landmark
                h_, w_ = frame.shape[:2]

                def pt(idx): return (lm[idx].x * w_, lm[idx].y * h_)
                L_sh, L_el, L_wr = pt(11), pt(13), pt(15)
                R_sh, R_el, R_wr = pt(12), pt(14), pt(16)
                L_hip, R_hip = pt(23), pt(24)
                L_knee, R_knee = pt(25), pt(26)
                L_heel, R_heel = pt(29), pt(30)
                L_toe, R_toe = pt(31), pt(32)
                nose = pt(0)

                elbow_angle = angle(L_sh, L_el, L_wr)
                hip_mid = ((L_hip[0] + R_hip[0]) / 2, (L_hip[1] + R_hip[1]) / 2)
                shoulder_mid = ((L_sh[0] + R_sh[0]) / 2, (L_sh[1] + R_sh[1]) / 2)
                vertical_ref = (hip_mid[0], hip_mid[1] - 100)
                spine_angle = angle(vertical_ref, hip_mid, shoulder_mid)
                head_knee_dist = abs(nose[0] - L_knee[0])
                foot_angle = angle((L_heel[0] - 100, L_heel[1]), L_heel, L_toe)

                metrics_log.append([elbow_angle, spine_angle, head_knee_dist, foot_angle])
                frame_idx = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                checks = {"foot_ok": (60 < foot_angle < 120)}

                if frame_idx < fps * 3:
                    checks["head_ok"] = (head_knee_dist < 50)
                    checks["balance_ok"] = (abs(spine_angle) < 20)
                    checks["elbow_ok"] = (100 < elbow_angle < 140)

                checks_log.append(checks)

                frame_data = {
                    "frame_idx": frame_idx,
                    "metrics": [{"elbow_angle:":elbow_angle}, {"spine_angle:":spine_angle}, {"head_knee_dist:":head_knee_dist}, {"foot_angle:":foot_angle}],
                    "checks": {k: str(v) for k, v in checks.items()},
                    # "landmarks": {i: (lm[i].x, lm[i].y, lm[i].z) for i in range(len(lm))}
                }
                all_frame_values.append(frame_data)

                draw_landmarks(frame, res)
                put_metrics(frame, elbow_angle, spine_angle, head_knee_dist, foot_angle)
                if frame_idx < fps * 3:
                    put_checks(frame, checks)

                # cv2.imshow("frame", frame)
                out.write(frame)

                # key = cv2.waitKey(1) & 0xFF
                # if key == ord('q'):
                #     break
                # elif key == ord('p'):
                #     while cv2.waitKey(1) != ord('p'):
                #         pass

    cap.release()
    out.release()

    if metrics_log:
        scores, feedback = compute_scores(metrics_log, checks_log)
        result = {"scores": scores, "feedback": feedback}
        save_evaluation(scores, feedback, out_dir)
    save_frame_data(all_frame_values, out_dir)
    print("Done. Outputs saved in /output/")
    get_recomendation(result,all_frame_values)
