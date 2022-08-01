from Player import *

player = Player("will")

commands = {
    "cmd": "lists all commands",
    "inv": player.get_inventory()
}

print(player.get_inventory())