import streamlit as st
import os
import shutil
from pathlib import Path
from analyzer.video_analyzer import analyze_video

# Set page config
st.set_page_config(page_title="Batting Analysis App", layout="wide")

def main():
    st.title("🏏 Batting Technique Analysis")
    
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a batting video", type=["mp4", "mov", "avi"])
    
    if uploaded_file is not None:
        # Save the uploaded file
        input_path = output_dir / "input_video.mp4"
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the video
        with st.spinner("Analyzing your video..."):
            analyze_video(str(input_path))
        
        st.success("Analysis complete!")
        
       # Display the processed video
        st.subheader("Processed Video")
        output_video = output_dir / "annotated_video.mp4"

        if output_video.exists():
            # Show video
            # st.video(str(output_video))   # use path, not raw bytes

            # Add download button
            with open(output_video, "rb") as f:
                st.download_button(
                    label="⬇️ Download Processed Video",
                    data=f,
                    file_name="annotated_video.mp4",
                    mime="video/mp4"
                )


        
        # Create download buttons for JSON files
        st.subheader("Analysis Results")
        
        col1, col2 = st.columns(2)
        
        
        import json
        import pandas as pd

        # Evaluation JSON
        eval_file = output_dir / "evaluation.json"
        if eval_file.exists():
            with open(eval_file, 'r') as f:
                eval_data = json.load(f)

            st.subheader("📊 Evaluation Scores")
            scores_df = pd.DataFrame(list(eval_data["scores"].items()), columns=["Metric", "Score"])
            st.table(scores_df)

            st.subheader("💡 Feedback")
            for metric, fb in eval_data["feedback"].items():
                st.markdown(f"**{metric}:** {fb}")

            col1.download_button(
                label="⬇️ Download Evaluation",
                data=json.dumps(eval_data, indent=2),
                file_name="evaluation.json",
                mime="application/json"
            )

        # Recommendation JSON
        rec_file = output_dir / "recomendation.json"
        if rec_file.exists():
            with open(rec_file, 'r') as f:
                rec_data = json.load(f)

            st.subheader("📝 Recommendations")
            st.markdown(rec_data["recommendation"])  # already nicely formatted markdown

            col2.download_button(
                label="⬇️ Download Recommendations",
                data=json.dumps(rec_data, indent=2),
                file_name="recomendation.json",
                mime="application/json"
            )


    # Add some instructions
    st.sidebar.markdown("""
    ### How to use:
    1. Upload a video of a batting shot
    2. Wait for the analysis to complete
    3. View the processed video with analysis
    4. Download the evaluation and recommendations
    """)

if __name__ == "__main__":
    main()
