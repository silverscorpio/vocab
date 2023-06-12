from tkinter import *
from tkinter import ttk
from datetime import datetime
from word_list import WordList


class VocabGUI:

    def __init__(self):
        self.word_list = None
        # 1280 X 800
        self.root = Tk()
        self.root.title("Russian Vocab App")
        self.root.geometry(self._center_screen(win_width=700, win_height=500))
        self.root.resizable(False, False)
        self.root.configure(bg="#5B5C73")

        # style
        s = ttk.Style()
        s.theme_use("clam")

        # FIXME unqual sizes of frame and root
        # content frame
        # self.mainframe = ttk.Frame(self.root, width=600, height=400, relief=tkinter.GROOVE, borderwidth=5)
        # self.mainframe.grid(column=0, row=0, sticky=NSEW)

        self.root.columnconfigure(0, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)

        # widgets
        self.date_label = ttk.Label(self.root, text=VocabGUI.date_today(), font=("Ariel", 16,))
        # self.word = ttk.Label(self.root, text="Word", font=("Ariel", 16,))
        self.word = self._update_insert_word(word_to_display="first")
        self.remember = ttk.Button(self.root, text="Remember", command=self._remember_button)
        self.dont_remember = ttk.Button(self.root, text="Don't Remember", command=self._dont_remember_button)
        self.close = ttk.Button(self.root, text="Close", command=self._close_button)
        self.meaning = ttk.Button(self.root, text="Show Meaning")
        self.timer_label = ttk.Label(self.root, text="Timer", font=("Ariel", 16,))
        self.status_learnt = ttk.Label(self.root, text="Learnt", font=("Ariel", 16,))
        self.status_remaining = ttk.Label(self.root, text="Remaining", font=("Ariel", 16,))

        # placing the widgets in grid
        self.date_label.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
        self.timer_label.grid(row=0, column=5, sticky=NE, padx=10, pady=10)

        self.word.grid(row=1, column=2, padx=10, pady=10)
        self.remember.grid(row=2, column=1, padx=10, pady=10)
        self.dont_remember.grid(row=2, column=3, padx=10, pady=10)
        self.meaning.grid(row=3, column=2, padx=10, pady=10)

        self.status_learnt.grid(row=4, column=0, sticky=SW, padx=10, pady=10)
        self.status_remaining.grid(row=5, column=0, sticky=SW, padx=10, pady=10)
        self.close.grid(row=5, column=5, sticky=SE, padx=10, pady=10)

    @staticmethod
    def date_today():
        return datetime.today().strftime("%d-%m-%Y")

    def _center_screen(self, win_width: int, win_height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - win_width) // 2
        y_coordinate = (screen_height - win_height) // 2
        return f"{win_width}x{win_height}+{x_coordinate}+{y_coordinate}"

    def run_gui(self):
        # main event loop tkinter
        self.root.mainloop()

    def _close_button(self):
        self.root.destroy()

    def _remember_button(self):
        pass

    def _dont_remember_button(self):
        pass

    # MAIN APP LOGIC
    def app_logic(self) -> None:
        temp_wl = WordList(filename="sputnik_words.txt")
        temp_wl.get_shuffled_list()
        self.word_list = temp_wl

    def _update_insert_word(self, word_to_display):
        return ttk.Label(self.root, text=word_to_display, font=("Ariel", 16,))

    def get_wd_list(self) -> list[tuple]:
        return self.word_list.parsed_wd_list


if __name__ == '__main__':
    y = VocabGUI()
    y.app_logic()
    print(y.get_wd_list())
