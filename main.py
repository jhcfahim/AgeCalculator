from datetime import date
import tkinter as tk
from tkinter import messagebox

today = date.today()

# Functions
def exit():
    window.destroy()

def find_age(d, m, y):
    age =today.year-y-((today.month, today.day)<(m,d))
    return age

def display_calc_age(age):
    t1.config(state='normal')
    
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')

def validation():
  # gets the three entries
  d = e_date.get()
  m = e_month.get()
  y = e_year.get()

  msg = ''

  if len(d) == 0 or len(m) == 0 or len (y) == 0:
      msg = 'day, month and year can\'t be empty'
  else:
    try:
      if any(ch.isdigit() for ch in d) == False:
        msg = 'day must be a NUMBER'
      elif any(ch.isdigit() for ch in m) == False:
        msg = 'month must be a NUMBER'
      elif any(ch.isdigit() for ch in y) == False:
        msg = 'year must be a NUMBER'
      else:
        msg = 'Success!'
        day = int(d)
        month = int(m)
        year = int(y)
        calc_age = find_age(day, month, year)
        display_calc_age(calc_age)

    except Exception as ep:
      messagebox.showerror('error', ep)

  messagebox.showinfo('message', msg)


# Making Window
window = tk.Tk()
window.geometry("500x230")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title("Age Calculator")

# Heading and Subheading
l1 = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

# Date, Month and Year labels and entry
l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
e1=tk.Entry(window,width=5)
e2=tk.Entry(window,width=5)
e3=tk.Entry(window,width=5)

# Calculate Age
b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=validation)
l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
t1=tk.Text(window,width=3,height=0,state="disabled",bg="lightgreen",font=("Arial",24,"bold"))

# Exit 
b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

# Placement
l1.place(x=70,y=5)
l2.place(x=10,y=40)
l_d.place(x=60,y=80)
l_m.place(x=60,y=105)
l_y.place(x=60,y=130)
e1.place(x=120,y=80)
e2.place(x=120,y=105)
e3.place(x=120,y=130)
b1.place(x=30,y=170)
l3.place(x=230,y=70)
t1.place(x=300,y=100)
b2.place(x=300,y=170)

"""
Improvments:
Make GUI look better
Prevent error when user enters word instead of number
"""