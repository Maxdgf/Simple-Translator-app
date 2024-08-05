from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from googletrans import Translator
from googletrans import LANGUAGES
from tkinter import messagebox

# import os
# import requests
# import time


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.connController()
        self.title("Simple Translator")
        self.geometry("500x500")

        self.languages = languages = [lang for lang in LANGUAGES.values()]
        # print(self.languages)

        self.frame = Frame(self)
        self.frame.pack()

        self.menu = Menu(self)
        self.menu.add_command(label="Save as", command=self.saveTranslate)
        self.menu.add_command(label="Load file", command=self.selectFile)
        self.menu.add_command(label="Start translate", command=self.startTranslate)
        # self.netLabelconnection = Label(self, text="Internet connection: analyzing...")
        # self.netLabelconnection.pack(anchor="nw", side="top")
        self.btnExit = Button(self, text="exit", bg="red", command=self.exitApp)
        self.btnExit.pack(side="top", anchor="ne")
        self.fileLabel = Label(self, text="File: not selected!")
        self.fileLabel.pack(anchor="nw", side="top")
        self.langcombo1 = Combobox(self, values=self.languages)
        self.langcombo1.pack()
        self.inputField = scrolledtext.ScrolledText(self, width=250, height=20)
        self.inputField.pack()
        self.outputField = scrolledtext.ScrolledText(self, width=250, height=20)
        self.outputField.pack()

        self.config(menu=self.menu)

    def exitApp(self):
        self.destroy()

    # def connController(self):
    # while True:
    # try:
    # requests.get("http://www.google.com", timeout=5)
    # self.netLabelconnection.configure(text="Internet connection: normal")
    # except requests.ConnectionError:
    # self.netLabelconnection.configure(text="Internet connection: bad")

    # time.sleep(2)

    def selectFile(self):
        try:
            self.file_path = filedialog.askopenfilename(
                defaultextension=".txt", filetypes=[("TEXT files", "*.txt")]
            )
            self.file_name = self.file_path.split("/")[-1]
            # print(self.file_name)
            self.fileLabel.configure(text="File: " + self.file_name)
            if self.file_path:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    self.file_content = file.read()
                    self.inputField.insert("1.0", self.file_content)
        except:
            messagebox.showerror(
                "Error",
                "Please, chek a file format, must have txt format and try again.",
            )

    def saveTranslate(self):
        try:
            self.saveContent = self.outputField.get("1.0", "end")
            self.file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("TEXT files", "*.txt")]
            )
            if self.file_path:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(self.saveContent)
            if self.saveContent == "":
                messagebox.showerror("Error", "nothing to save!")

        except:
            messagebox.showerror("Error", "Please, try again.")

    def startTranslate(self):
        try:
            self.langValue = self.langcombo1.get()
            # print(self.langValue)
            self.textValue = str(self.inputField.get("1.0", "end-1c"))
            self.translator = Translator()
            self.translate = self.translator.translate(
                self.textValue, dest=self.langValue
            ).text
            # print(self.translate)
            self.outputField.delete("1.0", "end")

            self.outputField.insert("end", self.translate)
        except Exception as e:
            messagebox.showerror(
                "Error",
                "Please, chek input field, language\nvalue and internet connection",
            )
            # print("error: ", e)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
