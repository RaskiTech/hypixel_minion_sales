import requests

api_key = "" # Put your api key here between the quatation marks
prices = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()["products"]

class Drop:
    def __init__(self, amount_per_action, sell_name, times_base_value):
        self.amount_per_action = amount_per_action
        self.sell_name = sell_name
        self.times_base_value = times_base_value


class Minion:
    def __init__(self, name, speed, drops):
        self.name = name
        self.speed = speed
        self.drops = drops


class Sale:
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name


def calculate_earnings(minion_id, action_time, money_per_action):
    without = 86400 / float(action_time) * float(money_per_action)
    print(f"With diamond spreading {minions[minion_id].name} minion will make {round(without + 138240 / float(action_time), 1)} "
          f"a day and without {round(without, 1)}")


def ask_prices(num):  # Calculates average price per action
    price = []
    for drop_ in minions[num].drops:
        #value_ = input(f"What is the sell price of {drop_.sell_name}? ")
        value_ = prices[drop_.sell_name]['buy_summary'][0]['pricePerUnit']
        price.append(float(value_) * (drop_.amount_per_action / drop_.times_base_value))

    calculate_earnings(num, minions[num].speed, sum(price))


min1 = Minion("Zombie", 22, (Drop(0.5, "ENCHANTED_ROTTEN_FLESH", 160),))
min2 = Minion("Revenant", 23, (Drop(2.5, "ENCHANTED_ROTTEN_FLESH", 160), Drop(0.1, "ENCHANTED_DIAMOND", 160)))
min3 = Minion("Skeleton", 22, (Drop(0.5, "ENCHANTED_BONE", 160),))
min4 = Minion("Creeper", 23, (Drop(0.5, "ENCHANTED_GUNPOWDER", 160),))
min5 = Minion("Spider", 22, (Drop(0.5, "ENCHANTED_STRING", 192), Drop(0.25, "ENCHANTED_SPIDER_EYE", 160)))
min6 = Minion("Tarantula", 23, (Drop(1.58, "ENCHANTED_STRING", 192), Drop(0.5, "ENCHANTED_SPIDER_EYE", 160), Drop(0.1, "ENCHANTED_IRON_INGOT", 160)))
min7 = Minion("Cave Spider", 22, (Drop(0.25, "ENCHANTED_STRING", 192), Drop(0.5, "ENCHANTED_SPIDER_EYE", 160)))
min8 = Minion("Blaze", 28.5, (Drop(0.5, "ENCHANTED_BLAZE_POWDER", 160),))
min9 = Minion("Magma cube", 28, (Drop(0.5, "ENCHANTED_MAGMA_CREAM", 160),))
min10 = Minion("Enderman", 28, (Drop(0.5, "ENCHANTED_ENDER_PEARL", 20),))
min11 = Minion("Ghast", 44, (Drop(0.5, "ENCHANTED_GHAST_TEAR", 160),))
min12 = Minion("Slime", 22, (Drop(0.5, "ENCHANTED_SLIME_BALL", 160),))
min13 = Minion("Cow", 22, (Drop(0.5, "ENCHANTED_LEATHER", 576), Drop(0.5, "ENCHANTED_RAW_BEEF", 160)))
min14 = Minion("Pig", 22, (Drop(0.5, "ENCHANTED_PORK", 160),))
min15 = Minion("Chicken", 22, (Drop(0.5, "ENCHANTED_RAW_CHICKEN", 160), Drop(0.5, "ENCHANTED_FEATHER", 160), Drop(0.5, "ENCHANTED_EGG", 144)))
min16 = Minion("Sheep", 20, (Drop(0.5, "ENCHANTED_MUTTON", 160), Drop(0.5, "ENCHANTED_WOOL", 160)))
min17 = Minion("Rabbit", 22, (Drop(0.5, "ENCHANTED_RABBIT", 160), Drop(0.175, "ENCHANTED_RABBIT_FOOT", 160), Drop(0.175, "ENCHANTED_RABBIT_HIDE", 576)))

min18 = Minion("Cobblestone", 14, (Drop(0.5, "ENCHANTED_COBBLESTONE", 160),))
min19 = Minion("Obsidian", 39, (Drop(0.5, "ENCHANTED_OBSIDIAN", 160),))
min20 = Minion("Glowstone", 21, (Drop(1.5, "ENCHANTED_GLOWSTONE_DUST", 160),))
min21 = Minion("Gravel", 22, (Drop(0.5, "ENCHANTED_FLINT", 160),))
min22 = Minion("Sand", 22, (Drop(0.5, "ENCHANTED_SAND", 160),))
min23 = Minion("Clay", 27.5, (Drop(2, "ENCHANTED_CLAY", 160),))
min24 = Minion("Ice", 10, (Drop(0.5, "ENCHANTED_ICE", 160),))
min25 = Minion("Snow", 11, (Drop(2, "ENCHANTED_SNOW_BLOCK", 640),))
min26 = Minion("Coal", 12, (Drop(0.5, "ENCHANTED_COAL", 160),))
min27 = Minion("Iron", 14, (Drop(0.5, "ENCHANTED_IRON", 160),))
min28 = Minion("Gold", 18, (Drop(0.5, "ENCHANTED_GOLD", 160),))
min29 = Minion("Diamond", 25, (Drop(0.5, "ENCHANTED_DIAMOND", 160),))
min30 = Minion("Lapis", 25, (Drop(3, "ENCHANTED_LAPIS", 160),))
min31 = Minion("Redstone", 25, (Drop(2.25, "ENCHANTED_REDSTONE_DUST", 160),))
min32 = Minion("Emerald", 24, (Drop(0.5, "ENCHANTED_EMERALD", 160),))
min33 = Minion("Quartz", 19, (Drop(0.5, "ENCHANTED_QUARTZ", 160),))
min34 = Minion("Endstone", 22, (Drop(0.5, "ENCHANTED_ENDSTONE", 160),))
min35 = Minion("Wheat", 11, (Drop(0.5, "ENCHANTED_HAY_BALE", 1296), Drop(0.5, "ENCHANTED_SEED", 160),))
min36 = Minion("Melon", 21, (Drop(2.25, "ENCHANTED_MELON", 160),))
min37 = Minion("Pumpkin", 27, (Drop(0.5, "ENCHANTED_PUMPKIN", 160),))
min38 = Minion("Carrot", 16, (Drop(1.5, "ENCHANTED_CARROT", 160),))
min39 = Minion("Potato", 16, (Drop(1.5, "ENCHANTED_POTATO", 160),))
min40 = Minion("mushroom", 26, (Drop(0.25, "ENCHANTED_BROWN_MUSHROOM", 160), Drop(0.25, "ENCHANTED_RED_MUSHROOM", 160)))
min41 = Minion("Cactus", 23, (Drop(1.5, "ENCHANTED_CACTUS_GREEN", 160),))
min42 = Minion("Cocoa beans", 23, (Drop(1.5, "ENCHANTED_COCOA_BEAN", 160),))
min43 = Minion("Sugar cane", 18, (Drop(1.5, "ENCHANTED_SUGAR", 160),))
min44 = Minion("Nether wart", 44, (Drop(1.5, "ENCHANTED_NETHER_WART", 160),))

