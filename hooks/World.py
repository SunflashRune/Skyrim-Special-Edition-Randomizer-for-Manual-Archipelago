# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState
import logging
import random

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from .Options import FinalGoal



########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):

    pass


# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove = [] # List of location names
    locationNamesToExclude = []

    CompanionsEnable = get_option_value(multiworld, player, "CompanionsEnable")
    CollegeEnable = get_option_value(multiworld, player, "CollegeEnable")
    GuildEnable = get_option_value(multiworld, player, "GuildEnable")
    BrotherhoodEnable = get_option_value(multiworld, player, "BrotherhoodEnable")
    DawnguardEnable = get_option_value(multiworld, player, "DawnguardEnable")
    DragonbornEnable = get_option_value(multiworld, player, "DragonbornEnable")
    FishingEnable = get_option_value(multiworld, player, "FishingEnable")
    HuntingEnable = get_option_value(multiworld, player, "HuntingEnable")
    BountyEnable = get_option_value(multiworld, player, "BountyEnable")
    ExplorationEnable = get_option_value(multiworld, player, "ExplorationEnable")
    HousingEnable = get_option_value(multiworld, player, "HousingEnable")
    GoalSetting = get_option_value(multiworld, player, "FinalGoal")

    #Check and make sure you arn't trying to play a Goal that requires a Faction while also having ALL Factions disabled.
    if GoalSetting == FinalGoal.option_AlduinFaction and not CompanionsEnable and not CollegeEnable and not GuildEnable and not BrotherhoodEnable and not DawnguardEnable and not DragonbornEnable:
        raise Exception("You must have at least one Faction enabled to have the Goal of Alduin + Faction.")
    
    if GoalSetting == FinalGoal.option_FactionOnly and not CompanionsEnable and not CollegeEnable and not GuildEnable and not BrotherhoodEnable and not DawnguardEnable and not DragonbornEnable:
        raise Exception("You must have at least one Faction enabled to have the Goal of Faction Only.")
    
    if GoalSetting == FinalGoal.option_AllFactions and not CompanionsEnable and not CollegeEnable and not GuildEnable and not BrotherhoodEnable and not DawnguardEnable and not DragonbornEnable:
        raise Exception("You must have at least one Faction enabled to have the Goal of All Factions.")

    pass


    #If Dragonborn Acknowledged or Faction Only is your Goal, remove things locked by Main Quest Progressive 7+.
    #for location in location_table:
    #    if GoalSetting == FinalGoal.option_DragonAck and location.get("ack_enable"):
    #        logging.info(f"Removing {location['name']} from {player}'s world")
    #        locationNamesToRemove.append(location["name"])
    #    elif GoalSetting == FinalGoal.option_FactionOnly and location.get("ack_enable"):
    #        logging.info(f"Removing {location['name']} from {player}'s world")
    #        locationNamesToRemove.append(location["name"])

    #If All Factions is NOT your Goal, remove All Factions Complete location.
    for location in location_table:    
        if not GoalSetting == FinalGoal.option_AllFactions and location.get("AllFactEnable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])


    #Check for a Faction being disabled, and remove their Locations as needed.
    for location in location_table:
        if not CompanionsEnable and location.get("comp_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not CollegeEnable and location.get("coll_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not GuildEnable and location.get("guild_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not BrotherhoodEnable and location.get("brother_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not DawnguardEnable and location.get("dawn_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not DragonbornEnable and location.get("dragon_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not FishingEnable and location.get("fish_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world'")
            locationNamesToRemove.append(location["name"])
        elif not HuntingEnable and location.get("hunt_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not BountyEnable and location.get("bounty_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])
        elif not ExplorationEnable and location.get("explore_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location['name'])
        elif not HousingEnable and location.get("housing_enable"):
            logging.info(f"Removing {location['name']} from {player}'s world")
            locationNamesToRemove.append(location["name"])

    # Add your code here to calculate which locations to remove

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)
    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names

    CompanionsEnable = get_option_value(multiworld, player, "CompanionsEnable")
    CollegeEnable = get_option_value(multiworld, player, "CollegeEnable")
    GuildEnable = get_option_value(multiworld, player, "GuildEnable")
    BrotherhoodEnable = get_option_value(multiworld, player, "BrotherhoodEnable")
    DawnguardEnable = get_option_value(multiworld, player, "DawnguardEnable")
    DragonbornEnable = get_option_value(multiworld, player, "DragonbornEnable")
    GoalSetting = get_option_value(multiworld, player, "FinalGoal")


    #Check which Goal option is enabled, and set victory_name to the associated Location.
    if GoalSetting == FinalGoal.option_AlduinFaction or GoalSetting == FinalGoal.option_AlduinOnly:
        victory_name = "Alduin Slain (15)"
    elif GoalSetting == FinalGoal.option_DragonAck:
        victory_name = "Jurgen Horn Returned (7)"
    elif GoalSetting == FinalGoal.option_AllFactions:
        victory_name = "All Factions Complete"
    elif GoalSetting == FinalGoal.option_FactionOnly:
        #Create a list of Faction ending Locations, check for a Faction being enabled and remove from the list if its not, then randomly pick one.
        FactionList = ["Glory of the Dead Complete (6)", "Eye of Magnus Complete (8)", "Darkness Returns Complete (11)", "Hail Sithis Complete (13)", "Kindred Judgment Complete (11)", "Summit of Apocrypha Complete (7)"]
        if not CompanionsEnable:
            FactionList.remove("Glory of the Dead Complete (6)")
        if not CollegeEnable:
            FactionList.remove("Eye of Magnus Complete (8)")
        if not GuildEnable:
            FactionList.remove("Darkness Returns Complete (11)")
        if not BrotherhoodEnable:
            FactionList.remove("Hail Sithis Complete (13)")
        if not DawnguardEnable:
            FactionList.remove("Kindred Judgment Complete (11)")
        if not DragonbornEnable:
            FactionList.remove("Summit of Apocrypha Complete (7)")
        victory_name = random.choice(FactionList)

    #Find the Goal Complete item, then place it in the victory_name location from above.
    for item in item_pool:
        if item.name == "Goal Complete":
            victory_item = item
            break
    for location in multiworld.get_unfilled_locations(player):
        if location.name == victory_name:
            location.place_locked_item(victory_item)
    item_pool.remove(victory_item)

    #Check for if Dragonborn Acknowledged is your Goal, and remove excess Progressives in an attempt to ease generation.
    #if GoalSetting == FinalGoal.option_DragonAck or GoalSetting == FinalGoal.option_FactionOnly:
    #    itemNamesToRemove.extend(["MainQuestProgressive"]*8)
    #    itemNamesToRemove.extend(["ProgressiveWeaponTier"]*4)
    #    itemNamesToRemove.extend(["ProgressiveHeavyArmorTier"]*4)
    #    itemNamesToRemove.extend(["ProgressiveLightArmorTier"]*3)
    #    itemNamesToRemove.extend(["ProgressiveSpellTier"]*2)

    #Check if a Faction is enabled, and remove their Progressive Items and a Faction Complete if not.
    if not CompanionsEnable:
        itemNamesToRemove.extend(["CompanionProgressive"]*6)
        itemNamesToRemove.extend(["FactionComplete"]*1)

    if not CollegeEnable:
        itemNamesToRemove.extend(["CollegeProgressive"]*8)
        itemNamesToRemove.extend(["FactionComplete"]*1)

    if not GuildEnable:
        itemNamesToRemove.extend(["GuildProgressive"]*11)
        itemNamesToRemove.extend(["FactionComplete"]*1)

    if not BrotherhoodEnable:
        itemNamesToRemove.extend(["BrotherhoodProgressive"]*13)
        itemNamesToRemove.extend(["FactionComplete"]*1)

    if not DawnguardEnable:
        itemNamesToRemove.extend(["DawnguardProgressive"]*11)
        itemNamesToRemove.extend(["FactionComplete"]*1)

    if not DragonbornEnable:
        itemNamesToRemove.extend(["DragonbornProgressive"]*7)
        itemNamesToRemove.extend(["FactionComplete"]*1)


    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        logging.info(f"Removing {itemName} from {player}'s world'") #( Set this to itemName?)
        item_pool.remove(item)

    return item_pool

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

   # for itemName in itemNamesToRemove:
        #item = next(i for i in item_pool if i.name == itemName)
       # item_pool.remove(item)

   # return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location


    GoalSetting = get_option_value(multiworld, player, "FinalGoal")
    CompanionsEnable = get_option_value(multiworld, player, "CompanionsEnable")
    CollegeEnable = get_option_value(multiworld, player, "CollegeEnable")
    GuildEnable = get_option_value(multiworld, player, "GuildEnable")
    BrotherhoodEnable = get_option_value(multiworld, player, "BrotherhoodEnable")
    DawnguardEnable = get_option_value(multiworld, player, "DawnguardEnable")
    DragonbornEnable = get_option_value(multiworld, player, "DragonbornEnable")
    FactionAddSingle = lambda state: state.has("FactionComplete", player)
    FactionCompletestoAdd = int()


    #Check if a Faction is enabled, and add a 1 to FactionCompletestoAdd if so
    if CompanionsEnable:
        FactionCompletestoAdd += 1
    if CollegeEnable:
        FactionCompletestoAdd += 1
    if GuildEnable:
        FactionCompletestoAdd += 1
    if BrotherhoodEnable:
        FactionCompletestoAdd += 1
    if DawnguardEnable:
        FactionCompletestoAdd += 1
    if DragonbornEnable:
        FactionCompletestoAdd += 1

    logging.info(f"There are {FactionCompletestoAdd} Factions Enabled")
    #AllFactionsActive = sum(FactionCompletestoAdd)



    #FactionAddAll = lambda state: state.count_group("FactionsDone", player) and FactionCompletestoAdd(state)

    #If Alduin + Faction is your Goal, find Alduin Slain Location and add a requirement of a FactionComplete Item to that location.
    if GoalSetting == FinalGoal.option_AlduinFaction:
        location = world.get_location("Alduin Slain (15)")
        victory_name = "Alduin Slain (15)"
        for location in multiworld.get_filled_locations(player):
            if location.name == victory_name:
                location = world.get_location("Alduin Slain (15)")
                old_rule = location.access_rule
                location.access_rule = lambda state: old_rule(state) and FactionAddSingle(state)
    elif GoalSetting ==FinalGoal.option_AllFactions:
        location = world.get_location("All Factions Complete")
        victory_name = "All Factions Complete"
        for location in multiworld.get_filled_locations(player):
            if location.name == victory_name:
                location = world.get_location("All Factions Complete")
                old_rule = location.access_rule
                #location.access_rule = lambda state: state.count_group("FactionsDone", world.player) >= FactionCompletestoAdd #This works but it slow.
                location.access_rule = lambda state: state.has_group("FactionsDone", world.player, FactionCompletestoAdd)





    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True




    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> list:
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    GoalSetting = get_option_value(multiworld, player, "FinalGoal")

    slot_data["Goal_Set"] = GoalSetting
    logging.info(f"Goal_Set for player {player} is set to {GoalSetting}")
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass
