from tkinter import *
import datetime
from datetime import date, timedelta
from calendar import monthrange

calender=Tk()
calender.title("My Calender")

def clear():
    list=calender.grid_slaves()
    for l in list:
        l.destroy()

def onclicknext():
    global calender_dates
    clear()
    if calender_dates.month>11:
        next_year=calender_dates.year+1
    else:
        next_year=calender_dates.year
    list_months=[1,2,3,4,5,6,7,8,9,10,11,12]
    next_month_index=calender_dates.month-1
    for i in list_months:
        if next_month_index >10:
            next_month=list_months[11-next_month_index]
        else:
            next_month=list_months[next_month_index+1]
    calender_dates= date(year=next_year,month=next_month,day=1)
    calender_layout()

def onclickprevious():
    global calender_dates
    clear()
    if calender_dates.month < 2:
        next_year=calender_dates.year-1
    else:
        next_year=calender_dates.year
    list_months=[1,2,3,4,5,6,7,8,9,10,11,12]
    next_month_index=calender_dates.month-1
    for i in list_months:
        if next_month_index <1:
            next_month=list_months[11-next_month_index]
        else:
            next_month=list_months[next_month_index-1]
    calender_dates= date(year=next_year,month=next_month,day=1)
    calender_layout()

def calender_layout():
    #to get days
    calender_days=['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(7):
        label=Label(calender, text=calender_days[i])
        label.grid(row=1,column=i)
    x= list(monthrange(calender_dates.year,calender_dates.month))
    print(x)
    calender_daterange=[calender_dates+timedelta(days=x) for x in range(1,(x[1]+1))]
    calender_daterange_day=[(x.day) for x in calender_daterange]
    calender_row= 2
    calender_column=calender_dates.weekday()
    for i in range(1,len(calender_daterange_day)+1):
        button = Button(calender, text= i).grid(row=calender_row, column=calender_column)
        calender_column+=1
        if calender_column >6:
            calender_row+=1
            calender_column=0
    #To print Title

    months_list=['Nil','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
    sel_month=months_list[calender_dates.month]
    label1=Label(calender, text=str(sel_month)).grid(row=0, column=2)
    label1=Label(calender, text=str(calender_dates.year)).grid(row=0, column=3)
    button1=Button(calender, text="<<",command=onclickprevious).grid(row=0,column=0)
    button2=Button(calender,text=">>",command=onclicknext).grid(row=0,column=6)


#to get date
today_date=date.today()
calender_dates= date(year=today_date.year, month=today_date.month, day=1)
calender_layout()
# row_n=6-calender_dates.weekday()
# row_day=today_date.day//row_n
#
# column_n=7-(calender_dates.weekday()+1)
# def col_day():
#     column_k =today_date.day-column_n
#     while column_k > 6:
#         col_day()
#         if column_k < 6:
#             return column_k
#
# print(column_k)
#
# button_today=Button(calender,text=today_date.day).grid()

calender.mainloop()
