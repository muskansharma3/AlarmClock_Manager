import sys
from tkinter import font, messagebox
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from pygame import mixer
from threading import Thread

# colors used
bgc = '#FFFFFF'
color1 = '#4425e2'
color2 = '#6600fe'
color3 = '#ae00fe'
color4 = '#d800fe'

#### --------------------------- MAIN WINDOW STYLING ------------------------------------------ 

root = Tk()
root.title("Alarm Manager")
root.geometry('370x160+550+200')
root.config(background=bgc)
root.resizable(False,False)

iconImage = PhotoImage(file="C:\\Users\\91958\\Alarm_clock Project\\static\\icon.png")
root.iconphoto(False, iconImage)

# frames
border_line = Frame(root, width=400, height=5, background=color1)
border_line.grid(row=0, column=0)

frame_body = Frame(root, width=400, height=200, background=bgc)
frame_body.grid(row=1, column=0)

# frame body
img = Image.open('static/clock.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

clock_image = Label(frame_body, height=100, image=img, background=bgc)
clock_image.place(x=30, y=20)

title = Label(frame_body, text = "Set Alarm", height=1, font=('serif 20 italic bold'), foreground=color1, background=bgc)
title.place(x=180, y=10)

hour = Label(frame_body, text = "Hour", height=1, font=('Ivy 11 bold'), background=bgc, foreground=color2)
hour.place(x=159, y=46)
set_hour = Combobox(frame_body, width=3, font=('arial 15'), foreground=color3, state='readonly')
set_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
set_hour.current(0)
set_hour.place(x=150, y=70)

minute = Label(frame_body, text = "Minute", height=1, font=('Ivy 11 bold'), background=bgc, foreground=color2)
minute.place(x=210, y=46)
set_min = Combobox(frame_body, width=3, font=('arial 15'), foreground=color3, state='readonly')
set_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
set_min.current(0)
set_min.place(x=210, y=70)


second = Label(frame_body, text = "Second", height=1, font=('Ivy 11 bold'), background=bgc, foreground=color2)
second.place(x=268, y=46)
set_sec = Combobox(frame_body, width=3, font=('arial 15'), foreground=color3, state='readonly')
set_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
set_sec.current(0)
set_sec.place(x=270, y=70)


#### -------------------------------- functionality of Alarm Manager --------------------------------


def activating_alarm():
    t = Thread(target=set_alarm)
    t.start()


def deactivating_alarm():
    mixer.music.stop()
    root.destroy()


choice = IntVar()

activeButton = Radiobutton(frame_body, font=('arial 12 bold'), value=1, text="Activate", background=bgc, command=activating_alarm, variable=choice, foreground=color4)
activeButton.place(x=140, y=110)


def alarm_sound():
    mixer.music.load('static/ringtone.mp3')
    mixer.music.play()
    choice.set(0)

    deactiveButton = Radiobutton(frame_body, font=('arial 12 bold'), value=2, text="Deactivate", background=bgc, command=deactivating_alarm, variable=choice, foreground=color4)
    deactiveButton.place(x=250, y=110)


def set_alarm():
    while True:
        control_command = choice.get()

        hour = set_hour.get()
        minute = set_min.get()
        second = set_sec.get()

        current_time = datetime.now()

        system_hour = current_time.strftime('%H')
        system_minute = current_time.strftime('%M')
        system_second = current_time.strftime('%S')

        if control_command == 1:
            if hour == system_hour:
                if minute == system_minute:
                    if second == system_second:
                        alarm_sound()
                        messagebox.showinfo("Alarm!", "Hello! Your alarm is ringing. Don’t forget to turn it off.")
                        break
        sleep(1)


mixer.init()

root.mainloop()