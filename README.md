
---

# Gesture-Based Presentation Controller  

## Description  
An innovative project designed to make presentations seamless and hands-free using hand gestures. This application leverages computer vision and gesture recognition technology to navigate slides, zoom in/out, and control the slideshow.

---

## Features  
- **Navigate Left/Right**: Use hand gestures to move between slides.  
- **Zoom In/Out**: Control zoom using two-finger gestures.  
- **Start/Stop Presentation**: Start or exit the slideshow with a thumbs-up gesture.  
- **Integrated Camera Feed**: Displays a real-time camera feed for use during presentations.  

---

## Technologies Used  
- **Python**: Programming language.  
- **OpenCV**: For computer vision.  
- **Mediapipe**: For gesture recognition.  
- **PyAutoGUI**: To control keyboard actions programmatically.  

---

## How It Works  
1. **Gesture Detection**: The system detects hand gestures using Mediapipe.  
2. **Action Mapping**: Each gesture is mapped to a specific keyboard action.  
3. **Real-Time Camera Feed**: Displays a live video feed to provide visual feedback during operation.  

---

## Setup and Installation  

1. Clone the repository and navigate to the folder.  
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the application:  
   ```bash
   python main.py
   ```  

---

## Gesture Controls  

| Gesture                  | Action                            |
|--------------------------|-----------------------------------|
| Index Finger (Right Hand)| Next Slide                       |
| Index Finger (Left Hand) | Previous Slide                   |
| Thumb Up                 | Start/Stop Presentation          |
| Two Fingers (Right Hand) | Zoom In                          |
| Two Fingers (Left Hand)  | Zoom Out                         |
| Swipe Right (Right Hand) | Navigate to the Right            |
| Swipe Left (Left Hand)   | Navigate to the Left             |

---

## Example Usage  

1. **Start the script**: Run `main.py`.  
2. **Switch to your presentation**: Ensure your presentation is ready in slideshow mode.  
3. **Use gestures**: Control the slideshow as per the mapped gestures described above.  

---

## Dependencies  

The project requires the following Python libraries:  
- `mediapipe==0.10.0`  
- `opencv-python==4.8.0`  
- `pyautogui==0.9.53`  

Install them using:  
```bash
pip install mediapipe opencv-python pyautogui
```  

---

## License  

This project is licensed under the MIT License.  

---
