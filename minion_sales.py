import requests

api_key = "f0aea64a-b1fa-48ec-94dc-7dcb672ffe97"
prices = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()["products"]

class Drop:
    def __init__(self, amount_per_action, sell_name, times_base_value):
        self.amount_per_action = amount_per_action
        self.sell_name = sell_name
        self.times_base_value = times_base_value


class Minion:
    def __init__(self, name, speeds, drops, upg1_index, upg2_index):
        self.name = name
        self.speeds = speeds # Speeds contains tier V to tier IX
        self.drops = drops
        self.upg1_index = upg1_index
        self.upg2_index = upg2_index


class Fuel:
    def __init__(self, name, recourse_multiplier, duration): # duration = Duration is in hours
        self.name = name
        self.recourse_multiplier = recourse_multiplier
        self.duration = duration


class PriceObject:
    def __init__(self, amount, name, pos_ID):
        self.amount = amount
        self.name = name
        self.pos_ID = pos_ID


def calculate_earnings(action_time, money_per_action):
    without = 86400 / float(action_time) * float(money_per_action)
    return (round(without, 1), round(without + 138240 / float(action_time), 1))


def ask_prices(num):  # Calculates average price per action
    price = []
    for drop_ in minions[num].drops:
        if type(drop_.sell_name) == str:
            value_ = prices[drop_.sell_name]['buy_summary'][0]['pricePerUnit'] # buy_summary is sell_offer/insta_buy. sell_summary is others
        else:
            value_ = float(drop_.sell_name)
        price.append(float(value_) * (drop_.amount_per_action / drop_.times_base_value))

    # Print the information
    print(f"\n{minions[num].name} minion\n")
    for i in range(4):
        print(f"Tier {roman_numbers[i * 2]}{roman_numbers[i * 2 + 1]}:")
        print(f"    {calculate_earnings(minions[num].speeds[i], sum(price))[0]} a day ")
        print(f"    With diamond spreading {calculate_earnings(minions[num].speeds[i], sum(price))[1]}")
        print("    Fuels: (Buying cost included if needed)")
        for j in range(5):
            money = round(calculate_earnings(minions[num].speeds[i], sum(price))[1] * fuels[j].recourse_multiplier) # How much money is made in a day
            money -= round(24 / fuels[j].duration * prices[fuels[j].name.replace(" ", "_").upper()]['sell_summary'][0]['pricePerUnit']) # Cost of a fuel of 24h
            if money > 0:
                money = "+" + str(money)
            print(f"        {fuels[j].name} {money}")


def tier_to_index(min_tier): # Input can be "V" or "5" and it returns 0. 
    if min_tier == "V" or min_tier == "VI":
        min_tier = 5
    elif min_tier == "VII" or min_tier == "VIII":
        min_tier = 7
    elif min_tier == "IX" or min_tier == "X":
        min_tier = 9
    elif min_tier == "XI":
        min_tier = 11
    return int((int(min_tier) - 5) / 2)


# Bazaar api name searces it and gives the price. If number is in that location, it is set to the price

