import sys
from datetime import datetime
from tkinter import *
from tkinter import ttk

from word_list import WordList


class VocabGUI:
    WORDS_FILENAME = "sputnik_words.txt"

    def __init__(self, width: int = 700, height: int = 500, bg_color: str = "#5B5C73"):

        # app logic variables
        self.word_list = None
        self._current_word = None
        self.width = width
        self.height = height
        self.bg_color = bg_color

        # tkinter specific variables
        # 1280 X 800
        self.root = Tk()
        self.root.title("Russian Vocab App")
        self.root.geometry(
            self._center_screen(win_width=self.width, win_height=self.width)
        )
        self.root.resizable(False, False)
        self.root.configure(bg=self.bg_color)

        # string variables for tkinter elements
        self.word_variable = StringVar(master=self.root, value="WORDS")
        self.meaning_variable = StringVar(master=self.root, value="MEANING")

        # style
        s = ttk.Style()
        s.theme_use("clam")

        # FIXME unqual sizes of frame and root
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)

        # widgets
        self.date_label = ttk.Label(
            self.root,
            text=VocabGUI.date_today(),
            font=(
                "Ariel",
                16,
            ),
        )
        self.word = ttk.Label(
            self.root,
            font=(
                "Ariel",
                16,
            ),
            textvariable=self.word_variable,
        )
        self.start = ttk.Button(self.root, text="Start", command=self._start_button)
        self.remember = ttk.Button(
            self.root, text="Remember", command=self._remember_button
        )
        self.dont_remember = ttk.Button(
            self.root, text="Don't Remember", command=self._dont_remember_button
        )
        self.close = ttk.Button(self.root, text="Close", command=self._close_button)
        self.meaning = ttk.Button(
            self.root, textvariable=self.meaning_variable, command=self._show_meaning
        )
        self.timer_label = ttk.Label(
            self.root,
            text="Timer",
            font=(
                "Ariel",
                16,
            ),
        )
        self.status_learnt = ttk.Label(
            self.root,
            text="Learnt",
            font=(
                "Ariel",
                16,
            ),
        )
        self.status_remaining = ttk.Label(
            self.root,
            text="Remaining",
            font=(
                "Ariel",
                16,
            ),
        )

        # placing the widgets in grid
        self.date_label.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
        self.start.grid(row=0, column=2, sticky=NE, padx=10, pady=10)
        self.timer_label.grid(row=0, column=5, sticky=NE, padx=10, pady=10)

        self.word.grid(row=1, column=2, padx=10, pady=10)
        self.remember.grid(row=2, column=1, padx=10, pady=10)
        self.dont_remember.grid(row=2, column=3, padx=10, pady=10)
        self.meaning.grid(row=3, column=2, padx=10, pady=10)

        self.status_learnt.grid(row=4, column=0, sticky=SW, padx=10, pady=10)
        self.status_remaining.grid(row=5, column=0, sticky=SW, padx=10, pady=10)
        self.close.grid(row=5, column=5, sticky=SE, padx=10, pady=10)

        self.initiate_app()

    @staticmethod
    def date_today():
        return datetime.today().strftime("%d-%m-%Y")

    def _center_screen(self, win_width: int, win_height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - win_width) // 2
        y_coordinate = (screen_height - win_height) // 2
        return f"{win_width}x{win_height}+{x_coordinate}+{y_coordinate}"

    def initiate_app(self):
        self.set_word_list()
        self.root.mainloop()

    def _close_button(self):
        self.root.destroy()

    def _start_button(self):
        self.fetch_update_word()

    def fetch_update_word(self):
        self.generate_word()
        self.display_word()
        self.meaning_variable.set(value="Show Meaning")

    def _remember_button(self):
        removed_word = self.word_list.parsed_wd_list.pop(
            self.word_list.parsed_wd_list.index(self._current_word)
        )
        print(removed_word)
        self.fetch_update_word()

    def _dont_remember_button(self):
        self.fetch_update_word()

    def set_word_list(self) -> None:
        temp_wl = WordList(filename=VocabGUI.WORDS_FILENAME)
        temp_wl.get_shuffled_list()
        self.word_list = temp_wl

    def generate_word(self):
        _word_gen = self.word_list.wd_list_generator
        try:
            self._current_word = next(_word_gen)
        except StopIteration:
            print("Word list empty")
            sys.exit()

    def display_word(self):
        self.word_variable.set(value=self._current_word[0])

    def get_wd_list(self) -> list[tuple]:
        return self.word_list.parsed_wd_list

    def _show_meaning(self):
        self.meaning_variable.set(value=self._current_word[1])


if __name__ == "__main__":
    y = VocabGUI()
