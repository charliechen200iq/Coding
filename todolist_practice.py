from tkinter import *

root = Tk()
root.title("practice")
root.geometry("400x1000")



#frame
my_frame = Frame(root)
my_frame.pack()


#list box and scrollbar 
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
#single, MUTIPLE, EXTENED, BROWSE
my_listbox = Listbox(my_frame, width=50, selectmode=MULTIPLE, yscrollcommand=my_scrollbar.set)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_listbox.pack(pady=10)

#Add item to listbox
my_listbox.insert(END, "this is the first item")
my_listbox.insert(END, "this is the second item")

my_list = ["One", "Second", "Third", 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    my_listbox.insert("end", item)



#button
def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text = '')

def select():
    my_label.config(text = my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0, END)

def select_all():
    result = ''
    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + "\n"
        my_label.config(text=result)

def delete_mutiple():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)
    my_label.config(text='')


delete_button = Button(root, text="Delete", command=delete)
delete_button.pack(pady=10)

select_button = Button(root, text="select", command=select)
select_button.pack(pady=10)

delete_all_button = Button(root, text="Delete All", command=delete_all)
delete_all_button.pack(pady=10)

select_mutiple_button = Button(root, text="select all", command=select_all)
select_mutiple_button.pack(pady=10)

delete_mutiple_button = Button(root, text="delete mutiple", command=delete_mutiple)
delete_mutiple_button.pack(pady=10)

my_label = Label(root, text='')
my_label.pack()

root.mainloop()