def check():
    for i in range(2):
        yield i


# x = check()
# print(x)
# print(next(x))
# print(next(x))


x = [1, 2, 3]

while x:
    print("p")
    x.pop()

# content frame code for tkinter
# content frame
# self.mainframe = ttk.Frame(self.root, width=600, height=400, relief=tkinter.GROOVE, borderwidth=5)
# self.mainframe.grid(column=0, row=0, sticky=NSEW)
