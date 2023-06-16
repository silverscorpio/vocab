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

# if not (Path.cwd() / "word_lists" / "parsed_word_lists").exists():
#     (Path.cwd() / "word_lists" / "parsed_word_lists").mkdir(parents=True, exist_ok=True)

# if filename is None:
#     self.dir_path = Path.cwd().parents[0] / "word_lists"

# self.filepaths = [(Path.cwd().parents[0] / "word_lists" / f) for f in filenames]
# self.raw_wd_lists = [self.read_wd_list(file_path=f_path) for f_path in self.filepaths]
