from tkinter import *
from tkinter import ttk

tk = Tk()

tk['bg'] = '#fafafa'
tk.title('Телефонный справочник')
tk.wm_attributes('-alpha', 0.95)
tk.geometry('676x600')
tk.resizable(width=False, height=False)

# canvas = Canvas(tk, height=600, width=800)
# # canvas.create_text(200, 200, text='Тест', fill='red', font=('Times', 35))
# canvas.pack()


frame1 = Frame(tk, bg='grey')
frame1.place(relx=0.02, rely=0.02, relheight=0.06, relwidth=0.95)
frame2 = Frame(tk, bg='grey')
frame2.place(relx=0.02, rely=0.10, relheight=0.88, relwidth=0.95)


def button1():
    print('Кнопка 1 нажата')


def button2():
    print('Кнопка 2 нажата')


def button3():
    print('Кнопка 3 нажата')


def button4():
    print('Кнопка 4 нажата')


def button5():
    print('Кнопка 5 нажата')


def button6():
    print('Кнопка 6 нажата')


def button7():
    print('Кнопка 7 нажата')


def button8():
    print('Кнопка 8 нажата')


def button9():
    print('Кнопка 9 нажата')


but1 = Button(frame1, text='Открыть TXT-файл',
              border=3, bg='lightgray', anchor='s', command=button1)
but1.pack(side=LEFT, anchor='nw')
but1.config(wraplength=90)

but2 = Button(frame1, text='Открыть CSV-файл',
              border=3, bg='lightgray', command=button2)
but2.pack(side=LEFT, anchor='nw')
but2.config(wraplength=90)

but3 = Button(frame1, text='Сохранить TXT-файл',
              border=3, bg='lightgray', command=button3)
but3.pack(side=LEFT, anchor='nw')
but3.config(wraplength=90)

but4 = Button(frame1, text='Сохранить CSV-файл(ANSI)',
              border=3, bg='lightgray', command=button4)
but4.pack(side=LEFT, anchor='nw')
but4.config(wraplength=90)

but5 = Button(frame1, text='Показать все контакты',
              border=3, bg='lightgray', command=button5)
but5.pack(side=LEFT, anchor='nw')
but5.config(wraplength=90)

but6 = Button(frame1, text='Поиск контакта',
              border=3, bg='lightgray', command=button6)
but6.pack(side=LEFT, anchor='nw')
but6.config(wraplength=85)

but7 = Button(frame1, text='Добавить конаткт',
              border=3, bg='lightgray', command=button7)
but7.pack(side=LEFT, anchor='nw')
but7.config(wraplength=90)

but8 = Button(frame1, text='Изменить контакт',
              border=3, bg='lightgray', command=button8)
but8.pack(side=LEFT, anchor='nw')
but8.config(wraplength=90)

but9 = Button(frame1, text='Удалить контакт',
              border=3, bg='lightgray', command=button9)
but9.pack(side=LEFT, anchor='nw')
but9.config(wraplength=85)


my_tree = ttk.Treeview(frame2)

my_tree['columns'] = ("Name", "PhoneNumber", "Comment")
my_tree.column("#0", width=20, minwidth=2)
my_tree.column("Name", anchor=W, width=220, minwidth=25)
my_tree.column("PhoneNumber", anchor=W, width=120, minwidth=25)
my_tree.column("Comment", anchor=W, width=220, minwidth=25)

my_tree.heading("#0", anchor=CENTER)
my_tree.heading("Name", anchor=CENTER)
my_tree.heading("PhoneNumber", anchor=CENTER)
my_tree.heading("Comment", anchor=CENTER)

my_tree.insert(parent='', index='end', iid=0, text='Parents',
               values=('Иван Иванов', '89114563322', 'юрист'))
my_tree.insert(parent='', index='end', iid=1, text='Parents',
               values=('Иван Иванов', '89114563322', 'юрист'))
my_tree.insert(parent='', index='end', iid=2, text='Parents',
               values=('Иван Иванов', '89114563322', 'юрист'))

my_tree.pack(pady=20)

tk.mainloop()
