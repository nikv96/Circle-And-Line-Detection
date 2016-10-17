# Circle-And-Line-Detection
Python script to detect lines and circles in an image using Hough Transform algorithms in a video capture. 

This script makes use of OpenCV python. The code is compatible with both OpenCV 2 and 3 versions.

# Dependencies
1. Install [python 2.7](https://www.python.org/downloads/) and add it to your system path.
  1. On Windows systems, open up Advanced System Settings, edit your Path variable and append ```C:\Python27\Scripts``` at the end.
  
2. Install OpenCV python on your system.
  1. For Windows:
    1. Download a precompiled version of [OpenCV](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.1.0/opencv-3.1.0.exe/download).
    2. Install by double clicking the executable file.
    3. Now, copy the cv2.pyd file at opencv\build\python\2.7\cv2.pyd to C:\python27\Scripts\site-packages.
  2. For MacOS:
    1. Install [homebrew](http://brew.sh).
    2. Install opencv with ```brew install opencv3```
  3. For Ubuntu, install with ```sudo apt-get install python-numpy python-opencv```. This should install a stable version of OpenCV-Python 2.4.9. 
  
3. Test the installation by opening a terminal. Type in ```python```. 
  1. In the prompt type, ```import cv2``` and then ```cv2.__version__```.
  
# Run
1. Run ```python LineAndCircleDetection.py```

# Contributors
[Nikhil Venkatesh](https://github.com/nikv96)
