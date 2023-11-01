import tkinter as tk
import subprocess
import speech_recognition as sr
from tkinter import PhotoImage

# Initialize the Speech recognizer
recognizer = sr.Recognizer()

# Mapping Inputs to application paths
app_mapping = {
    "open chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "open vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
    "open git" : r"C:\Program Files\Git\git-bash.exe",
    "open vs code" : r"C:\Users\Dr. Shraddha Garg\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

# Function to recognize and execute voice command
def recognize_and_execute_voice():
    with sr.Microphone() as source:
        print("Listening for a voice command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized voice command: {command}")

            if command in app_mapping:
                app_path = app_mapping[command]
                subprocess.Popen(app_path)
                print(f"Opening {app_path}")
            else:
                print("Voice command not recognized.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your voice command.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

# Function to execute text command
def execute_text_command():
    text_command = text_input.get().lower()
    if text_command in app_mapping:
        app_path = app_mapping[text_command]
        subprocess.Popen(app_path)
        feedback_label.config(text=f"Opening {app_path}")
    else:
        feedback_label.config(text="Text command not recognized.")

# Create the main window
window = tk.Tk()
window.title("Creative Problem Solving - Assingment Ajay Garg --> 03")
window.geometry("800x400")

bg_image = PhotoImage(file=r"C:\Users\Dr. Shraddha Garg\Desktop\bg.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create and place GUI components
label = tk.Label(window, text="Enter a text command:", font=("Times New Roman", 16), fg="black", bg="white")
label.pack(pady=20)
label.pack(pady=10)

text_input = tk.Entry(window, font=("Times New Roman", 12))
text_input.pack()

buttons_frame = tk.Frame(window)
buttons_frame.pack(pady=20)

text_button = tk.Button(buttons_frame, text="Submit Text Command", font=("Times New Roman", 14, "bold"), command=execute_text_command)
text_button.pack(side="left")

voice_button = tk.Button(buttons_frame, text="Voice Command", font=("Times New Roman", 14, "bold" , "italic"), command=recognize_and_execute_voice)
voice_button.pack(side="left")

feedback_label = tk.Label(window, text="", font=("Times New Roman", 14), fg="green", bg="white")
feedback_label.pack()

# Start the GUI main loop
window.mainloop()
