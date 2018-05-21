from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os


# Define global list to hold files --------------
files = [0]*2


# Open file function ----------------------------
def open_file1():
    type_list = [("PDF files", "*.pdf")]
    file1_path = filedialog.askopenfilename(filetypes=type_list)
    file1_name = os.path.basename(file1_path)[:25]+'...'
    label_file1_name.config(text=file1_name)

    files[0] = file1_path

def open_file2():
    type_list = [("PDF files", "*.pdf")]
    file2_path = filedialog.askopenfilename(filetypes=type_list)
    file2_name = os.path.basename(file2_path)[:25]+'...'
    label_file2_name.config(text=file2_name)

    files[1] = file2_path

# Merge the files -------------------------------
def merge():
    output = PdfFileMerger()

    output.append(PdfFileReader(open(files[0], "rb")))
    output.append(PdfFileReader(open(files[1], "rb")))

    saved_file_name = filedialog.asksaveasfile(mode="wb", defaultextension=".pdf")
    if saved_file_name is None:
        return

    output.write(saved_file_name)


# Create application window and add frame -------
window = Tk()
window.title("PDF Merger")
window.geometry("350x120")

frame = Frame()
frame.grid(padx=5, pady=5)


# Create and add text labels --------------------
label_file1 = Label(frame, text="File 1")
label_file1.grid(row=0, column=0)

label_file2 = Label(frame, text="File 2")
label_file2.grid(row=1, column=0)


# Create buttons for 'Open' file dialog ---------
button_open_file1 = Button(frame, text="Choose PDF file 1", command=open_file1)
button_open_file1.grid(row=0, column=2, padx=2, pady=2)

button_open_file2 = Button(frame, text="Choose PDF file 2", command=open_file2)
button_open_file2.grid(row=1, column=2, padx=2, pady=2)


# Blank label to hold name of chose file --------
label_file1_name = Label(frame, width=25)
label_file1_name.grid(row=0, column=3)

label_file2_name = Label(frame, width=25)
label_file2_name.grid(row=1, column=3)


# Create and add button for merging -------------
button_merge = Button(frame, text="Merge", command=merge)
button_merge.grid(row=2, column=2, padx=2, pady=2, sticky=N+S+E+W)


window.mainloop()
