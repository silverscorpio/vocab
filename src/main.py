from pathlib import Path

from app_gui import VocabGUI


def main():
    test_fpath = Path.cwd().parents[0] / "word_lists" / "rt_learn_rus.txt"
    VocabGUI(filepath=test_fpath, parser="general")


if __name__ == "__main__":
    main()
