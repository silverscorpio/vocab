import random
from pathlib import Path

from parsers_utils import general_parser, read_wd_list_from_file, yandex_parser


class WordList:
    def __init__(self, filepath: str | Path):
        self.filepath = filepath
        self.wd_list_generator = self.get_wd_list_gen()
        self.parsed_wd_list: list[tuple] = []

    def get_yandex_parsed_wl(self):
        self.parsed_wd_list = yandex_parser(
            raw_list=read_wd_list_from_file(file_path=self.filepath)
        )

    def get_general_parsed_wl(self):
        self.parsed_wd_list = general_parser(
            raw_list=read_wd_list_from_file(file_path=self.filepath)
        )

    def get_wd_list_gen(self):
        yield from self.parsed_wd_list

    def get_next_word(self):
        return next(self.wd_list_generator)

    def shuffle_wd_list(self):
        random.shuffle(self.parsed_wd_list)

    def get_wd_list(self):
        return f"{self.parsed_wd_list[:3]}..."


if __name__ == "__main__":
    test_fpath = Path.cwd().parents[0] / "word_lists" / "rt_learn_rus.txt"
    wl = WordList(filepath=test_fpath)
    wl.get_general_parsed_wl()
    print(wl.get_wd_list())
    g = wl.get_wd_list_gen()
    print(g)
