
class Player(object):
    def __init__(self, name):
        self.name = name
        self.culture_points = 0
        self.language_points = 0
        self.nature_points = 0
        self.history_points = 0
        self.money = 10000
        self.visited = set()

    def language(self, points):
        self.language_points += points

    def culture(self, points):
        self.culture_points += points

    def nature(self, points):
        self.nature_points += points

    def history(self, points):
        self.history_points += points

    def visit(self, new_location):
        self.visited.add(new_location)

    def spend(self, cost):
        self.money -= cost

# Parent Class
class Destination(object):
    def arrive(self):
        pass

    # Interface with user to select next sight and run that visit. Return to this method after visit.
    def select(self):
        choice = ""
        while choice != "Next":
            print "Where would you like to go?"
            for name in self.choices:
                print name
            print "Type 'Next' to go to another destination"

            choice = raw_input("> ")
            if choice in self.player.visited:
                print "You've already visited %s. Pick again or type 'Next' to choose another trip." % (choice)
            elif choice not in self.player.visited and choice != "Next":
                if choice in self.sights:
                    self.visit(choice)
                else:
                    print "Sorry, that name is not on the list"



    # Visit makes changes to points and money and shows a sight description
    def visit(self, sight):
        points = self.get_points(sight)
        print points['desc']
        self.player.language(points['language'])
        self.player.history(points['history'])
        self.player.culture(points['culture'])
        self.player.nature(points['nature'])
        self.player.spend(points['cost'])
        self.player.visit(sight)
        self.select()


class London(Destination):

    sights = {"Lake District": {'language': 0, 'history': 30, 'culture': 0, 'nature': 30, 'cost': 700,
                                'desc': "Lake District National park has many fells, including Scafell Pike (3,210 ft), the highest mountain in England, lovely little towns and villages such as Grasmere, as well as boat excursions across Lake Windermere and Ullswater."},
              "Windsor Castle": {'language': 0, 'history': 50, 'culture': 20, 'nature': 0, 'cost': 500,
                        'desc': "Windsor Castle has served as the summer residence of British Royals since William the Conqueror built the first fortress here in 1078."},
              "Eden Project": {'language': 0, 'history': 10, 'culture': 0, 'nature': 50, 'cost': 700,
                             'desc': "The incredible Eden Project is a collection of unique artificial biomes containing an amazing collection of plants from around the world."}}
    country = "England"
    choices = ["Windsor Castle", "Lake District", "Eden Project"]


    def __init__(self, player):
        self.player = player
        self.new = True
        self.arrive()

    def arrive(self):
        while self.new is True:
            print "Welcome to %s!" % (self.country)
            self.player.spend(1000)
            self.new = False
            self.select()

    def get_points(self, sight):
        return self.sights[sight]


class Mexico(Destination):

    sights = {'teotihuacan': {'language': 20, 'history': 50, 'culture': 50, 'nature': 5, 'cost': 400,
                              'desc': "On the edge of the high-lying valley of Anahuac and dating from around AD 600, this once influential political, religious, and cultural center - now a UNESCO World Heritage Site - was reduced to ruins long before the arrival of the Spanish."},
              'anthro_museum': {'language': 20, 'history': 50, 'culture': 50, 'nature': 0, 'cost': 100,
                                'desc': "One of the most important of its kind in the world, the National Museum of Anthropology holds one of the most impressive collections of Mesoamerican artifacts in the world."},
              'xochi': {'language': 20, 'history': 25, 'culture': 25, 'nature': 200, 'cost': 100,
                        'desc': "Xochimilco is the last remnant of the vast system of causeways, canals, manmade islands and floating gardens created out of the vast lake system that once covered today's Valley of Mexico"}}

    country = "Mexico"
    choices = ["Teotihuacan", "Museum of Anthropology", "Xochimilco"]


    def __init__(self, player):
        self.player = player
        self.new = True

    def arrive(self):
        while self.new is True:
            print "Welcome to %s!" % (country)
            self.player.spend(1000)
            self.new = False
            self.select()

    def get_points(self, sight):
        return sights[sight]



    # * Lima, Peru
    #     - visit_MP
    #     - visit_Huacachina
    #     - see_amazon
    # * Juno, Alaska
    #     - see_polar_bear
    #     - see_orca
    #     - see_glacier
    #     - visit_Klondike
    # * Nairobi, Kenya
    #     - see_leopard
    #     - visit_Lamu
    #     - visit_Mombasa
    # * Jerusalem, Israel
    #     - visit_wailingwall
    #     - visit_Holy_Sepulchre
    #     - visit_Muslim_quarter
    # * Mumbai, India
    #     - visit_Sanjay_Gandhi_np
    #     - visit_Taj-Mahal
    #     - visit_Tibet-House
    # * Bangkok, Thailand
    #     - visit_Great_Palace
    #     - visit_Ko_Pangan
    #     - visit_Sukhothai
    # * Tokyo, Japan
    #     - visit_Asakusa
    #     - visit_Ueno
    #     - visit_Imperial_Palace
    #     - visit_mt_fuji
    # * Broke
    #     - visit

class Engine(object):

    def __init__(self, a_map, player):
        self.map = a_map
        self.player = player

    def play(self):
        print "You have $100,000 and time to travel!"
        print "Every place you can go offers something new: history, language, culture, natural beauty."
        print "Pick your trip and find out what your journey brings! You'll get points for every place you visit."
        self.pick_next()

    def pick_next(self):
        while self.player.money > 1000:
            print "Where would you like to go? London or Mexico City?"
            next_location = raw_input("> ")
            if next_location == "London":
                val = self.map.locations.get("london")
                self.pick_next()
            elif next_location == "Mexico":
                val = self.map.locations.get("mexico")
                self.pick_next()
        else:
            print "You don't have enough money to get to another destination."
            print "Your final score is:"
            print "Language: %s, \n History: %s \n Culture: %s, Nature: %s" % (player.language, player.history, player.culture, player.nature)


class Map(object):

    def __init__(self, player):
        self.player = player
        self.locations = {'london': London(player),
                 'mexico': Mexico(player)
                 # 'peru': Lima(player),
                 # 'alaska': Juno(player),
                 # 'kenya': Nairobi(player),
                 # 'israel': Jerusalem(player),
                 # 'india': Mumbai(player),
                 # 'thailand': Bangkok(player),
                 # 'japan': Tokyo(player),
                 # 'broke': Broke(player)
                 }

    def travel(self, next_location):
        self.next = next_location

name = raw_input("What's your name? ")
a_player = Player(name)
a_map = Map(a_player)
a_game = Engine(a_map, a_player)
a_game.play()
