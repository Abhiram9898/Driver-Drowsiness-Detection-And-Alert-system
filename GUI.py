import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer

class DrowsinessApp:+
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Drowsiness Detection")

        self.model = load_model('F:\Driver Drowsiness Detection\models\cnnCat2.h5')
        self.path = os.getcwd()
        self.cap = cv2.VideoCapture(0)
        self.font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.count = 0
        self.score = 0
        self.thicc = 2
        self.rpred = [99]
        self.lpred = [99]

        # Initialize mixer
        mixer.init() 

        # Initialize face, leye, and reye attributes
        self.face = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_frontalface_alt.xml')
        self.leye = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_lefteye_2splits.xml')
        self.reye = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_righteye_2splits.xml')

        # Check if mixer is initialized before creating Sound object
        if mixer.get_init():
            self.sound = mixer.Sound('alarm.wav')
        else:
            print("Error: Mixer not initialized")

        self.create_widgets()

    def create_widgets(self):
        self.video_panel = tk.Label(self.root)
        self.video_panel.pack(padx=10, pady=10)

        self.start_button = ttk.Button(self.root, text="Start Detection", command=self.start_detection)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop Detection", command=self.stop_detection)
        self.stop_button.pack(pady=5)

        self.status_label = ttk.Label(self.root, text="Status: Waiting for Start")
        self.status_label.pack(pady=5)

        self.update_frame()

    def start_detection(self):
        self.status_label.config(text="Status: Detection Started")
        self.count = 0
        self.score = 0
        self.thicc = 2
        self.rpred = [99]
        self.lpred = [99]

    def stop_detection(self):
        self.status_label.config(text="Status: Detection Stopped")
        self.cap.release()
        self.root.destroy()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            height, width = frame.shape[:2]
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
            left_eye = self.leye.detectMultiScale(gray)
            right_eye = self.reye.detectMultiScale(gray)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)

            for (x, y, w, h) in right_eye:
                r_eye = frame[y:y + h, x:x + w]
                self.count += 1
                r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye, (24, 24))
                r_eye = r_eye / 255
                r_eye = r_eye.reshape(24, 24, -1)
                r_eye = np.expand_dims(r_eye, axis=0)
                self.rpred = np.argmax(self.model.predict(r_eye), axis=1)
                if self.rpred[0] == 1:
                    lbl = 'Open'
                if self.rpred[0] == 0:
                    lbl = 'Closed'
                break

            for (x, y, w, h) in left_eye:
                l_eye = frame[y:y + h, x:x + w]
                self.count += 1
                l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
                l_eye = cv2.resize(l_eye, (24, 24))
                l_eye = l_eye / 255
                l_eye = l_eye.reshape(24, 24, -1)
                l_eye = np.expand_dims(l_eye, axis=0)
                self.lpred = np.argmax(self.model.predict(l_eye), axis=1)
                if self.lpred[0] == 1:
                    lbl = 'Open'
                if self.lpred[0] == 0:
                    lbl = 'Closed'
                break

            if self.rpred[0] == 0 and self.lpred[0] == 0:
                self.score += 1
                cv2.putText(frame, "Closed", (10, height - 20), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            else:
                self.score -= 1
                cv2.putText(frame, "Open", (10, height - 20), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)

            if self.score < 0:
                self.score = 0
            cv2.putText(frame, 'Score:' + str(self.score), (100, height - 20), self.font, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            if self.score > 15:
                cv2.imwrite(os.path.join(self.path, 'image.jpg'), frame)
                try:
                    self.sound.play()
                except:
                    pass
                if self.thicc < 16:
                    self.thicc = self.thicc + 2
                else:
                    self.thicc = self.thicc - 2
                    if self.thicc < 2:
                        self.thicc = 2
                cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), self.thicc)

            # Convert the frame to RGB format for displaying in Tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_panel.imgtk = imgtk
            self.video_panel.config(image=imgtk)

        # Repeat the update after 10 milliseconds
        self.root.after(10, self.update_frame)

    def run(self):
        self.face = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_frontalface_alt.xml')
        self.leye = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_lefteye_2splits.xml')
        self.reye = cv2.CascadeClassifier('F:\Driver Drowsiness Detection\haar cascade files\haarcascade_righteye_2splits.xml')
        self.sound = mixer.Sound('alarm.wav')

        self.root.mainloop()
        # Release the camera when the Tkinter window is closed
        self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrowsinessApp(root)
    app.run()
