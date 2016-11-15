

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

    def print_map(self, player, monster_table):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.win.addch(i, j, self.map[i][j])
        for i in range(len(monster_table.table)):
            if monster_table.table[i].hp > 0:
                self.win.addch(monster_table.table[i].posY, monster_table.table[i].posX, monster_table.table[i].skin)
        self.win.addch(player.posY, player.posX, player.skin)
        self.win.addnstr(16, 0, "                                        ", len("                                        "))
        self.win.addnstr(17, 0, "                                        ", len("                                        "))

        self.win.addnstr(17, 0, player.status, len(player.status))
        hp = "Hp: {}".format(player.hp)
        self.win.addnstr(18, 0, hp, len(hp))
        if player.target != None:
            self.win.addnstr(16, 0, player.target.status, len(player.target.status))
        self.win.refresh()
