import string
import tkinter.font as tkf
import tkinter.ttk as ttk
import random
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import *

window = Tk()
window.title("Caesar Encryption")
window.geometry("400x500")
TAB_CONTROL = ttk.Notebook(window)
helv10 = tkf.Font(family="Helvetica", size=10, weight="bold")

TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Caesar Encoder')
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Caesar Decoder')
TAB_CONTROL.pack(expand=1, fill="both")


def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[int(shift):] + alphabet[:int(shift)]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


def click_encode(key):
    plain_text = sctText.get("1.0", 'end-1c')
    key = cboShift.get()
    if key == '':
        messagebox.showinfo('Error:', 'Please choose shift!')
        res = "Invalid Input"
    else:
        try:
            key = int(key) % 26
            if var1.get() == 1 and var2.get() == 0:
                res = caesar(plain_text, key, [string.ascii_lowercase])
            elif var1.get() == 0 and var2.get() == 1:
                res = caesar(plain_text, key, [string.ascii_uppercase])
            elif var1.get() == 0 and var2.get() == 0:
                messagebox.showinfo('Error:', 'Please choose Lowercase, Uppercase or both!')
                res = "Invalid Input"
            else:
                res = caesar(plain_text, key, [string.ascii_lowercase, string.ascii_uppercase])
        except Exception:
            messagebox.showinfo('Error:', 'Shift must be integer!')
            res = "Invalid Input"

    sctRes.delete("1.0", END)
    sctRes.insert("1.0", res)


def rand(num):
    num = random.randrange(1, 26, 1)
    cboShift.delete(0, END)
    cboShift.insert(0, num)


text = Label(TAB1, text='Paste the text you wish to Caesar encode here:', font=helv10)
text.place(x=7, y=3)
sctText = scrolledtext.ScrolledText(TAB1, width=45, height=8)
sctText.place(x=10, y=25)
sctText.insert(INSERT, 'Your text go here')

shift = Label(TAB1, text='Shift')
shift.place(x=7, y=170)
cboShift = Entry(TAB1, width=20)
cboShift.place(x=43, y=170)
randb = Button(TAB1, text='Random Shift', padx=8, pady=8)
randb.bind("<Button-1>", rand)
randb.place(x=288, y=170)
encode = Button(TAB1, text='Caesar Encode!', padx=5, pady=8)
encode.bind("<Button-1>", click_encode)
encode.place(x=286, y=220)
var1 = IntVar()
var1.set(1)
var2 = IntVar()
ckbOpt1 = Checkbutton(TAB1, text="Lowercase", var=var1)
ckbOpt1.place(x=7, y=190)

ckbOpt2 = Checkbutton(TAB1, text="Uppercase", var=var2)
ckbOpt2.place(x=7, y=210)

res = Label(TAB1, text='Copy your Caesar encoded text here:', font=helv10)
res.place(x=7, y=270)
sctRes = scrolledtext.ScrolledText(TAB1, width=45, height=8)
sctRes.place(x=10, y=292)


def click_decode(key):
    plain_text = sctText1.get("1.0", 'end-1c')
    key = cboShift1.get()
    if key == '':
        messagebox.showinfo('Error:', 'Please choose shift!')
        res = "Invalid Input"
    else:
        try:
            key = int(key) % 26
            if var3.get() == 1 and var4.get() == 0:
                res = caesar(plain_text, 26-key, [string.ascii_lowercase])
            elif var3.get() == 0 and var4.get() == 1:
                res = caesar(plain_text, 26-key, [string.ascii_uppercase])
            elif var3.get() == 0 and var4.get() == 0:
                messagebox.showinfo('Error:', 'Please choose Lowercase, Uppercase or both!')
                res = "Invalid Input"
            else:
                res = caesar(plain_text, 26-key, [string.ascii_lowercase, string.ascii_uppercase])
        except Exception:
            messagebox.showinfo('Error:', 'Shift must be integer!')
            res = "Invalid Input"

    sctRes1.delete("1.0", END)
    sctRes1.insert("1.0", res)


def all_shift(key):
    plain_text = sctText1.get("1.0", 'end-1c')
    sctRes1.delete("1.0", END)
    for key in range(25, 0, -1):
        res = caesar(plain_text, 26 - key, [string.ascii_lowercase, string.ascii_uppercase])
        sctRes1.insert("1.0", '{0}: {1}'.format(key, res) + '\n')
    sctRes1.insert("1.0", 'Decode lowercase & uppercase with all shift:' + '\n')
    for key in range(25, 0, -1):
        res = caesar(plain_text, 26 - key, [string.ascii_uppercase])
        sctRes1.insert("1.0", '{0}: {1}'.format(key, res) + '\n')
    sctRes1.insert("1.0", 'Decode uppercase with all shift:' + '\n')
    for key in range(25, 0, -1):
        res = caesar(plain_text, 26 - key, [string.ascii_lowercase])
        sctRes1.insert("1.0", '{0}: {1}'.format(key, res) + '\n')
    sctRes1.insert("1.0", 'Decode lowercase with all shift:' + '\n')

text1 = Label(TAB2, text='Paste the text you wish to Caesar decode here:', font=helv10)
text1.place(x=7, y=3)
sctText1 = scrolledtext.ScrolledText(TAB2, width=45, height=8)
sctText1.place(x=10, y=25)
sctText1.insert(INSERT, 'Your text go here')

shift1 = Label(TAB2, text='Shift')
shift1.place(x=7, y=170)
cboShift1 = Entry(TAB2, width=20)
cboShift1.place(x=43, y=170)
allb = Button(TAB2, text='All Case', padx=24, pady=8)
allb.bind("<Button-1>", all_shift)
allb.place(x=288, y=170)
decode = Button(TAB2, text='Caesar Decode!', padx=5, pady=8)
decode.bind("<Button-1>", click_decode)
decode.place(x=286, y=220)

var3 = IntVar()
var4 = IntVar()
ckbOpt3 = Checkbutton(TAB2, text="Lowercase", var=var3)
ckbOpt3.place(x=7, y=190)
ckbOpt4 = Checkbutton(TAB2, text="Uppercase", var=var4)
ckbOpt4.place(x=7, y=210)

res1 = Label(TAB2, text='Copy your Caesar decoded text here:', font=helv10)
res1.place(x=7, y=270)
sctRes1 = scrolledtext.ScrolledText(TAB2, width=45, height=8)
sctRes1.place(x=10, y=292)


window.mainloop()