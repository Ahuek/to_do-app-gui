import os
from tkinter import *

root = Tk()
root.title('To do app')
root.configure(background="blue")


def add_task_to_file():
  with open('gtask.txt', 'a') as file:
    file.write(f"\n{addentry.get()},{Date.get()}")


def add_task():
  addlabel = Label(root, text='Add task')
  addlabel.pack()
  global addentry
  addentry = Entry(root)
  addentry.pack()
  date_label = Label(root, text='Input Date:').pack()
  global Date
  Date = Entry(root)
  Date.pack()
  addbutton = Button(root, text='Add', command=add_task_to_file, bg='green')
  addbutton.pack()


def read_task():
  global text_read
  text_read = Text(root)
  text_read.pack()
  with open('gtask.txt', 'r') as file:
    read = file.readlines()
    for i in read:
      text_read.insert(END, i)

def final_del():
  with open('gtask.txt', 'r') as file:
    read = file.readlines()
    with open('gtask.txt', 'w') as file1:
      for i in read:
       if i.strip('\n') != delete_entry.get():
         file1.write(i)
         read = file.readlines()
         with open('gtask.txt', 'w') as file1:
          for i in read:
           if i.strip('\n') == delete_entry:
            continue
           else:
             file1.write(i)
def delete_task():
  global delete_entry
  delete_entry = Entry(root)
  delete_entry.pack()
  deleted=Button(root, text='Delete', command=final_del).pack()
  


          


def delete_all():
  with open('gtask.txt', 'w') as file:
    file.write('')
    text_read.delete(1.0, END)


delete_tasks = Button(root, text='Delete Task', command=delete_task,
                      bg='red').pack()
delete_all = Button(root,
                    text='Delete All tasks',
                    command=delete_all,
                    bg='red').pack()
read_button = Button(root, text='Readtask', command=read_task,
                     bg='orange').pack()
task_button = Button(root, text='Add task', command=add_task,
                     bg='orange').pack()
root.mainloop()
