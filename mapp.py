

class   Map_generator():

    def __init__(self, win):
        self.map = []
        self.map.append(" #########                                                  ")
        self.map.append(" #.......#          #####           #########               ")
        self.map.append(" #.......#          #...+++++       #.......#               ")
        self.map.append(" #.......#       ++++...#   +       #.......#               ")
        self.map.append(" ###+#####       +  #####   +       #.......#               ")
        self.map.append("    +            +          +++++++++.......#               ")
        self.map.append("    +            +                  #.......#               ")
        self.map.append("    +    ########+#######           #.......#               ")
        self.map.append("    +    #..............#           ####+####               ")
        self.map.append("    +    #..............#               +++                 ")
        self.map.append("    ++++++..............#             ####+###########      ")
        self.map.append("         ##########+#####             #..............#      ")
        self.map.append("                   +      +++++++++++++..............#      ")
        self.map.append("                   +      +           ################      ")
        self.map.append("                   ++++++++                                 ")
        self.win = win
        self.spawnX = 3
        self.spawnY = 3

    def print_map(self, player, monster_table, turn):
        self.win.clear()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.win.addch(i, j, self.map[i][j])
        for i in range(len(monster_table.table)):
            if monster_table.table[i].hp > 0:
                self.win.addch(monster_table.table[i].posY, monster_table.table[i].posX, monster_table.table[i].skin)
        self.win.addch(player.posY, player.posX, player.skin)

        self.win.addnstr(17, 0, player.status, len(player.status))

        t = "You are at turn {}".format(turn)
        hp = "Hp: {}".format(player.hp)
        strength = "str: {}".format(player.strength)
        resist = "arm: {}".format(player.armor)
        gold = "gold: {}".format(player.gold)
        level = "lvl: {}".format(player.level)

        self.win.addnstr(1, 61, t, len(t))
        self.win.addnstr(2, 61, "Your stats:", len("Your stats:"))
        self.win.addnstr(4, 65, level, len(level))
        self.win.addnstr(5, 65, hp, len(hp))
        self.win.addnstr(6, 65, strength, len(strength))
        self.win.addnstr(7, 65, resist, len(resist))
        self.win.addnstr(9, 65, gold, len(gold))

        if player.target != None:
            self.win.addnstr(16, 0, player.target.status, len(player.target.status))
        self.win.refresh()
