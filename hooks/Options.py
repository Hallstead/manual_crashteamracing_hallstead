# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, SpecialRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world. 
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class include_single_race(Choice):
    """
    Choose whether to include Single Race arcade mode.
    """
    display_name = "Include Single Race Mode?"
    option_false = 0
    option_true = 1
    default = 1

class include_turbo_track(Choice):
    """
    Choose whether to include Turbo Track in Single Race arcade mode.
    To unlock Turbo Track, you can enter the following code at the main menu:
    Hold L1+R1 and Press Right (x2), Left, Triangle, Right, Down (x2)
    """
    display_name = "Include Turbo Track?"
    option_false = 0
    option_true = 1
    default = 1

class include_cups(Choice):
    """
    Choose whether to include Cups in the locations pool.
    """
    display_name = "Include Cups?"
    option_false = 0
    option_true = 1
    default = 0

class include_time_trial(Choice):
    """
    Choose whether to include Time Trial ghosts in the locations pool.
    """
    display_name = "Include Cups?"
    option_false = 0
    option_true = 1
    default = 0

class included_ghosts(Choice):
    """
    Choose whether to include Time Trial ghosts in the locations pool.
    Each ghost will also include the ghosts before it.
    This setting does nothing if Time Trial is not included.
    """
    display_name = "Select Ghosts"
    option_none = 0
    option_n_tropy = 1
    option_n_oxide = 2
    default = 2

class select_difficulty(Choice):
    """
    Select what difficulty locations are included in the randomizer.
    Each difficulty adds three checks per race track.
    """
    display_name = "Select Difficulties to include"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_easy_medium = 3
    option_easy_hard = 4
    option_medium_hard = 5
    option_all = 6
    default = 2

class percentage_trophies(Range):
    """
    Select what percentage (1-100) of trophies are needed to achieve the goal.
    100 is all available trophies are required for the goal.
    """
    display_name = "What percentage of trophies to collect?"
    range_start = 1
    range_end = 100
    default = 100

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["percentage_trophies"] = percentage_trophies
    options["select_difficulty"] = select_difficulty
    options["include_turbo_track"] = include_turbo_track
    options["include_cups"] = include_cups
    options["include_time_trial"] = include_time_trial
    options["included_ghosts"] = included_ghosts
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    #print(options["easy_difficulty_enabled"])
    #input("Press enter...")
    return options