import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x150')

        self.top_frame = tkinter.Frame(self.main_window, height=20, bd=14, bg='red')
        self.top_frame.pack(expand=True)

        self.bottom_frame = tkinter.Frame(self.main_window, height=20, bd=14, bg='blue')
        self.bottom_frame.pack(expand=True)

        self.label1 = tkinter.Label(self.top_frame, text='Winken', width=15)
        self.label2 = tkinter.Label(self.top_frame, text='Blinken', width=15)
        self.label3 = tkinter.Label(self.top_frame, text='Nod', width=15)

        self.label4 = tkinter.Label(self.bottom_frame, text='Sailed Off', width=15)
        self.label5 = tkinter.Label(self.bottom_frame, text='in a wooden', width=15)
        self.label6 = tkinter.Label(self.bottom_frame, text='Shoe', width=15)


        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='right')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='right')

        self.bottom_frame.pack()
        self.top_frame.pack()
        tkinter.mainloop()

my_gui = MyGUI()
