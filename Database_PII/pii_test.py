from tkinter import ttk
from tkinter import *
import tkinter as tk
import json
import pymongo

window1 = tk.Tk()
window1.title("Authentification")
window1.iconbitmap("Icons/icon1.ico")
window1.geometry('750x500')


class Database:

    def __init__(self, username, location = "mongodb://localhost:27017/"):
        x = pymongo.MongoClient(location)
        db = x[username]
        self.db = db
        self.types = db['Types']
        self.rel_def = db['Relationships_def']
        self.rel = db['Relationships']
    
    def create_types(self,d_type):
        types = self.types
        types.insert_one(d_type)
    
    def add_node(self, type_name, dict_):
        type = self.db[type_name]
        type.insert_one(dict_)
    
    def attributes(self,type_name):
        type = self.types
        query = {'Name of type ':type_name}
        results = type.find(query)
        for elt in results:
            result = elt
        x = 0
        result2 = {}
        for elt in result:
            if x > 1:
                result2[elt] = result[elt]
            x = x + 1  
        return result2
    
    def retrieve_id(self,type, dict_):
        query = dict_
        collection = self.db[type]
        results = collection.find(query)
        for elt in results:
            result = elt
        id = result['_id']
        return id
    
    def retrieve_idrel(self, type1, type2, name1, name2):
        d = {'Type 1':type1, 'Type2':type2, 'Name1':name1,'Name2':name2}
        collection = self.rel_def
        results = collection.find_one(d)
        for elt in results:
            result = elt
        id = result['_id']
        return id
    
    def define_relationship(self,type1, type2, name1, name2):
        rel = self.rel_def
        d = {'Type 1':type1, 'Type2':type2, 'Name1':name1,'Name2':name2}
        rel.insert_one(d)
    
    def add_relationship(self, id1, id2, id3):
        rel = self.rel
        d = {'Relationship' : id1, 'Node 1': id2, 'Node 2' : id3}
        rel.insert_one(d)
    
    def is_in_db(self, type, dict_):
        collection = self.db[type]
        results = collection.find_one(dict_)
        if results != None:
            return True
        else:
            return False