min1 = Minion("Zombie", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_ROTTEN_FLESH", 160),), 1, 2)
min2 = Minion("Revenant", (23, 19, 14.5, 10), (Drop(2.5, "ENCHANTED_ROTTEN_FLESH", 160), Drop(0.1, "ENCHANTED_DIAMOND", 160)), 1, 2)
min3 = Minion("Skeleton", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_BONE", 160),), 1, 2)
min4 = Minion("Creeper", (23, 21, 18, 14), (Drop(0.5, "ENCHANTED_GUNPOWDER", 160),), 1, 2)
min5 = Minion("Spider", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_STRING", 192), Drop(0.25, "ENCHANTED_SPIDER_EYE", 160)), 1, 2)
min6 = Minion("Tarantula", (23, 19, 14.5, 10), (Drop(1.58, "ENCHANTED_STRING", 192), Drop(0.5, "ENCHANTED_SPIDER_EYE", 160), Drop(0.1, "ENCHANTED_IRON", 160)), 1, 2)
min7 = Minion("Cave Spider", (22, 20, 17, 13), (Drop(0.25, "ENCHANTED_STRING", 192), Drop(0.5, "ENCHANTED_SPIDER_EYE", 160)), 1, 2)
min8 = Minion("Blaze", (28.5, 25, 21, 16.5), (Drop(0.5, "ENCHANTED_BLAZE_POWDER", 160),), 1, 2)
min9 = Minion("Magma cube", (28, 25, 22, 18), (Drop(0.5, "ENCHANTED_MAGMA_CREAM", 160),), 1, 2)
min10 = Minion("Enderman", (28, 25, 22, 18), (Drop(0.5, "ENCHANTED_ENDER_PEARL", 20),), 1, 2)
min11 = Minion("Ghast", (44, 41, 38, 32), (Drop(0.5, "ENCHANTED_GHAST_TEAR", 160),), 1, 2)
min12 = Minion("Slime", (22, 19, 16, 12), (Drop(0.5, "ENCHANTED_SLIME_BALL", 160),), 1, 2)
min13 = Minion("Cow", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_LEATHER", 576), Drop(0.5, "ENCHANTED_RAW_BEEF", 160)), 1, 2)
min14 = Minion("Pig", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_PORK", 160),), 1, 2)
min15 = Minion("Chicken", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_RAW_CHICKEN", 160), Drop(0.5, "ENCHANTED_FEATHER", 160), Drop(0.5, "ENCHANTED_EGG", 144)), 1, 2)
min16 = Minion("Sheep", (20, 20, 17, 13), (Drop(0.5, "ENCHANTED_MUTTON", 160),), 1, 2)
min17 = Minion("Rabbit", (22, 20, 17, 13), (Drop(0.5, "ENCHANTED_RABBIT", 160), Drop(0.175, "ENCHANTED_RABBIT_FOOT", 160), Drop(0.175, "ENCHANTED_RABBIT_HIDE", 576)), 1, 2)

min18 = Minion("Cobblestone", (14, 9, 8, 7), (Drop(0.5, "ENCHANTED_COBBLESTONE", 160),), 1, 2)
min19 = Minion("Obsidian", (39, 35, 30, 24), (Drop(0.5, "ENCHANTED_OBSIDIAN", 160),), 1, 2)
min20 = Minion("Glowstone", (21, 19, 16, 13), (Drop(1.5, "ENCHANTED_GLOWSTONE_DUST", 160),), 1, 2)
min21 = Minion("Gravel", (22, 19, 16, 13), (Drop(0.5, "ENCHANTED_FLINT", 160),), 2, 4)
min22 = Minion("Sand", (22, 19, 16, 13), (Drop(0.5, "ENCHANTED_SAND", 160),), 1, 2)
min23 = Minion("Clay", (27.5, 24, 20, 16), (Drop(2, "ENCHANTED_CLAY_BALL", 160),), 1, 2)
min24 = Minion("Ice", (10, 9, 8, 7), (Drop(0.5, "ENCHANTED_ICE", 160),), 1, 2)
min25 = Minion("Snow", (11, 9.5, 8, 6.5), (Drop(2, 600, 640),), 1, 2)
min26 = Minion("Coal", (12, 10, 9, 7), (Drop(0.5, "ENCHANTED_COAL", 160),), 1, 2)
min27 = Minion("Iron", (14, 12, 10, 8), (Drop(0.5, "ENCHANTED_IRON", 160),), 1, 2)
min28 = Minion("Gold", (18, 16, 14, 11), (Drop(0.5, "ENCHANTED_GOLD", 160),), 1, 2)
min29 = Minion("Diamond", (25, 22, 19, 15), (Drop(0.5, "ENCHANTED_DIAMOND", 160),), 1, 2)
min30 = Minion("Lapis", (25, 23, 21, 18), (Drop(3, "ENCHANTED_LAPIS_LAZULI", 160),), 1, 2)
min31 = Minion("Redstone", (25, 23, 21, 18), (Drop(2.25, "ENCHANTED_REDSTONE", 160),), 1, 2)
min32 = Minion("Emerald", (24, 21, 18, 14), (Drop(0.5, "ENCHANTED_EMERALD", 160),), 1, 2)
min33 = Minion("Quartz", (19, 17, 14.5, 11.5), (Drop(0.5, "ENCHANTED_QUARTZ", 160),), 1, 2)
min34 = Minion("Endstone", (22, 19, 16, 13), (Drop(0.5, "ENCHANTED_ENDSTONE", 160),), 1, 2)
min35 = Minion("Wheat", (11, 10, 9, 8), (Drop(0.5, "ENCHANTED_HAY_BLOCK", 1296), Drop(0.5, "ENCHANTED_SEEDS", 160),), 2, 3)
min36 = Minion("Melon", (21, 18.5, 16, 13), (Drop(2.25, "ENCHANTED_MELON", 160),), 1, 2)
min37 = Minion("Pumpkin", (27, 24, 20, 16), (Drop(0.5, "ENCHANTED_PUMPKIN", 160),), 1, 2)
min38 = Minion("Carrot", (16, 14, 12, 10), (Drop(1.5, "ENCHANTED_CARROT", 160),), 1, 2)
min39 = Minion("Potato", (16, 14, 12, 10), (Drop(1.5, "ENCHANTED_POTATO", 160),), 1, 2)
min40 = Minion("Mushroom", (26, 23, 20, 16), (Drop(0.25, "ENCHANTED_BROWN_MUSHROOM", 160), Drop(0.25, "ENCHANTED_RED_MUSHROOM", 160)), 1, 2)
min41 = Minion("Cactus", (23, 21, 18, 15), (Drop(1.5, "ENCHANTED_CACTUS_GREEN", 160),), 0, 2)
min42 = Minion("Cocoa beans", (23, 21, 18, 15), (Drop(1.5, "ENCHANTED_COCOA", 160),), 1, 2)
min43 = Minion("Sugar cane", (18, 16, 14.5, 12), (Drop(1.5, "ENCHANTED_SUGAR", 160),), 1, 2)
min44 = Minion("Nether wart", (44, 41, 38, 32), (Drop(1.5, "ENCHANTED_NETHER_STALK", 160),), 1, 2)

min45 = Minion("Oak", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_OAK_LOG", 160),), 1, 2)
min46 = Minion("Spruce", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_SPRUCE_LOG", 160),), 1, 2)
min47 = Minion("Birch", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_BIRCH_LOG", 160),), 1, 2)
min48 = Minion("Dark oak", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_DARK_OAK_LOG", 160),), 1, 2)
min49 = Minion("Acacia", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_ACACIA_LOG", 160),), 1, 2)
min50 = Minion("Jungle", (42, 38, 33, 27), (Drop(0.5, "ENCHANTED_JUNGLE_LOG", 160),), 1, 2)

minions = (min1, min2, min3, min4, min5, min6, min7, min8, min9, min10, min11, min12, min13, min14, min15, min16,
           min17, min18, min19, min20, min21, min22, min23, min24, min25, min26, min27, min28, min29, min30,
           min31, min32, min33, min34, min35, min36, min37, min38, min39, min40, min41, min42, min43, min44, min45,
           min46, min47, min48, min49, min50)

fuels = (Fuel("Coal", 0.05, 0.5), Fuel("Enchanted lava bucket", 0.25, 99999999999), Fuel("Hamster wheel", 0.5, 24), Fuel("Foul flesh", 0.9, 5), Fuel("Catalyst", 2, 3))
roman_numbers = ("V", ", VI", "VII", ", VIII", "IX", ", X", "XI", "")
upgrades = ("Auto-smelter", "Dia spr", "Sup comp", "Compactor", "Flint shovel")

full_test = input("Do you want to do a full money making comparison? (yes/no) ")
if full_test.lower() != "yes":
    min_type = input("Ok, Does the minion destroy blocks? (yes/no) ")
    if min_type.lower() == "no":
        print("\nWhat minion is it? (number)")
        for i in range(16):
            print(f"{i + 1} {minions[i].name}")
        number = int(input("17 Rabbit\n"))
        ask_prices(number - 1)
    else:
        print("\nWhat minion is it? (number)")
        for i in range(17, 49):
            print(f"{i - 16} {minions[i].name}")
        number = int(input("33 Jungle\n"))
        ask_prices(number + 16)  # The non-break minions are first

# Do full money making comparison
else:
    tier = input("What tier? (V - XI) ")

    tier = tier_to_index(tier)
    # Ask the prices
    sales = []
    # Ask for diamond for diamond spreading
    diamond = prices["ENCHANTED_DIAMOND"]['buy_summary'][0]['pricePerUnit'] / 160

    for i in range(len(minions)):
        cost = []
        for drop in minions[i].drops:
            if type(drop.sell_name) == str:
                value = prices[drop.sell_name]['buy_summary'][0]['pricePerUnit']
            else:
                value = drop.sell_name
            cost.append(float(value) * (drop.amount_per_action / drop.times_base_value))

        earnings = 86400 / float(minions[i].speeds[tier]) * sum(cost)
        if upgrades[minions[i].upg1_index] == "Dia spr" or upgrades[minions[i].upg2_index] == "Dia spr":
            earnings += 86400 / (float(minions[i].speeds[tier]) * 10) * diamond
        sales.append(PriceObject(earnings, minions[i].name, i))
    # Sort the list using insertion sort
    index_length = range(1, len(sales))
    for i in index_length:
        value_to_sort = sales[i].amount
        while sales[i - 1].amount < value_to_sort and i > 0:
            sales[i], sales[i - 1] = sales[i - 1], sales[i]
            i = i - 1

    # Print the list
    for i in range(len(minions)):
        string = f"{i + 1}# {sales[i].name} minion - {round(sales[i].amount)}$ a day - {upgrades[minions[sales[i].pos_ID].upg1_index]}, {upgrades[minions[sales[i].pos_ID].upg2_index]}"
        print(string)
