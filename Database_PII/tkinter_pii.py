from tkinter import *
from tkinter import ttk
import tkinter as tk
import json


window1 = tk.Tk()
window1.title("Authentification")
window1.iconbitmap("Icons/icon1.ico")
window1.geometry('750x500')

##   _________________________________________________________________________________

## Variables

## Page2

username_login = StringVar()
username_pass = StringVar()
user_test = StringVar()
pass_test = StringVar()

fname = StringVar()
lname = StringVar()
pass1 = StringVar()
pass2 = StringVar()
username = StringVar()
var_texte = StringVar()
var_texte2 = StringVar()

var_1 = StringVar()
pass_var = StringVar()
username_var = StringVar()
##   _________________________________________________________________________________

##   functions


## Database
#
#

def go_to_db(user):

    window1.destroy()
    window2.mainloop()
#
#
#

##   frame1/2

def page1():
    window1.configure(bg = "#34495e")
    frame1.pack(fill = 'x', expand = True)
    frame2.pack(fill = 'both', expand = True)

def page2():
    window1.configure(bg = '#388E8E')
    frame3.pack(fill = 'x', expand = True)
    frame4.pack(fill = 'both', expand = True)
    username_login.set("")
    username_pass.set("")
    user_test.set("")
    pass_test.set("")
    
def page3():
    window1.configure(bg = '#8B2323')
    frame5.pack(fill = 'x', expand = True)
    frame6.pack(fill = 'both', expand = True)
    fname.set("")
    lname.set("")
    pass1.set("")
    pass2.set("")
    username.set("")
    var_texte.set("")
    var_texte2.set("")
    var_1.set("")
    pass_var.set("")
    username_var.set("")


def login():
    frame1.pack_forget()
    frame2.pack_forget()
    page2()
    
def signup():
    frame1.pack_forget()
    frame2.pack_forget()
    page3()

def back2_1():
    username_login.set("")
    username_pass.set("")
    frame3.pack_forget()
    frame4.pack_forget()
    page1()

def next2_():
    user_ = username_login.get()
    pass_ = username_pass.get()
    user_test.set("")
    pass_test.set("")
    d = import_()
    if user_ not in d:
        user_test.set("Username doesn't exist!")
        username_login.set("")
        username_pass.set("")
    else:
        if d[user_] != pass_:
            user_test.set("")
            pass_test.set("Wrong password!")
            username_pass.set("")
        else:
            go_to_db(user_)

def reset1_(event):
    user_test.set("")
    pass_test.set("")

def next3_():
    d1 = import_()
    d2 = import2_()
    u = username.get()
    p1 = pass1.get()
    p2 = pass2.get()
    f = fname.get()
    l = lname.get()
    if (f=="" or l == "" or p1 == "" or p2 == "" or u == ""):
        var_texte.set("All information are requiered!")
        return
    else:
        test = False
        for i in f:
            if i != " ":
                test = True
        test1 = False
        for i in l:
            if i != " ":
                test1 = True
        test2 = False
        for i in p1:
            if i != " ":
                test2 = True
        test3 = False
        for i in p2:
            if i != " ":
                test3 = True
        test4 = False
        for i in u:
            if i != " ":
                test4 = True
        
        if not(test and test1 and test2 and test3 and test4):
            var_texte.set("All information are requiered!")
            return
        
    if u in d1:
        username.set("")
        username_var.set("Username already taken!")
        pass1.set("")
        pass2.set("")
    else:
        if len(u) < 5 or len(u) > 12:
            username_var.set("From 5 to 12 characters!")
            pass1.set("")
            pass2.set("")
            username.set("")
        else:
            if p1 != p2:
                pass_var.set("Password doesn't match!")
                pass1.set("")
                pass2.set("")
            else:
                if len(p1) < 5 or len(p1) > 12:
                    pass_var.set("Password between 5 and 12 characters!")
                    pass1.set("")
                    pass2.set("")
                else:
                    d1[u] = p1
                    save_dict(d1)
                    d2[u] = (f,l)
                    save2_dict(d2)
                    go_to_db(u)
def back3_1():
    frame5.pack_forget()
    frame6.pack_forget()
    fname.set("")
    lname.set("")
    pass1.set("")
    pass2.set("")
    username.set("")
    var_texte.set("")
    var_texte2.set("")
    var_1.set("")
    pass_var.set("")
    username_var.set("")
    page1()

