import speech_recognition as sr
from tkinter import *
import tkinter as tk
import threading

"""r = sr.Recognizer()
def speexh():
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print("bir şeyt söle")
        audio = r.listen(mic)
        try:
            
            print(r.recognize_google(audio,language="tr-TR"))
        except Exception as e:
            print("error occured --> ",e)
#sr.Microphone.list_microphone_names()
def speexh_t():
    threading.Thread(target=speexh).start()

window = tk.Tk()
window.geometry("100x100")
button = tk.Button(text="button",command=speexh_t)
button.pack()
window.mainloop()"""


def sesi_anlik_yaziya_cevir():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinleme başladı. Konuşun...")

        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language="tr-TR")
                if text:
                    print(text)
            except sr.UnknownValueError:
                print("ses anlaşılamadı.")
                pass
            except sr.RequestError as e:
                print("İstek başarısız oldu; {0}".format(e))

def thread_speech():
    t = threading.Thread(target=sesi_anlik_yaziya_cevir)
    t.start()
    

thread_speech()