import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/303b0e8e1241fc4aa6917782fcb6acc5e397301c948a6bda6c311c30e4c5f84f"

master = Tk()
master.title("Weather App")
master.config(bg="#34495e")

img = Image.open("icon.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def GetWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--kyTeL").text
    temp = soup.find('span', class_="CurrentConditions--tempValue--3a50n").text
    weather = soup.find('div', class_="CurrentConditions--phraseValue--2Z18W").text

    locationLabel.config(text=location)
    tempLabel.config(text=temp)
    weatherLabel.config(text=weather)

    tempLabel.after(60000, GetWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold", 20), bg="#34495e")
locationLabel.grid(row=0, sticky="N", padx=40)

tempLabel = Label(master, font=("Calibri bold", 70), bg="#34495e")
tempLabel.grid(row=1, sticky="W", padx=40)

Label(master, image=img, bg="#34495e").grid(row=1, sticky="E")

weatherLabel = Label(master, font=("Calibri bold", 15), bg="#34495e")
weatherLabel.grid(row=2, sticky="W", padx=40)

GetWeather()
master.mainloop()