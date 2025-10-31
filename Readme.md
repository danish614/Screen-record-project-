# Screen Recorder in Python

##  Overview
This project is a simple yet efficient **screen recorder** built with Python using the `mss`, `cv2`, and `numpy` libraries.  
It captures the entire screen and saves it as a `.avi` video file at a defined frame rate (default: 20 FPS).  
A live preview window is available, and recording can be stopped by pressing **Q**.


## ⚙️ Features
- Records full-screen display in real-time  
- Adjustable FPS, codec, and output path  
- Live preview option during recording  
- Keyboard interrupt support (`Q` to stop)  
- Displays total frames, duration, and average FPS after saving  

---

##  Requirements
Install the required dependencies before running:
```bash
pip install mss opencv-python numpy
