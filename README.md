# MANDATORY :

Go Throught the AkashaShuddhi.pptx in the folder to get detailed insight on project (tool).

# 🛰️ Avshesha Anveshanam using OpenCV

This project is a real-time computer vision system that detects and categorizes space debris in video footage using **OpenCV** and **Python**.

---

## 🚀 Overview

The system processes a video feed (e.g., from satellites or simulations) to:
- Detect space debris against a dark background.
- Track debris persistently across frames.
- Categorize debris as **Small**, **Medium**, or **Large** based on contour area.
- Display a **unique count** of each size category without fluctuation.
- Show bounding boxes with object IDs.

---

## 🎯 Features

✅ Real-time object detection  
✅ Debris size classification  
✅ Persistent tracking using Euclidean distance  
✅ Stable counting logic (no repeated counts)  
✅ Watermark and FPS overlay  
✅ Final counts printed to terminal when exited  

---

## 🛠️ Installation & Running the Script

### 1. Clone the Repository
```bash
git clone https://github.com/adityatiwari-dev/space-debris-detection.git
cd space-debris-detection
2. Install Dependencies
Make sure you have Python 3.7+ installed. Then run:

bash
Copy
Edit
pip install opencv-python numpy
3. Run the Script
Ensure your video file is named debris.mp4 and placed in the same directory. Then start detection with:

bash
Copy
Edit
python debris_detector.py
Press ESC to stop the video and view final debris counts in the terminal.