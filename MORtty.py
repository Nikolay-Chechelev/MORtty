from tkinter import *


class MORtty:
    def __init__(self, top=None):
        self.root = top
        top.geometry("800x500")
        top.title("MORtty Terminal")
        top.configure(background="#e0ffff")
        top.configure(highlightcolor="black")

        self.ConfFrame = Frame(top)
        self.ConfFrame.place(relx=0.0, rely=0.0, relheight=0.15, relwidth=1.0)
        self.ConfFrame.configure(relief=GROOVE)
        self.ConfFrame.configure(borderwidth="2")
        self.ConfFrame.configure(relief=GROOVE)
        self.ConfFrame.configure(background="#ffffff")
        self.ConfFrame.configure(width=255)

        self.ConnectButton = Button(self.ConfFrame)
        self.ConnectButton.place(relx=0.01, rely=0.05, height=30, width=100)
        self.ConnectButton.configure(activebackground="#e0ffff")
        self.ConnectButton.configure(background="#ffffff")
        self.ConnectButton.configure(relief=FLAT)
        self.ConnectButton.configure(text='Connect')
        self.ConnectButton.configure(command=self.Play)

        self.DisconnectButton = Button(self.ConfFrame)
        self.DisconnectButton.place(relx=0.01, rely=0.5, height=30, width=100)
        self.DisconnectButton.configure(activebackground="#e0ffff")
        self.DisconnectButton.configure(background="#ffffff")
        self.DisconnectButton.configure(relief=FLAT)
        self.DisconnectButton.configure(text='Disconnect')
        self.DisconnectButton.configure(command=self.Pause)

        self.SendButton = Button(self.ConfFrame)
        self.SendButton.place(relx=0.85, rely=0.5, height=30, width=100)
        self.SendButton.configure(activebackground="#e0ffff")
        self.SendButton.configure(background="#ffffff")
        self.SendButton.configure(relief=FLAT)
        self.SendButton.configure(text='Send')
        self.SendButton.configure(command=self.Stop)

        self.NewLine = Checkbutton(self.ConfFrame)
        self.NevLine.place(relx=0.041, rely=0.162, relheight=0.046, relwidth=0.845)
        self.NevLine.configure(activebackground="#e0ffff")
        self.NevLine.configure(anchor=W)
        self.NevLine.configure(background="#ffffff")
        self.NevLine.configure(highlightbackground="#ffffff")
        self.NevLine.configure(justify=LEFT)
        self.NevLine.configure(text='''Test 1''')
        self.NevLine.configure(width=207)

        self.CarrigeReturn = Checkbutton(self.ConfFrame)
        self.CarrigeReturn.place(relx=0.041, rely=0.222, relheight=0.046, relwidth=0.845)
        self.CarrigeReturn.configure(activebackground="#e0ffff")
        self.CarrigeReturn.configure(anchor=W)
        self.CarrigeReturn.configure(background="#ffffff")
        self.CarrigeReturn.configure(highlightbackground="#ffffff")
        self.CarrigeReturn.configure(justify=LEFT)
        self.CarrigeReturn.configure(text='''Test 2''')

        self.ProgressFrame = Frame(top)
        self.ProgressFrame.place(relx=0.0, rely=0.15, relheight=0.85, relwidth=0.975)
        self.ProgressFrame.configure(relief=GROOVE)
        self.ProgressFrame.configure(borderwidth="2")
        self.ProgressFrame.configure(relief=GROOVE)
        self.ProgressFrame.configure(background="#ffffff")
        self.ProgressFrame.configure(width=565)

        self.ProgressList = Listbox(self.ProgressFrame)
        self.ProgressList.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.ProgressList.configure(background="white")
        self.ProgressList.configure(font="TkFixedFont")
        self.ProgressList.configure(width=564)

        self.Scale1 = Scale(top)
        self.Scale1.place(relx=0.975, rely=0.15, relwidth=0.50, relheight=1.0, width=10, bordermode='ignore')
        self.Scale1.configure(activebackground="#ffffff")
        self.Scale1.configure(background="#ffffff")
        self.Scale1.configure(font="TkTextFont")
        self.Scale1.configure(highlightbackground="#ffffff")
        self.Scale1.configure(length="398")
        self.Scale1.configure(showvalue="0")
        self.Scale1.configure(troughcolor="#ffffff")

    def Play(self):
        self.ProgressList.insert('end', 'Start')

    def Pause(self):
        self.ProgressList.insert('end', 'Pause')

    def Stop(self):
        self.ProgressList.insert('end', 'Stop')

    def List_insert(self, data):
        self.ProgressList.insert('end', data)
        self.ProgressList.see('end')
        self.ProgressList.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.root.update()


root = Tk()
top = MORtty(root)
root.mainloop()