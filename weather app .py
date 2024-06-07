from tkinter import *
from tkinter import ttk
import os


win = Tk()

win.title("MAUSAM DEKHO APP ")
win.configure(bg="green")
win.geometry("500x500")
name_label = Label(win, text="MAUSAM DEKHO APP", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh ",
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
image_path = "C:/Users/hi/OneDrive/Documents/dice roller/MMM/logo.png"

# Load the logo image
if os.path.isfile(image_path):
    try:
        Logo_image = PhotoImage(file=image_path)
        logo = Label(win, image=Logo_image)
        logo.place(x=150, y=100)
    except Exception as e:
        print(f"Error loading image: {e}")
else:
    print(f"File not found: {image_path}")
com = ttk.Combobox(
    win, text="MAUSAM DEKHO APP", values=list_name, font=("Times New Roman", 30, "bold")
)
com.place(x=25, y=120, height=50, width=450)

done_button = Button(win, text="DONE", font=("Times New Roman", 15, "bold"))
done_button.place(x=200, y=190, height=50, width=100)


win.mainloop()
