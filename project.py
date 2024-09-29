# final project for CS50 Python
# Author: Jerome Schmutz


import tkinter as tk
from tkinter import Image, ttk
from PIL import ImageTk,Image
from datetime import datetime
import calendar

from weatherApi import get_week_data, get_day_data, get_list_location

color_scale = ["medium blue", "DeepSkyBlue3", "SeaGreen1", "green2", "green4", "chartreuse4", "VioletRed4", "magenta4"]

def main():
   
    my_app = App_gui()
    my_app.mainloop()



def get_kiteometer(wd):
    wd=18 if wd >= 18.4 else wd
    return color_scale[int(wd / 2.3)]

def convert_wind(wd, metric):
    if metric == "m/s":
        return round(float(wd), 2)
    elif metric == "ft/s":
        return round(float(wd) * 3.28084, 2)
    elif metric == "knt":
        return round(float(wd) * 1.94384, 2)
    elif metric == "mph":
        return round(float(wd) * 2.23694, 2)

def convert_temp(tp, metric):
    if metric == 'F':
        return round((float(tp) * 9 / 5) + 32, 1)
    else:
        return tp
        

class App_gui(tk.Tk):
    def __init__(self):
        super().__init__()

        # MAIN WINDOW SETUP
        self.title("Kitesurfing forecast APP")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 1250
        window_height = 750
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
        self.minsize(window_width, window_height)
        self.pack_propagate(False)

        icon = tk.PhotoImage(file="icons/icon-32.png")
        self.iconphoto(True, icon)

        self.configure(bg='#E7E8D8')
        style = ttk.Style()
        style.configure('TFrame', background='#CADABF')

        # CREATE LAYOUT
        style.configure('menu.TFrame', background='#E7E8D8')
        self.menu = Menu(self)
        style.configure('topbar.TFrame', background='#E7E8D8')
        self.topbar = Topbar(self)
        style.configure('main.TFrame', background='#E7E8D8')
        self.mainscreen = Mainscreen(self)
        
        # data
        self.refresh_screen_data()

    def refresh_screen_data(self):
        if not self.mainscreen.location_selected:
            return
        self.mainscreen.title_week['text'] = f"Daily forecast for {self.mainscreen.location_to_display}"
        for i in range(7):
            self.mainscreen.tab_days[i].title_day['text'] = self.mainscreen.array_data_days[i]["day"]
            self.mainscreen.tab_days[i].summary_day['text'] = self.mainscreen.array_data_days[i]["summary"]
            self.mainscreen.tab_days[i].icon_img = tk.PhotoImage(file=f"icons/{self.mainscreen.array_data_days[i]['icon']}.png").zoom(1)
            self.mainscreen.tab_days[i].canvas_icon.create_image(25,25, anchor=tk.CENTER, image=self.mainscreen.tab_days[i].icon_img)
            self.mainscreen.tab_days[i].icon_day['text'] = f" "
            
            temp = convert_temp(self.mainscreen.array_data_days[i]['temp'], self.menu.temp_metrics.get())
            self.mainscreen.tab_days[i].temperature_day['text'] = f"{temp} {chr(176)}{self.menu.temp_metrics.get()}"
            temp_max = convert_temp(self.mainscreen.array_data_days[i]['temp_max'], self.menu.temp_metrics.get())
            self.mainscreen.tab_days[i].temperature_max['text'] = f"Max. {temp_max} {chr(176)}{self.menu.temp_metrics.get()}"
            temp_min = convert_temp(self.mainscreen.array_data_days[i]['temp_min'], self.menu.temp_metrics.get())
            self.mainscreen.tab_days[i].temperature_min['text'] = f"Min. {temp_min} {chr(176)}{self.menu.temp_metrics.get()}"

            wind = convert_wind(self.mainscreen.array_data_days[i]["wind"], self.menu.wind_metrics.get())
            self.mainscreen.tab_days[i].wind_day['text'] = f"Wind {wind} {self.menu.wind_metrics.get()}"
            self.mainscreen.tab_days[i].rain_day['text'] = f"Rain {self.mainscreen.array_data_days[i]['rain']} mm/h"

           
        self.mainscreen.title_day['text'] = f"Forecast for next 24 hours"
        self.mainscreen.row_temp_label['text'] = f"Temp.  ({chr(176)}{self.menu.temp_metrics.get()})"
        self.mainscreen.row_windspeed_label['text'] = f"Wind speed  ({self.menu.wind_metrics.get()})"

        self.wind_dir_img = []
        for i in range(24):
            temp = f"{convert_temp(self.mainscreen.array_data_hours[i]['temp'], self.menu.temp_metrics.get())}"
            self.mainscreen.cell_hourly_label = ttk.Label(master=self.mainscreen.grid_day, text=temp, justify="center", anchor="center", borderwidth=10, relief="groove", background='#B5CFB7')
            self.mainscreen.cell_hourly_label.grid(row=0, column=i+2, sticky= 'nsew')
            
            wind = f"{convert_wind(self.mainscreen.array_data_hours[i]['wind_speed'], self.menu.wind_metrics.get())}"
            self.mainscreen.cell_hourly_label = ttk.Label(master=self.mainscreen.grid_day, text=wind, justify="center", anchor="center", borderwidth=10, relief="groove", background='#B5CFB7')
            self.mainscreen.cell_hourly_label.grid(row=1, column=i+2, sticky= 'nsew')
            self.mainscreen.cell_hourly_label = ttk.Label(master=self.mainscreen.grid_day, text=self.mainscreen.array_data_hours[i]['wind_dir'], anchor="center", justify="center", borderwidth=10, relief="groove", background='#B5CFB7')
            self.mainscreen.cell_hourly_label.grid(row=2, column=i+2, sticky= 'nsew')
            
            angle = 180 - self.mainscreen.array_data_hours[i]['wind_dir_arrow']
            temp_img = Image.open("icons/arrow.png").rotate(angle)
            self.wind_dir_img.append(ImageTk.PhotoImage(temp_img))
            self.mainscreen.cell_hourly_label = tk.Canvas(master=self.mainscreen.grid_day, width=20, height=24, bg="#FFFFFF", bd=0, highlightthickness=0, background='#B5CFB7')
            self.mainscreen.cell_hourly_label.create_image(16,12, anchor=tk.CENTER, image=self.wind_dir_img[i])
            self.mainscreen.cell_hourly_label.grid(row=3, column=i+2, sticky= 'nsew')    

            self.mainscreen.cell_hourly_label = ttk.Label(master=self.mainscreen.grid_day, background=self.mainscreen.array_data_hours[i]['kitometer'], text="", borderwidth=10, relief="groove")
            self.mainscreen.cell_hourly_label.grid(row=4, column=i+2, sticky= 'nsew')  

    def get_data_by_place_name(self):
        self.data_forecast = get_week_data(self.mainscreen.location_id)
        if (("detail" in self.data_forecast) and ("does not exist" in self.data_forecast['detail'])):
            return
        data_daily_section = self.data_forecast.get('daily', {}).get('data', None)
        if data_daily_section == None:
            return
            
        for i in range(7):
            data_day = data_daily_section[i]
            dt = datetime.strptime(data_day['day'], "%Y-%m-%d")
            self.mainscreen.array_data_days[i]["day"] = calendar.day_name[dt.weekday()]
            self.mainscreen.array_data_days[i]["summary"] = data_day['weather'].replace('_', ' ')
            self.mainscreen.array_data_days[i]["icon"] = int(data_day['icon'])
            self.mainscreen.array_data_days[i]["temp"] = float(data_day['all_day']['temperature'])
            self.mainscreen.array_data_days[i]["temp_max"] = float(data_day['all_day']['temperature_max'])
            self.mainscreen.array_data_days[i]["temp_min"] = float(data_day['all_day']['temperature_min'])
            self.mainscreen.array_data_days[i]["wind"] = float(data_day['all_day']['wind']['speed'])
            self.mainscreen.array_data_days[i]["rain"] = float(data_day['all_day']['precipitation']['total'])         

        self.data_forecast_hourly = get_day_data(self.mainscreen.location_id)
        if (("detail" in self.data_forecast_hourly) and ("does not exist" in self.data_forecast_hourly['detail'])):
            return
            
        data_hourly_section = self.data_forecast_hourly.get('hourly', {}).get('data', None)
        if data_hourly_section == None:
            return
            
        for i in range(24):
            data_hour = data_hourly_section[i]
            self.mainscreen.array_data_hours[i]["temp"] = float(data_hour['temperature'])
            self.mainscreen.array_data_hours[i]["wind_speed"] = float(data_hour['wind']['speed'])
            self.mainscreen.array_data_hours[i]["wind_dir"] = data_hour['wind']['dir']
            self.mainscreen.array_data_hours[i]["wind_dir_arrow"] = int(data_hour['wind']['angle'])
            self.mainscreen.array_data_hours[i]["kitometer"] = get_kiteometer(self.mainscreen.array_data_hours[i]["wind_speed"])

        self.refresh_screen_data()

    def combobox_selected(self, event):
        self.mainscreen.location_to_display = self.mainscreen.list_location.get()
        self.mainscreen.location_id = self.mainscreen.locations_list[self.mainscreen.list_location.get()]
        self.mainscreen.location_selected = True
        self.get_data_by_place_name()    

    def check_event(self, event):
        if self.mainscreen.autoid != None:
            self.after_cancel(self.mainscreen.autoid)
        self.mainscreen.autoid = self.after(300, self.search_with_input)

    def search_with_input(self):
        self.mainscreen.locations_list.clear()
        user_input = self.mainscreen.list_location.get()
        data_from_api = get_list_location(user_input)
        if data_from_api == None:
            return
        
        for id in range(len(data_from_api)):
            if data_from_api[id] is None:
                continue
            if data_from_api[id]['type'] != "settlement":
                continue

            temp_area2 = "" if data_from_api[id]['adm_area2'] is None else f"{data_from_api[id]['adm_area2']}, "
            temp_location = f"{data_from_api[id]['name']}, {data_from_api[id]['adm_area1']}, {temp_area2}{data_from_api[id]['country']}"
            self.mainscreen.locations_list[temp_location] = data_from_api[id]["place_id"]

        self.mainscreen.list_location['values'] = []
        self.mainscreen.list_location['values'] = list(self.mainscreen.locations_list.keys())
        self.mainscreen.list_location.event_generate("<Down>")


class Mainscreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, style="main.TFrame")
        self.pack(side="top", expand=True, fill="both")
        self.array_data_days = {}
        for i in range(7):
            self.array_data_days[i] = {
                "day" : "n/a",
                "summary" : "n/a",
                "icon" : 1,
                "temp" : 0,
                "temp_max" : 0,
                "temp_min" : 0,
                "wind" : 0,
                "rain" : 0
            }
        self.array_data_hours = {}
        for i in range(24):
            self.array_data_hours[i] = {
                "temp" : 0,
                "wind_speed" : 0,
                "wind_dir" : " - ",
                "wind_dir_arrow" : 0,
                "kitometer" : "snow"
            }

        self.create_widgets(parent)

    def create_widgets(self, parent):
        # WE DEFINE A BOX FOR THE SEARCH FUNCTIONNALITY
        self.box_search = ttk.Frame(master=self, width=500, height=80, borderwidth=10, relief="groove")
        self.box_search.pack(padx=50, pady=20, fill="x")

        self.title_search = ttk.Label(master=self.box_search, text="Location: ", font="Calibri 18 bold", background="#CADABF")
        self.title_search.pack(side="left")

        self.frame_search = ttk.Frame(master=self.box_search)
        self.frame_search.pack(pady=8, side="left")
        
        self.locations_list = {}
        self.location_to_display = ""
        self.location_id = ""
        self.location_selected = False

        self.list_location = ttk.Combobox(master=self.frame_search, width=100, font="Calibri 14 bold", values=[])
        self.list_location.bind("<KeyRelease>", parent.check_event)
        self.list_location.bind("<<ComboboxSelected>>", parent.combobox_selected)
        self.autoid = None
        self.list_location.pack(expand=True, side="left", padx=10, fill="x")


        # WE DEFINE A BOX TO DISPLAY THE DAILY FORECAST
        self.box_week = ttk.Frame(master=self, borderwidth=10, relief="groove")
        self.box_week.pack(padx=50, pady=10, side="top", fill="x")

        self.title_week = ttk.Label(master=self.box_week, text="No location selected", font="Calibri 14 bold", background="#CADABF")
        self.title_week.pack()

        self.frame_week = ttk.Frame(master=self.box_week)
        self.tab_days = []
        for i in range(7):
            self.tab_days.append(FrameDay(self.frame_week))
            self.tab_days[i].pack(side='left', padx=10)
        self.frame_week.pack(pady=10)


        # WE DEFINE A BOX TO DISPLAY HOURLY FORECAST
        self.box_day = ttk.Frame(master=self, borderwidth=10, relief="groove")
        self.box_day.pack(padx=50, pady=20, side="top", fill="x")

        self.title_day = ttk.Label(master=self.box_day, text="Hourly forecast", font="Calibri 14 bold", background="#CADABF")
        self.title_day.pack()

        self.style_hourly_grid = ttk.Style()
        self.style_hourly_grid.configure('frame_hour.TFrame', background='#B5CFB7')
        self.grid_day = ttk.Frame(master=self.box_day, borderwidth=10, relief="groove", style='frame_hour.TFrame')
        self.grid_day.columnconfigure(0, weight = 2)
        self.grid_day.columnconfigure(1, weight = 1)
        for i in range(24):
            self.grid_day.columnconfigure(i+2, weight = 1)

        self.grid_day.rowconfigure(0, weight=1)
        self.grid_day.rowconfigure(1, weight=1)
        self.grid_day.rowconfigure(2, weight=1)
        self.grid_day.rowconfigure(3, weight=1)
        self.grid_day.rowconfigure(4, weight=1)
        self.grid_day.pack(padx=10, pady=10, expand=True, fill="x")

        self.row_temp_label = ttk.Label(master=self.grid_day, text="Temp.", borderwidth=10, relief="flat", font=('Roboto', 9), background='#B5CFB7')
        self.row_temp_label.grid(row=0, column=0, sticky="E")
        self.row_windspeed_label = ttk.Label(master=self.grid_day, text="Wind speed", borderwidth=10, relief="flat", font=('Roboto', 9), background='#B5CFB7')
        self.row_windspeed_label.grid(row=1, column=0, sticky="E")
        self.row_windarrow_label = ttk.Label(master=self.grid_day, text="Wind dir.", borderwidth=10, relief="flat", font=('Roboto', 9), background='#B5CFB7')
        self.row_windarrow_label.grid(row=2, column=0, sticky="E")
        self.row_winddir_label = ttk.Label(master=self.grid_day, text="", borderwidth=10, relief="flat", font=('Roboto', 9), background='#B5CFB7')
        self.row_winddir_label.grid(row=3, column=0, sticky="E")
        self.row_kite_indic = ttk.Label(master=self.grid_day, text="kitOmeter", borderwidth=10, relief="flat", font=('Roboto', 9), background='#B5CFB7')
        self.row_kite_indic.grid(row=4, column=0, sticky="E")

        for c in range(24):
            for r in range(3):
                self.cell_hourly_label = ttk.Label(master=self.grid_day, text=".", borderwidth=10, relief="groove", anchor="center", background='#B5CFB7')
                self.cell_hourly_label.grid(row=r, column=c+2, sticky= 'nsew')

            self.cell_hourly_label = ttk.Label(master=self.grid_day, text=".", justify="center", borderwidth=10, relief="groove", background='#B5CFB7')
            self.cell_hourly_label.grid(row=4, column=c+2, sticky= 'nsew')


