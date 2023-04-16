#for web requests
import requests

#import tkinter library
import tkinter as tk

import ijson

#buttons and boxes
from tkinter import *
from tkinter import ttk

#convert currency
def currency_convert():

    # global symbol
    app_id = '5d22fa3247fe4a58a520a75e7dd64f98'

    # Make a request to the latest exchange rates API endpoint
    response = requests.get(f'https://openexchangerates.org/api1/latest.json?app_id={app_id}')

    # Check if request was successful
    if response.status_code == 200:

        # Parse the JSON response and extract the exchange rates data
        exchange_rates = response.json()['rates']  # is a dictionary that contains the exchange rates of different
        # currencies with respect to a base currency.
        # print(exchange_rates)
        currency_1 = list.get()  # here we get the option from list 1
        currency_2 = option.get()  # here i get the option from list 2
        amount = float(inputt.get())  # here the value user will give
        rate_1 = exchange_rates[currency_1]
        rate_2 = exchange_rates[currency_2]
        converted_amount = round(amount / rate_1 * rate_2,
                                 2)  # The result is rounded to two decimal places using the round()
        formated = '{:,.2f}'.format(converted_amount)
        Result['text'] = formated
        print(converted_amount, formated)

    else:
        print(f'Request failed with status code {response.status_code}')

#reset
def reset():
    inputt.delete(0, END)
    list.set('')
    option.set('')
    Result['text'] = ''

#create window
GUI = tk.Tk()

#window size
GUI.geometry("500x500")
GUI.title("Junaid Curency Convertor")
GUI.resizable(height=False, width=False)  #fixed the size
# Fram for heading
heading = Frame(GUI, width=470, height=100)    # rectangular area
heading.place(x=15, y=30)

# input
inputt = Entry(GUI, width=22, justify=CENTER, relief='solid', font=("Ivy 12 bold"))
inputt.place(x=150, y=270)

# currency
Currency = ['PKR', 'EUR', 'USD','CLP', 'INR', 'KRW', 'ZAR']
From = Label(GUI, text='From', width=6, height=2, pady=0, padx=0, relief="flat", anchor=NW, font=("Ivy 10"), fg='black')
From.place(x=100, y=220)

list = ttk.Combobox(GUI, width=6, justify=CENTER, font=("sans-serif"))
list['values'] = Currency
list.place(x=140, y=220)
To_label = Label(GUI, text='To', width=6, height=2, pady=0, padx=0, relief="flat", anchor=NW, font=("sans-serif"), fg='black')
To_label.place(x=250, y=220)
option = ttk.Combobox(GUI, width=6, justify=CENTER, font=("sans-serif"))
option['values'] = Currency
option.place(x=280, y=220)

# input
inputt = Entry(GUI, width=22, justify=CENTER, relief='solid', font=("sans-serif"))
inputt.place(x=130, y=270)

# button
button = Button(GUI, text="Convert", width=7, padx=5, height=1, bg="white", fg='black', font=("Ivy 10 bold"), command=currency_convert)
button.place(x=170, y=310)
reset_button = Button(GUI, text="Reset", width=7, padx=5, height=1, bg="red", fg='white', font=("Ivy 10 bold"), command=reset)
reset_button.place(x=260, y=310)

GUI.mainloop()
