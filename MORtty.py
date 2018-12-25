#coding: utf-8
from tkinter import *
import tkinter.ttk as ttk
import serial, time, datetime, thread
import serial.tools.list_ports


class MORtty:
    def __init__(self, top=None):
        self.root = top
        top.geometry("800x500")
        top.title("MORtty Terminal")
        top.configure(background="#e0ffff")
        top.configure(highlightcolor="black")

        self.ttyS = None
        self.run = False

        self.appearing = StringVar()
        self.appearing.set('ASCII')
        self.lf = IntVar()
        self.cr = IntVar()

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
        self.ConnectButton.configure(command=self.Connect)

        self.DisconnectButton = Button(self.ConfFrame)
        self.DisconnectButton.place(relx=0.01, rely=0.5, height=30, width=100)
        self.DisconnectButton.configure(activebackground="#e0ffff")
        self.DisconnectButton.configure(background="#ffffff")
        self.DisconnectButton.configure(relief=FLAT)
        self.DisconnectButton.configure(text='Disconnect')
        self.DisconnectButton.configure(command=self.Disconnect)

        self.Port = ttk.Combobox(self.ConfFrame)
        self.Port.place(relx=0.15, rely=0.05, height=30, width=150)
        self.Port.configure(background="#ffffff")

        self.Baud = Entry(self.ConfFrame)
        self.Baud.place(relx=0.35, rely=0.05, height=30, width=150)
        self.Baud.insert(0, '115200')
        self.Baud.configure(background="#ffffff")

        self.Data = Entry(self.ConfFrame)
        self.Data.place(relx=0.15, rely=0.5, height=30, width=500)
        self.Data.configure(background="#ffffff")

        self.SendButton = Button(self.ConfFrame)
        self.SendButton.place(relx=0.85, rely=0.5, height=30, width=100)
        self.SendButton.configure(activebackground="#e0ffff")
        self.SendButton.configure(background="#ffffff")
        self.SendButton.configure(relief=FLAT)
        self.SendButton.configure(text='Send')
        self.SendButton.configure(command=self.Send)

        self.NewLine = Checkbutton(self.ConfFrame)
        self.NewLine.place(relx=0.7, rely=0.01, relheight=0.2, relwidth=0.1)
        self.NewLine.configure(activebackground="#e0ffff")
        self.NewLine.configure(anchor=W, variable=self.lf)
        self.NewLine.configure(background="#ffffff")
        self.NewLine.configure(highlightbackground="#ffffff")
        self.NewLine.configure(justify=LEFT)
        self.NewLine.configure(text='New Line')
        self.NewLine.configure(width=207)

        self.CarriageReturn = Checkbutton(self.ConfFrame)
        self.CarriageReturn.place(relx=0.825, rely=0.01, relheight=0.2, relwidth=0.16)
        self.CarriageReturn.configure(activebackground="#e0ffff")
        self.CarriageReturn.configure(anchor=W, variable=self.cr)
        self.CarriageReturn.configure(background="#ffffff")
        self.CarriageReturn.configure(highlightbackground="#ffffff")
        self.CarriageReturn.configure(justify=LEFT)
        self.CarriageReturn.configure(text='Carriage Return')

        self.HexAppear = Radiobutton(self.ConfFrame)
        self.HexAppear.place(relx=0.7, rely=0.25, relheight=0.2, relwidth=0.1)
        self.HexAppear.configure(text='HEX', variable=self.appearing, value='HEX')
        self.HexAppear.configure(background="#ffffff")

        self.DecAppear = Radiobutton(self.ConfFrame)
        self.DecAppear.place(relx=0.8, rely=0.25, relheight=0.2, relwidth=0.1)
        self.DecAppear.configure(text='DEC', variable=self.appearing, value='DEC')
        self.DecAppear.configure(background="#ffffff")

        self.ASCIIAppear = Radiobutton(self.ConfFrame)
        self.ASCIIAppear.place(relx=0.9, rely=0.25, relheight=0.2, relwidth=0.1)
        self.ASCIIAppear.configure(text='ASCII', variable=self.appearing, value='ASCII')
        self.ASCIIAppear.configure(background="#ffffff")

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

    def Connect(self):
        try:
            self.ttyS = serial.Serial(self.Port.get(), self.Baud.get())
            self.List_insert('Connected')
            self.run = True
            thread.start_new(self.Get_ttyS_Data, (True,))
        except:
            self.List_insert('Connection failed! Please, check for correct data entry.')

    def Disconnect(self):
        try:
            self.run = False
            self.ttyS.close()
            self.List_insert('Disconnected')
        except:
            self.List_insert('Nothing to disconnect.')
        print self.cr.get(), self.lf.get()

    def Send(self):
        if self.appearing.get() == 'HEX':
            l = ''
            line = self.Data.get()
            if self.cr.get():
                line = line + ' 0D'
            if self.lf.get():
                line = line + ' 0A'
            try:
                line = line.split(' ')
                for i in range(len(line)):
                    line[i] = eval('0x' + line[i])
                    l = l + hex(line[i]) + ' '
                for i in range(len(line)):
                    self.ttyS.write(line[i])
                self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + l)
            except:
                self.List_insert('Failed! Check your connecting or correct entry!')

        if self.appearing.get() == 'ASCII':
            line = self.Data.get()
            if self.cr.get():
                line = line + chr(13)
            if self.lf.get():
                line = line + chr(10)
            try:
                self.ttyS.write(line.encode('ascii','ignore'))
                self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + line)
            except:
                self.List_insert('Failed! Check your connecting or correct entry!')
        if self.appearing.get() == 'DEC':
            l = ''
            line = self.Data.get()
            if self.cr.get():
                line = line + ' 13'
            if self.lf.get():
                line = line + ' 10'
            try:
                line = line.split(' ')
                for i in range(len(line)):
                    line[i] = int(line[i])
                    l = l + str(line[i]) + ' '
                for i in range(len(line)):
                    self.ttyS.write(line[i])
                self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + l)
            except:
                self.List_insert('Failed! Check your connecting or correct entry!')

    def List_insert(self, data):
        self.ProgressList.insert('end', data)
        self.ProgressList.see('end')
        self.ProgressList.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.root.update()

    def Get_Port_List(self):
        lst = serial.tools.list_ports.comports()  # getting the list of available ports
        for i in range(len(lst)): # usualy for Mac
            if ' ' in str(lst[i]):  # attempt to find added data to path
                lst[i] = str(lst[i]).split(' ') # Deleting added data
                lst[i] = lst[i][0]
        self.Port.configure(values=[str(lst[i]) for i in range(len(lst))])

    def Get_ttyS_Data(self, *args):
        while self.run:
            line = ''
            if self.ttyS.inWaiting():
                data = self.ttyS.read(self.ttyS.inWaiting())

                if self.appearing.get() == 'HEX':
                    for i in range(len(data)):
                        line = line + hex(ord(data[i])) + ' '
                    self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + line)

                if self.appearing.get() == 'ASCII':
                    self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + data)

                if self.appearing.get() == 'DEC':
                    for i in range(len(data)):
                        line = line + ord(data[i]) + ' '
                    self.List_insert(str(datetime.datetime.now()) + ' Read >> ' + line)

print datetime.datetime.now()
root = Tk()
top = MORtty(root)
top.Get_Port_List()
root.mainloop()