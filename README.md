# The Kitesurfing planner app

A basic weather forecast application

## General Info

As any kitesurfer I'm using forecast apps all the time, so I've decided to try de develop my own app.

You can simply enter a place you would like to get the forecast, the list will update and propose up to 10 possible locations matching with your input  
Select the place you are looking for in the list, and "voila".  
The data will be updated, with the general forecast for the next 7 days, and a more detailled forecast for the next 24 hours.  
  
You can change the metrics in the left menu.
For temperatures you can choose between Celsius or Farenheit.
For the wind metrics, you can select meter/s, feet/s, miles/h or knots.

    

## Technologies

Python with TKinter for the GUI  
I'm using the API of MeteoSource https://www.meteosource.com/

    


## Setup

To run this app, you need to copy   
* **project.py**  
  This is the main file, it builds the GUI elements with their functions. It also contains some fonctions for metrics conversation.
    
* **weatherApi.py**  
  This file contains the functions that will connect tot he API and retrieve data.
  In this first version it is quite simple, but in future versions we could add many other features to get different set of data.

You can also check if you have the needed python packages already installed with the `requirements.txt`  
```
$ git clone https://github.com/schmotDev/Windy.git
$ cd Windy
$ pip3 install -r requirements.txt
$ python3 project.py
```


## Demo

When you start the app for the first time, there is no data to display.  
You can enter the name of the place you would like to go, let's try Tarifa in Spain, a very well known kitesurf spot.  

![demo1](https://github.com/user-attachments/assets/b6f2d6af-97f4-495e-bd2f-3cd476f2907b)


The list of possible locations shows several options corresponding to our entry.  
We select the first one, that is the place we are looking for.  

![demo2](https://github.com/user-attachments/assets/eb53313c-7e41-46c6-af58-e6a729ead733)

And we get the forecast for the next 7 days, with more details for the next 24 hours.  
The KiteOmeter indicator is green for the next hours !! grab your 12 meters kite and go for a light session!  





