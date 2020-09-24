import pyperclip as pyperclip
import tkinter as tk

root = tk.Tk()
root.title("Paste Buddy uwu")
root.resizable(width=False, height=False)
btn_frame = tk.Frame(master=root, padx=3, pady=3)
btn_frame.grid(row=0, column=0,  sticky='nsew')

global tracker
tracker = {
    "buttonCount": 0
}
class buddyButton:
    def __init__(self, text):
        self.text = "RIGHT CLICK TO PASTE"


    def clearText(self):
        self.text = ''

    def changeText(self, input):
        self.text = input

class PasteBox:
    def __init__(self, text):
        self.text = "Default Text"
    def clearText(self):
        self.text = ''
    def changeText(self, input):
        self.text = input

def handle_right_click(event):
    makeButton()
def handle_left_click(event):
    pyperclip.copy

def makeButton():#makes new buttons
    btn = tk.Button(master=btn_frame,height=3, width=40, text=displayFormat(pyperclip.paste(), 20))
    btn.grid(row=tracker["buttonCount"], column=0, sticky='nsew', padx=2, pady=2)
    btn.rowconfigure(0, weight=1)

    btn.bind("<Button-3>", handle_right_click)
    btn.bind("<Button-1>", handle_left_click)

    tracker["buttonCount"] += 1

def displayFormat(string, chop):#formats text to fit in buttons
    string = string.replace("\n","")
    if len(string) > chop:
        #print("string larger than chop")#testing
        #print("string[:"+str(chop)+"]+"+'"'+"......"+'"'+"+string[ ("+str(len(string)-chop)+"):"+str(len(string))+"]")#testing
        return string[:chop]+"......"+string[ (len(string)-chop):len(string) ]

    else:
        #print("string smaller than chop")#testing
        return string


makeButton()
root.mainloop()