min45 = Minion("Oak", 42, (Drop(0.5, "ENCHANTED_OAK_WOOD", 160),))
min46 = Minion("Spruce", 42, (Drop(0.5, "ENCHANTED_SPRUCE_WOOD", 160),))
min47 = Minion("Birch", 42, (Drop(0.5, "ENCHANTED_BIRCH_WOOD", 160),))
min48 = Minion("Dark oak", 42, (Drop(0.5, "ENCHANTED_DARK_OAK_WOOD", 160),))
min49 = Minion("Acacia", 42, (Drop(0.5, "ENCHANTED_ACACIA_WOOD", 160),))
min50 = Minion("Jungle", 42, (Drop(0.5, "ENCHANTED_JUNGLE_WOOD", 160),))

minions = (min1, min2, min3, min4, min5, min6, min7, min8, min9, min10, min11, min12, min13, min14, min15, min16,
           min17, min18, min19, min20, min21, min22, min23, min24, min25, min26, min27, min28, min29, min30,
           min31, min32, min33, min34, min35, min36, min37, min38, min39, min40, min41, min42, min43, min44, min45,
           min46, min47, min48, min49, min50)


full_test = input("Do you want to do a full comparison? (yes/no) ")
if full_test.lower() != "yes":
    min_type = input("Does the minion destroy blocks? (yes/no) ")
    if min_type.lower() == "no":
        print("\nWhat minion is it? (number)")
        print("1 Zombie")
        print("2 Revenant")
        print("3 Skeleton")
        print("4 Creeper")
        print("5 Spider")
        print("6 Tarantula")
        print("7 Cave_spider")
        print("8 Blaze")
        print("9 Magma_Cube")
        print("10 Enderman")
        print("11 Ghast")
        print("12 Slime")
        print("13 Cow")
        print("14 Pig")
        print("15 Chicken")
        print("16 Sheep")
        number = int(input("17 Rabbit\n"))
        ask_prices(number - 1)

    else:
        print("\nWhat minion is it? (number)")
        print("1 Cobblestone")
        print("2 Obsidian")
        print("3 Glowstone")
        print("4 Gravel")
        print("5 Sand")
        print("6 Clay")
        print("7 Ice")
        print("8 Snow")
        print("9 Coal")
        print("10 Iron")
        print("11 Gold")
        print("12 Diamond")
        print("13 Lapis")
        print("14 Redstone")
        print("15 Emerald")
        print("16 Quartz")
        print("17 Endstone")
        print("18 Wheat")
        print("19 Melon")
        print("20 Carrot")
        print("21 Pumpkin")
        print("22 Potato")
        print("23 Mushroom")
        print("24 Cactus")
        print("25 Cocoa beans")
        print("26 Sugar cane")
        print("27 Nether wart")
        print("28 Oak")
        print("29 Spruce")
        print("30 Birch")
        print("31 Dark oak")
        print("32 Acacia")
        number = int(input("33 Jungle\n"))
        ask_prices(number + 16)  # The non-break minions are first

# Do full sale comparison
else:
    # Ask the prices
    sales = []
    # Ask for diamond for diamond spreading
    diamond = prices["ENCHANTED_DIAMOND"]['buy_summary'][0]['pricePerUnit']

    for minion in minions:
        cost = []
        for drop in minion.drops:
            value = prices[drop.sell_name]['buy_summary'][0]['pricePerUnit']
            cost.append(float(value) * (drop.amount_per_action / drop.times_base_value))

        sales.append(Sale(86400 / float(minion.speed) * sum(cost) + 86400 / (float(minion.speed) * 10) * (diamond/160), minion.name)) # asked[0].amount/160 is diamond

    # Sort the list using insertion sort
    index_length = range(1, len(sales))
    for i in index_length:
        value_to_sort = sales[i].amount
        while sales[i - 1].amount < value_to_sort and i > 0:
            sales[i], sales[i - 1] = sales[i - 1], sales[i]
            i = i - 1

    # Print the list
    print("\nIncludes diamond spreading")
    for i in range(len(minions)):
        string = f"{sales[i].name} {round(sales[i].amount)}$ a day"
        print(string)

