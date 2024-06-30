from tkinter import *
from tkcalendar import *

root = Tk()
root.title("calender")
root.geometry("500x500")

calendar = Calendar(root, setmode="day")
calendar.pack(pady=20)

def add_event():
    event = Label(root, text=calendar.get_date())
    event.pack()

add_event_button = Button(root, text="add event", command=add_event)
add_event_button.pack(pady=20)


root.mainloop()