#coding: utf-8
from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

MainMenu = Menubutton(top, text='Main')
MainMenu.grid(row=0, column=0)
MainMenu.menu = Menu(MainMenu, tearoff=0)
MainMenu["menu"] = MainMenu.menu
MainMenu.menu.add_command(label="Connect")
MainMenu.menu.add_command(label="Disconnect")
MainMenu.menu.add_separator()
MainMenu.menu.add_command(label='Exit')

OptionsMenu = Menubutton(top, text='Options')
OptionsMenu.grid(row=0, column=1)
OptionsMenu.menu = Menu(OptionsMenu, tearoff=0)
OptionsMenu["menu"] = OptionsMenu.menu
OptionsMenu.menu.add_command(label='Settings')
OptionsMenu.menu.add_command(label='Macros')

AboutMenu = Menubutton(top, text='About')
AboutMenu.grid(row=0, column=2)
AboutMenu.menu = Menu(AboutMenu, tearoff=0)
AboutMenu["menu"] = AboutMenu.menu
AboutMenu.menu.add_command(label='Help')
AboutMenu.menu.add_separator()
AboutMenu.menu.add_command(label='About us')


top.mainloop()