# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


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
"""
Skyrim Special Edition Manual AP Randomizer, Version 0.8
"""

class FinalGoal(Choice):
    """
    What do you want to be your final Goal?
    Kill Alduin Plus Faction(default): You must complete 1 of your enabled Faction Questlines(Companions/College/Guild/Brotherhood/Dawnguard/Dragonborn) and then kill Alduin in the Main Quest.
    Kill Alduin Only: You must kill Aludin. Removes Faction Complete requirements, but does NOT REMOVE any Enabled Factions from the Location Pool! You may still have to do an amount of your Enabled Factions to get your required items.
    Dragonborn Acknowledged: You must return the Horn of Jurgen Windcaller and be acknowledged as Dragonborn by the Greybeards. This disables all Locations past those associated with Main Quest Progressives 6(Blade in the Dark), and also removes about half of the progressive armor/offensive item upgrades to ease generation.
    Faction Only: You must complete one of your available Faction Questlines. This disables all Locations past those associated with Main Quest Progressives 6(Blade in the Dark), and also removes about half of the progressive armor/offensive item upgrades to ease generation.
                    **It is STRONGLY suggested you put "Goal Complete" in your start_hints: section (near the bottom of this YAML) if playing this mode, for now.**
    All Factions: You must complete all of your enabled Faction Questlines.
    """
    display_name = "Final Goal"
    option_AlduinFaction = 0
    option_AlduinOnly = 1
    option_DragonAck = 2
    option_FactionOnly = 3
    option_AllFactions = 4
    default = 0

class CompanionsToggle(Toggle):
    """
    Include The Companions quests in the Location Pool.
    If enabled, the first quest(Take Up Arms) will require 1 ProgressiveCompanions Item AND either the One-Handed or Two-Handed Items acquired to be in logic. 
    Each following quest will require an additional ProgressiveCompanions Item.
    """
    display_name = "Companions Toggle"
    default = True

class CollegeToggle(Toggle):
    """
    Include The College of Winterhold quests in the Location Pool.
    If enabled, the first quest(First Lessons) will require 1 CollegeProgressive Item AND one of Destruction/Conjuration/Illusion/Alteration, AND Restoration, AND 1 Progressive Spell Tier Items acquired to be in logic.
    Each following quest will require an additional ProgressiveCollege Item.
    """
    display_name = "College Toggle"
    default = True

class GuildToggle(Toggle):
    """
    Include The Thieves' Guild quests in the Location Pool.
    If enabled, the first quest(A Chance Arrangement) will require 1 GuildProgressive Item AND Sneak AND Pickpocket AND Lockpicking Items acquired to be in logic.
    Each following quest will require an additional GuildProgressive Item.
    """
    display_name = "Guild Toggle"
    default = True

class BrotherhoodToggle(Toggle):
    """
    Include the Dark Brotherhood quests in the Location Pool.
    If enabled, the first quest(Innocence Lost) will require 1 BrotherhoodProgressive Item AND Sneak AND Lockpicking acquired to be in logic.
    Each following quest will require an additional BrotherhooldProgressive Item.
    """
    display_name = "Brotherhood Toggle"
    default = True

class DawnguardToggle(Toggle):
    """
    Include the Dawnguard quests in the Location Pool.
    If enabled, the first quest(Dawnguard) will require 1 DawnguardProgressive Item AND 4 MainQuestProgressive Items acquired to be in logic.
    Each following quest will require an additional DawnguardProgressive Item.
    """
    display_name = "Dawnguard Toggle"
    default = True

class DragonbornToggle(Toggle):
    """
    Include the Dragonborn quests in the Location Pool.
    If enabled, the first quest(Dragonborn) will require 1 DragonbornProgressive Item AND 4 MainQuestProgressive Items acquired to be in logic.
    Each following quest will require an additional DragonbornProgressive Item.
    """
    display_name = "Dragonborn Toggle"
    default = True

class FishingToggle(Toggle):
    """
    Include the Fishing quests in the Location Pool.
    If enabled, Five(5) additional Fishing quests will be added to the Location Pool from Riften Fishery(from both Swims-In-Deep-Water and Viriya).
    Please check the Location Logic Explanation file, or the Mindmap file for more information.
    """
    display_name = "Fishing Quests Toggle"
    default = True

class HuntingToggle(Toggle):
    """
    Include the custom Hunting Objectives in the Location Pool.
    If enabled, Three(3) additional Hunting Objectives will be added to the Location Pool.
    Please check the Location Logic Explanation file, or the Mindmap file for more information.
    """
    display_name = "Hunting Objectives Toggle"
    default = True

class BountyToggle(Toggle):
    """
    Include more Bounty Objectives in the Location Pool.
    If enabled, Five(5) additional Bounty Objectives will be aded to the Location Pool.
    Please check the Location Logic Explanation file, or the Mindmap file for more information.
    """
    display_name = "Bounty Objectives Toggle"
    default = True

class ExplorationToggle(Toggle):
    """
    Include more Exploration Objectives in the Location Pool.
    If enabled, Eight(8) additional Exploration Objectives will be added to the Location Pool.
    Please check the Location Logic Explanation file, or the Mindmap file for more information.
    """
    display_name = "Exploration Objectives Toggle"
    default = True

class HousingToggle(Toggle):
    """
    Include more Housing Objectives in the Location Pool.
    If enabled, Six(6) additional Housing Objectives will be added to the Location Pool.
    Please check the Location Logic Explanation file, or the Mindmap file for more information.
    """
    display_name = "Housing Objectives Toggle"
    default = True

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:

    options["FinalGoal"] = FinalGoal
    options["CompanionsEnable"] = CompanionsToggle
    options["CollegeEnable"] = CollegeToggle
    options["GuildEnable"] = GuildToggle
    options["BrotherhoodEnable"] = BrotherhoodToggle
    options["DawnguardEnable"] = DawnguardToggle
    options["DragonbornEnable"] = DragonbornToggle
    options["FishingEnable"] = FishingToggle
    options["HuntingEnable"] = HuntingToggle
    options["BountyEnable"] = BountyToggle
    options["ExplorationEnable"] = ExplorationToggle
    options["HousingEnable"] = HousingToggle

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
