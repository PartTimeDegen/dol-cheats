import re
from pathlib import Path

from packaging.version import Version


def find_game_file(
    input_folder: str = "input",
    file_name_prefix: str = "Degrees of Lewdity",
) -> Path:
    # Get Folder
    input_folder_path = Path(input_folder)

    # Look for Games
    game_files_found = list(
        input_folder_path.glob(f"{file_name_prefix}*.html")
    )

    # Find Highest Version
    highest_version = max(
        game_files_found,
        key=lambda f: Version(re.search(r"(\d+(?:\.\d+)+)", f.stem).group(1)),  # type: ignore # Not going to be None
    )

    # Return
    return highest_version
