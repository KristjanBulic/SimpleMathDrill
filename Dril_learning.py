#!/usr/bin/env python3

from tkinter import *
import random
import os

version = 1.0

#files functions
def read_config():
    """
    reads config file and returns tuple (number_range, write_file)
    """
    file = open("dril_conf.txt", 'r')
    data = file.read()
    data = data.split("\n")
    file.close()

    highest_number = data[0][data[0].index('=') + 1 ::]
    q_num = data[1][data[1].index('=') + 1 ::]
    return (highest_number, q_num)

#####read congig

top_number, q_num = read_config()
top_number = int(top_number)
q_num = int(q_num)

def get_numbers():
    """
    returns tuple of result_number and other number
    """
    result_number = random.choice(range(1, top_number + 1))
    first_number = random.choice(range(1, top_number + 1))

    if result_number >= first_number:
        sec_number = result_number - first_number
        operation = "+"
    elif result_number < first_number:
        sec_number = first_number - result_number
        operation = "-"

    return (first_number, operation, sec_number, result_number)

def compare(x, right_x, main, check_Label):
    """
    Returns true and kills childen if answer is correct
    """
    if x == right_x:
            check_Label.config(bg="green")
            main.destroy()
            return True
    check_Label.config(bg="red")
    return False

top = Tk()
top.title("Get started")
L1 = Label(top, text = "Click Start When Ready")
L1.grid( row = 0)
B1 = Button(top, command = top.destroy, text = "START")
B1.grid( row = 1)
quit_button = Button(top, text = "EXIT", command = lambda: exit(top))
quit_button.grid(row = 2)
top.mainloop()

def exit(window):
    """
    exit program without solving
    """
    window.destroy()
    os._exit(0)

def main_program():
    main = Tk()
    main.title("Dril learning {}".format(version))
    #main.geometry("400x200")

    #set numbers
    numbers = get_numbers()
    n1, operation, n2, result = numbers
    options = sorted([random.choice(range(top_number)),
                    random.choice(range(top_number)),
                    n2,])


    Number1 = Label(main, text = n1)
    operation = Label(main, text = operation)
    Number2 = Label(main, text = "X")
    equalSign = Label(main, text = "=")
    Result = Label(main, text = result)

    Lans1 = Label(main, text = options[0])
    Lans2 = Label(main, text = options[1])
    Lans3 = Label(main, text = options[2])

    ans1 = Button(main, text = "^", command = lambda: compare(options[0], n2, main, ans1))
    ans2 = Button(main, text = "^", command = lambda: compare(options[1], n2, main, ans2))
    ans3 = Button(main, text = "^", command = lambda: compare(options[2], n2, main, ans3))
    quit_button = Button(main, text = "EXIT", command = lambda: exit(main))

    Number1.grid(column = 0, row = 1)
    operation.grid(column = 1, row = 1)
    Number2.grid(column = 2, row = 1)
    equalSign.grid(column = 3, row = 1)
    Result.grid(column = 4, row = 1)

    Lans1.grid(row =2, column=1)
    Lans2.grid(row =2, column=2)
    Lans3.grid(row =2, column=3)

    ans1.grid(column = 1, row = 3)
    ans2.grid(column = 2, row = 3)
    ans3.grid(column = 3, row = 3)
    quit_button.grid(column = 2, row = 4)

    main.mainloop()

def program_loop():
    for i in range(q_num):
        main_program()


program_loop()
