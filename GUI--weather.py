from tkinter import *
from APIFILE import base1
from tkinter import messagebox as ms
import sys
r=Tk()
c=StringVar()
r.geometry("750x450")
r.title("Weather Info--AJAY MALIK")
header=Label(r,text="Weather Infomations",font=("Times",30,"bold"))
header.pack()
class homepage(base1):
    def frame1(self):
        self.f1=Frame(r)
        self.current_loca=Button(self.f1,text="Current Location weather",command=self.frame4)
        self.current_loca.pack(padx=10,pady=10)
        self.city_name_b=Button(self.f1,text="City Name", command=self.city_name)
        self.city_name_b.pack(padx=10,pady=10)
        self.f1.pack()
    def city_name(self):
        self.f1.destroy()
        self.f2=Frame(r)
        self.city_name_l=Label(self.f2,text="City Name",font=("Times",15,'bold'))
        self.city_name_l.pack()
        self.e=Entry(self.f2)
        self.e.pack()
        r.bind("<Return>",self.Enter_action)
        self.b=Button(self.f2,text="Submit",command=self.output,font=("Times",12,'bold'))
        self.b.pack(padx=10,pady=10)
        self.b2h=Button(self.f2,text="Back",command=self.b2hfromframe2,font=("Times",12,"bold"))
        self.b2h.pack()
        self.f2.pack()
    def b2hfromframe2(self):
        self.f2.destroy()
        self.frame1()
    def output(self):
        try:
            self.cityname(self.e.get())
            self.error=False
        except KeyError:
            ms.showerror("Error","INVALID INPUT")
            self.error=True
        if self.error!=True:    
            self.f2.destroy()
            self.f3=Frame(r)
            self.l1x=Label(self.f3,text=self.ax,font=("Times",12,'bold'))
            self.l1x.pack()
            self.l2x=Label(self.f3,text=self.bx,font=("Times",12,'bold'))
            self.l2x.pack()
            self.l3x=Label(self.f3,text=self.cx,font=("Times",12,'bold'))
            self.l3x.pack()
            self.l4x=Label(self.f3,text=self.dx,font=("Times",12,'bold'))
            self.l4x.pack()
            self.l5x=Label(self.f3,text=self.ex,font=("Times",12,'bold'))
            self.l5x.pack()
            self.l6x=Label(self.f3,text=self.fx,font=("Times",12,'bold'))
            self.l6x.pack()
            self.l7x=Label(self.f3,text=self.gx,font=("Times",12,'bold'))
            self.l7x.pack()
            self.l8x=Label(self.f3,text=self.hx,font=("Times",12,'bold'))
            self.l8x.pack()
            self.backtof2=Button(self.f3,text="Back",command=self.backtoframe2,font=("Times",12,'bold'))
            self.backtof2.pack()
            self.f3.pack()
    def backtoframe2(self):
        self.f3.destroy()
        self.city_name()
        
    def Enter_action(self,event):
        self.output()
        
    def frame4(self):
        self.f1.destroy()
        self.f4=Frame(r)
        self.lat_lon_f()
        self.l1y=Label(self.f4,text=self.ay,font=("Times",12,'bold'))
        self.l1y.pack()
        self.l2y=Label(self.f4,text=self.by,font=("Times",12,'bold'))
        self.l2y.pack()
        self.l3y=Label(self.f4,text=self.cy,font=("Times",12,'bold'))
        self.l3y.pack()
        self.l4y=Label(self.f4,text=self.dy,font=("Times",12,'bold'))
        self.l4y.pack()
        self.l5y=Label(self.f4,text=self.ey,font=("Times",12,'bold'))
        self.l5y.pack()
        self.l6y=Label(self.f4,text=self.fy,font=("Times",12,'bold'))
        self.l6y.pack()
        self.l7y=Label(self.f4,text=self.gy,font=("Times",12,'bold'))
        self.l7y.pack()
        self.l8y=Label(self.f4,text=self.hy,font=("Times",12,'bold'))
        self.l8y.pack()
        self.back=Button(self.f4,text='Back',command=self.backhome,font=("Times",12,'bold'))
        self.back.pack()
        self.f4.pack()
    def backhome(self):
        self.f4.destroy()
        self.frame1()
        
        

        
        
        
obj=homepage()
obj.frame1()
mainloop()