def on_entry_firstname_change(event):
    var_texte.set("")
    new = fname.get()
    new = new.lower()
    var_texte2.set("")
    i = 0
    while i < len(new):
        y = new[i]
        if y not in "abcdefghijklmnopqrstuvwxyz-àáâãäåæçèéêëìíîïñòóôõöùúûüý":
            new = new[:i] + new[i+1:]
            var_texte2.set("Names musn't contain numbers or special characters!")
        else:
            i = i + 1
    if len(new)> 1:
        x = new[0]
        x = x.upper()
        new = x + new[1:]
    else:
        if len(new) == 1:
            x = new[0]
            x = x.upper()
            new = x
    if len(new) > 15:
        fname.set(new[:15])
        var_texte2.set("Name too long!")
    else:
        fname.set(new)

def on_entry_lastname_change(event):
    var_texte.set("")
    new = lname.get()
    new = new.lower()
    var_texte2.set("")
    i = 0
    while i < len(new):
        y = new[i]
        if y not in "abcdefghijklmnopqrstuvwxyz-àáâãäåæçèéêëìíîïñòóôõöùúûüý ":
            new = new[:i] + new[i+1:]
            var_texte2.set("Names musn't contain numbers or special characters!")
        else:
            i = i + 1
    if len(new)> 1:
        x = new[0]
        x = x.upper()
        new = x + new[1:]
    else:
        if len(new) == 1:
            x = new[0]
            x = x.upper()
            new = x
    if len(new) > 15:
        lname.set(new[:15])
        var_texte2.set("Name too long!")
    else:
        lname.set(new)
    
def reset_(event):
    pass_var.set("")
    username_var.set("")
    var_texte.set("")

## Dict

def save_dict(my_dict):
    with open('ID/my_dict.json', 'w') as f:
        json.dump(my_dict, f)


def import_():
    with open('ID/my_dict.json', 'r') as f:
        d = json.load(f)
        return d

def save2_dict(my_dict):
    with open('ID/my2_dict.json', 'w') as f:
        json.dump(my_dict, f)


def import2_():
    with open('ID/my2_dict.json', 'r') as f:
        d = json.load(f)
        return d

###


## Page 1

frame1 = tk.Frame(window1, bg = 'white')

label1 = tk.Label(frame1, text = 'WELCOME',fg = 'black', bg ='white', font = ('Arial',24))
label1.pack(pady = 20)

frame2 = tk.Frame(window1, bg ='#34495e')

page1()

image1 = tk.PhotoImage(file = 'Backgrounds/login_.png')
image2 = tk.PhotoImage(file = 'Backgrounds/sign_up.png')


button1 = tk.Button(frame2, image = image1, width = 241, height = 150, compound="center", command = login)
button1.pack()

labelx = tk.Label(frame2, text = "                         ", bg = '#34495e')
labelx.pack()

button2 = tk.Button(frame2, image = image2, width = 241, height=150, command = signup)
button2.pack()

## Page 2

bold_font = ('TkDefaultFont', 13, 'bold')
bold_font2 = ('TkDefaultFont', 10, 'bold','italic')

frame3 = tk.Frame(window1, bg = 'white')
label2 = tk.Label(frame3, text = 'LOGIN',fg = 'blue', bg ='white', font = ('Arial',24,'bold'))
label2.pack(pady = 20)

frame4 = tk.Frame(window1,bg = '#388E8E')

label3 = ttk.Label(frame4, text = "Username",font = bold_font, background = '#388E8E')
label3.grid(row = 0, pady = 0, column = 2)

entry0 = ttk.Entry(frame4, textvariable = username_login)
entry0.grid(row = 1, pady = 0, column = 2)
entry0.bind('<KeyRelease>', reset1_)

label4 = ttk.Label(frame4, textvariable = user_test, background = '#388E8E', font = bold_font2, foreground= "white")
label4.grid(row = 2, column = 2)


label5 = ttk.Label(frame4, text = "Password",font = bold_font, background = '#388E8E')
label5.grid(row = 3, column = 2)

entry1 = ttk.Entry(frame4, textvariable = username_pass, show = '●')
entry1.grid(row = 4, column = 2)
entry1.bind('<KeyRelease>', reset1_)

