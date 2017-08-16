
# CIS168. Week 4/5 Team Project.  Ryan Behrens, Durias, 10/20/2016

from tkinter import *
from tkinter import messagebox
import random

class Application(Frame):
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)    
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create three buttons for the start menu"""
        # create first button
        self.bttnStart = Button(self, text = "START", command = main_game )
        self.bttnStart.grid()

        # create second button
        self.bttnHelp = Button(self, text = "HELP", command = help_window)
        self.bttnHelp.grid()	

        # create third button
        self.bttnExit = Button(self, text = "EXIT", command = close_window)
        self.bttnExit.grid()
        
# method to close the application with button
def close_window():
    root.destroy()
    
# method to open a window with instructions
def help_window():
    messagebox.showinfo("HELP", "Pick a spot on the board, but be careful" +
                        " there are mines everywhere!")

# opens a cell, run a check function here , check for: 1.bomb, 2. numhbers, 3.empty 
def _close(self,):
    # check for 1. 2. 3. here before we destroy the cell....
    self.grid_remove()

# right click changes text to '?' (Flag), and color to 'dark blue' 
def rightClick(event):
    event.widget['text'] = '?'
    event.widget['fg'] = 'dark blue'


def bang(self):
    print("BANG!")
    self['fg'] = 'red'
    self['text'] = 'B!'
    print('GAME OVER!!!')

# dbl right click changes text to 'B! (Bomb), and changes color to 'red'
def dblRightClick(event):
    event.widget['text'] = 'B!'
    event.widget['fg'] = 'red'

# allows program to run multiple functions with a button click event
#( ref(http://stackoverflow.com/questions/13865009/have-multiple-commands-when-button-is-pressed-in-tkinter-with-python-2-7)
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
        return combined_func
##
#allows a list of unknown length to be a parameter
#http://stackoverflow.com/questions/13865009/have-multiple-commands-when-button-is-pressed-in-tkinter-with-python-2-7
##
def CommonValueButton(*button):
    for i in button:
        i.destroy()

def GameOver(main):
    main.destroy()
    randomNumer = random.randint(1,2)
    if (randomNumer == 1):
        messagebox.showinfo("GAMEOVER", " Uh-Oh, you stepped on a bomb!")
    else:
        messagebox.showinfo("GAMEOVER", " HAHA You lost!")

#main game function
def main_game():
    # create a root window
        main = Tk()
        main.title("MineSweeper Remake")
        main.geometry("350x350")


        # create a frame in the window to hold other widgets
        mainApp = Frame(main)
        mainApp.grid()

        # create a label in the frame
        lbl1 = Label(mainApp, text = "")
        lbl1.grid(row = 90, column = 120)

        mainApp.bind("<Button-3>")
        
##
#got "lambda from source
#http://effbot.org/zone/tkinter-callbacks.htm
##
        #labels that hold values for the cells, set to ' ', can be changed
        lbl1 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl1.grid(row = 0, column = 0,)

        lbl2 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl2.grid(row = 0, column = 1)

        lbl3 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl3.grid(row = 0, column = 2)

        lbl4 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl4.grid(row = 0, column = 3)

        lbl5 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl5.grid(row = 0, column = 4)

        lbl6 = Label(mainApp,height = 2, width = 3, text = "9")
        lbl6.grid(row = 0, column = 5)

        lbl7 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl7.grid(row = 1, column = 0)

        lbl8 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl8.grid(row = 1, column = 1)

        lbl9 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl9.grid(row = 1, column = 2)

        lbl10 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl10.grid(row = 1, column = 3)

        lbl11 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl11.grid(row = 1, column = 4)

        lbl12 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl12.grid(row = 1, column = 5)

        lbl13 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl13.grid(row = 2, column = 0)

        lbl14 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl14.grid(row = 2, column = 1)

        lbl15 = Label(mainApp,height = 2, width = 3, text = "9")
        lbl15.grid(row = 2, column = 2)

        lbl16 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl16.grid(row = 2, column = 3)

        lbl17 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl17.grid(row = 2, column = 4)

        lbl18 = Label(mainApp,height = 2, width = 3, text = "9")
        lbl18.grid(row = 2, column = 5)

        lbl19 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl19.grid(row = 3, column = 0)

        lbl20 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl20.grid(row = 3, column = 1)

        lbl21 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl21.grid(row = 3, column = 2)

        lbl22 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl22.grid(row = 3, column = 3)

        lbl23 = Label(mainApp,height = 2, width = 3, text = "3",fg='purple')
        lbl23.grid(row = 3, column = 4)

        lbl24 = Label(mainApp,height = 2, width = 3, text = "9")
        lbl24.grid(row = 3, column = 5)

        lbl25 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl25.grid(row = 4, column = 0)

        lbl26 = Label(mainApp,height = 2, width = 3, text = "0")
        lbl26.grid(row = 4,column = 1 )

        lbl27 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl27.grid(row = 4, column = 2)

        lbl28 = Label(mainApp,height = 2, width = 3, text = "9")
        lbl28.grid(row = 4, column = 3)

        lbl29 = Label(mainApp,height = 2, width = 3, text = "2",fg='green')
        lbl29.grid(row = 4, column = 4)

        lbl30 = Label(mainApp,height = 2, width = 3, text = "1",fg='blue')
        lbl30.grid(row = 4, column = 5)
        
        #row 1
        bttn1 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn1.grid(row = 0, column = 0)
        bttn1.bind('<Button-3>',rightClick,)
        bttn1.bind('<Double-3>', dblRightClick,)

        bttn2 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn2.grid(row = 0, column = 1)
        bttn2.bind('<Button-3>',rightClick,)
        bttn2.bind('<Double-3>', dblRightClick,)

        bttn3 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn3.grid(row = 0, column = 2)
        bttn3.bind('<Button-3>',rightClick,)
        bttn3.bind('<Double-3>', dblRightClick,)

        bttn4 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))

        bttn4.grid(row = 0, column = 3)
        bttn4.bind('<Button-3>',rightClick,)
        bttn4.bind('<Double-3>', dblRightClick,)

        bttn5 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn5.grid(row = 0, column = 4)
        bttn5.bind('<Button-3>',rightClick,)
        bttn5.bind('<Double-3>', dblRightClick,)

        bttn6 = Button(mainApp, text = "   ",height = 1, command = lambda: GameOver(main))
        bttn6.grid(row = 0, column = 5)
        bttn6.bind('<Button-3>',rightClick,)
        bttn6.bind('<Double-3>', dblRightClick,)

        #row 2
        bttn7 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn7.grid(row = 1, column = 0)
        bttn7.bind('<Button-3>',rightClick,)
        bttn7.bind('<Double-3>', dblRightClick,)

        bttn8 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn8.grid(row = 1, column = 1)
        bttn8.bind('<Button-3>',rightClick,)
        bttn8.bind('<Double-3>', dblRightClick,)

        bttn9 = Button(mainApp, text = "   ",height = 1,
                       command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn9.grid(row = 1, column = 2)
        bttn9.bind('<Button-3>',rightClick,)
        bttn9.bind('<Double-3>', dblRightClick,)

        bttn10 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn10.grid(row = 1, column = 3)
        bttn10.bind('<Button-3>',rightClick,)
        bttn10.bind('<Double-3>', dblRightClick,)

        bttn11 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn11,bttn16,bttn17,bttn22,bttn23)) 
        bttn11.grid(row = 1, column = 4)
        bttn11.bind('<Button-3>',rightClick,)
        bttn11.bind('<Double-3>', dblRightClick,)

        bttn12 = Button(mainApp, text = "   ",height = 1, command = lambda: CommonValueButton(bttn12))
        bttn12.grid(row = 1, column = 5)
        bttn12.bind('<Button-3>',rightClick,)
        bttn12.bind('<Double-3>', dblRightClick,)

        # row 3
        bttn13 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn13.grid(row = 2, column = 0)
        bttn13.bind('<Button-3>',rightClick,)
        bttn13.bind('<Double-3>', dblRightClick,)

        bttn14 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn14.grid(row = 2, column = 1)
        bttn14.bind('<Button-3>',rightClick,)
        bttn14.bind('<Double-3>', dblRightClick,)

        bttn15 = Button(mainApp, text = "   ",height = 1, command = lambda: GameOver(main))
        bttn15.grid(row = 2, column = 2)
        bttn15.bind('<Button-3>',rightClick,)
        bttn15.bind('<Double-3>', dblRightClick,)

        bttn16 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn11,bttn16,bttn17,bttn22,bttn23))
        bttn16.grid(row = 2, column = 3)
        bttn16.bind('<Button-3>',rightClick,)
        bttn16.bind('<Double-3>', dblRightClick,)

        bttn17 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn11,bttn16,bttn17,bttn22,bttn23))
        bttn17.grid(row = 2, column = 4)
        bttn17.bind('<Button-3>',rightClick,)
        bttn17.bind('<Double-3>', dblRightClick,)

        bttn18 = Button(mainApp, text = "   ",height = 1, command = lambda: GameOver(main))
        bttn18.grid(row = 2, column = 5)
        bttn18.bind('<Button-3>',rightClick,)
        bttn18.bind('<Double-3>', dblRightClick,)

        #row 4
        bttn19 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn19.grid(row = 3, column = 0)
        bttn19.bind('<Button-3>',rightClick,)
        bttn19.bind('<Double-3>', dblRightClick,)

        bttn20 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn20.grid(row = 3, column = 1)
        bttn20.bind('<Button-3>',rightClick,)
        bttn20.bind('<Double-3>', dblRightClick,)

        bttn21 = Button(mainApp, text = "   ",height = 1, command = lambda: CommonValueButton(bttn21))
        bttn21.grid(row = 3, column = 2)
        bttn21.bind('<Button-3>',rightClick,)
        bttn21.bind('<Double-3>', dblRightClick,)

        bttn22 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn11,bttn16,bttn17,bttn22,bttn23))
        bttn22.grid(row = 3, column = 3)
        bttn22.bind('<Button-3>',rightClick,)
        bttn22.bind('<Double-3>', dblRightClick,)

        bttn23 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn11,bttn16,bttn17,bttn22,bttn23))
        bttn23.grid(row = 3, column = 4)
        bttn23.bind('<Button-3>',rightClick,)
        bttn23.bind('<Double-3>', dblRightClick,)

        bttn24 = Button(mainApp, text = "   ",height = 1, command = lambda: GameOver(main))
        bttn24.grid(row = 3, column = 5)
        bttn24.bind('<Button-3>',rightClick,)
        bttn24.bind('<Double-3>', dblRightClick,)

        #row 5
        bttn25 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,
                                                          bttn7,bttn13,bttn19,bttn25,bttn26))
        bttn25.grid(row = 4, column = 0)
        bttn25.bind('<Button-3>',rightClick,)
        bttn25.bind('<Double-3>', dblRightClick,)

        bttn26 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,
                                                          bttn7,bttn13,bttn19,bttn25,bttn26))
        bttn26.grid(row = 4, column = 1)
        bttn26.bind('<Button-3>',rightClick,)
        bttn26.bind('<Double-3>', dblRightClick,)

        bttn27 = Button(mainApp, text = "   ",height = 1,
                        command = lambda: CommonValueButton(bttn1,bttn2,bttn3,bttn4,bttn5,
                        bttn7,bttn8,bttn9,bttn10,bttn13,bttn14,bttn19,bttn20,bttn25,bttn26,bttn27))
        bttn27.grid(row = 4, column = 2)
        bttn27.bind('<Button-3>',rightClick,)
        bttn27.bind('<Double-3>', dblRightClick,)

        bttn28 = Button(mainApp, text = "   ",height = 1, command = lambda: GameOver(main))
        bttn28.grid(row = 4, column = 3)
        bttn28.bind('<Button-3>',rightClick,)
        bttn28.bind('<Double-3>', dblRightClick,)

        bttn29 = Button(mainApp, text = "   ",height = 1, command = lambda: CommonValvuesButton(bttn29,bttn30))
        bttn29.grid(row = 4, column = 4)
        bttn29.bind('<Button-3>',rightClick,)
        bttn29.bind('<Double-3>', dblRightClick,)

        bttn30 = Button(mainApp, text = "   ",height = 1, command = lambda: CommonValvuesButton(bttn29,bttn30))
        bttn30.grid(row = 4, column = 5)
        bttn30.bind('<Button-3>',rightClick,)
        bttn30.bind('<Double-3>', dblRightClick,)


      
        # the root window's event loop
        main.mainloop()



# Start Menu
root = Tk()   
root.title("MineSweeper")
root.geometry("250x150")
app = Application(root)
root.mainloop()
