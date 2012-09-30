from Tkinter import *
from pprint import pprint
class optionlist:
    def __init__(self, searchResult):
        self.result = searchResult
    
    def callback(self, event):
        pprint(event)
    
    def makeList(self):
        root = Tk()
        ListBox = Listbox(root)
        i=1
        for option in self.result:
           ListBox.insert(i,option['name'])
           i+1
        ListBox.bind("<Return>", self.callback)
        ListBox.pack()
        root.mainloop()
    
