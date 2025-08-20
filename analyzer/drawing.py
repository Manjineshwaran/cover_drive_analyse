import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def draw_landmarks(frame, res):
    mp_drawing.draw_landmarks(frame, res.pose_landmarks, mp_pose.POSE_CONNECTIONS)

def put_metrics(frame, elbow_angle, spine_angle, head_knee_dist, foot_angle):
    cv2.putText(frame, f"Elbow: {int(elbow_angle)} degree", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
    cv2.putText(frame, f"Spine Lean: {int(spine_angle)} degree", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
    cv2.putText(frame, f"Head-Knee Xdist: {int(head_knee_dist)}px", (10,90), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
    cv2.putText(frame, f"Foot Dir: {int(foot_angle)} degree", (10,120), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)

def put_checks(frame, checks):
    cv2.putText(frame, f"Head Pos: {'OK' if checks['head_ok'] else 'Wrong'}", (10,170),
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0) if checks['head_ok'] else (0,0,255),2)
    cv2.putText(frame, f"Balance: {'OK' if checks['balance_ok'] else 'Off'}", (10,200),
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0) if checks['balance_ok'] else (0,0,255),2)
    cv2.putText(frame, f"Elbow: {'OK' if checks['elbow_ok'] else 'Wrong'}", (10,230),
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0) if checks['elbow_ok'] else (0,0,255),2)