class FrameDay(ttk.Frame):
    def __init__(self, master):
        self.style_frame_day = ttk.Style()
        self.style_frame_day.configure('frame_day.TFrame', background='#B5CFB7')
        ttk.Frame.__init__(self, master, borderwidth=10, relief='groove', style='frame_day.TFrame')
        
        #self.configure(bg='#B5CFB7')
        self.create_widgets() 
        self.display_widgets()
    
    def create_widgets(self):
        self.title_day = tk.Label(master=self, text='n/a', font="Calibri 18 bold", background='#B5CFB7')
        self.summary_day = tk.Label(master=self, text='n/a', background='#B5CFB7')

        self.icon_img = tk.PhotoImage(file="icons/1.png").zoom(1)
        self.canvas_icon = tk.Canvas(master=self, width=50, height=50, bg="#B5CFB7", bd=0, highlightthickness=0)
        self.canvas_icon.create_image(25,25, anchor=tk.CENTER, image=self.icon_img)

        self.icon_day = tk.Label(self, text="icon", background='#B5CFB7')
        self.temperature_day = tk.Label(master=self, text='n/a', font="Calibri 12 bold", background='#B5CFB7')
        self.temperature_max = tk.Label(master=self, text='n/a', font="Calibri 12 bold", background='#B5CFB7')
        self.temperature_min = tk.Label(master=self, text='n/a', font="Calibri 12 bold", background='#B5CFB7')
        self.wind_day = tk.Label(master=self, text='n/a', background='#B5CFB7')
        self.rain_day = tk.Label(master=self, text='n/a', background='#B5CFB7')

    def display_widgets(self):
        self.title_day.pack()
        self.summary_day.pack()
        self.canvas_icon.pack()
        self.icon_day.pack()
        self.temperature_day.pack()
        self.temperature_max.pack()
        self.temperature_min.pack()
        self.wind_day.pack()
        self.rain_day.pack()


