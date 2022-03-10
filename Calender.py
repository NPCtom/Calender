#Calendar Project 2.27
#5 Mar 2022
#Copyright 2022 Winz Tom

from tkinter import *
from datetime import date, timedelta, datetime
import calendar
import os
import math

class SlideShowGUI:
    def __init__(self, parent):
        self.photos = [PhotoImage(file = os.path.dirname(__file__) + "//img/1.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/2.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/3.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/4.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/5.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/6.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/7.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/8.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/9.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/10.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/11.png"),PhotoImage(file = os.path.dirname(__file__) + "/img/12.png")]
        self.months = ["Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat" , "Sun"]
        self.dObjects = []

        self.btn_left = Button(parent, text = "<", command = self.moveLeft)
        self.btn_right = Button(parent, text = ">", command = self.moveRight)
        self.target = 0
        self.imageLabel = Label(parent, image = self.photos[0], height = 150, width = 150, fg="lime", bg="black")
        selectedMonth=self.target+1
        date = datetime.today().replace(month=selectedMonth,day=1)
        StartingMonthDay = date.weekday()
        DaysInMonth = calendar.monthrange(date.year, date.month)[1]
        WeeksInMonth = math.ceil((DaysInMonth+StartingMonthDay)/7)+1
        OverflowCount = 1
        for x in range(WeeksInMonth):
            for y in range(7):
                day = (7*x)+(1+y)-7
                if(x == 0): toAdd = Label(parent, height=1,width=4,text=self.days[y], anchor="se", fg="lime", bg="black")
                elif(day <= StartingMonthDay):
                    toAdd = Label(parent, height=2,width=4, anchor="se", bg="black",highlightbackground="black",text=" ")
                    self.dObjects.append(toAdd)
                else:
                    toAdd = Label(parent, height=2,width=4,text=day-StartingMonthDay, anchor="se",bg=getGridColour(day-1))
                    self.dObjects.append(toAdd)
                toAdd.grid(row=2+x,column=1+y, sticky=SE)
                if((day-StartingMonthDay)>DaysInMonth):
                    toAdd.config(bg="black",highlightbackground="black",text=" ")
                    OverflowCount+=1
        self.my_label = Label(parent,
                 text = self.months[0],fg="lime", bg="black", font='Helvetica 18 bold')
        self.imageLabel.grid(row = 0,column=1, columnspan=7)
        self.my_label.grid(row=1,column=2,columnspan=5)
        self.btn_left.grid(row = 1, column = 0, sticky = W)
        self.btn_right.grid(row = 1, column = 8, sticky = E)
        parent.configure(bg = "black")

    def moveLeft(self): updateDays(self,-1)
    def moveRight(self): updateDays(self, 1)

def updateDays(self,changeBy):
    self.target += changeBy
    if(self.target < 0): self.target = len(self.photos)
    elif(self.target >= len(self.photos)): self.target = 0

    self.imageLabel.configure(image = self.photos[self.target])
    self.my_label.configure(text = self.months[self.target])

    date = datetime.today().replace(month=(self.target+1),day=1)
    StartingMonthDay = date.weekday() # month=X
    DaysInMonth = calendar.monthrange(date.year, date.month)[1]
    WeeksInMonth = math.ceil((DaysInMonth+StartingMonthDay)/7)+1
    StartingCount = 1
    for i in range(0, len(self.dObjects)):
        if(i >= DaysInMonth+StartingMonthDay or i < StartingMonthDay):
            self.dObjects[i].config(bg="black",text=" ")
            continue
        elif(StartingMonthDay+i <= len(self.dObjects)):
            self.dObjects[StartingMonthDay+StartingCount-1].config(text = str(StartingCount),bg=getGridColour(StartingMonthDay+StartingCount-1))
            StartingCount+=1
def getGridColour(index):
    if(index%2 == 0): return "pink"
    else: return "lime"

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title(str(datetime.today().year) + " calender")
    window = SlideShowGUI(root)
    root.geometry("400x500+0+0")
    root.mainloop()
