from typing import Optional
from BaseClasses import MultiWorld
from .. import Helpers


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(world: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Easy" or category_name == "Medium" or category_name == "Hard":
        selection = Helpers.get_option_value(world, player, "select_difficulty")
        if category_name == "Easy":
            if selection == 0 or selection == 3 or selection == 4 or selection == 6:
                return True
            elif selection == 1 or selection == 2 or selection == 5:
                return False
        if category_name == "Medium":
            if selection == 1 or selection == 3 or selection == 5 or selection == 6:
                return True
            elif selection == 0 or selection == 2 or selection == 4:
                return False
        if category_name == "Hard":
            if selection == 2 or selection == 4 or selection == 5 or selection == 6:
                return True
            elif selection == 0 or selection == 1 or selection == 3:
                return False
    if category_name == "TTrack":
        if Helpers.get_option_value(world, player, "include_turbo_track") == 1:
            return True
        else:
            return False
    if category_name == "Cups":
        if Helpers.get_option_value(world, player, "include_cups") == 1:
            return True
        else:
            return False
            
    return None