def go_to_db(user_):

    window1.destroy()

    db = Database(user_)


    d_condition = {'A':'No Conditions', 'B':'Only Letters','C':'Number','D': 'Integer','E':"Yes or No"}



    ### Functions



    def add_():
        framep1.pack_forget()
        frame_add1.pack(fill = 'y')

    def to_home():
        frame_add1.pack_forget()
        framep1.pack(fill = 'y')
        b.set(0)

    def create_type():
        frame_add1.pack_forget()
        frame_newtype.pack()
        row_var.set(0)
        button_var.set('Save (& Add)')
        condition.set("A")
        button1_1_2.grid(row =9, column = 7 )
        button2_1_2.grid(row =9, column = 8)
        button3_1_2.grid(row =9, column = 9)
        button4_1_2.grid(row =9, column = 10)
        button5_1_2.grid(row =9, column = 11)
        label2_2.grid(row =7, column = 7, padx = 10)
        label3_2.grid(row =7, column = 8, padx = 10)
        label4_2.grid(row =7, column = 9, padx = 10)
        label5_2.grid(row =7, column = 10, padx = 10)
        label6_2.grid(row =7, column = 11, padx = 10)
        att1_2.grid(row = 9, column = 5)
        global d
        d = {'Name of type ':''}

    def add_att():
        global d
        a = select_condition()
        z = row_var.get()
        y = att1.get()
        l = y.split()
        y = ''
        for elt in l:
            y = y + elt + " "
        if y == '':
            x0 = 1
        elif y in d:
            att1.set('')
            x4.grid(row = 3, column = 6, columnspan = 3)
            condition.set('A')

        elif z == 0:
            global x1
            att_test.set(True)
            x4.grid_forget()
            button1_1_2.grid(row = 10, column = 7)
            button2_1_2.grid(row = 10, column = 8)
            button3_1_2.grid(row = 10, column = 9)
            button4_1_2.grid(row = 10, column = 10)
            button5_1_2.grid(row = 10, column = 11)
            button_variable.grid_configure(row = 11)
            att1_2.grid_configure(row = 10)
            t = d_condition[a]
            d[y] = t
            x1.configure(text = " " + y + " ")
            x2.configure(text = t)
            x1.grid(row = 9, column = 5, pady = 10)
            x2.grid(row = 9, column = 6, pady = 10)
            att1.set('')
            condition.set('A')
            row_var.set(1)
        
        elif z == 1:
            x4.grid_forget()
            button1_1_2.grid(row = 11, column = 7)
            button2_1_2.grid(row = 11, column = 8)
            button3_1_2.grid(row = 11, column = 9)
            button4_1_2.grid(row = 11, column = 10)
            button5_1_2.grid(row = 11, column = 11)
            button_variable.grid_configure(row = 12)
            att1_2.grid_configure(row = 11)
            t = d_condition[a]
            d[y] = t
            x1_.configure(text = " " + y + " ")
            x2_.configure(text = t)
            x1_.grid(row = 10, column = 5, pady = 10)
            x2_.grid(row = 10, column = 6, pady = 10)
            att1.set('')
            condition.set('A')
            row_var.set(2)

        elif z == 2:
            x4.grid_forget()
            button1_1_2.grid(row = 12, column = 7)
            button2_1_2.grid(row = 12, column = 8)
            button3_1_2.grid(row = 12, column = 9)
            button4_1_2.grid(row = 12, column = 10)
            button5_1_2.grid(row = 12, column = 11)
            button_variable.grid_configure(row = 13)
            att1_2.grid_configure(row = 12)
            t = d_condition[a]
            d[y] = t
            x_1.configure(text = " " + y + " ")
            x_2.configure(text = t)
            x_1.grid(row = 11, column = 5, pady = 10)
            x_2.grid(row = 11, column = 6, pady = 10)
            att1.set('')
            condition.set('A')
            row_var.set(3)

        elif z == 3:
            x4.grid_forget()
            button1_1_2.grid(row = 13, column = 7)
            button2_1_2.grid(row = 13, column = 8)
            button3_1_2.grid(row = 13, column = 9)
            button4_1_2.grid(row = 13, column = 10)
            button5_1_2.grid(row = 13, column = 11)
            button_variable.grid_configure(row = 14)
            att1_2.grid_configure(row = 13)
            t = d_condition[a]
            d[y] = t
            x_1_.configure(text = " " + y + " ")
            x_2_.configure(text = t)
            x_1_.grid(row = 12, column = 5, pady = 10)
            x_2_.grid(row = 12, column = 6, pady = 10)
            att1.set('')
            condition.set('A')
            button_var.set(" Save ")
            row_var.set(4)

        elif z == 4:
            x4.grid_forget()
            button1_1_2.grid_forget()
            button2_1_2.grid_forget()
            button3_1_2.grid_forget()
            button4_1_2.grid_forget()
            button5_1_2.grid_forget()
            label3_2.grid_forget()
            label2_2.grid_forget()
            label4_2.grid_forget()
            label5_2.grid_forget()
            label6_2.grid_forget()
            x3 = ttk.Label(frame_newtype, text = '          ', background = '#8B0000')
            x3.grid(row = 3, column = 12)
            button_variable.grid_forget()
            att1_2.grid_forget()
            t = d_condition[a]
            x1_5.configure(text =" "+ y + " ")
            x2_5.configure(text = t)
            d[y] = t
            x1_5.grid(row = 13, column = 5, pady = 10)
            x2_5.grid(row = 13, column = 6, pady = 10)
            row_var.set(5)
        
        else:
            x1 = 0

    def quit_frame_new_type():
        x1.grid_forget()
        x2.grid_forget()
        x1_.grid_forget()
        x2_.grid_forget()
        x_1_.grid_forget()
        x_2_.grid_forget()
        x_1.grid_forget()
        x_2.grid_forget()
        x1_5.grid_forget()
        x2_5.grid_forget()
        type_name.set("")
        b.set(0)
        att1.set("")
        condition.set("")
        row_var.set(0)
        button_var.set("")
        att_test.set(False)
        frame_newtype.pack_forget()
        frame_add1.pack(fill = 'y')



    def save_type():
        x4.grid_forget()
        y = type_name.get()
        dict_ = import_names(user_)
        test = False
        x = att_test.get()
        for elt in y:
            if elt != " ":
                test = True
        
        if y == '' or test == False or len(y) >10:
            x4.grid_forget()
            x4.configure(text = 'Type name between 1 and 10 caracters' )
            x4.grid(row = 3, column = 6, columnspan = 3)
            type_name.set("")
        
        elif y in dict_:
            x4.grid_forget()
            x4.configure(text = 'Type already added' )
            x4.grid(row = 3, column = 6, columnspan = 3)
            type_name.set("")
        
        elif x == False:
            x4.grid_forget()
            x4.configure(text = 'Add & Save at least one attribute' )
            x4.grid(row = 3, column = 6, columnspan = 3)
        
        else:
            global d
            d['Name of type '] = y
            dict_[y] = " "
            save_names(dict_, user_)
            db.create_types(d)
            quit_frame_new_type()

    def select_condition():
        y = condition.get()
        return y

    def att_1_set_():
        y = bool1.get()
        att_1.set(y)

    def att_2_set_():
        y = bool2.get()
        att_2.set(y)

    def att_3_set_():
        y = bool3.get()
        att_3.set(y)

    def att_4_set_():
        y = bool4.get()
        att_4.set(y)

    def att_5_set_():
        y = bool5.get()
        att_5.set(y)

    def back_addpage():
        x1.grid_forget()
        x2.grid_forget()
        x1_.grid_forget()
        x2_.grid_forget()
        x_1_.grid_forget()
        x_2_.grid_forget()
        x_1.grid_forget()
        x_2.grid_forget()
        x1_5.grid_forget()
        x2_5.grid_forget()
        type_name.set("")
        b.set(0)
        att1.set("")
        condition.set("")
        row_var.set(0)
        button_var.set("")
        att_test.set(False)
        frame_newtype.pack_forget()
        frame_add1.pack(fill = 'y')

    def frameadd_1():
        enrty5_1.grid_forget() 
        enrty5_2.grid_forget() 
        enrty5_3.grid_forget() 
        enrty5_4.grid_forget() 
        enrty5_5.grid_forget() 
        label5_1.grid_forget() 
        label5x_2.grid_forget()
        label5_3.grid_forget() 
        label5_5.grid_forget() 
        label5_6.grid_forget() 
        button_yes1.grid_forget() 
        button_no1.grid_forget() 
        button_yes2.grid_forget() 
        button_no2.grid_forget() 
        button_yes3.grid_forget() 
        button_no3.grid_forget() 
        button_yes4.grid_forget() 
        button_no4.grid_forget() 
        button_yes5.grid_forget() 
        button_no5.grid_forget() 
        frame_newtype.pack_forget()
        frame_elt2.pack_forget()
        canvas.pack_forget()
        for widget in canvas.winfo_children():
            widget.grid_forget()
        frame_add1.pack(fill = 'y')


    def type_value():
        t = type_names.get()
        label5_4.configure(text = t)
        label5_4.grid(row = 3, column = 3, columnspan = 3)
        for widget in canvas.winfo_children():
            widget.grid_forget()
        canvas.pack_forget()
        frame_elt2.pack(fill = 'y')
        d_att = db.attributes(t)
        l = []
        for elt in d_att:
            l.append(elt)
        n = len(d_att)
        enrty5_1.grid_forget()
        enrty5_2.grid_forget()
        enrty5_3.grid_forget()
        enrty5_4.grid_forget()
        enrty5_5.grid_forget()
        if n > 0:
            label5_1.configure(text = " "+l[0] + " ", font = font2_)
            label5_1.grid(row =4 , column = 3, pady = 7, padx = 10)
            enrty5_1.grid(row =4 , column = 4, pady = 7, padx = 10, columnspan = 2)
            if d_att[l[0]] == 'Yes or No':
                enrty5_1.grid_forget()
                button_yes1.grid(row = 4, column = 4)
                button_no1.grid(row = 4, column = 5)

        if n > 1:
            label5x_2.configure(text = " "+l[1] + " ", font = font2_)
            label5x_2.grid(row =5 , column = 3, pady = 7, padx = 10)
            enrty5_2.grid(row = 5, column = 4, pady = 7, padx = 10, columnspan = 2)
            if d_att[l[1]] == 'Yes or No':
                enrty5_2.grid_forget()
                button_yes2.grid(row = 5, column = 4)
                button_no2.grid(row = 5, column = 5)

        if n > 2:
            label5_3.configure(text = " "+l[2] + " ", font = font2_)
            label5_3.grid(row =6 , column = 3, pady = 7, padx = 10)
            enrty5_3.grid(row = 6, column = 4, pady = 7, padx = 10, columnspan = 2)
            if d_att[l[2]] == 'Yes or No':
                enrty5_3.grid_forget()
                button_yes3.grid(row = 6, column = 4)
                button_no3.grid(row = 6, column = 5)

        if n > 3:
            enrty5_4.grid(row = 7, column = 4, pady = 7, padx = 10, columnspan = 2)
            label5_5.configure(text = " "+l[3] + " ", font = font2_)
            label5_5.grid(row =7 , column = 3, pady = 7, padx = 10)
            if d_att[l[3]] == 'Yes or No':
                enrty5_4.grid_forget()
                button_yes4.grid(row = 7, column = 4)
                button_no4.grid(row = 7, column = 5)

        if n > 4:
            label5_6.configure(text = " "+l[4] + " ", font = font2_)
            label5_6.grid(row = 8 , column = 3, pady = 7, padx = 10)
            enrty5_5.grid(row = 8, column = 4, pady = 7, columnspan = 2)
            if d_att[l[4]] == 'Yes or No':
                enrty5_5.grid_forget()
                button_yes5.grid(row = 8, column = 4)
                button_no5.grid(row = 8, column = 5)

    def frame_elt():
        frame_add1.pack_forget()
        canvas.pack(fill = 'y')
        label3x_2.grid(row = 0, pady = 10, padx = 20, columnspan = 5, column = 1)
        space5_3.grid(row = 1)
        d_ = import_names(user_)
        k = 0
        for elt in d_:
            radio = ttk.Radiobutton(canvas, text = elt, variable = type_names, value = elt, command = type_value)
            if k < 10:
                radio.grid(padx = 6, pady = 6, row = k + 3, column = 1)
            elif k < 20:
                radio.grid(padx = 6, pady = 6, row = k - 7, column = 2)
            elif k < 30:
                radio.grid(padx = 6, pady = 6,row = k - 17, column = 3)
            elif k < 40:
                radio.grid(padx = 6, pady = 6, row = k - 27, column = 4)
            else:
                radio.grid(padx = 6, pady = 6, row = k - 37, column = 5)
            k = k + 1
        button_back4_3 = ttk.Button(canvas, text = ' Back ',command =  frameadd_1)
        button_back4_3.grid(pady = 20, columnspan = 5, column = 1) 

    def save_node():
        label_vare.set('                                      ')
        a = att_1.get()
        b = att_2.get()
        c = att_3.get()
        d = att_4.get()
        e = att_5.get()
        error1 = False
        error2 = False
        y = type_names.get()
        d_ = db.attributes(y)
        print(d_)
        k = 0
        test = False
        test1 = False
        test2 = False
        test3 = False
        test4 = False
        for i in a:
            if i != " ":
                test = True
        for i in b:
            if i != " ":
                test1 = True
        for i in c:
            if i != " ":
                test2 = True
        for i in d:
            if i != " ":
                test3 = True
        for i in e:
            if i != " ":
                test4 = True
        for elt in d_:
            if k == 0:
                if a != "" and test == True:
                    if d_[elt] == 'No Conditions' or d_[elt] == 'Yes or No':
                        a = a
                    elif d_[elt] == 'Only Letters':
                        for j in a:
                            j = j.lower()
                            if j not in ' abcdefghijklmnopqrstuvwxyz ':
                                att_1.set('')
                                error2 = True
                    elif d_[elt] == 'Number':
                        for j in a:
                            if j not in '1234567890.- ':
                                att_1.set('')
                                error2 = True
                    else:
                        for j in a:
                            if j not in '1234567890 ':
                                att_1.set("")
                                error2 = True
                    k = k + 1
                else:
                    att_1.set("")
                    error1 = True
                    k = k + 1
            elif k == 1:
                if b != "" and test1 == True:
                    if d_[elt] == 'No Conditions' or d_[elt] == 'Yes or No':
                        a = a
                    elif d_[elt] == 'Only Letters':
                        for j in b:
                            j = j.lower()
                            if j not in 'abcdefghijklmnopqrstuvwxyz ':
                                att_2.set('')
                                error2 = True
                    elif d_[elt] == 'Number':
                        for j in b:
                            if j not in '1234567890.- ':
                                att_2.set('')
                                error2 = True
                    else:
                        for j in b:
                            if j not in '1234567890 ':
                                att_2.set("")
                                error2 = True
                    k = k + 1
                else:
                    att_2.set("")
                    error1 = True
                    k = k + 1

            elif k == 2:
                if c != "" and test2 == True:
                    if d_[elt] == 'No Conditions' or d_[elt] == 'Yes or No':
                        a = a
                    elif d_[elt] == 'Only Letters':
                        for j in c:
                            j = j.lower()
                            if j not in 'abcdefghijklmnopqrstuvwxyz ':
                                att_3.set('')
                                error2 = True
                    elif d_[elt] == 'Number':
                        for j in c:
                            if j not in '1234567890.- ':
                                att_3.set('')
                                error2 = True
                    else:
                        for j in c:
                            if j not in '1234567890 ':
                                att_3.set("")
                                error2 = True
                    k = k + 1
                else:
                    att_3.set("")
                    error1 = True
                    k = k + 1
            elif k == 3:
                if d != "" and test3 == True:
                    if d_[elt] ==  'No Conditions' or d_[elt] == 'Yes or No':
                        a = a
                    elif d_[elt] == 'Only Letters':
                        for j in d:
                            j = j.lower()
                            if j not in 'abcdefghijklmnopqrstuvwxyz ':
                                att_4.set('')
                                error2 = True
                    elif d_[elt] == 'Number':
                        for j in d:
                            if j not in '1234567890.- ':
                                att_4.set('')
                                error2 = True
                    else:
                        for j in d:
                            if j not in '1234567890 ':
                                att_4.set("")
                                error2 = True
                    k = k + 1
                else:
                    att_4.set("")
                    error1 = True
                    k = k + 1
            elif k == 4:
                if e != "" and test4 == True:
                    if d_[elt] == 'No Conditions' or d_[elt] == 'Yes or No':
                        a = a
                    elif d_[elt] == 'Only Letters':
                        for j in e:
                            j = j.lower()
                            if j not in 'abcdefghijklmnopqrstuvwxyz ':
                                att_5.set('')
                                error2 = True
                    elif d_[elt] == 'Number':
                        for j in e:
                            if j not in '1234567890.- ':
                                att_5.set('')
                                error2 = True
                    else:
                        for j in e:
                            if j not in '1234567890 ':
                                att_5.set("")
                                error2 = True
                    k = k + 1
                else:
                    att_5.set("")
                    error1 = True
                    k = k + 1
        if error1:
            label_vare.set('Some missed information !')
        elif error2:
            label_vare.set('Incorrect format !')
        else:
            dict_ = {}
            l = [a,b,c,d,e]
            s = 0
            for elt in d_:
                dict_[elt] = l[s]
                s = s + 1
            if not db.is_in_db(y,dict_):
                att_1.set("")
                att_2.set("")
                att_3.set("")
                att_4.set("")
                att_5.set("")
                frame_elt2.pack_forget()
                type_names.set('')
                frame_add1.pack(fill = 'y')
                db.add_node(y,dict_)
                enrty5_1.grid_forget() 
                enrty5_2.grid_forget() 
                enrty5_3.grid_forget() 
                enrty5_4.grid_forget() 
                enrty5_5.grid_forget() 
                label5_1.grid_forget() 
                label5x_2.grid_forget()
                label5_3.grid_forget() 
                label5_5.grid_forget() 
                label5_6.grid_forget() 
                button_yes1.grid_forget() 
                button_no1.grid_forget() 
                button_yes2.grid_forget() 
                button_no2.grid_forget() 
                button_yes3.grid_forget() 
                button_no3.grid_forget() 
                button_yes4.grid_forget() 
                button_no4.grid_forget() 
                button_yes5.grid_forget() 
                button_no5.grid_forget() 
            else:
                label_vare.set('Element already existing !')

    ## Init Page

    def import2_():
        with open('ID/my2_dict.json', 'r') as f:
            d = json.load(f)
            return d

    def import_names(user):
        with open('ID/name_dict.json'+user, 'r') as f:
            d = json.load(f)
            return d

    def save_names(d,user):
        with open('ID/name_dict.json'+user, 'w') as f:
            json.dump(d, f)

    window2 = tk.Tk()

    ###


    ### Variables

    ## Create type

    type_name = StringVar()
    b = IntVar()
    att1 = StringVar()
    condition = StringVar()
    row_var = IntVar()
    button_var = StringVar()
    att_test = BooleanVar()

    att_1 = StringVar()
    att_2 = StringVar()
    att_3 = StringVar()
    att_4 = StringVar()
    att_5 = StringVar()

    type_names = StringVar()

    bool1 = StringVar()
    bool2 = StringVar()
    bool3 = StringVar()
    bool4 = StringVar()
    bool5 = StringVar()

    label_vare = StringVar()

    ### Fonts

    font1_ = ('TkDefaultFont', 14, 'bold')
    font2_ = ('TkDefaultFont', 12, 'bold')
    font3_ = ('TkDefaultFont', 10, 'bold')

    ##


    d2 = import2_()
    t = d2[user_]
    texte = t[0] + " " + t[1]
    window2.title("Database - "+ texte )
    window2.geometry("1200x650")
    window2.configure(bg = '#53868B')

    frame_user = tk.Frame(window2, bg = '#CD3333', relief = "solid", borderwidth= 5)
    frame_user.pack(side="top", anchor="ne")


    label_0 = ttk.Label(frame_user, text = "", background = '#CD3333')
    label_0.grid(row = 4)

    label_1 = ttk.Label(frame_user, text =" " + texte + " ", font = font1_,foreground = 'white', background = '#CD3333')
    label_1.grid(row = 5)

    label_2 = ttk.Label(frame_user, text = " " + user_ + " ", font = font2_,foreground = 'black', background = '#CD3333')
    label_2.grid(row = 6)

    label_3 = ttk.Label(frame_user, text = "", background = '#CD3333')
    label_3.grid(row = 7)

    button_0 = tk.Button(frame_user, text = " Sign out & Exit ",bg = 'white', fg = '#CD3333', font = font3_)
    button_0.grid(row = 8)

    label_4 = ttk.Label(frame_user, text = "", background = '#CD3333')
    label_4.grid(row = 9)

    ##
    #
    #
    #

    ## Page 1

    framep1 = tk.Frame(window2, bg = '#8B0000')
    framep1.pack(fill = 'y')

    image_find = tk.PhotoImage(file = 'Backgrounds/find_bg.png')
    image_edit = tk.PhotoImage(file = 'Backgrounds/edit_bg.png')
    image_add = tk.PhotoImage(file = 'Backgrounds/add_bg.png')

    button_edit = ttk.Button(framep1, image = image_edit)
    button_edit.grid(row = 0, column = 0)

    space1 = ttk.Label(framep1, text = '     ', background='#8B0000')
    space1.grid(row = 0, column = 1)

    button_add = ttk.Button(framep1, image = image_add, command = add_)
    button_add.grid(row = 1, column = 2)


    space1 = ttk.Label(framep1, text = '     ', background = '#8B0000')
    space1.grid(row = 0, column = 3)

    button_find = ttk.Button(framep1, image = image_find)
    button_find.grid(row = 2, column = 4)

    ###

    ### Add page

    frame_add1 = tk.Frame(window2,bg = '#8B0000')

    image_createtype = tk.PhotoImage(file = 'Backgrounds/create_type.png')
    image_createnode = tk.PhotoImage(file = 'Backgrounds/create_node.png')
    image_createrel = tk.PhotoImage(file = 'Backgrounds/create_rel.png')
    image_addrel = tk.PhotoImage(file = 'Backgrounds/add_rel.png')
    image_to_home = tk.PhotoImage(file = 'Backgrounds/home_page.png')

    button_createtype = ttk.Button(frame_add1, image = image_createtype, command = create_type)
    button_createtype.grid(row = 0, column = 0)

    space1 = ttk.Label(frame_add1, text = '     ', background='#8B0000')
    space1.grid(row = 1, column = 1)

    space1 = ttk.Label(frame_add1, text = '     ', background = '#8B0000')
    space1.grid(row = 0, column = 3)

    button_home = ttk.Button(frame_add1, image = image_to_home, command = to_home)
    button_home.grid(row = 1, column = 2)

    button_addnode = ttk.Button(frame_add1, image = image_createnode, command = frame_elt)
    button_addnode.grid(row = 2, column = 0)

    button_createrel = ttk.Button(frame_add1, image = image_createrel)
    button_createrel.grid(row = 0, column = 4)

    button_addrel = ttk.Button(frame_add1, image = image_addrel)
    button_addrel.grid(row = 2, column = 4)

    ###

    ## Create new type

    frame_newtype = tk.Frame(window2, bg = '#8B0000')

    space1_2 = ttk.Label(frame_newtype, background= '#8B0000', text = "             ")
    space1_2.grid(row = 0)

    space2_2 = ttk.Label(frame_newtype, background= '#8B0000', text = "             ")
    space2_2.grid(row = 1)

    text1_2 = ttk.Label(frame_newtype, background='#8B0000',foreground='white', text = "Enter the type name", font = font2_)
    text1_2.grid(row = 2, column = 5)

    entry1_2 = ttk.Entry(frame_newtype, textvariable= type_name)
    entry1_2.grid(row = 3, column = 5)

    space5_2 = ttk.Label(frame_newtype, background = '#8B0000', text = '       ')
    space5_2.grid(row = 4, column = 5)

    text2_2 = ttk.Label(frame_newtype, background = '#8B0000', foreground = 'white', text = "Add attributes (At least 1)", font = font2_)
    text2_2.grid(row = 5, column = 5)

    space6_2 = ttk.Label(frame_newtype, background = '#8B0000', text = '       ')
    space6_2.grid(row = 6, column = 5)

    label0_2 = ttk.Label(frame_newtype,text = 'Attributes', background= 'black', foreground = 'white', font = font2_)
    label0_2.grid(row = 7, column = 5, padx = 10)

    label1_2 = ttk.Label(frame_newtype, text = 'Conditions : ', background= 'black', foreground = 'white', font = font2_)
    label1_2.grid(row = 7, column = 6, padx = 10)

    label2_2 = ttk.Label(frame_newtype,text = 'No conditions', background= 'white', foreground = 'black', font = font2_)
    label2_2.grid(row = 7, column = 7, padx = 10)

    label3_2 = ttk.Label(frame_newtype, text = 'Only Letters', background= 'white', foreground = 'black', font = font2_)
    label3_2.grid(row = 7, column = 8, padx = 10)

    label4_2 = ttk.Label(frame_newtype,text = 'Number', background= 'white', foreground = 'black', font = font2_)
    label4_2.grid(row = 7, column = 9, padx = 10)

    label5_2 = ttk.Label(frame_newtype, text = 'Integer', background= 'white', foreground = 'black', font = font2_)
    label5_2.grid(row = 7, column = 10, padx = 10)

    label6_2 = ttk.Label(frame_newtype, text = 'Yes or No', background= 'white', foreground = 'black', font = font2_)
    label6_2.grid(row = 7, column = 11, padx = 10)

    space7_2 = ttk.Label(frame_newtype, background = '#8B0000', text = '       ')
    space7_2.grid(row = 8, column = 5)

    button1_1_2 = ttk.Radiobutton(frame_newtype,variable = condition, value = 'A', command = select_condition)
    button1_1_2.grid(row = 9, column = 7)

    button2_1_2 = ttk.Radiobutton(frame_newtype,variable = condition, value = 'B', command = select_condition)
    button2_1_2.grid(row = 9, column = 8)

    button3_1_2 = ttk.Radiobutton(frame_newtype,variable = condition, value = 'C', command = select_condition)
    button3_1_2.grid(row = 9, column = 9)

    button4_1_2 = ttk.Radiobutton(frame_newtype,variable = condition, value = 'D', command = select_condition)
    button4_1_2.grid(row = 9, column = 10)

    button5_1_2 = ttk.Radiobutton(frame_newtype,variable = condition, value = 'E', command = select_condition)
    button5_1_2.grid(row = 9, column = 11)

    att1_2 = ttk.Entry(frame_newtype, textvariable = att1)
    att1_2.grid(row = 9, column = 5, pady = 14)

    button_variable = ttk.Button(frame_newtype, textvariable = button_var, command = add_att)
    button_variable.grid(column = 5, row = 10)


    space3_2 = ttk.Label(frame_newtype, background= '#8B0000', text = "                     ")
    space3_2.grid(row = 20)

    space4_2 = ttk.Label(frame_newtype, background= '#8B0000', text = "                     ")
    space4_2.grid(row = 21)

    button_savetype = ttk.Button(frame_newtype, text = '  Save Type  ', command = save_type)
    button_savetype.grid(row = 3, column = 10, columnspan = 2)

    x1 = ttk.Label(frame_newtype, background = 'red', foreground = 'black', font = font2_)
    x2 = ttk.Label(frame_newtype, background = 'white', foreground = 'red', font = font2_)

    x1_ = ttk.Label(frame_newtype, background = 'red', foreground = 'black', font = font2_)
    x2_ = ttk.Label(frame_newtype, background = 'white', foreground = 'red', font = font2_)

    x_1_ = ttk.Label(frame_newtype, background = 'red', foreground = 'black', font = font2_)
    x_2_ = ttk.Label(frame_newtype,  background = 'white', foreground = 'red', font = font2_)

    x_1 = ttk.Label(frame_newtype, background = 'red', foreground = 'black', font = font2_)
    x_2 = ttk.Label(frame_newtype, background = 'white', foreground = 'red', font = font2_)

    x1_5 = ttk.Label(frame_newtype, background = 'red', foreground = 'black', font = font2_)
    x2_5 = ttk.Label(frame_newtype, background = 'white', foreground = 'red', font = font2_)

    x4 = ttk.Label(frame_newtype, text = 'Attribute already mentionned', background = 'yellow', font = font2_)

    button_back3_2 = ttk.Button(frame_newtype, text = ' Back ', command = back_addpage)
    button_back3_2.grid(column = 3, row = 14, padx = 10)


    ### Add_element

    canvas = tk.Frame(window2,bg = '#8B0000')

    label3x_2 = ttk.Label(canvas, background= '#8B0000', text = " Choose type ", font = font2_, foreground = 'white')

    space5_3 = ttk.Label(canvas, background= '#8B0000', text = "               ")

    frame_elt2 = tk.Frame(window2, bg = '#8B0000')

    space1_4 = ttk.Label(frame_elt2, text = '        ', background = '#8B0000')
    space1_4.grid(row = 0, column = 0)

    space2_4 = ttk.Label(frame_elt2, text = '        ', background = '#8B0000')
    space2_4.grid(row = 20, column = 0)

    space3_4 = ttk.Label(frame_elt2, text = '        ', background = '#8B0000')
    space3_4.grid(row = 0, column = 20)

    space4_4 = ttk.Label(frame_elt2, text = '        ', background = '#8B0000')
    space4_4.grid(row = 20, column = 0)

    button_back5_4 = ttk.Button(frame_elt2, text = ' Back ', command = frameadd_1)

    label5_4 = ttk.Label(frame_elt2, background = '#8B0000', foreground = 'white', font = font1_)
    label5_4.grid(row = 3, column =2, pady = 10, columnspan = 3)

    space5_4 = ttk.Label(frame_elt2, text = '        ', background = '#8B0000')

    enrty5_1 = ttk.Entry(frame_elt2, textvariable = att_1)
    enrty5_2 = ttk.Entry(frame_elt2, textvariable = att_2)
    enrty5_3 = ttk.Entry(frame_elt2, textvariable = att_3)
    enrty5_4 = ttk.Entry(frame_elt2, textvariable = att_4)
    enrty5_5 = ttk.Entry(frame_elt2, textvariable = att_5)

    label5_1 = ttk.Label(frame_elt2)
    label5x_2 = ttk.Label(frame_elt2)
    label5_3 = ttk.Label(frame_elt2)
    label5_5 = ttk.Label(frame_elt2)
    label5_6 = ttk.Label(frame_elt2)

    button_yes1 = ttk.Radiobutton(frame_elt2, text = "Yes", variable = bool1, value = 'Yes',command = att_1_set_)
    button_no1 = ttk.Radiobutton(frame_elt2, text = "No", variable = bool1, value = 'No', command = att_1_set_)

    button_yes2 = ttk.Radiobutton(frame_elt2, text = "Yes", variable = bool2, value = 'Yes', command = att_2_set_)
    button_no2 = ttk.Radiobutton(frame_elt2, text = "No", variable = bool2, value = 'No', command = att_2_set_)

    button_yes3 = ttk.Radiobutton(frame_elt2, text = "Yes", variable = bool3, value = 'Yes', command = att_3_set_)
    button_no3 = ttk.Radiobutton(frame_elt2, text = "No", variable = bool3, value = 'No', command = att_3_set_)

    button_yes4 = ttk.Radiobutton(frame_elt2, text = "Yes", variable = bool4, value = 'Yes', command = att_4_set_)
    button_no4 = ttk.Radiobutton(frame_elt2, text = "No", variable = bool4, value = 'No', command = att_4_set_)

    button_yes5 = ttk.Radiobutton(frame_elt2, text = "Yes", variable = bool5, value = 'Yes', command = att_5_set_)
    button_no5 = ttk.Radiobutton(frame_elt2, text = "No", variable = bool5, value = 'No', command = att_5_set_)
    

    space4_4.grid(row = 5, column = 3)

    button_savenode = ttk.Button(frame_elt2, text = " Save ", command = save_node)
    button_savenode.grid(row = 19, column = 6, padx = 7)

    label_var = ttk.Label(frame_elt2, textvariable = label_vare, font = font2_, background='#8B0000', foreground = 'yellow' )
    label_var.grid(row = 18, column = 2, columnspan = 4)

    window2.mainloop()


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

