import json
import os

def save_evaluation(scores, feedback, out_dir):
    result = {"scores": scores, "feedback": feedback}
    with open(f"{out_dir}/evaluation.json", "w") as f:
        json.dump(result, f, indent=2)

def save_frame_data(all_frame_values, out_dir):
    with open(f"{out_dir}/all_frame_values.json", "w") as f:
        json.dump(all_frame_values, f, indent=2)
