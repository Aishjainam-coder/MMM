from tkinter import *
from tkinter import ttk
import os
import requests


# Function to get weather data from API and update the labels
def data_get():
    city = city_name.get()  # Get the city name entered by the user

    # Get data from OpenWeatherMap API
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid=bc0ef522aa874d675bd75fe4e366bb03"
    ).json()

    # Update the labels with the data from the API
    w_label1.config(text=data["weather"][0]["main"])  # Weather main type
    wb_label1.config(text=data["weather"][0]["description"])  # Weather description
    temp_label1.config(
        text=str(int(data["main"]["temp"] - 273.15))
    )  # Temperature in Celsius
    pres_label1.config(text=data["main"]["pressure"])  # Atmospheric pressure


win = Tk()  # Create the main window

win.title("MAUSAM DEKHO APP")  # Set the title of the window
win.configure(bg="violet")  # Set the background color of the window
win.geometry("500x700")  # Set the size of the window

# Create the main title label
name_label = Label(win, text="MAUSAM DEKHO APP", font=("Times New Roman", 25, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()  # Variable to store the city name

# List of city names for the dropdown
list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Lakshadweep",
    "National Capital Territory of Delhi",
    "Puducherry",
]

# Add the logo image
Logo_image = PhotoImage(file=os.path.join(r"C:\Users\hi\Downloads\hey", "real.png.png"))

# Assuming the logo image size is 200x200
logo = Label(win, image=Logo_image)
logo.place(
    x=150, y=500
)  # Adjust the x and y coordinates to position the logo at the bottom

# Create a combobox for city selection
com = ttk.Combobox(
    win,
    text="MAUSAM DEKHO APP",
    values=list_name,
    font=("Times New Roman", 20, "bold"),
    textvariable=city_name,
)
com.place(x=25, y=120, height=50, width=450)

# Create a label for Weather Climate
w_label = Label(win, text="Weather Climate", font=("Candara", 20, "bold"))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Candara", 20, "bold"))
w_label1.place(x=250, y=260, height=50, width=210)

# Create a label for Weather Description
wb_label = Label(win, text="Weather Description", font=("Candara", 17, "bold"))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Candara", 20, "bold"))
wb_label1.place(x=250, y=330, height=50, width=210)

# Create a label for Temperature
temp_label = Label(win, text="Temperature", font=("Candara", 20, "bold"))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text=" ", font=("Candara", 20, "bold"))
temp_label1.place(x=250, y=400, height=50, width=210)

# Create a label for Pressure
pres_label = Label(win, text="Pressure", font=("Candara", 20, "bold"))
pres_label.place(x=25, y=470, height=50, width=210)
pres_label1 = Label(win, text="", font=("Candara", 20, "bold"))
pres_label1.place(x=250, y=470, height=50, width=210)

# Create a button to fetch the weather data
done_button = Button(
    win, text="DONE", font=("Times New Roman", 15, "bold"), command=data_get
)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()  # Run the main loop of the window
