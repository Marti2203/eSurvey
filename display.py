#!/bin/python3
#import the library
from tkinter import *
import requests
from PIL import ImageTk,Image  
from translation_data import TranslationService
from scanner import BarcodeScanner
from speaker import Speaker
from config import *

translator = TranslationService()
get_translated_field = translator.get_translated_field
change_lang = translator.change_lang

facility_id = "1"

buttons = []

# Create an instance of window - fullscreen to hide the desktop
win=Tk()
win.attributes("-fullscreen", True)
win.configure(bg='#ffffff')

scanner = BarcodeScanner(win)
scanner.start()

# Setup question state
current_q = 0
q_text = StringVar()
q_text.set(get_translated_field("welcome"))

mute = BooleanVar()
mute.set(False)

# Setup language state
language = StringVar(win,get_translated_field('display'))

# Setup button state
back_button_text = StringVar(win,get_translated_field('back'))
quit_button_text = StringVar(win,get_translated_field('quit'))

mute_text = StringVar()
mute_text.set(get_translated_field('unmuted'))

succ_text = StringVar()

survey_data = {"facility_id": facility_id}
def on_base_survey_success():
    q_text.set(get_translated_field("extra_help"))
    Speaker(get_translated_field("questions_voice")[-1]).start()

    global buttons
    for button in buttons:
        button.destroy()
    button_yes = Button(text = "✓",bg="#00ff00",font=emoji_font,command = lambda: extra_help_button_pressed(True))
    button_yes.place(relx=0.6,rely=0.4,anchor = CENTER)
    button_no = Button(text ="x",bg="#ff0000",font=emoji_font,command = lambda: extra_help_button_pressed(False))
    button_no.place(relx=0.4,rely=0.4,anchor = CENTER)
    buttons = [
             button_yes,
             button_no
            ]

def extra_help_button_pressed(result):
    survey_data['extra_information'] = result
    q_text.set("")
    succ_text.set(get_translated_field("success_survey"))
    print(survey_data)
    #requests.post("http://192.168.63.75:5000/",data=survey_data)
    global buttons
    for button in buttons:
        button.destroy()
    buttons = []

def add_rating(question,value):
    survey_data[question] = value
    print(f"{question} -> {value}")

def present_next_question():
    if not mute.get():
        Speaker(get_translated_field('questions_voice')[current_q]).start()
    q_text.set( get_translated_field('questions')[current_q])

def rating_button_pressed(v):
    global current_q
    add_rating(current_q,v)
    current_q =  (current_q + 1)

    if current_q == len( get_translated_field('questions') ):
        on_base_survey_success()
        current_q = 0
    else:
        present_next_question()

    if current_q == 0:
        back_button['state']=DISABLED
    else:
        back_button['state']=NORMAL
    win.focus()


def language_button_pressed():
    change_lang()
    language.set(get_translated_field('display'))
    if q_text.get() != "":
        q_text.set(get_translated_field('questions')[current_q])
    
    if succ_text.get() != "":
        succ_text.set(get_translated_field('success_survey')[current_q])

    back_button_text.set(get_translated_field('back'))
    quit_button_text.set(get_translated_field('quit'))


def back_button_pressed():
    global current_q
    current_q =  max(0,(current_q - 1)) % len( get_translated_field('questions'))
    q_text.set(get_translated_field('questions')[current_q])
    if current_q == 0:
        back_button['state']=DISABLED
    else:
        back_button['state']=NORMAL

def start(*args):
    global survey_data
    survey_data["id"]= scanner.get_patient_id()
    succ_text.set("")
    mute.set(False)
    # Render buttons
    
    present_next_question()
    
    for grading in range(gradings):
        text = str(grading)
        but = Button(win, text=emojis[grading],font=emoji_font, command = (lambda t: (lambda : rating_button_pressed(t)))(text), height=2,width=5,bg=color_gradient[grading])
        but.place(relx = 0.15 + 0.9 / gradings * (grading), rely=0.6, anchor=CENTER)
        buttons.append(but)

# Create exit button
#quit_button=Button(win, textvariable=quit_button_text, font=font,command=win.destroy)
#quit_button.place(relx=0.8, rely=0.8, anchor=CENTER)

# Create back button
back_button=Button(win, textvariable=back_button_text, font=font, command=back_button_pressed)
back_button.place(relx=0.6,rely=0.2,anchor=CENTER)
back_button['state']=DISABLED

language_button = Button(win, textvariable=language,font=font, command = language_button_pressed)
language_button.place(relx=0.8, rely=0.2, anchor=CENTER)

# Create question label
q_label=Label(win, textvariable=q_text, font=font,bg='#ffffff')
q_label.place(relx=0.5, rely=0.3, anchor=CENTER)

succ_label=Label(win, textvariable=succ_text, font=font,bg='#ffffff')
succ_label.place(relx=0.5, rely=0.4, anchor=CENTER)

def mute_button_pressed():
    mute.set(not mute.get())
    mute_text.set(get_translated_field('muted' if mute.get() else 'unmuted'))

mute_button = Button(win, textvariable = mute_text,command = mute_button_pressed,bg='#ffffff')
mute_button.place(relx=0.2,rely=0.2,anchor=CENTER)

img = PhotoImage(file="cordaid-logo.png") 
img_label = Label(win,image=img)
img_label.place(relx=0.15,rely=0.9,anchor=CENTER)

win.bind("<<start_logic>>",start)
win.mainloop()
