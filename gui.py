# final project for CS50
# Author: Jerome Schmutz
# start Date: 30/12/2023


import tkinter as tk
from tkinter import ttk

from weatherApi import get_data



def start_gui():
    # window
    window = tk.Tk()
    window.title("Kitesurfing forecast APP")
    window.geometry("1000x500")

    paint_search_bar(window)

    # run
    window.mainloop()



def retrieve_data(loc, fore):
    data = get_data(loc)
    fore.set(data)


def paint_search_bar(wd):
    
    loc_label = ttk.Label(master=wd, text="Location: ", font="Calibri 24 bold")
    loc_label.pack()

    forecast = tk.StringVar()

    loc_input_frame = ttk.Frame(master=wd)
    location = tk.StringVar()
    loc_input_txt = ttk.Entry(master=loc_input_frame, textvariable=location)
    loc_button_search = ttk.Button(master=loc_input_frame, text="Search", command=lambda: retrieve_data(location.get(), forecast))
    loc_input_txt.pack(side="left", padx=10)
    loc_button_search.pack(side="left")
    loc_input_frame.pack(pady=10)

    #forecast = tk.StringVar()
    loc_output_txt = ttk.Label(
        master=wd,
        text="forecast",
        font="Calibri 20",
        textvariable=forecast)
    loc_output_txt.pack(pady = 5)

