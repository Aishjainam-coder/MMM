from tkinter import *
from tkinter import ttk

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


com = ttk.Combobox(
    win, text="MAUSAM DEKHO APP", values=list_name, font=("Times New Roman", 30, "bold")
)
com.place(x=25, y=50, height=50, width=450)


win.mainloop()
