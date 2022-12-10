import tkinter
from ctypes import *


def screenoff():
    windll.user32.PostMessageW( 0xffff , 0x0112 , 0xF170 , 2 )
    shell32 = windll.LoadLibrary( "shell32.dll" )
    shell32.ShellExecuteW( None , 'open' , 'rundll32.exe', 'USER32' , '' , 5 )


root = tkinter.Tk()
b = tkinter.Button( root , text = "turn off screen" , command = screenoff )
b.pack()
root.mainloop()