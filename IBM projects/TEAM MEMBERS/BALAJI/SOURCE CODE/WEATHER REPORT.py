from tkinter import* 
base = Tk() 
base.geometry("500x500") 
base.title("WEATHER REPORT")

labl_0 = Label(base, text="WEATHER REPORT",width=20,font=("bold", 20)) 
labl_0.place(x=90,y=53) 
 
lb1= Label(base, text="TEMPERATURE", width=20, font=("arial",12)) 
lb1.place(x=20, y=120) 
en1= Entry(base) 
en1.place(x=200, y=120) 
 
lb3= Label(base, text="PRESSURE", width=20, font=("arial",12)) 
lb3.place(x=19, y=160) 
en3= Entry(base) 
en3.place(x=200, y=160) 
 
lb4= Label(base, text="HUMIDITY", width=20,font=("arial",12)) 
lb4.place(x=19, y=200) 
en4= Entry(base) 
en4.place(x=200, y=200) 
 
lb5= Label(base, text="Select SEASON", width=20, font=("arial",12)) 
lb5.place(x=5, y=240) 
var = IntVar() 
Radiobutton(base, text="RAINY", padx=5,variable=var, value=1).place(x=180, y=240) 
Radiobutton(base, text="SUMMER", padx =10,variable=var, value=2).place(x=240,y=240) 
Radiobutton(base, text="SPRING", padx=15, variable=var, value=3).place(x=310,y=240) 
 
list_of_cntry = ("TAMILNADU", "ANDHRA", "KERALA") 
cv = StringVar() 
drplist= OptionMenu(base, cv, *list_of_cntry) 
drplist.config(width=15) 
cv.set("TAMILNADU") 
lb2= Label(base, text="Select states", width=13,font=("arial",12)) 
lb2.place(x=14,y=280) 
drplist.place(x=200, y=275) 
 
lb6= Label(base, text="weather condition", width=13,font=("arial",12)) 
lb6.place(x=19, y=320) 
en6= Entry(base, show='*') 
en6.place(x=200, y=320) 
 
lb7= Label(base, text="weather description", width=15,font=("arial",12)) 
lb7.place(x=21, y=360) 
en7 =Entry(base, show='*') 
en7.place(x=200, y=360) 
 
Button(base, text="current status", width=10).place(x=200,y=400) 
base.mainloop()
