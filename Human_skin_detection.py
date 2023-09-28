import cv2
import numpy as np
import tkinter as tki
from PIL import Image, ImageTk

def skin_detection(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a binary mask where skin pixels are white and others are black
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Bitwise-AND the mask with the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result

def update_frame():
    ret, frame = cap.read()
    if ret:
        skin_frame = skin_detection(frame)
        photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(skin_frame, cv2.COLOR_BGR2RGB)))
        panel.config(image=photo)
        panel.photo = photo
        panel.after(10, update_frame)

def close():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()  # Close the tkinter window

cap = cv2.VideoCapture(0)

root = tki.Tk()
root.title("ICT 4362: Artificial Intelligence Lab: Human Skin Detection")

panel = tki.Label(root)
panel.pack(padx=10, pady=10)

update_frame()

# Create a "Close" button
close_button = tki.Button(root, text="Close", command=close)
close_button.pack(pady=10)

root.mainloop()
