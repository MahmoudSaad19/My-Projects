import calendar as cal
from tkinter import *

calendar=Tk()
calendar.title('Modi 2019 Calendar')
calendar.geometry('420x240+400+200')

def show():
    month=var.get()
    val=cal.month(2019,month)
    #print(val)
    Label(text=val,width=44,height=10,bg='purple',padx=10,fg='cyan',font=5)\
        .grid(sticky=N,row=3,column=0,columnspan=8)


var=IntVar()

selector=Radiobutton(text='Jan',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=1).grid(row=0,column=0,sticky=NSEW)
selector=Radiobutton(text='Feb',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=2).grid(row=0,column=1,sticky=NSEW)
selector=Radiobutton(text='March',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=3).grid(row=0,column=2,sticky=NSEW)
selector=Radiobutton(text='April',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=4).grid(row=0,column=3,sticky=NSEW)
selector=Radiobutton(text='May',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=5).grid(row=0,column=4,sticky=NSEW)
selector=Radiobutton(text='June',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=6).grid(row=0,column=5,sticky=NSEW)
selector=Radiobutton(text='July',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=7).grid(row=1,column=0,sticky=NSEW)
selector=Radiobutton(text='Aug',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=8).grid(row=1,column=1,sticky=NSEW)
selector=Radiobutton(text='Sept',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=9).grid(row=1,column=2,sticky=NSEW)
selector=Radiobutton(text='Oct',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=10).grid(row=1,column=3,sticky=NSEW)
selector=Radiobutton(text='Nov',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=11).grid(row=1,column=4,sticky=NSEW)
selector=Radiobutton(text='Dec',command=show,variable=var,bg='yellow',fg='blue',indicatoron=1,
                     padx=5,pady=2,font=7,value=12).grid(row=1,column=5,sticky=NSEW)

calendar.mainloop()

