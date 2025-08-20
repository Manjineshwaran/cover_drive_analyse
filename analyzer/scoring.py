import numpy as np

def compute_scores(metrics_log, checks_log):
    total_frames = len(metrics_log)
    scores, feedback = {}, {}

    foot_ok = sum(1 for c in checks_log if "foot_ok" in c and c["foot_ok"])
    scores["Footwork"] = int((foot_ok / total_frames) * 10)
    feedback["Footwork"] = f"Footwork OK in {foot_ok}/{total_frames} frames."

    head_checks = [c["head_ok"] for c in checks_log if "head_ok" in c]
    if head_checks:
        head_ok = sum(head_checks)
        scores["Head Position"] = int((head_ok / len(head_checks)) * 10)
        feedback["Head Position"] = f"Head aligned in {head_ok}/{len(head_checks)} frames (first 3s)."

    elbow_checks = [c["elbow_ok"] for c in checks_log if "elbow_ok" in c]
    if elbow_checks:
        elbow_ok = sum(elbow_checks)
        scores["Swing Control"] = int((elbow_ok / len(elbow_checks)) * 10)
        feedback["Swing Control"] = f"Elbow correct in {elbow_ok}/{len(elbow_checks)} frames (first 3s)."

    balance_checks = [c["balance_ok"] for c in checks_log if "balance_ok" in c]
    if balance_checks:
        balance_ok = sum(balance_checks)
        scores["Balance"] = int((balance_ok / len(balance_checks)) * 10)
        feedback["Balance"] = f"Balanced in {balance_ok}/{len(balance_checks)} frames (first 3s)."

    elbow_vals = np.array(metrics_log)[:,0]
    last_n = max(5, int(total_frames * 0.1))
    follow_ok = np.sum(elbow_vals[-last_n:] > 130)
    scores["Follow-through"] = int((follow_ok / last_n) * 10)
    feedback["Follow-through"] = f"Good follow-through in {follow_ok}/{last_n} end frames."

    return scores, feedback
