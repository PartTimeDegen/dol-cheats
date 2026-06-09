MAX_VALUE = 999_999_999

_infinite_money = {
    "set $money to 500": f"set $money to {MAX_VALUE}",
    "startingMoney: { earned: 500": "startingMoney: { earned: "
    + str(MAX_VALUE),
}
_no_more_bad_stats = {
    "set $stressmax to 10000": f"set $stressmax to {MAX_VALUE}",
    "set $traumamax to 5000": f"set $traumamax to {MAX_VALUE}",
    "set $tirednessmax to 2000": f"set $tirednessmax to {MAX_VALUE}",
}

_infinite_wardrobe_space = {
    "wardrobe.space = 40": f"wardrobe.space = {MAX_VALUE}",
    "wardrobe.space = 30": f"wardrobe.space = {MAX_VALUE}",
    "wardrobe.space = 20": f"wardrobe.space = {MAX_VALUE}",
}
_max_skills = {
    # Skills
    "set $seductionskill to 0": f"set $seductionskill to {MAX_VALUE}",
    "set $oralskill to 0": f"set $oralskill to {MAX_VALUE}",
    "set $vaginalskill to 0": f"set $vaginalskill to {MAX_VALUE}",
    "set $analskill to 0": f"set $analskill to {MAX_VALUE}",
    "set $handskill to 0": f"set $handskill to {MAX_VALUE}",
    "set $feetskill to 0": f"set $feetskill to {MAX_VALUE}",
    "set $bottomskill to 0": f"set $bottomskill to {MAX_VALUE}",
    "set $thighskill to 0": f"set $thighskill to {MAX_VALUE}",
    "set $chestskill to 0": f"set $chestskill to {MAX_VALUE}",
    "set $penileskill to 0": f"set $penileskill to {MAX_VALUE}",
    # Abilities
    "set $skulduggery to 0": f"set $skulduggery to {MAX_VALUE}",
    "set $skulduggeryday to 0": f"set $skulduggeryday to {MAX_VALUE}",
    "set $danceskill to 0": f"set $danceskill to {MAX_VALUE}",
    "set $swimmingskill to 0": f"set $swimmingskill to {MAX_VALUE}",
    "set $athletics to 0": f"set $athletics to {MAX_VALUE}",
    "set $tending to 0": f"set $tending to {MAX_VALUE}",
    "set $housekeeping to 0": f"set $housekeeping to {MAX_VALUE}",
}

_UNCOMFORTABLE_BEFORE = """
set $uncomfortable to {
		underwear: true,
		nude: true,
		prostituting: true,
		lewd: true,
		hypnosis: true
	
"""
_UNCOMFORTABLE_UPPER = """
set $uncomfortable to {
		underwear: false,
		nude: false,
		prostituting: false,
		lewd: false,
		hypnosis: false,
        flaunting: false
	
"""
_remove_uncomfortable = {
    # General
    _UNCOMFORTABLE_BEFORE: _UNCOMFORTABLE_UPPER,
    # Avoid it Resetting
    "set $uncomfortable.underwear to true": "set $uncomfortable.underwear to false",
    "set $uncomfortable.nude to true": "set $uncomfortable.nude to false",
    "set $uncomfortable.prostituting to true": "set $uncomfortable.prostituting to false",
    "set $uncomfortable.lewd to true": "set $uncomfortable.lewd to false",
    "set $uncomfortable.hypnosis to true": "set $uncomfortable.hypnosis to false",
    "set $uncomfortable.flaunting to true": "set $uncomfortable.flaunting to false",
    # Exposure Mechanic
    # NOTE: This is what I'm ideally trying to disable, basically when you walk
    #       around naked, the game doesn't let you and you have to run around
    #       cars and stuff, this disables that so you can walk around bits out.
    #
    # # gte
    "$exposed gte 1": f"$exposed gte {MAX_VALUE}",
    "$exposed gte 2": f"$exposed gte {MAX_VALUE}",
    # # gt
    "$exposed gt 0": f"$exposed gt {MAX_VALUE}",
    "$exposed gt 1": f"$exposed gt {MAX_VALUE}",
    "$exposed gt 2": f"$exposed gt {MAX_VALUE}",
    # # lte
    "$exposed lte 0": f"$exposed lte {MAX_VALUE}",
    "$exposed lte 1": f"$exposed lte {MAX_VALUE}",
    "$exposed lte 2": f"$exposed lte {MAX_VALUE}",
    # # lt
    "$exposed lt 1": f"$exposed lt {MAX_VALUE}",
    "$exposed lt 2": f"$exposed lt {MAX_VALUE}",
    # # is
    "$exposed is 1": f"$exposed is {MAX_VALUE}",
    "$exposed is 2": f"$exposed is {MAX_VALUE}",
}


cheats_catalogue: dict[str, dict[str, str]] = {  # Cheat Name : {Before : After}
    "infinite_money": _infinite_money,
    "no_more_bad_stats": _no_more_bad_stats,
    "infinite_wardrobe_space": _infinite_wardrobe_space,
    "max_skills":_max_skills,
    "remove_uncomfortable":_remove_uncomfortable,
}
