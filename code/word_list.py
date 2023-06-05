from pathlib import Path


class WordList:

    def __init__(self, filename: str):
        self.filepath = Path.cwd().parents[0] / "word_lists" / filename
        self.parsed_wd_list = WordList.clean_list(raw_list=self.read_wd_list())
        self.wd_list_generator = self.get_wd_list_gen()

    def read_wd_list(self) -> list:
        with open(self.filepath, 'r') as f:
            raw_wd_list = f.readlines()
        return raw_wd_list

    def get_wd_list_gen(self):
        yield from self.parsed_wd_list.items()

    def get_next_word(self):
        return next(self.wd_list_generator)

    @staticmethod
    def clean_list(raw_list: list) -> dict:
        # TODO currently suitable for yandex translate export copy format
        word_trans_dict = {}
        remove_newlines = [word.strip("\n") for word in raw_list if word != "\n"]
        for idx in range(0, len(remove_newlines), 2):
            word_trans_dict[remove_newlines[idx].lower()] = remove_newlines[idx + 1].lower()
        return word_trans_dict

    def __str__(self):
        for key, val in self.parsed_wd_list.items():
            print(f"{key} - {val}")


if __name__ == '__main__':
    wl = WordList(filename="sputnik_words.txt")
