from pathlib import Path


def read_list(filename: str) -> list:
    word_list_path = Path.cwd() / "word_lists" / filename
    with open(word_list_path, 'r') as f:
        list_data = f.readlines()
    return list_data


def clean_list(raw_list: list) -> dict:
    word_trans_dict = {}
    remove_newlines = [word.strip("\n") for word in raw_list if word != "\n"]
    for idx in range(0, len(remove_newlines), 2):
        word_trans_dict[remove_newlines[idx].lower()] = remove_newlines[idx + 1].lower()
    return word_trans_dict


if __name__ == '__main__':
    word_data = read_list(filename="sputnik_words.txt")
    for key, val in clean_list(raw_list=word_data).items():
        print(f"{key} - {val}")
