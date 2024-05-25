#IT-209 – Lab Assignment 12 (LA12)
# Purpose:Python GUI / tkinter
# Name: Samuel Essandoh

print("START OF LAB")
from tkinter import *

class DesignCard(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.suit_symbols_dict = { "hearts" :"\u2665", "spades": "\u2660" ,"diamonds":"\u2666", "clubs": "\u2663"}
        self.root = root
        self.labels = {"UpperRight" : None, "Center" : None, "LowerLeft": None}
        self.create_widgets()
        self.canvas = None

    def create_widgets(self):
        self.rank_label = Label(self, text="Rank:")
        self.rank_entry = Entry(self)
        self.suit_label = Label(self, text="Suit:")
        self.suit_entry = Entry(self)
        self.submit_button = Button(self, text="Submit", command=self.create_card)
        self.rank_label.grid(row=0, column=0)
        self.rank_entry.grid(row=0, column=1)
        self.suit_label.grid(row=1, column=0)
        self.suit_entry.grid(row=1, column=1)
        self.submit_button.grid(row=2, columnspan=2)

    pass


    def create_card(self):
        rank = self.rank_entry.get()
        suit = self.suit_entry.get()

        if self.validate(rank, suit):
            self.initialise_the_canvas()
            self.labels["UpperRight"].config(text=rank + self.suit_symbols_dict[suit])
            self.labels["Center"].config(text=rank + self.suit_symbols_dict[suit])
            self.labels["LowerLeft"].config(text=rank + self.suit_symbols_dict[suit])
        else:
            error_label = Label(self, text="Incorrect input. Please try again.")
            error_label.grid(row=3, columnspan=2)
            pass

    def initialise_the_canvas(self):
        if self.canvas is None:
            self.canvas = Canvas(self, width=200, height=300, bg='green')
            self.canvas.create_rectangle(50, 50, 150, 250, fill='white')
            self.canvas.grid(row=4, columnspan=2)
            self.labels["UpperRight"] = Label(self.canvas, text="")
            self.labels["Center"] = Label(self.canvas, text="")
            self.labels["LowerLeft"] = Label(self.canvas, text="")
            self.labels["UpperRight"].place(relx=0.7, rely=0.2, anchor=NE)
            self.labels["Center"].place(relx=0.5, rely=0.5, anchor=CENTER)
            self.labels["LowerLeft"].place(relx=0.3, rely=0.8, anchor=SW)

            pass

    def validate(self, rank="", suit=""):
        if rank in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q",
                    "A"] and suit in self.suit_symbols_dict.keys():
            return True
        else:
            print(rank, suit)
            return False


root = Tk()
app = DesignCard(root)
app.pack()
root.mainloop()
print("END OF LAB")