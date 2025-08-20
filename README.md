# Cricket Cover Drive Analysis

![Cover Drive Analysis](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.9.0%2B-FF6B6B)

A computer vision application that analyzes cricket cover drive technique using pose estimation and provides detailed feedback on the player's form.
mediapi
![Alt text](pose_tracking_full_body_landmarks.png)

## Run the file

-- streamlit run streamlit_app.py
-- or
-- python main.py
## 🎯 Features

- **Pose Detection**: Uses MediaPipe for accurate human pose estimation
- **Technique Analysis**: Evaluates key aspects of the cover drive technique
- **Real-time Feedback**: Provides immediate visual and metric feedback
- **Detailed Reports**: Generates comprehensive analysis reports
- **Configurable**: Easily adjustable parameters for different analysis needs

## 📋 Prerequisites

- Python 3.8+
- OpenCV
- MediaPipe
- NumPy

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AthleteRise_CoverDrive_Analysis.git
   cd AthleteRise_CoverDrive_Analysis
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Usage

1. Place your input video file in the `input` directory
2. Update the `config.py` file with your video filename and desired settings
3. Run the analysis:
   ```bash
   python main.py
   ```
4. View the output in the `output` directory

## 📊 Workflow

1. **Video Input**: The system reads the input video file
2. **Pose Estimation**: MediaPipe processes each frame to detect body landmarks
3. **Metric Calculation**: Key metrics are calculated for each frame:
   - Elbow angle
   - Spine lean
   - Head-knee distance
   - Foot angle
4. **Analysis**: The system evaluates the metrics against ideal values
5. **Visualization**: Results are overlaid on the video
6. **Reporting**: A detailed report is generated with scores and feedback


## ⚙️ Configuration

Modify `config.py` to adjust:
- Input/output file paths
- Pose detection parameters
- Metric thresholds
- Visualization styles
- Logging preferences

## 📈 Sample Output

```
=== Analysis Results ===
Overall Score: 85.0/100

=== Detailed Metrics ===
Elbow Angle: 92.5° (Ideal: 90.0°, Score: 95/100)
Spine Lean: 12.3° (Ideal: 10.0°, Score: 88/100)
Head-Knee Distance: 0.45 (Ideal: 0.5, Score: 90/100)
Foot Angle: 25.0° (Ideal: 30.0°, Score: 83/100)

=== Feedback ===
- Excellent technique! Your cover drive is well-executed with great form.
- Try to maintain a slightly more upright spine position.
- Your foot alignment is good, but could be slightly more open.
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- MediaPipe for the excellent pose estimation model
- OpenCV for computer vision capabilities
- All contributors who helped improve this project
#

