#weather app using python

from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url_api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_key = 'fa2eb84d7a619a9a2cf007c34299aa48'

def weather_find(city):
    final = requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file['main']['temp']
        c_temperature = k_temperature - 273.15
        f_temperature = (k_temperature - 273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        humidity_display = json_file['main']['humidity']
        result = (city,country_name,c_temperature,f_temperature,weather_display,humidity_display)

        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text']='{}, {}'.format(weather[0],weather[1])
        temperature_entry['text'] = '{:.2f}C , {:.2f}F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]
        humidity_entry['text'] = 'Humidity : '+str( weather[5])
    else:
        messagebox.showerror('Error','Please enter a valid city name. Cannot find this city')


root = Tk()
root.title("WEATHER App")
root.config(background='black')
root.geometry("700x400")

search_city=StringVar()
enter_city = Entry(root,textvariable = search_city,width=20,font=('Arial',20),fg='Purple')
enter_city.pack(pady=10)

search_button = Button(root,text='Search',font=('Arial',20),width=10,bg="Pink",fg="Green",command=print_weather)
search_button.pack(pady=10)

location_entry=Label(root,text='',font=("Bold",25),bg='Yellow',fg='Blue')
location_entry.pack(pady=10)  

temperature_entry = Label(root,text='',font=("Bold",25),fg='Red',bg='orange')
temperature_entry.pack(pady=(20,0))

weather_entry = Label(root,text='',font=("Bold",25),fg='Orange',bg='Red')
weather_entry.pack(pady=(20,0))

humidity_entry = Label(root,text='',font = ("Bold",25),fg='purple',bg='light blue')
humidity_entry.pack(pady=(5,0))

root.mainloop()
