"""Different parsers for word lists depending on format """

from pathlib import Path, PosixPath


def yandex_parser(raw_list: list[str]) -> list[tuple]:
    """Yandex translate based word lists"""
    # format -> word, /n, meaning
    remove_newlines = [word.strip("\n") for word in raw_list if word != "\n"]
    return [
        (remove_newlines[idx].lower(), remove_newlines[idx + 1].lower())
        for idx in range(0, len(remove_newlines), 2)
    ]


def general_parser(raw_list: list[str]) -> list[tuple]:
    """General parser for vocab lists"""
    # format –> word – meaning
    parsed_wd_list = []
    for pair in raw_list:
        word_meaning = pair.split("–")  # en dash (option + hyphen)
        parsed_wd_list.append(
            (word_meaning[0].strip().lower(), word_meaning[1].strip().lower())
        )
    return parsed_wd_list


def read_wd_list_from_file(file_path: str | Path) -> list[str]:
    """Read a word list file using its location"""
    with open(file_path, "r") as f:
        return f.readlines()


def write_parsed_wd_list_to_file(wd_list_data: list[tuple]) -> None:
    """store the parsed word lists in a file"""
    folder_path = Path.cwd().parents[0] / "word_lists" / "test.txt"
    with open(folder_path, "w") as f:
        for pair in wd_list_data:
            f.write(f"{pair[0]} - {pair[1]}\n")


def combine_parsed_wd_lists_from_files(save_combined_data: bool = True) -> None:
    # write combined data to file in format: "word - meaning"
    combined_list_data = []
    parsed_lists_folder_path = (
        Path.cwd().parents[0] / "word_lists" / "parsed_word_lists"
    )
    text_files = [i for i in parsed_lists_folder_path.glob("*.txt") if i.is_file()]
    for f in text_files:
        combined_list_data.extend(read_wd_list_from_file(file_path=str(f)))
    if save_combined_data:
        combined_file_path = parsed_lists_folder_path / "combined_wd_list.txt"
        with open(combined_file_path, "w") as f:
            f.writelines(combined_list_data)


if __name__ == "__main__":
    # x = [('panda', 'world'), ('spider', 'tiger')]
    # write_parsed_wd_list(x)
    combine_parsed_wd_lists_from_files()
    # raw_data = read_wd_list_from_file(file_name="rt_learn_rus.txt")
    # print(general_parser(raw_data))
