import pyperclip as pyperclip
import tkinter as tk

root = tk.Tk()
root.title("Paste Buddy uwu")
root.rowconfigure(0)
root.columnconfigure(0, minsize=800)

class PasteBox:
    def __init__(self, text):
        self.text = "Default Text"
    def clearText(self):
        self.text = ''
    def changeText(self, input):
        self.text = input

def handle_right_click(event):
    print("paste")
def handle_left_click(event):
    print("copy")




root.mainloop()
