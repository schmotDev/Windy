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
* project.py
* weatherApi.py

You can also check if you have the needed python packages already installed with the `requirements.txt`  
```
$ pip3 install -r requirements.txt
$ python3 project.py
```






