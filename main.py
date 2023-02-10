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
    tbox_age.config(state='normal')
    
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END,age)
    tbox_age.config(state='disabled')

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
        #msg = 'Success!'
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
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

# Date, Month and Year labels and entry
lb_date=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_month=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_year=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
e_date=tk.Entry(window,width=5)
e_month=tk.Entry(window,width=5)
e_year=tk.Entry(window,width=5)

# Calculate Age
btn_calculate_age=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=validation)
lb_calculated_age = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
tbox_age=tk.Text(window,width=3,height=0,state="disabled",bg="lightgreen",font=("Arial",24,"bold"))

# Exit 
btn_exit=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

# Placement
lb_heading.place(x=70,y=5)
lb_subheading.place(x=10,y=40)
lb_date.place(x=60,y=80)
lb_month.place(x=60,y=105)
lb_year.place(x=60,y=130)
e_date.place(x=120,y=80)
e_month.place(x=120,y=105)
e_year.place(x=120,y=130)
btn_calculate_age.place(x=30,y=170)
lb_calculated_age.place(x=230,y=70)
tbox_age.place(x=300,y=100)
btn_exit.place(x=300,y=170)

"""
Improvments:
Make GUI look better
Prevent error when user enters word instead of number
"""