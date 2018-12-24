from tkinter import *


class MORtty:
    def __init__(self, top=None):
        self.root = top
        top.geometry("800x500")
        top.title("MORtty Terminal")
        top.configure(background="#e0ffff")
        top.configure(highlightcolor="black")

        self.ConfFrame = Frame(top)
        self.ConfFrame.place(relx=0.0, rely=0.0, relheight=0.2, relwidth=1.0)
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

        self.Port = Entry(self.ConfFrame)
        self.Port.place(relx=0.15, rely=0.05, height=30, width=150)

        self.Baud = Entry(self.ConfFrame)
        self.Baud.place(relx=0.35, rely=0.05, height=30, width=150)

        self.Data = Entry(self.ConfFrame)
        self.Data.place(relx=0.15, rely=0.5, height=30, width=500)

        self.SendButton = Button(self.ConfFrame)
        self.SendButton.place(relx=0.85, rely=0.5, height=30, width=100)
        self.SendButton.configure(activebackground="#e0ffff")
        self.SendButton.configure(background="#ffffff")
        self.SendButton.configure(relief=FLAT)
        self.SendButton.configure(text='Send')
        self.SendButton.configure(command=self.Stop)

        self.NewLine = Checkbutton(self.ConfFrame)
        self.NewLine.place(relx=0.7, rely=0.01, relheight=0.2, relwidth=0.1)
        self.NewLine.configure(activebackground="#e0ffff")
        self.NewLine.configure(anchor=W)
        self.NewLine.configure(background="#ffffff")
        self.NewLine.configure(highlightbackground="#ffffff")
        self.NewLine.configure(justify=LEFT)
        self.NewLine.configure(text='New Line')
        self.NewLine.configure(width=207)

        self.CarriageReturn = Checkbutton(self.ConfFrame)
        self.CarriageReturn.place(relx=0.825, rely=0.01, relheight=0.2, relwidth=0.16)
        self.CarriageReturn.configure(activebackground="#e0ffff")
        self.CarriageReturn.configure(anchor=W)
        self.CarriageReturn.configure(background="#ffffff")
        self.CarriageReturn.configure(highlightbackground="#ffffff")
        self.CarriageReturn.configure(justify=LEFT)
        self.CarriageReturn.configure(text='Carriage Return')

        self.HexAppear = Radiobutton(self.ConfFrame)
        self.HexAppear.place(relx=0.7, rely=0.25, relheight=0.2, relwidth=0.1)
        self.HexAppear.configure(text='HEX')

        self.DecAppear = Radiobutton(self.ConfFrame)
        self.DecAppear.place(relx=0.8, rely=0.25, relheight=0.2, relwidth=0.1)
        self.DecAppear.configure(text='DEC')

        self.ASCIIAppear = Radiobutton(self.ConfFrame)
        self.ASCIIAppear.place(relx=0.9, rely=0.25, relheight=0.2, relwidth=0.1)
        self.ASCIIAppear.configure(text='ASCII')

        self.ProgressFrame = Frame(top)
        self.ProgressFrame.place(relx=0.0, rely=0.2, relheight=0.85, relwidth=0.975)
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
        self.Scale1.place(relx=0.975, rely=0.2, relwidth=0.50, relheight=0.8, width=10, bordermode='ignore')
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