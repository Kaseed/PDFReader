import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

information = tk.Label(root, text = "Wybierz plik PDF", font = "Impact")
information.grid(columnspan = 3, column = 0, row = 1)

def openFile():
    buttonText.set("Wczytywanie...")

    file = askopenfile(parent = root, mode='rb', filetype = [("Pdf file", "*.pdf")])
    if file:
        readPdf = PyPDF2.PdfFileReader(file)
        page = readPdf.getPage(0)
        pageData = page.extractText()
        print(pageData)

        textBox = tk.Text(root, height = 15, width= 50, padx = 15, pady = 15)
        textBox.insert(1.0, pageData)
        textBox.configure(state='disabled', wrap = 'word')
        textBox.grid(column = 1, row = 3)

        buttonText.set("Wybierz plik")

buttonText = tk.StringVar()
button = tk.Button(root, textvariable = buttonText, command=lambda:openFile(), font = "Impact", bg = "#2596be", height = 2, width = 15)
buttonText.set("Wybierz plik")
button.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)

root.mainloop()
