from pathlib import Path

from backend.cheat_changes import cheats_catalogue
from backend.file_changer import change_file
from backend.file_management import find_game_file


def main():
    # Intro
    print("Hello World")

    # Find Folder
    game_file = find_game_file()

    # Get Cheats
    cheats = cheats_catalogue

    # Apply Cheats
    game_content = game_file.read_text()
    new_file = change_file(game_content, cheats)

    # Save File to Output
    new_file_name = Path("output/Degrees of Lewdity CHEATED.html")
    with new_file_name.open("w") as f:
        f.write(new_file)


if __name__ == "__main__":
    main()
