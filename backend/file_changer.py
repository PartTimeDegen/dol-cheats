def change_file(
    game_contents: str,
    enabled_cheats: dict[str, dict[str, str]],
) -> str:
    # Apply Changes
    for cheat_name, cheat_dict in enabled_cheats.items():
        # Declare Cheat
        print(f"- Applying: {cheat_name.replace('_', ' ').title()}")
        replacement_count = 0

        # Text Replacer
        for old_text, new_text in cheat_dict.items():
            replacement_count += game_contents.count(old_text)
            game_contents = game_contents.replace(old_text, new_text)

        # Info
        print(f"- - Replaced Total substrings: {replacement_count}")
        print()

    # Return Contents
    return game_contents
