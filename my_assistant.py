import google.generativeai as genai
import os
from tkinter import *
import re
import pyttsx3
import customtkinter as ct
import speech_recognition as sr
from dotenv import load_dotenv

home = ct.CTk()
home.title("myAssistant")
home.geometry("600x500")
ct.set_appearance_mode("dark")
icon = PhotoImage(file = r"C:\Users\andre\Downloads\technical-support_9733214.png")
home.iconphoto(True,icon)

load_dotenv()

api_key = os.getenv("API_KEY")

engine = pyttsx3.init()
ai = genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def speak():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...")
        audio = rec.listen(source)
        
        speech = rec.recognize_google(audio)

        response = model.generate_content(speech)
        clean_response = re.sub(r'\*+', '', response.text)
        entry.delete(0,END)
        entry.insert(0,clean_response)
        
        engine.say(clean_response)
        engine.runAndWait()
        engine.stop()

btn = ct.CTkButton(home, text="click to speak", width = 40, command = speak)
btn.pack(pady = 20)

entry = ct.CTkTextbox(home, width = 500)
entry.pack(pady= 20)

home.mainloop()
