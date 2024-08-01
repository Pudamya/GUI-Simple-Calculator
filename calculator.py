import tkinter

window=tkinter.Tk()
window.title("Simple Calculator")
window.geometry("400x100")

label1=tkinter.Label(window,text="Value 01",font="15")
label1.grid(column=0,row=0)

label2=tkinter.Label(window,text="Value 02",font="15")
label2.grid(column=0,row=1)

label3=tkinter.Label(window,text="Answer : ",font="15")
label3.grid(column=2,row=0)

label4=tkinter.Label(window,text="",font="15")
label4.grid(column=3,row=0)

txt1=tkinter.Entry(window,width=20)
txt1.grid(column=1,row=0)

txt2=tkinter.Entry(window,width=20)
txt2.grid(column=1,row=1)


def clickb1():
    label4.config(text=str(float(txt1.get())+float(txt2.get())))
    
def clickb2():
    label4.config(text=str(float(txt1.get())-float(txt2.get())))
    
def clickb3():
    label4.config(text=str(float(txt1.get())*float(txt2.get())))
    
def clickb4():
    label4.config(text=str(float(txt1.get())/float(txt2.get())))
    
button1=tkinter.Button(window,text=" Add ",bg="light pink",fg="dark blue",command=clickb1)
button1.grid(column=0,row=2)

button2=tkinter.Button(window,text="Substract",bg="light pink",fg="dark blue",command=clickb2)
button2.grid(column=1,row=2)

button3=tkinter.Button(window,text=" Multiply ",bg="light pink",fg="dark blue",command=clickb3)
button3.grid(column=2,row=2)

button4=tkinter.Button(window,text=" Divide ",bg="light pink",fg="dark blue",command=clickb4)
button4.grid(column=3,row=2)



window.mainloop()
