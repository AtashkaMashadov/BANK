from tkinter import *
from tkinter import messagebox


class Users():
    def __init__(self, username, password, name, balans, surname, birthday, gender):
        self.username = username
        self.password = password
        self.name = name
        self.balans = balans
        self.surname = surname
        self.bir = birthday
        self.gender = gender

    def save(self):
        f = open('Data.txt', 'a')
        f.write(self.username+':'+self.password+':'+self.name+':' +
                str(self.balans)+':'+self.surname+':'+self.bir+':'+self.gender+'\n')

    def change_pass(self, old, new):
        if self.password == old:
            self.password = new
            print('OK')
        else:
            mesg = messagebox.showerror(message='Old pass is not correct')

    def givem(self, money):
        self.balans = str(int(self.balans)+money)

    def takem(self, money):
        self.balans = str(int(self.balans)-money)

    def chargem(self, money, uname):
        if Users.find_user(uname) is not None:
            reciver = Users.find_user(uname)

            self.balans = str(int(self.balans)-money)
            reciver.balans = str(int(reciver.balans)+money)

            self.update()
            reciver.update()
        else:
            mesg = messagebox.showerror(
                info='Not found 404', message='User not found')

    def update(self):
        users = open('Data.txt').readlines()
        f = open('Data.txt', 'w')
        for i in users:
            if i.split(':')[0] == self.username:
                f.write(self.username+':'+self.password+':'+self.name+':' +
                        str(self.balans)+':'+self.surname+':'+self.bir+':'+self.gender)
            else:
                f.write(i)

    def find_user(uname):
        f = open('Data.txt')
        for i in f:
            if i.split(':')[0] == uname:
                return Users(i.split(':')[0], i.split(':')[1], i.split(':')[2], i.split(':')[3], i.split(':')[4], i.split(':')[5], i.split(':')[6])
        return None


root = Tk()
root.resizable(0, 0)


