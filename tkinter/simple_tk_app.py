import tkinter


class MyGui(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=5, pady=5)
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack(fill="both", expand=True, padx=5, pady=5)
        self.name = tkinter.StringVar()
        self.name.set("Ihr Name...")
        self.nameEntry["textvariable"] = self.name
        self.ok = tkinter.Button(self)
        self.ok["text"] = "Ok"
        self.ok["command"] = self.quit
        self.ok.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        self.rev = tkinter.Button(self)
        self.rev["text"] = "Umdrehen"
        self.rev["command"] = self.onReverse
        self.rev.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    def onReverse(self):
        self.name.set(self.name.get()[::-1])


root = tkinter.Tk()
gui = MyGui(root)
gui.mainloop()
