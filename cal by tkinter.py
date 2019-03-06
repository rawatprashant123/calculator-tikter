from tkinter import*
from tkinter import ttk

number = []

root = Tk()
root.title('Calculator')

operator =""

txt_input = StringVar()


display = Entry(root,font=('arial',20,'bold') , textvariable=txt_input , bd=10  , justify="right" ).grid(columnspan=4)

bu1 = Button(root ,text="AC" , bd=10 ,fg="black" )
bu1.grid(row= 0 , column= 0 , ipadx = 40 , ipady=4)
bu1.config(command=lambda: ButtonClick('AC'))

bu2 = Button(root ,text="DEL" , bd=10 ,fg="black" )
bu2.grid(row= 0 , column= 3 , ipadx = 40 , ipady=4)
bu2.config(command=lambda: ButtonClick('DEL'))

bu5 = Button(root, text='7' , bd=10 , fg="black")
bu5.grid(row=1, column=0, ipadx=60, ipady=20)
bu5.config(command=lambda: ButtonClick(7))

bu6 = Button(root, text='8' , bd=10 , fg="black")
bu6.grid(row=1, column=1, ipadx=60, ipady=20)
bu6.config(command=lambda: ButtonClick(8))

bu7 = Button(root, text='9' , bd=10 , fg="black")
bu7.grid(row=1, column=2, ipadx=60, ipady=20)
bu7.config(command=lambda: ButtonClick(9))

bu8 = Button(root, text='X' , bd=10 , fg="black")
bu8.grid(row=1, column=3, ipadx=60, ipady=20)
bu8.config(command=lambda: ButtonClick("*"))

bu9 = Button(root, text='4',bd=10 , fg="black")
bu9.grid(row=2, column=0, ipadx=60, ipady=20)
bu9.config(command=lambda: ButtonClick(4))

bu10 =Button(root, text='5' ,bd=10 , fg="black")
bu10.grid(row=2, column=1, ipadx=60, ipady=20)
bu10.config(command=lambda: ButtonClick(5))

bu11 = Button(root, text='6' ,bd=10 , fg="black")
bu11.grid(row=2, column=2, ipadx=60, ipady=20)
bu11.config(command=lambda: ButtonClick(6))

bu12 = Button(root, text='+' ,bd=10 , fg="black")
bu12.grid(row=2, column=3, ipadx=60, ipady=20)
bu12.config(command=lambda: ButtonClick('+'))

bu13 =Button(root, text='1' , bd=10 , fg="black")
bu13.grid(row=3, column=0, ipadx=60, ipady=20)
bu13.config(command=lambda: ButtonClick(1))

bu14 = Button(root, text='2' ,bd=10 , fg="black")
bu14.grid(row=3, column=1, ipadx=60, ipady=20)
bu14.config(command=lambda: ButtonClick(2))

bu15 = Button(root, text='3',bd=10 , fg="black")
bu15.grid(row=3, column=2, ipadx=60, ipady=20)
bu15.config(command=lambda: ButtonClick(3))

bu16 =Button(root, text='-' ,bd=10 , fg="black")
bu16.grid(row=3, column=3, ipadx=60, ipady=20)
bu16.config(command=lambda: ButtonClick('-'))

bu17 = Button(root, text='0' ,bd=10 , fg="black")
bu17.grid(row=4, column=0, ipadx=60, ipady=20)
bu17.config(command=lambda: ButtonClick(0))

bu18 =Button(root, text='.', bd=10 , fg="black")
bu18.grid(row=4, column=1, ipadx=60, ipady=20)
bu18.config(command=lambda: ButtonClick("."))

bu19 = Button(root, text='=' , bd=10 , fg="black")
bu19.grid(row=4, column=2, ipadx=60, ipady=20)
bu19.config(command=lambda: ButtonClick("="))

bu20 = Button(root, text='/' , bd=10 , fg="black")
bu20.grid(row=4, column=3, ipadx=60, ipady=20)
bu20.config(command=lambda: ButtonClick("/"))


def ButtonClick(id):

    global operator

    if str(id)=="DEL":
        operator= " "
        txt_input.set(" ")

    elif str(id)=="=":
        try:
            sum= str(eval(operator))
            ans=sum
            txt_input.set(sum)
            operator= " "

        except:
            operator=" "
            txt_input.set("math error")
            operator= " "



    elif str(id)=="AC":
        operator=" "
        txt_input.set("0")
        operator= " "

    else:
        operator=operator + str(id)

        txt_input.set(operator)


root.mainloop()