def test():
    FONT = ('Klavika', 30)
    COLOR = '#3b5998'
    COLOR1 = 'black'
    a = qent.get()
    b = qent2.get()
    c = open('Data.txt')
    d = c.readlines()
    q = d[0].removesuffix('\n')
    q = q.split(':')
    print(q[0])
    print(q[1])
    if q[0] == a and q[1] == b:
        win2 = Toplevel()

        def dle():
            global data, f
            new()
            qq = open('Data.txt')
            oo = qq.readlines()
            d = lst.curselection()
            lst.delete(d)
            oo.pop(d[0]+1)
            opp = open('Data.txt', 'w')
            for i in oo:
                opp.write(i)
            qq.close()
            opp.close()
            f = open('Data.txt')
            data = f.readlines()

        def new():
            ent1.delete(0, END)
            ent2.delete(0, END)
            ent3.delete(0, END)
            ent4.delete(0, END)
            ent5.delete(0, END)
            ent6.delete(0, END)
            rdb1.deselect()
            rdb2.deselect()
        o1 = open('Data.txt')
        o2 = o1.readlines()
        frm = Frame(win2, bg=COLOR)
        lst = Listbox(frm, bg=COLOR, fg=COLOR1)
        btn1 = Button(frm, text='NEW', height=3, width=20,
                      command=new, bg=COLOR, fg=COLOR1)
        btn2 = Button(frm, text='Delete', height=3, width=20,
                      comman=dle, bg=COLOR, fg=COLOR1)
        frm.grid(row=0, column=0, rowspan=8, sticky=N)
        btn1.grid(row=1, column=0)
        btn2.grid(row=2, column=0)
        lst.grid(row=0, column=0)
        for i in range(1, len(o2)):
            q = o2[i].split(':')
            lst.insert(END, q[2]+' '+q[4])

        win2['bg'] = COLOR
        frm1 = Frame(win2, bg=COLOR)
        lbl1 = Label(frm1, text='UserName', bg=COLOR, fg=COLOR1)
        lbl2 = Label(frm1, text='Pass', bg=COLOR, fg=COLOR1)
        lbl3 = Label(frm1, text='Name', bg=COLOR, fg=COLOR1)
        lbl4 = Label(frm1, text='Birthday', bg=COLOR, fg=COLOR1)
        lbl5 = Label(frm1, text='Surname', bg=COLOR, fg=COLOR1)
        lbl6 = Label(frm1, text='Balance', bg=COLOR, fg=COLOR1)
        ent1 = Entry(frm1, bg=COLOR, fg=COLOR1)
        ent2 = Entry(frm1, bg=COLOR, fg=COLOR1)
        ent3 = Entry(frm1, bg=COLOR, fg=COLOR1)
        ent4 = Entry(frm1, bg=COLOR, fg=COLOR1)
        ent5 = Entry(frm1, bg=COLOR, fg=COLOR1)
        ent6 = Entry(frm1, bg=COLOR, fg=COLOR1)
        frm1.grid(row=0, column=1)
        lbl1.grid(row=0, column=0)
        lbl2.grid(row=0, column=1)
        lbl3.grid(row=2, column=0)
        lbl4.grid(row=4, column=1)
        lbl5.grid(row=4, column=0)
        lbl6.grid(row=2, column=1)
        ent1.grid(row=1, column=0)
        ent2.grid(row=1, column=1)
        ent3.grid(row=3, column=0)
        ent4.grid(row=3, column=1)
        ent5.grid(row=5, column=0)
        ent6.grid(row=5, column=1)
        # Frame_2 part 2
        o0 = ''

        def rdbl1():
            global o0
            if rdb.get() == 0:
                o0 = 'Male'
            else:
                o0 = 'Female'
        rdb = IntVar()
        frm3 = Frame(win2, bg=COLOR)
        lbl6 = Label(frm3, text='Gender', font=(
            'Times New Roman Bold', 18), bg=COLOR, fg=COLOR1)
        rdb1 = Radiobutton(frm3, text='Male', variable=rdb, value=0, font=(
            'Times New Roman Bold', 18), command=rdbl1, bg=COLOR, fg=COLOR1)
        rdb2 = Radiobutton(frm3, text='Female', variable=rdb, value=1, font=(
            'Times New Roman Bold', 18), command=rdbl1, bg=COLOR, fg=COLOR1)

        frm3.grid(row=0, column=4, sticky=E, rowspan=3, padx=20)
        lbl6.grid(row=0, column=0)
        rdb1.grid(row=1, column=0, sticky=W)
        rdb2.grid(row=2, column=0, sticky=W)
        rdb1.deselect()
        rdb2.deselect()
        # Frame_2

        def save():
            o = open('Data.txt', 'a')
            global o0, f, data
            a = ''
            l1 = ent1.get()
            l2 = ent2.get()
            l3 = ent3.get()
            l4 = ent4.get()
            l5 = ent5.get()
            l6 = ent6.get()
            user = Users((a+l1), (a+l2), (a+l3), (a+l4), (a+l5), (a+l6), o0)
            user.save()
            a = (a+l1)+':'+(a+l2)+':'+(a+l3)+':' + \
                (a+l4)+':'+(a+l5)+':'+(a+l6)+':'+o0
            q = a.split(':')
            lst.insert(END, q[2]+' '+q[4])
            f = open('Data.txt')
            data = f.readlines()

        def slect(e):
            global data
            new()
            f = open('Data.txt')
            data = f.readlines()
            a = lst.curselection()[0]
            pp = data[a+1].split(':')
            s1 = pp[0]
            s2 = pp[1]
            s3 = pp[2]
            s4 = pp[3]
            s5 = pp[4]
            s6 = pp[5]
            ent1.insert(0, s1)
            ent2.insert(0, s2)
            ent3.insert(0, s3)
            ent4.insert(0, s4)
            ent5.insert(0, s5)
            ent6.insert(0, s6)

            s5 = pp[5]
            if s5 == 'Female':
                rdb.set(1)
            else:
                rdb.set(0)

        lst.bind('<<ListboxSelect>>', slect)
        f = open('Data.txt')
        data = f.readlines()

        SAVE = Button(win2, text='SAVE', width=16, height=2,
                      font=('', 40), command=save, bg=COLOR, fg=COLOR1)
        SAVE.grid(row=4, column=1, columnspan=7)
        win2.mainloop()
        root.iconify()
    else:
        r = open('Data.txt')
        r1 = r.readlines()
        o = 0
        global p
        for i in range(1, len(r1)):
            p = r1[i].removesuffix('\n')
            p = p.split(':')
            if p[0] == a and p[1] == b:
                win1 = Toplevel()
                popop = i
                win1.title('User '+a)

                def give():
                    win3 = Toplevel()
                    win3.title('Give Money')

                    def sumb():
                        print(a)
                        a2 = int(entry1.get())
                        reciver1 = Users.find_user(a)
                        if reciver1 is not None:
                            print(reciver1.balans)
                            reciver1.givem(a2)
                            reciver1.update()
                            moneyw = reciver1.balans
                            label3['text'] = 'Balance: '+str(moneyw)
                            win3.destroy()

                    lbl = Label(win3, text='Write here the amount of money')
                    lbl.grid(row=0, column=0)
                    entry1 = Entry(win3)
                    entry1.grid(row=1, column=0)
                    btn = Button(win3, text='Sumbit', command=sumb)
                    btn.grid(row=2, column=0)

                def take():
                    win4 = Toplevel()
                    win4.title('Take Money')

                    def sumb():
                        print(a)
                        a2 = int(entry1.get())
                        reciver1 = Users.find_user(a)
                        if reciver1 is not None:
                            reciver1.takem(a2)
                            reciver1.update()
                            moneyw = reciver1.balans
                            label3['text'] = 'Balance: '+str(moneyw)
                            win4.destroy()
                    lbl = Label(
                        win4, text='Write here the amount of money you take')
                    lbl.grid(row=0, column=0)
                    entry1 = Entry(win4)
                    entry1.grid(row=1, column=0)
                    btn = Button(win4, text='Sumbit', command=sumb)
                    btn.grid(row=2, column=0)

                def change():
                    win5 = Toplevel()

                    def chn():
                        print(a)
                        a1 = ent1.get()
                        b1 = ent2.get()
                        c1 = ent3.get()
                        reciver1 = Users.find_user(a)
                        if reciver1 is not None and b1 == c1:
                            reciver1.change_pass(a1, b1)
                            reciver1.update()
                            passw = reciver1.password
                            label2['text'] = 'Pass: '+passw
                            win5.destroy()
                        else:
                            mesg = messagebox.showerror(
                                message='New passes doesnt match correct')
                    lbl = Label(win5, text='Old pass')
                    lbl.grid(row=0, column=0)
                    ent1 = Entry(win5)
                    ent1.grid(row=1, column=0)
                    lbl1 = Label(win5, text='New pass')
                    lbl1.grid(row=2, column=0)
                    ent2 = Entry(win5)
                    ent2.grid(row=3, column=0)
                    lbl1 = Label(win5, text='New pass again')
                    lbl1.grid(row=4, column=0)
                    ent3 = Entry(win5)
                    ent3.grid(row=5, column=0)
                    btn = Button(win5, text='Change', command=chn)
                    btn.grid(row=6, column=0)

                def charge():
                    win6 = Toplevel()

                    def chr():
                        print(a)
                        a1 = ent1.get()
                        b1 = ent2.get()
                        reciver1 = Users.find_user(a)
                        if reciver1 is not None:
                            reciver1.chargem(int(b1), a1)
                            reciver1.update()
                            monw = int(reciver1.balans)
                            label3['text'] = 'Balance: '+str(monw)
                            win6.destroy()
                    lbl = Label(win6, text='Username')
                    lbl.grid(row=0, column=0)
                    ent1 = Entry(win6)
                    ent1.grid(row=1, column=0)
                    lbl1 = Label(win6, text='Amount of money')
                    lbl1.grid(row=2, column=0)
                    ent2 = Entry(win6)
                    ent2.grid(row=3, column=0)
                    btn = Button(win6, text='Charge', command=chr)
                    btn.grid(row=4, column=0)

                COLOR = '#3b5998'
                COLOR1 = 'white'
                FONT = ('Klavika', 30)
                win1['bg'] = COLOR
                frm1 = Frame(win1)
                frm1.grid(row=0, column=1, rowspan=7)
                label1 = Label(win1, text='Username: ' +
                               p[0], bg=COLOR, fg=COLOR1, font=FONT)
                label1.grid(row=0, column=0)
                label2 = Label(win1, text='Pass: ' +
                               p[1], bg=COLOR, fg=COLOR1, font=FONT)
                label2.grid(row=1, column=0)
                label3 = Label(win1, text='Balance: ' +
                               p[3], bg=COLOR, fg=COLOR1, font=FONT)
                label3.grid(row=2, column=0)
                label4 = Label(win1, text='Name: ' +
                               p[2], bg=COLOR, fg=COLOR1, font=FONT)
                label4.grid(row=3, column=0)
                label5 = Label(win1, text='Surname: ' +
                               p[4], bg=COLOR, fg=COLOR1, font=FONT)
                label5.grid(row=4, column=0)
                label6 = Label(win1, text='Date of B: ' +
                               p[5], bg=COLOR, fg=COLOR1, font=FONT)
                label6.grid(row=5, column=0)
                label7 = Label(win1, text='Gender: ' +
                               p[6], bg=COLOR, fg=COLOR1, font=FONT)
                label7.grid(row=6, column=0)
                but5 = Button(frm1, text='Give Money', height=4, width=10,
                              bg=COLOR, fg=COLOR1, font=FONT, command=give)
                but5.grid(row=0, column=1)
                but6 = Button(frm1, text='Take Money', height=4,
                              width=10, bg=COLOR, fg=COLOR1, font=FONT, command=take)
                but6.grid(row=1, column=1, rowspan=2)
                but7 = Button(frm1, text='Charge Money', height=4,
                              width=11, bg=COLOR, fg=COLOR1, font=FONT, command=charge)
                but7.grid(row=1, column=2, rowspan=2)
                but8 = Button(frm1, text='Change pass', height=4,
                              width=11, bg=COLOR, fg=COLOR1, font=FONT, command=change)
                but8.grid(row=0, column=2)

                o += 1

        if o == 0:
            messagebox.showerror(title='Not found', message=str(
                a)+' is not found or pass is not correct')


lbl = Label(root, text='BANK', font=('Times New Roman Bold', 45))
qent = Entry(root, font=('Times New Roman Bold', 25))
qent2 = Entry(root, font=('Times New Roman Bold', 25), show='*')
but = Button(root, text='Sumbit', font=(
    'Times New Roman Bold', 25), command=test)
lbl.grid(row=0, column=0)
qent.grid(row=1, column=0)
qent2.grid(row=2, column=0)
but.grid(row=3, column=0)
root.mainloop()
