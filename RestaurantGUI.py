import tkinter as tk
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time.time()))


class App1:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S 101} 30 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier  New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        #_______ Info Food ________

        self.Label1 = tk.Label(master=top, text='Restaurant Management System',
                               background="#091833", font=font11, foreground="#f2a343")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=610)

        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16,
                           fg="steel blue")
        localtime1.place(relx=0.420, rely=0.12)

        #________ Label Food _______

        self.Label1 = tk.Label(master=top, text='Order Num:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.300)
        self.Label1 = tk.Label(master=top, text='Fried Potato:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.350)
        self.Label1 = tk.Label(master=top, text='Chicken Burger:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.400)
        self.Label1 = tk.Label(master=top, text='Big king:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.450)
        self.Label1 = tk.Label(master=top, text='Chicken Royal:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.500)
        self.Label1 = tk.Label(master=top, text='Vegetable Salad:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.550)
        self.Label1 = tk.Label(master=top, text='Drinks:', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.054, rely=0.600)

        #______ Entry Food________

        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.300)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.200, rely=0.350)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.400)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.450)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.500)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.550)
        self.entry1 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.200, rely=0.600)

        #_____Calculator_________

        self.entry12 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry12.place(relx=0.700, rely=0.300, height=35, relwidth=0.247)

        self.Button1 = tk.Button(master=top, text='''7''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.700, rely=0.400, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''8''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.770, rely=0.400, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''9''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.840, rely=0.400, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''/''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.910, rely=0.400, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''4''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.700, rely=0.500, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''5''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.770, rely=0.500, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''6''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.840, rely=0.500, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''*''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.910, rely=0.500, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''1''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.700, rely=0.600, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''2''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.770, rely=0.600, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''3''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.840, rely=0.600, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''-''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.910, rely=0.600, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''0''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.700, rely=0.700, height=44, width=140)
        self.Button1 = tk.Button(master=top, text='''.''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.840, rely=0.700, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''+''', bg="#122c63", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.910, rely=0.700, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''=''', bg="#f2a343", fg="#ffffff", font=font14, borderwidth='0')
        self.Button1.place(relx=0.700, rely=0.805, height=44, width=251)

        #______Cost______

        self.Label1 = tk.Label(master=top, text='Cost :', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.370, rely=0.300)
        self.Label1 = tk.Label(master=top, text='Service Charge :', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.370, rely=0.400)
        self.Label1 = tk.Label(master=top, text='Tax :', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.370, rely=0.500)
        self.Label1 = tk.Label(master=top, text='Total :', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.370, rely=0.600)
        self.Label1 = tk.Label(master=top, text='Subtotal :', background="#091833", font=font12,
                               foreground="#bac8bd")
        self.Label1.place(relx=0.370, rely=0.700)

        #_____Entry Cost______

        self.entry13 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.490, rely=0.300)
        self.entry13 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.490, rely=0.400)
        self.entry13 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.490, rely=0.500)
        self.entry13 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.490, rely=0.600)
        self.entry13 = tk.Entry(master=top, bg="#d9d9d9", fg="#c60000", selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.490, rely=0.700)

        #_____Control Buttons________

        self.Button2 = tk.Button(master=top, text="Price", bg="#e16740", font=font16)
        self.Button2.place(relx=0.054, rely=0.805, width=107)
        self.Button2 = tk.Button(master=top, text="Total", bg="#e16740", font=font16)
        self.Button2.place(relx=0.164, rely=0.805, width=107)
        self.Button2 = tk.Button(master=top, text="Reset", bg="#e16740", font=font16)
        self.Button2.place(relx=0.274, rely=0.805, width=107)
        self.Button2 = tk.Button(master=top, text="Exit", bg="#e16740", font=font16)
        self.Button2.place(relx=0.384, rely=0.805, width=107)


root = tk.Tk()
my_gui = App1(root)
root.mainloop()

