# Skyrim Special Edition Randomizer for Manual Archipelago
 A Manual Archipelago Randomizer for Skyrim Special Edition

## What is Archipelago?

Archipelago (or AP for short) is a cross-game modification system that randomizes different games, then uses the result to build a single unified randomized experience.
The website can be found at https://archipelago.gg/ and their Discord is https://discord.gg/8Z65BR2

## What is a Manual AP Randomizer?

A Manual AP Randomizer is a specialized client designed to simply run beside an unmodified game you want to Randomize in spirit.

Unlike non-Manual randomizers, a Manual Randomizer does not modify the game you are randomizing at all; but instead has a seperate client that sits outside the game that you click various buttons in to declare to the AP server you've connected to that you have done a Location task.

The server in turn will tell your client what items you have receieved.

Manual AP has a Discord server here: https://discord.gg/jsJrxR5X2f

## What is Randomized for Skyrim Special Edition?

Your ability to use various Skills will be considered Locked until you have recieved their associated Item which Unlocks their use.
    `So for example, a new character will not be allowed to use Destruction Magic until they have Unlocked that Skill by completing a Location check and eventually recieving that Item.`

The player is not allowed to start Main Quests, Faction Quests(The Companions, College of Winterhold, Thieves' Guild, Dark Brotherhood, Dawnguard, or Dragonborn), or Daedric Quests until you have met certain Unlock requirements. See the [Location Logic Explanation](docs/en_SkyrimSpecialEdition_Location%20Logic%20Explanation.txt) file in the docs folder on GitHub, or unzip the .apworld to read it from the docs folder therin.

As a Manual Randomizer, everything functions on the honor system. As Skyrim is not actually modified in any way, there is nothing actually preventing you from accessing these Locations or using these Skills except your commitment to playing by the rules.

## So how do I set up the Manual AP Randomizer for Skyrim Special Edition?

We're going to assume you have followed the Archipelago setup guide located here https://archipelago.gg/tutorial/Archipelago/setup/en

If you have not, go do that first.
Welcome back! Now for our stuff.

Take the SkyrimSpecialEditionSunflashRune.apworld file you download from the [Releases page](https://github.com/SunflashRune/Skyrim-Special-Edition-Randomizer-for-Manual-Archipelago/releases/latest), and then copy that into your Archpipelago install's custom_worlds folder. Something like `.../Archipelago/custom_worlds/` is where you wanna drop it.

Next, you'll need a Manual_SkyrimSpecialEdition_SunflashRune.yaml file to tell your Archipelago install that you want a randomized game of Skyrim!

The simplest way to acquire one is by going to your `.../Archipelago/` install and finding `'ArchipelagoLauncher.exe'` and running that program.
On the left will be "Generate Template Options", which will fill your `.../Archipelago/Players/Templates/` folder with some default templates, one of which should be the afore-mentioned yaml file we need.
You'll want to open that in an editor of your choice (we use Notepad++), and find the "name: Player{number}" line. Replace that with whatever name you want, change any other options or settings you would like(like Goals or disabling certain Factions), then save it.
Move it or a copy of it up a folder level so it's in `.../Archipelago/Players/` along with any other Yamls of other games you have setup and want to randomize together.
The Archipelago site has setup guides for all the offical supported games here: https://archipelago.gg/tutorial/

### Since you're playing with a Manual AP game, you MUST Generate your randomized game locally(That is, on your own machine); before you can decide on how to host the game.

To do so, once your `.../Archipelago/Players/` folder has all the Yamls you want to randomize together, go find in ArchipelagoGenerate.exe (should be in `.../Archipelago/` )and run that program.
If everything goes as it should, you'll have a file (Named AP_stringofnumbershere.zip) delivered to your `.../Archipelago/Output/` folder.

The simplest next step, and the only one we'll describe here; is to take that zip file and upload it on the AP site and let it do the hosting for you.

https://archipelago.gg/uploads

This will eventually lead to you getting a room assigned, along with connection info (usually something like `archipelago.gg:PortNumbersHere`).

## FINALLY time to connect!

Go open ArchipelagoLauncher.exe again, and on the right-hand side (you may need to scroll) should be Manual Client.
At the top, the Server box should read the same as your server host. If you've followed these instructions, it'll be the info you have from the room assigned in the previous step; that archipelago.gg:PortNumberHere line. 

The Manual Game Id box will need to read `Manual_SkyrimSpecialEdition_SunflashRune`  EXACTLY, caps and everything.
You may then click Connect in the top right, and then the window should ask you to put your Player Name (from that Yaml you edited!), into the Command box at the bottom. Be sure to press Enter afterwards.
That should be it!


If you have issues with this process, a quick visit to the [Manual Discord](https://discord.gg/jsJrxR5X2f) and a search therein for 'Skyrim Special Edition' should get you to the forum post where I keep information up to date and try to help with what trouble-shooting I can. 
