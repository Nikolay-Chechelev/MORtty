#!/usr/local/bin/python
#coding: utf-8
from tkinter import *
import tkinter.ttk as ttk
import serial, time, datetime, thread
import serial.tools.list_ports
from tkinterhtml import HtmlFrame
import urllib



class MORtty:
    def __init__(self, parent):
        self.root = parent
        self.root.geometry("800x500")
        self.root.title("MORtty Terminal")
        self.root.configure(background="white")

        self.ttyS = None
        self.run = False

        self.appearing = StringVar()
        self.appearing.set('ASCII')
        self.lf = IntVar()
        self.cr = IntVar()

        self.BaseFrame = Frame(self.root)
        self.BaseFrame.place(relx=0.0, rely=0.0, relheight=0.05, relwidth=1.0)
        self.MORttyMenu = Menu(self.BaseFrame)
        self.root.config(menu=self.MORttyMenu)

        self.MainMenu = Menubutton(self.BaseFrame, text='Main')
        self.MainMenu.grid(row=0, column=0)
        self.MainMenu.menu = Menu(self.MainMenu, tearoff=0)
        self.MainMenu["menu"] = self.MainMenu.menu
        self.MainMenu.menu.add_command(label="Connect", command=self.Connect)
        self.MainMenu.menu.add_command(label="Disconnect", command=self.Disconnect)
        self.MainMenu.menu.add_separator()
        self.MainMenu.menu.add_command(label="Clear", command=self.Clear)
        self.MainMenu.menu.add_separator()
        self.MainMenu.menu.add_command(label='Exit', command=self.Exit)

        self.OptionsMenu = Menubutton(self.BaseFrame, text='Features')
        self.OptionsMenu.grid(row=0, column=1)
        self.OptionsMenu.menu = Menu(self.OptionsMenu, tearoff=0)
        self.OptionsMenu["menu"] = self.OptionsMenu.menu
        self.OptionsMenu.menu.add_command(label='Export to file', command=self.ExportFile)
        self.OptionsMenu.menu.add_command(label='Import file', command=self.ImportFile)

        self.AboutMenu = Menubutton(self.BaseFrame, text='About')
        self.AboutMenu.grid(row=0, column=2)
        self.AboutMenu.menu = Menu(self.AboutMenu, tearoff=0)
        self.AboutMenu["menu"] = self.AboutMenu.menu
        self.AboutMenu.menu.add_command(label='Help', command=self.Help)
        self.AboutMenu.menu.add_separator()
        self.AboutMenu.menu.add_command(label='About us')

        self.ConfFrame = Frame(self.root)
        self.ConfFrame.place(relx=0.0, rely=0.05, relheight=0.2, relwidth=1.0)
        self.ConfFrame.configure(relief=GROOVE)
        self.ConfFrame.configure(borderwidth="1")
        self.ConfFrame.configure(relief=GROOVE)
        self.ConfFrame.configure(background="#ffffff")
        self.ConfFrame.configure(width=255)

        self.ConnectButton = Button(self.ConfFrame)
        self.ConnectButton.place(relx=0.01, rely=0.05, height=30, width=100)
        self.ConnectButton.configure(activebackground="#e0ffff")
        self.ConnectButton.configure(background="#ffffff")
        self.ConnectButton.configure(text='Connect')
        self.ConnectButton.configure(command=self.Connect)

        self.DisconnectButton = Button(self.ConfFrame)
        self.DisconnectButton.place(relx=0.01, rely=0.5, height=30, width=100)
        self.DisconnectButton.configure(activebackground="#e0ffff")
        self.DisconnectButton.configure(background="#ffffff")
        self.DisconnectButton.configure(text='Disconnect')
        self.DisconnectButton.configure(command=self.Disconnect)

        self.Port = ttk.Combobox(self.ConfFrame)
        self.Port.place(relx=0.15, rely=0.05, height=30, width=150)

        self.Baud = Entry(self.ConfFrame)
        self.Baud.place(relx=0.35, rely=0.05, height=30, width=150)
        self.Baud.insert(0, '115200')

        self.Data = Entry(self.ConfFrame)
        self.Data.place(relx=0.15, rely=0.5, height=30, width=500)
        self.Data.configure(background="#ffffff")

        self.SendButton = Button(self.ConfFrame)
        self.SendButton.place(relx=0.85, rely=0.5, height=30, width=100)
        self.SendButton.configure(activebackground="#e0ffff")
        self.SendButton.configure(background="#ffffff")
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

        self.ProgressFrame = Frame(self.root)
        self.ProgressFrame.place(relx=0.0, rely=0.25, relheight=0.75, relwidth=1.0)
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

        self.Scale1 = Scrollbar(self.ProgressList)
        self.Scale1.pack(side=RIGHT, fill=Y)
        self.Scale1.configure(activebackground="#ffffff")
        self.Scale1.configure(background="#ffffff")
        self.Scale1.configure(highlightbackground="#ffffff")
        self.Scale1.configure(troughcolor="#ffffff")

        self.ProgressList.configure(yscrollcommand=self.Scale1.set)
        self.Scale1.config(command=self.ProgressList.yview)
        thread.start_new(self.Get_Port_List, (None,))

    def mainloop(self):
        self.root.update()
        self.root.mainloop()

    def Connect(self):
        try:
            self.ttyS = serial.Serial(self.Port.get(), self.Baud.get())
            self.List_insert('Connected')
            self.run = True
            thread.start_new(self.Get_ttyS_Data, (True,))
        except:
            self.List_insert('Connection failed! Please, check for correct data entry.')

    def Disconnect(self):
        self.run = False
        try:
            if self.ttyS.isOpen():
                self.ttyS.close()
                self.List_insert('Disconnected')
            else:
                self.List_insert('Nothing to disconnect.')
        except:
            self.List_insert('Nothing to disconnect.')

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
                try:
                    l = ''
                    line = self.Data.get()
                    if self.cr.get():
                        line = line + ' 0D'
                    if self.lf.get():
                        line = line + ' 0A'
                    for i in range(len(line)):
                        self.ttyS.write(line[i])
                        l = l + hex(ord(line[i])) + ' '
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

    def Get_Port_List(self, *args):
        while 1:
            lst = serial.tools.list_ports.comports()  # getting the list of available ports
            for i in range(len(lst)): # usualy for Mac
                if ' ' in str(lst[i]):  # attempt to find added data to path
                    lst[i] = str(lst[i]).split(' ') # Deleting added data
                    lst[i] = lst[i][0]
            self.Port.configure(values=[str(lst[i]) for i in range(len(lst))])
            time.sleep(0.5)

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

    def ExportFile(self):
        d = Dialog('Export File')
        d.mainloop()

    def ImportFile(self):
        d = Dialog('Import File')
        d.mainloop()

    def Help(self):
        w = HelpWindow()
        w.mainloop()

    def Exit(self):
        exit()

    def Clear(self):
        for i in range(self.ProgressList.size()):
            self.ProgressList.delete('end')
        return 0

class HelpWindow():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("MORtty Terminal - Info")
        self.root.configure(background="white")
        self.WebPage = HtmlFrame(self.root)
        self.WebPage.set_content('''<p align=center>hgihk</p>''')
        self.WebPage.place(relx=0.0, rely=0.0, relheight=0.9, relwidth=1.0)

        self.ButtonFrame = Frame(self.root)
        self.ButtonFrame.place(relx=0.0, rely=0.9, relheight=0.1, relwidth=1.0)

        self.Closebutton = Button(self.ButtonFrame)
        self.Closebutton.configure(text='Close', command=self.root.destroy)
        self.Closebutton.place(relx=0.5, rely=0.5, anchor='center')

    def mainloop(self):
        self.root.mainloop()


class Dialog():
    def __init__(self, text):
        self.root = Tk()
        self.text = text
        self.root.title("MORtty Terminal - " + self.text)
        self.root.configure(background="white")

        self.cleandat = IntVar()

        self.label1 = Label(self.root, text='Filename: ')
        self.label1.grid(row=0, column=0)
        self.Name = Entry(self.root)
        self.Name.grid(row=0, column=1)

        self.label2 = Label(self.root, text='Signature: ')
        self.label2.grid(row=1, column=0)
        self.Signature = Entry(self.root)
        self.Signature.grid(row=1, column=1)

        self.label3 = Label(self.root, text='End: ')
        self.label3.grid(row=2, column=0)
        self.End = Entry(self.root)
        self.End.grid(row=2, column=1)

        self.Data = Checkbutton(self.root, text='Only data')
        self.Data.configure(variable=self.cleandat)
        self.Data.grid(row=3, columnspan=2)

        self.CancelButton = Button(self.root, text='Cancel', command=self.root.destroy)
        self.CancelButton.grid(row=4, column=0)
        self.OKButton = Button(self.root, text='OK', command=self.FileRW)
        self.OKButton.grid(row=4, column=1)

    def FileRW(self):
        if 'Export' in self.text:
            f = open(self.Name.get(), 'w')
            f.write(self.Signature.get())
            f.write(chr(13) + chr(10))
            for i in range(m.ProgressList.size()):
                print self.cleandat.get()
                if self.cleandat.get() == True:
                    f.write(m.ProgressList.get(i).split(' Read >> ')[1])
                    f.write(chr(13)+chr(10))
                else:
                    f.write(m.ProgressList.get(i))
                    f.write(chr(13) + chr(10))
            f.write(self.End.get())
            f.close()

    def mainloop(self):
        self.root.mainloop()

        


m = MORtty(Tk())
m.mainloop()