label6 = ttk.Label(frame4, textvariable = pass_test, background = '#388E8E', font = bold_font2, foreground= "white")
label6.grid(row = 5, column = 2)

button_back = ttk.Button(frame4, text = "Back",command= back2_1)
button_back.grid(row = 6, column = 1, padx = 25, pady = 20)

button_next = ttk.Button(frame4, text = "Next", command = next2_)
button_next.grid(row = 6, column = 3, padx = 25, pady = 20)

frame4.grid_columnconfigure(0, weight=1)
frame4.grid_columnconfigure(4, weight=1)

## Page 3

frame5 = tk.Frame(window1, bg = 'white')
label7 = tk.Label(frame5, text = 'SIGN UP',fg = 'red', bg ='white', font = ('Arial',24,'bold'))
label7.pack(pady = 20)

frame6 = tk.Frame(window1, bg ='#8B2323' )

label7 = ttk.Label(frame6, text = "First Name", font = bold_font, background ='#8B2323' )
label7.grid(row = 3, column = 1)

label8 = ttk.Label(frame6, text = "Last Name", font = bold_font, background= '#8B2323')
label8.grid(row = 3, column = 3)

entry3 = ttk.Entry(frame6, textvariable = fname)
entry3.grid(row = 4, column = 1)
entry3.bind('<KeyRelease>', on_entry_firstname_change)

entry4 = ttk.Entry(frame6, textvariable = lname)
entry4.grid(row = 4, column = 3)
entry4.bind('<KeyRelease>', on_entry_lastname_change)

space1 = ttk.Label(frame6, background='#8B2323', text = "")
space1.grid(row = 5, column = 1)

label9 = ttk.Label(frame6, text = "Create username", font = bold_font, background ='#8B2323' )
label9.grid(row = 6, column = 1)

entry4_ = ttk.Entry(frame6, textvariable = username)
entry4_.grid(row = 7, column = 1)
entry4_.bind('<KeyRelease>', reset_)

label10 = ttk.Label(frame6, background='#8B2323', textvariable = username_var, font = bold_font2, foreground= 'white')
label10.grid(row = 7, column = 2, columnspan = 2)

space2 = ttk.Label(frame6, background='#8B2323', text = "")
space2.grid(row = 8, column = 1)

label7 = ttk.Label(frame6, text = "Create password", font = bold_font, background ='#8B2323' )
label7.grid(row = 9, column = 1)

label8 = ttk.Label(frame6, text = "Confirm password", font = bold_font, background= '#8B2323')
label8.grid(row = 9, column = 3)

entry5 = ttk.Entry(frame6, textvariable = pass1, show = '●')
entry5.grid(row = 10, column = 1)
entry5.bind('<KeyRelease>', reset_)

entry6 = ttk.Entry(frame6, textvariable = pass2, show = '●')
entry6.grid(row = 10, column = 3)
entry6.bind('<KeyRelease>', reset_)

space3 = ttk.Label(frame6, background='#8B2323', text = "               ")
space3.grid(row = 3, column = 2)

button_n = ttk.Button(frame6, text = "Next", command = next3_)
button_n.grid(row =13, column = 3)

space4 = ttk.Label(frame6, background='#8B2323', textvariable = pass_var, font = bold_font2, foreground='white')
space4.grid(row = 11, column = 1, columnspan=3)

space5 = ttk.Label(frame6, background='#8B2323', text = "")
space5.grid(row = 12, column = 1)

button_b = ttk.Button(frame6, text = "Back", command = back3_1)
button_b.grid(row =13, column = 1)

frame6.grid_columnconfigure(0, weight=1)
frame6.grid_columnconfigure(4, weight=1)

var_text = ttk.Label(frame6, textvariable = var_texte, background ='#8B2323',foreground='white',font = bold_font2)
var_text.grid(row = 0, column = 1, columnspan = 3)

space4 = ttk.Label(frame6, background='#8B2323', text = "")
space4.grid(row = 1, column = 1)

var_text2 = ttk.Label(frame6, textvariable = var_texte2, background ='#8B2323',foreground='white',font = bold_font2)
var_text2.grid(row = 2, column = 1, columnspan = 3)


window1.mainloop()

