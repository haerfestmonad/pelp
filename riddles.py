from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("riddles")

def riddle1():
    riddle1 = Label(text="what needs to be broken before it can be used?")
    entry1 = Entry()
    bttn1 = Button(text="guess!", 
                   command=lambda: game1(riddle2))
    riddle1.pack()
    entry1.pack()
    bttn1.pack()
    def game1(riddle2):
        if entry1.get().lower() == "egg":
            riddle2()
            bttn1.pack_forget()
            messagebox.showinfo("correct", 
                                "nice!")
        else:
            messagebox.showerror("wrong", 
                                 "wrong, try again.")


def riddle2():
    riddle2 = Label(text="what month of the year has 28 days?")
    entry2 = Entry()
    bttn2 = Button(text="guess!", 
                   command=lambda: game2(riddle3))
    riddle2.pack()
    entry2.pack()
    bttn2.pack()
    def game2(riddle3):
        if entry2.get().lower() == "all of them":
            riddle3()
            bttn2.pack_forget()
            messagebox.showinfo("correct", 
                                "right! you got this!")
        else:
            messagebox.showerror("wrong", 
                                 "ouch, try again.")

def riddle3():
    riddle3 = Label(text="what is full of holes but still holds water?")
    entry3 = Entry()
    bttn3 = Button(text="guess!", 
                   command=lambda: game3(riddle4))
    riddle3.pack()
    entry3.pack()
    bttn3.pack()
    def game3(riddle4):
        if entry3.get().lower() == "sponge":
            riddle4()
            bttn3.pack_forget()
            messagebox.showinfo("correct", 
                                "nailed it! 2 more riddles!")
        else:
            messagebox.showerror("wrong", 
                                 "nooo... try again!")

def riddle4():
    riddle4 = Label(text="what question can you never answer yes to?")
    entry4 = Entry()
    bttn4 = Button(text="guess!", 
                   command=lambda: game4(riddle5))
    riddle4.pack()
    entry4.pack()
    bttn4.pack()
    def game4(riddle5):
        if entry4.get().lower() == "are you asleep yet?":
            riddle5()
            bttn4.pack_forget()
            messagebox.showinfo("correct",
                                "you guessed it!")
        else:
            messagebox.showinfo("wrong",
                                "nope. maybe second time is the charm?")

def riddle5():
    riddle5 = Label(text="what is always in front of you but can't be seen?")
    entry5 = Entry()
    bttn5 = Button(text="guess!", 
                   command=lambda: game5())
    riddle5.pack()
    entry5.pack()
    bttn5.pack()
    def game5():
        if entry5.get().lower() == "future":
            bttn5.pack_forget()
            messagebox.showinfo("win",
                                "you won! congratulations!")
        else:
            messagebox.showerror("wrong", 
                                 "wrong... try again.")
#me when

riddle1()

root.mainloop()