class Topbar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, height=80, style="topbar.TFrame")
        self.pack(side="top", fill="y")
        self.create_widgets()
        self.display_widgets()

    def create_widgets(self):
        self.title_app = ttk.Label(master=self, text="Kitesurfing Session Planner", background="#E7E8D8", font="Calibri 20 bold")
        self.logo_img = tk.PhotoImage(file="icons/images.png").zoom(35).subsample(32)
        self.canvas_logo = tk.Canvas(master=self, width=40, height=40, bg="#E7E8D8", bd=0, highlightthickness=0)
        self.canvas_logo.create_image(20, 20, image=self.logo_img)

    def display_widgets(self):
        self.title_app.pack(pady=5, side="left", expand=True, fill="x")
        self.canvas_logo.pack(pady=5, side="left", expand=True, fill="x")


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, width=180, style="menu.TFrame")
        self.pack(side="left", fill="y")
        self.create_widgets(parent)
        self.display_widgets()

    def create_widgets(self, parent):
        self.box_options = ttk.Frame(master=self, borderwidth=10, width=150, height=350, relief="groove")

        self.options_title = ttk.Label(master=self.box_options, text="Options", font="Calibri 18 bold", background="#CADABF")
        self.sep = ttk.Label(master=self.box_options, text="", background="#CADABF")
        
        style_rbutton = ttk.Style()
        style_rbutton.configure('TRadiobutton', font=('Roboto', 9))
        style_rbutton.map('TRadiobutton', 
            foreground=[
                ('disabled', 'white'),
                ('selected', 'black'),
                ('!selected', 'gray30')],
            focuscolor=[('active', 'cyan4')],
            background=[
                ('selected', '#CADABF'),
                ('!selected', '#CADABF')])
        
        self.option_temp_label = ttk.Label(master=self.box_options, text="Temp metrics:", font="Calibri 12 bold", background="#CADABF")
        self.temp_metrics = tk.StringVar(value="C")
        self.option_temp_celsius = ttk.Radiobutton(
            master=self.box_options, 
            text="Celsius", 
            value="C", 
            variable=self.temp_metrics, 
            command=parent.refresh_screen_data)
        self.option_temp_farenheit = ttk.Radiobutton(
            master=self.box_options, 
            text="Farenheit", 
            value="F", 
            variable=self.temp_metrics, 
            command=parent.refresh_screen_data)

        self.sep2 = ttk.Label(master=self.box_options, text="", background="#CADABF")

        self.option_wind_label = ttk.Label(master=self.box_options, text="Wind metrics:", font="Calibri 12 bold", background="#CADABF")
        self.wind_metrics = tk.StringVar(value="m/s")
        self.option_wind_meter = ttk.Radiobutton(
            master=self.box_options, 
            text="meter/s", 
            value="m/s", 
            variable=self.wind_metrics, 
            command=parent.refresh_screen_data)
        self.option_wind_feet = ttk.Radiobutton(
            master=self.box_options, 
            text="feet/s", 
            value="ft/s", 
            variable=self.wind_metrics, 
            command=parent.refresh_screen_data)
        self.option_wind_miles = ttk.Radiobutton(
            master=self.box_options, 
            text="miles/h", 
            value="mph", 
            variable=self.wind_metrics, 
            command=parent.refresh_screen_data)
        self.option_wind_knots = ttk.Radiobutton(
            master=self.box_options, 
            text="knots", 
            value="knt", 
            variable=self.wind_metrics, 
            command=parent.refresh_screen_data)

    def display_widgets(self):
        self.box_options.pack(side="left", padx = 10)
        self.options_title.pack(pady=5)
        self.sep.pack()
        self.option_temp_label.pack_propagate(False)
        self.option_temp_label.pack(pady=2, expand=True, fill="x")
        self.option_temp_celsius.pack(expand=True, fill="x")
        self.option_temp_farenheit.pack(expand=True, fill="x")
        self.sep2.pack(pady=5)
        self.option_wind_label.pack(pady=2, expand=True, fill="x")
        self.option_wind_meter.pack(expand=True, fill="x")
        self.option_wind_feet.pack(expand=True, fill="x")
        self.option_wind_miles.pack(expand=True, fill="x")
        self.option_wind_knots.pack(expand=True, fill="x")



if __name__ == "__main__":
   main()


