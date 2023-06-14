import sys
from datetime import datetime
from tkinter import *
from tkinter import ttk

from word_list import WordList


class VocabGUI:
    WORDS_FILENAME = "sputnik_words.txt"
    DATE_TODAY = datetime.today().strftime("%d-%m-%Y")

    def __init__(
        self,
        width: int = 700,
        height: int = 500,
        bg_color: str = "#5B5C73",
        font_size: int = 16,
        font_family: str = "Ariel",
    ):

        # app logic variables
        self.word_list = None
        self.orig_word_list_length: int = 0
        self._current_word = None
        self.words_learnt: int = 0

        # app props
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.font_size = font_size
        self.font_family = font_family
        self.font: tuple = (self.font_family, self.font_size)

        # tkinter specific variables
        # 1280 X 800
        self.root = Tk()
        self.root.title("Russian Vocab App")
        self.root.geometry(
            self._center_screen(win_width=self.width, win_height=self.height)
        )
        self.root.resizable(False, False)
        self.root.configure(bg=self.bg_color)

        # string variables for tkinter elements
        self.word_variable = StringVar(master=self.root, value="Words ")
        self.meaning_variable = StringVar(master=self.root, value="Show Meaning")
        self.status_learnt_variable = StringVar(master=self.root, value="Words Learnt ")
        self.status_remaining_variable = StringVar(
            master=self.root, value="Words Remaining "
        )

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
            text=VocabGUI.DATE_TODAY,
            font=self.font,
        )
        self.word = ttk.Label(
            self.root,
            font=self.font,
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
            self.root,
            textvariable=self.meaning_variable,
            command=lambda: VocabGUI._show_variable(
                variable_to_set=self.meaning_variable,
                text_to_show=self._current_word[1],
            ),
        )
        self.timer_label = ttk.Label(
            self.root,
            text="Timer",
            font=self.font,
        )
        self.status_learnt = ttk.Label(
            self.root, font=self.font, textvariable=self.status_learnt_variable
        )
        self.status_remaining = ttk.Label(
            self.root, font=self.font, textvariable=self.status_remaining_variable
        )

        # placing the widgets in grid
        # top row
        self.date_label.grid(row=0, column=0, sticky=NW, padx=10, pady=10)
        self.start.grid(row=0, column=2, sticky=NE, padx=10, pady=10)
        self.timer_label.grid(row=0, column=5, sticky=NE, padx=10, pady=10)

        # middle row
        self.word.grid(row=1, column=2, padx=10, pady=10)
        self.remember.grid(row=2, column=1, padx=10, pady=10)
        self.dont_remember.grid(row=2, column=3, padx=10, pady=10)
        self.meaning.grid(row=3, column=2, padx=10, pady=10)

        # bottom row
        self.status_learnt.grid(row=4, column=0, sticky=SW, padx=10, pady=10)
        self.status_remaining.grid(row=5, columnspan=2, sticky=SW, padx=10, pady=10)
        self.close.grid(row=5, column=5, sticky=SE, padx=10, pady=10)

        # start the main event loop of tkinter and get word list
        self.initiate_app()

    def _center_screen(self, win_width: int, win_height: int) -> str:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - win_width) // 2
        y_coordinate = (screen_height - win_height) // 2
        return f"{win_width}x{win_height}+{x_coordinate}+{y_coordinate}"

    def initiate_app(self) -> None:
        self.set_word_list()
        self.root.mainloop()

    def _close_button(self) -> None:
        self.root.destroy()

    def _start_button(self) -> None:
        self.update()

    def update(self) -> None:
        self.generate_word()
        VocabGUI._show_variable(
            variable_to_set=self.word_variable, text_to_show=self._current_word[0]
        )
        VocabGUI._show_variable(
            variable_to_set=self.meaning_variable, text_to_show="Show Meaning"
        )
        VocabGUI._show_variable(
            variable_to_set=self.status_learnt_variable,
            text_to_show=f"Words Learnt: {self.words_learnt}",
        )
        VocabGUI._show_variable(
            variable_to_set=self.status_remaining_variable,
            text_to_show=f"Words Remaining: {self.orig_word_list_length - self.words_learnt}",
        )

    def _remember_button(self) -> None:
        removed_word = self.word_list.parsed_wd_list.pop(
            self.word_list.parsed_wd_list.index(self._current_word)
        )
        print(removed_word)
        self.words_learnt += 1
        self.update()

    def _dont_remember_button(self) -> None:
        self.update()

    def set_word_list(self) -> None:
        temp_wl = WordList(filename=VocabGUI.WORDS_FILENAME)
        temp_wl.get_shuffled_list()
        self.word_list = temp_wl
        self.orig_word_list_length = len(self.word_list.parsed_wd_list)

    def generate_word(self) -> None:
        _word_gen = self.word_list.wd_list_generator
        try:
            self._current_word = next(_word_gen)
        except StopIteration:
            print("Word List is Empty!")
            sys.exit()

    def get_wd_list(self) -> list[tuple]:
        return self.word_list.parsed_wd_list

    @staticmethod
    def _show_variable(variable_to_set, text_to_show: str) -> None:
        variable_to_set.set(value=text_to_show)


if __name__ == "__main__":
    app_gui = VocabGUI()
