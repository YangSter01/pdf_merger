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

    output.write("output.pdf")


# Create application window and add frame -------
window = Tk()
window.title("PDF Merger")
window.geometry("350x150")

frame1 = Frame()
frame1.grid(padx=5, pady=5)

frame2 = Frame()
frame2.grid(padx=5, pady=5)

frame3 = Frame()
frame3.grid(padx=5, pady=5)


# Create and add text labels --------------------
label_file1 = Label(frame1, text="File 1")
label_file1.grid(row=1, column=1, sticky=S+E)

label_file2 = Label(frame2, text="File 2")
label_file2.grid(row=2, column=1, sticky=S+E)


# Blank label to hold name of chose file --------
label_file1_name = Label(frame1)
label_file1_name.grid(row=1, column=3)

label_file2_name = Label(frame2)
label_file2_name.grid(row=2, column=3)


# Create buttons for 'Open' file dialog ---------
button_open_file1 = Button(frame1, text="Choose PDF file 1", command=open_file1)
button_open_file1.grid(row=1, column=2)

button_open_file2 = Button(frame2, text="Choose PDF file 2", command=open_file2)
button_open_file2.grid(row=2, column=2)


# Create and add button for merging -------------
button_merge = Button(frame3, text="Merge", command=merge)
button_merge.grid(row=3, column=2, columnspan=2)


window.mainloop()
