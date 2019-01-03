MORtty - is a simple open source crossplatform Serial Terminal with UI.
I'm very glad that you choose MORtty for work. If you have any offers or
ideas please write on morttyserial@gmail.com

HOW TO INSTALL

MORtty is appearing as executable .py file. To start it you should:
1. Download and install Python 2.7.x
    https://www.python.org/downloads/

2. Download some libs with pip. After Python installation open terminal
(command line) and type:
    cd c://Python27/scripts (this command is only for Windows)
    pip install serial pyserial tkinterhtml (for any systems)

3. To execute MORtty you shod click on it (Windows) or type in terminal
    python MORtty.py (any systems)


HOW TO WORK.

When you executed MORtty successfully it will automatically check your
system for available serial ports and show this list in ComboBox.
For connection you should choose necessary port in ComboBox, type necessary
Baudrate (port speed) in textbox (default is 115200) and press CONNECT Button
or Menu->Main->Connect. If MORtty writes 'Connected' it means that the
connection successful. In unsuccessful case it will write 'Connection failed!'.

To disconnect from port press DISCONNECT Button or Menu->Main->Disconnect.

You can work with 3 types of data.
ASCII - string type (any letters, signs and numbers)
HEX - from 0x00 to 0xff
DEC - any decimals

If you choose ASCII type of data then you need to use only letters,
sings and numbers.

If you choose HEX type, you should write weather ASCII (it will be automatically
translate to HEX), or 00 to FF (without 0x). Bytes should be separate with space.
If you will type '0xFF' MORtty will recognize it as ascii string, and if 'FF'
than as hex (255 decimal). You can also type data that includes more then 1 byte,
for example E5FAD7 will send to port 3 bytes.

If you choose DEC type you should write any integer numbers (you can use sign)
separated with space.

If you need to add LF or/and CR to end of your string you should set appropriate
checkboxes.

To clear/reset data window choose Menu->Main->Clear.

WORK WITH FILES
With MORtty you can import end export data from/to any file you want.
To Export the data from data window you should choose Menu->Main->Export. The
Export window will be opened. You should type necessary file name and press
OK Button. You also can type Signature (Header) and End of file if necessary.
If you will set ONLY DATA checkbox, MORtty will import only data (without
time and 'READ >> ')

To Import any files you should choose Menu->Main->Import. The import window
will be opened. You should write necessary filename. You also can write
necessary Header and End of data and it will transmit in the start and in the
end of file!

THANKS THAT YOU WORK WITH US!