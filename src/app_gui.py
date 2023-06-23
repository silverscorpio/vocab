import sys
from datetime import datetime
from pathlib import Path
from tkinter import *
from tkinter import messagebox, ttk

from word_list import WordList


class VocabGUI:
    DATE_TODAY = datetime.today().strftime("%d-%m-%Y")
    HELP_INFO_MSG = """
    Welcome to Vocab Practice App! Bring along a word list to practice, use the app to learn the words,
    track the ones you remember and the ones you don't. Have fun!
    """
    DONE_INFO_MSG = "All words learnt, Great Work!"

    def __init__(
        self,
        filepath: str | Path,
        parser: str,
        width: int = 800,
        height: int = 600,
        bg_color: str = "#ffcf40",
        font_size: int = 13,
        font_family: str = "Avenir",
        font_type: str = "bold",
    ):
        # wordlist variables
        self.wd_list_filepath = filepath
        self.wd_list_parser = parser

        # app logic variables
        self.word_list_obj = None
        self.orig_word_list_length: int = 0
        self._current_word = None
        self.words_learnt: int = 0
        self.word_list_gen = None

        # app props
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.font_size = font_size
        self.font_family = font_family
        self.font_type = font_type
        self.font: tuple = (self.font_family, self.font_size, self.font_type)
        self.padding: dict = {"padx": 10, "pady": 10}

        # tkinter specific variables
        # 1280 X 800
        self.root = Tk()
        self.root.title("Vocab Practice App")
        self.root.geometry(
            self._center_screen(win_width=self.width, win_height=self.height)
        )
        self.root.resizable(False, False)
        self.root.configure(bg=self.bg_color)

        # string variables for tkinter elements
        self.word_variable = StringVar(master=self.root, value="Word ")
        self.meaning_variable = StringVar(master=self.root, value="Show Meaning")
        self.status_learnt_variable = StringVar(master=self.root, value="Words Learnt ")
        self.status_remaining_variable = StringVar(
            master=self.root, value="Words Remaining "
        )
        # TODO - time-based mode, couple it with save progress (db) functionality
        # self.timer_variable = StringVar(master=self.root, value="Timer")

        # style
        s = ttk.Style()
        s.theme_use("clam")

        # button style
        s.configure(
            "TButton",
            font=self.font,
            foreground="#23272a",
            background="#baffc9",
            padding=5,
            relief="flat",
        )

        # label style
        s.configure(
            "TLabel",
            font=self.font,
            foreground="#23272a",
            background="#baffc9",
            padding=5,
            relief="flat",
        )

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)

        # widgets
        self.date_label = ttk.Label(
            self.root,
            text=VocabGUI.DATE_TODAY,
            font=self.font,
        )
        self.start = ttk.Button(self.root, text="Start", command=self._start_button)
        self.info = ttk.Button(
            self.root,
            text="Info",
            command=lambda: VocabGUI.info_button(msg=VocabGUI.HELP_INFO_MSG),
        )

        self.word = ttk.Label(
            self.root,
            font=self.font,
            textvariable=self.word_variable,
        )
        self.remember = ttk.Button(
            self.root,
            text="Remember",
            command=self._remember_button,
            state="disabled",
        )

        self.dont_remember = ttk.Button(
            self.root,
            text="Don't Remember",
            command=self._dont_remember_button,
            state="disabled",
        )
        self.meaning = ttk.Button(
            self.root,
            textvariable=self.meaning_variable,
            command=lambda: VocabGUI._show_variable(
                variable_to_set=self.meaning_variable,
                text_to_show=self._current_word[1],
            ),
        )
        self.status_learnt = ttk.Label(
            self.root, font=self.font, textvariable=self.status_learnt_variable
        )
        self.status_remaining = ttk.Label(
            self.root, font=self.font, textvariable=self.status_remaining_variable
        )
        self.close = ttk.Button(self.root, text="Close", command=self._close_button)

        # self.timer_label = ttk.Label(
        #     self.root, font=self.font, textvariable=self.timer_variable
        # )

        # placing the widgets in grid
        # top row
        self.date_label.grid(row=0, column=0, columnspan=2, sticky=NW, **self.padding)
        self.start.grid(row=0, column=2, columnspan=2, sticky=N, **self.padding)
        self.info.grid(row=0, column=4, columnspan=2, sticky=NE, **self.padding)
        # self.timer_label.grid(row=0, column=5, sticky=NE, **self.padding)

        # middle row
        self.word.grid(row=1, column=1, columnspan=4, sticky=N, **self.padding)
        self.remember.grid(row=2, column=1, columnspan=2, sticky=NE, **self.padding)
        self.dont_remember.grid(
            row=2, column=3, columnspan=2, sticky=NW, **self.padding
        )
        self.meaning.grid(row=3, column=2, columnspan=2, **self.padding)

        # bottom row
        self.status_learnt.grid(row=4, columnspan=3, sticky=SW, **self.padding)
        self.status_remaining.grid(row=5, columnspan=3, sticky=SW, **self.padding)
        self.close.grid(row=5, column=5, sticky=SE, **self.padding)

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

    def _start_button(self) -> None:
        self.remember.configure(state="normal")
        self.dont_remember.configure(state="normal")
        self.update()

    def _remember_button(self) -> None:
        if self.words_learnt == (
            self.orig_word_list_length - 1
        ):  # one before the last word
            VocabGUI.info_button(msg=VocabGUI.DONE_INFO_MSG)
            sys.exit()

        self.word_list_obj.parsed_wd_list.pop(
            self.word_list_obj.parsed_wd_list.index(self._current_word)
        )
        self.words_learnt += 1
        self.update()

    def _dont_remember_button(self) -> None:
        self.word_list_obj.parsed_wd_list.append(
            self.word_list_obj.parsed_wd_list.pop(
                self.word_list_obj.parsed_wd_list.index(self._current_word)
            )
        )

        self.update()

    def set_word_list(self) -> None:
        # dependency wordlist
        temp_wl = WordList(filepath=self.wd_list_filepath, parser=self.wd_list_parser)
        # temp_wl.shuffle_wd_list()
        self.word_list_obj = temp_wl
        self.orig_word_list_length = len(self.word_list_obj.parsed_wd_list)

    def generate_word(self) -> None:
        self.word_list_gen = self.word_list_obj.get_wd_list_gen()
        try:
            self._current_word = next(self.word_list_gen)
        except StopIteration:
            print("Word list is empty")
            sys.exit()

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

    def _close_button(self) -> None:
        self.root.destroy()

    def get_wd_list(self) -> list[tuple]:
        return self.word_list_obj.parsed_wd_list

    @staticmethod
    def _show_variable(variable_to_set, text_to_show: str) -> None:
        variable_to_set.set(value=text_to_show)

    @staticmethod
    def info_button(msg: str) -> None:
        messagebox.showinfo(
            title="Info",
            message=msg,
        )


if __name__ == "__main__":
    test_fpath = Path.cwd().parents[0] / "word_lists" / "rt_learn_rus.txt"
    VocabGUI(filepath=test_fpath, parser="general")
