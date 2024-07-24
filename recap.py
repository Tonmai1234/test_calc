import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()
        
        self.root.geometry("300x500")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Calculator DIP 02", font=('Kanit Medium',18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=10, y=50)

        self.button = tk.Button(self.root, text="+/-", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=80, y=50)

        self.button = tk.Button(self.root, text="%", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=150, y=50)

        self.button = tk.Button(self.root, text="/", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=220, y=50)

        self.button = tk.Button(self.root, text="7", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=10, y=130)

        self.button = tk.Button(self.root, text="8", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=80, y=130)

        self.button = tk.Button(self.root, text="9", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=150, y=130)

        self.button = tk.Button(self.root, text="x", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=220, y=130)

        self.button = tk.Button(self.root, text="4", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=10, y=210)

        self.button = tk.Button(self.root, text="5", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=80, y=210)

        self.button = tk.Button(self.root, text="6", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=150, y=210)

        self.button = tk.Button(self.root, text="-", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=220, y=210)

        self.button = tk.Button(self.root, text="1", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=10, y=290)

        self.button = tk.Button(self.root, text="2", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=80, y=290)

        self.button = tk.Button(self.root, text="3", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=150, y=290)

        self.button = tk.Button(self.root, text="+", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=220, y=290)

        self.button = tk.Button(self.root, text="0", height=4, width=17, font=('Kanit Medium', 10))
        self.button.place(x=10, y=380)

        self.button = tk.Button(self.root, text=".", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=150, y=380)

        self.button = tk.Button(self.root, text="=", height=4, width=8, font=('Kanit Medium', 10))
        self.button.place(x=220, y=380)


        self.root.mainloop()

MyCalculator()
