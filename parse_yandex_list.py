def read_list(filename: str) -> list:
    with open(filename, 'r') as f:
        list_data = f.readlines()
    return list_data


def clean_list(raw_list: list) -> dict:
    word_trans_dict = {}
    remove_newlines = [word.strip("\n") for word in raw_list if word != "\n"]
    for idx in range(0, len(remove_newlines), 2):
        word_trans_dict[remove_newlines[idx]] = remove_newlines[idx + 1].lower()
    return word_trans_dict


if __name__ == '__main__':
    word_data = read_list("./word_lists/sputnik_words.txt")
    for key, val in clean_list(raw_list=word_data).items():
        print(f"{key} - {val}")
