import random
import numpy
import json

#toggle variables
greatsword = True
longsword = True
sns = True
db = True
hammer = True
hh = True
lance = True
glance = True
sa = True
cb = True
ig = True
lb = True
hb = True
bow = True

#global armors
global_weapon = ""
global_head = ""
global_chest = ""
global_arms = ""
global_waist = ""
global_legs = ""
global_charm = ""
global_weapon_type = ""

def set_greatsword():
    global greatsword
    if greatsword == True:
        greatsword = False
    elif greatsword == False:
        greatsword = True

def get_greatsword():
    return greatsword

def set_longsword():
    global longsword
    if longsword == True:
        longsword = False
    elif longsword == False:
        longsword = True

def get_longsword():
    return longsword

def set_sns():
    global sns
    if sns == True:
        sns = False
    elif sns == False:
        sns = True

def get_sns():
    return sns

def set_db():
    global db
    if db == True:
        db = False
    elif db == False:
        db = True

def get_db():
    return db

def set_hammer():
    global hammer
    if hammer == True:
        hammer = False
    elif hammer == False:
        hammer = True

def get_hammer():
    return hammer

def set_hh():
    global hh
    if hh == True:
        hh = False
    elif hh == False:
        hh = True

def get_hh():
    return hh

def set_lance():
    global lance
    if lance == True:
        lance = False
    elif lance == False:
        lance = True

def get_lance():
    return lance

def set_glance():
    global glance
    if glance == True:
        glance = False
    elif glance == False:
        glance = True

def get_glance():
    return glance

def set_sa():
    global sa
    if sa == True:
        sa = False
    elif sa == False:
        sa = True

def get_sa():
    return sa

def set_cb():
    global cb
    if cb == True:
        cb = False
    elif cb == False:
        cb = True

def get_cb():
    return cb

def set_ig():
    global ig
    if ig == True:
        ig = False
    elif ig == False:
        ig = True

def get_ig():
    return ig

def set_lb():
    global lb
    if lb == True:
        lb = False
    elif lb == False:
        lb = True

def get_lb():
    return lb

def set_hb():
    global hb
    if hb == True:
        hb = False
    elif hb == False:
        hb = True

def get_hb():
    return hb

def set_bow():
    global bow
    if bow == True:
        bow = False
    elif bow == False:
        bow = True

def get_bow():
    return bow

#############################################################################################################################

def get_random_skills():
    with open("Monster_Hunter_World_ERP\Json\SkillList.json", "r") as file:
            data = json.load(file)
        
    skillslist = []

    for every in data:
        skillslist.append(every)

    x = random.choice(skillslist)

    return x

def get_random_weapontype():

    #getting globals

    global greatsword
    global longsword
    global sns 
    global db 
    global hammer 
    global hh 
    global lance 
    global glance 
    global sa 
    global cb 
    global ig 
    global lb 
    global hb 
    global bow 

    choiceWeapons = ["Great Sword", "Long Sword", "S&S", "Hammer", "Lance", "Gunlance", "Switch Axe", "Charge Blade", "Insect Glaive", "Dual Blades", "Hunting Horn", "Bow", "Light Bowgun", "Heavy Bowgun"]

    if greatsword == True and longsword == True and sns == True and db == True and hammer == True and hh == True and lance == True and glance == True and sa == True and cb == True and ig == True and lb == True and hb == True and bow == True:
        x = random.choice(choiceWeapons)
        return x

    if greatsword == True:
        choiceWeapons.remove("Great Sword")
    if longsword == True:
        choiceWeapons.remove("Long Sword")
    if sns == True:
        choiceWeapons.remove("S&S")
    if db == True:
        choiceWeapons.remove("Dual Blades")
    if hammer == True:
        choiceWeapons.remove("Hammer")
    if hh == True:
        choiceWeapons.remove("Hunting Horn")
    if lance == True:
        choiceWeapons.remove("Lance")
    if glance == True:
        choiceWeapons.remove("Gunlance")
    if sa == True:
        choiceWeapons.remove("Switch Axe")
    if cb == True:
        choiceWeapons.remove("Charge Blade")
    if ig == True:
        choiceWeapons.remove("Insect Glaive")
    if bow == True:
        choiceWeapons.remove("Bow")
    if lb == True:
        choiceWeapons.remove("Light Bowgun")
    if hb == True:
        choiceWeapons.remove("Heavy Bowgun")
    
    x = random.choice(choiceWeapons)
    return x

def get_random_weapon(weaponType):

    with open("Monster_Hunter_World_ERP\Json\WeaponsList.json", "r") as file:
        data = json.load(file)
        
    weapon_choices = []

    if weaponType == "Great Sword":
        for every in data:
            if every["weapon_type"] == "Great Sword":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Long Sword":
        for every in data:
            if every["weapon_type"] == "Long Sword":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "S&S":
        for every in data:
            if every["weapon_type"] == "S&S":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Hammer":
        for every in data:
            if every["weapon_type"] == "Hammer":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Lance":
        for every in data:
            if every["weapon_type"] == "Lance":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Gunlance":
        for every in data:
            if every["weapon_type"] == "Gunlance":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Switch Axe":
        for every in data:
            if every["weapon_type"] == "Switch Axe":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Charge Blade":
        for every in data:
            if every["weapon_type"] == "Charge Blade":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Insect Glaive":
        for every in data:
            if every["weapon_type"] == "Insect Glaive":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Dual Blades":
        for every in data:
            if every["weapon_type"] == "Dual Blades":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Hunting Horn":
        for every in data:
            if every["weapon_type"] == "Hunting Horn":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Bow":
        for every in data:
            if every["weapon_type"] == "Bow":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Light Bowgun":
        for every in data:
            if every["weapon_type"] == "Light Bowgun":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    elif weaponType == "Heavy Bowgun":
        for every in data:
            if every["weapon_type"] == "Heavy Bowgun":
                weapon_choices.append(every)
        weapon = random.choice(weapon_choices)
    return weapon

def get_random_setbonus(percent):
    rand = random.random()
    if rand <= percent:
        with open("Monster_Hunter_World_ERP\Json\SetBonusList.json", "r") as file:
            data = json.load(file)
        
        x = []

        for every in data:
            x.append(every)

        x = random.choice(x)
    else:
        x = []
    return x

def get_set_bonus_armor(set_bonus):

    set_bonus_armor_choices = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["set_bonus"] == set_bonus["name"]:
            set_bonus_armor_choices.append(every)

    return set_bonus_armor_choices

def get_charm_list():

    charm_list = []

    with open("Monster_Hunter_World_ERP\Json\CharmsList.json", "r") as file:
        data = json.load(file)

    for every in data:
        charm_list.append(every)

    return charm_list

def get_random_head(skill):

    grouping = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["head"]["skill_name_1"] == skill["skill_name"]:
            grouping.append(every["head"])
        if every["head"]["skill_name_2"] == skill["skill_name"]:
            grouping.append(every["head"])

    if grouping == []:
        return "bad array"
    
    armor = random.choice(grouping)
    return armor

def get_random_chest(skill):

    grouping = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["chest"]["skill_name_1"] == skill["skill_name"]:
            grouping.append(every["chest"])
        if every["chest"]["skill_name_2"] == skill["skill_name"]:
            grouping.append(every["chest"])

    if grouping == []:
        return "bad array"
    
    armor = random.choice(grouping)
    return armor

def get_random_arms(skill):

    grouping = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["arms"]["skill_name_1"] == skill["skill_name"]:
            grouping.append(every["arms"])
        if every["arms"]["skill_name_2"] == skill["skill_name"]:
            grouping.append(every["arms"])

    if grouping == []:
        return "bad array"
    
    armor = random.choice(grouping)
    return armor

def get_random_waist(skill):

    grouping = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["waist"]["skill_name_1"] == skill["skill_name"]:
            grouping.append(every["waist"])
        if every["waist"]["skill_name_2"] == skill["skill_name"]:
            grouping.append(every["waist"])

    if grouping == []:
        return "bad array"
    
    armor = random.choice(grouping)
    return armor

def get_random_legs(skill):

    grouping = []

    with open("Monster_Hunter_World_ERP\Json\ArmorList.json", "r") as file:
        data = json.load(file)

    for every in data:
        if every["legs"]["skill_name_1"] == skill["skill_name"]:
            grouping.append(every["legs"])
        if every["legs"]["skill_name_2"] == skill["skill_name"]:
            grouping.append(every["legs"])

    if grouping == []:
        return "bad array"
    
    armor = random.choice(grouping)
    return armor

def get_useless_skills(weapon):

    if weapon == "Great Sword":
        x = ["Artillery", "Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost"]
        return x
    if weapon == "Long Sword":
        x = ["Artillery", "Horn Maestro", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
        return x
    if weapon == "S&S":
        x = ["Artillery", "Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots" "Bow Charge Plus", "Capacity Boost"]
        return x
    if weapon == "Hammer":
        x = ["Artillery", "Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots" "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
        return x
    if weapon == "Lance":
        x = ["Artillery", "Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots" "Bow Charge Plus", "Capacity Boost", "Focus"]
        return x
    if weapon == "Gunlance":
        x = ["Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus"]
        return x
    if weapon == "Switch Axe":
        x = ["Artillery", "Horn Maestro", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
        return x
    if weapon == "Charge Blade":
        x = ["Horn Maestro", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus"]
        return x
    if weapon == "Insect Glaive":
        x = ["Artillery", "Horn Maestro", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
        return x
    if weapon == "Dual Blades":
        x = ["Artillery", "Horn Maestro", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
        return x
    if weapon == "Hunting Horn":
        x = ["Artillery", "Power Prolonger", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots", "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Focus", "Guard Up"]
        return x
    if weapon == "Bow":
        x = ["Artillery", "Power Prolonger", "Capacity Boost", "Guard", "Offensive Guard", "Focus", "Horn Maestro", "Guard Up", "Handicraft"]
        return x
    if weapon == "Light Bowgun":
        x = ["Power Prolonger", "Capacity Boost", "Guard", "Offensive Guard", "Horn Maestro", "Bow Charge Plus", "Guard Up", "Handicraft"]
        return x
    if weapon == "Heavy Bowgun":
        x = ["Power Prolonger", "Capacity Boost", "Horn Maestro", "Bow Charge Plus", "Handicraft"]
        return x
    
def get_useless_elements(weapon, weaponType):

    x = ["Fire Attack", "Ice Attack", "Dragon Attack", "Thunder Attack", "Water Attack", "Blast Attack", "Sleep Attack", "Poison Attack", "Paralysis Attack", "Free Elem/Ammo Up", "Elderseal Boost", "Blast Functionality", "Paralysis Functionality", "Poison Functionality", "Sleep Functionality"]

    #BowGun
    if weaponType == "Light Bowgun" or weaponType == "Heavy Bowgun":
        x.remove("Free Elem/Ammo Up")
        for every in weapon["ammo_types"]:
            if every == "Fire":
                x.remove("Fire Attack")
            if every == "Water":
                x.remove("Water Attack")
            if every == "Thunder":
                x.remove("Thunder Attack")
            if every == "Ice":
                x.remove("Ice Attack")
            if every == "Dragon":
                x.remove("Dragon Attack")
            if every == "Poison":
                x.remove("Poison Attack")
            if every == "Sleep":
                x.remove("Sleep Attack")
            if every == "Paralysis":
                x.remove("Paralysis Attack")

    else:

        #Fire
        if "Fire" in weapon["element_name"]:
            x.remove("Fire Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Water
        if "Water" in weapon["element_name"]:
            x.remove("Water Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Thunder
        if "Thunder" in weapon["element_name"]:
            x.remove("Thunder Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Ice
        if "Ice" in weapon["element_name"]:
            x.remove("Ice Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Dragon
        if "Dragon" in weapon["element_name"]:
            x.remove("Dragon Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
            if weapon["elderseal_boost_level"] == 1 or weapon["elderseal_boost_level"] == 2:
                x.remove("Elderseal Boost")
        #Poison
        if "Poison" in weapon["element_name"]:
            x.remove("Poison Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Sleep
        if "Sleep" in weapon["element_name"]:
            x.remove("Sleep Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Para
        if "Paralysis" in weapon["element_name"]:
            x.remove("Paralysis Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")
        #Blast
        if "Blast" in weapon["element_name"]:
            x.remove("Blast Attack")
            if "Hidden" in weapon["hidden_element"]:
                x.remove("Free Elem/Ammo Up")

        #Double ELement Check
        if weaponType == "Dual Blades" or weaponType == "Hunting Horn":
            if "Fire" in weapon["dual_element"]:
                x.remove("Fire Attack")

            if "Water" in weapon["dual_element"]:
                x.remove("Water Attack")

            if "Thunder" in weapon["dual_element"]:
                x.remove("Thunder Attack")

            if "Ice" in weapon["dual_element"]:
                x.remove("Ice Attack")

            if "Dragon" in weapon["dual_element"]:
                x.remove("Dragon Attack")

            if "Poison" in weapon["dual_element"]:
                x.remove("Poison Attack")

            if "Sleep" in weapon["dual_element"]:
                x.remove("Sleep Attack")

            if "Paralysis" in weapon["dual_element"]:
                x.remove("Paralysis Attack")

            if "Blast" in weapon["dual_element"]:
                x.remove("Blast Attack")
        
        #Bow Coatings
        if weaponType == "Bow":
            if "Paralysis" not in weapon["coatings"]:
                x.remove("Paralysis Functionality")
            if "Poison" not in weapon["coatings"]:
                x.remove("Poison Functionality")
            if "Sleep" not in weapon["coatings"]:
                x.remove("Sleep Functionality")
            if "Sleep" not in weapon["coatings"]:
                x.remove("Blast Functionality")

    return x

#############################################################################################################################

def roll_that_shiz():

    global global_weapon
    global global_head
    global global_chest
    global global_arms
    global global_waist
    global global_legs
    global global_charm
    global global_weapon_type

    # Defining the armor pieces
    head = "bad array"
    chest = "bad array"
    arms = "bad array"
    waist = "bad array"
    legs = "bad array"
    charm = "bad array"

    # Flags to Mark a piece has been slotted
    headflag = 0
    chestflag = 0
    armsflag = 0
    waistflag = 0
    legsflag = 0
    charmflag = 1

    print("")
    print("")
    print("")

    # Getting weapons
    weaponType = get_random_weapontype()
    weapon = get_random_weapon(weaponType)

    print(weapon["weapon_type"],weapon["weapon_name"])

    # Array for what skills have already been rolled so we dont repeate skill beyond max level in insane quanties
    skillsprevious = []
    charmskills = []

    # Rolling to see if it wants a set bonus and if so what set bonuse
    set_bonus_percentage = .2
    set_bonus = get_random_setbonus(set_bonus_percentage)
    needed_set = 0

    #Sees if it should do 1 level of set bonus or 2, so it can mix between set bonuses
    if set_bonus != []:
        print(set_bonus["name"])
        if set_bonus["activation_2"] != 0:
            if random.random() >= .5:
                needed_set = set_bonus["activation_2"]
            else:
                needed_set = set_bonus["activation_1"]
        else:
            needed_set = set_bonus["activation_1"]

        #Rolling for what set pieces to grab so that it can get add further mixture. Without this, it will always go Head, Chest, Arms, Waist and then legs.
        set_bonus_pieces = set()
        while len(set_bonus_pieces) < needed_set:
            set_bonus_pieces.add(random.randint(1, 5))

        set_bonus_armor_choices = get_set_bonus_armor(set_bonus)

    #Checks for each armor piece if it rolled and slots that armor in accordingly
    if needed_set != 0:
        if 1 in set_bonus_pieces:
            headchoice = random.choice(set_bonus_armor_choices)
            head = headchoice["head"]
            headflag = 1
        if 2 in set_bonus_pieces:
            chestchoice = random.choice(set_bonus_armor_choices)
            chest = chestchoice["chest"]
            chestflag = 1
        if 3 in set_bonus_pieces:
            armschoice = random.choice(set_bonus_armor_choices)
            arms = armschoice["arms"]
            armsflag = 1
        if 4 in set_bonus_pieces:
            waistchoice = random.choice(set_bonus_armor_choices)
            waist = waistchoice["waist"]
            waistflag = 1
        if 5 in set_bonus_pieces:
            legschoice = random.choice(set_bonus_armor_choices)
            legs = legschoice["legs"]
            legsflag = 1
    
    # Getting Useless skills so we don't roll them
    weapon_useless_skills = get_useless_skills(weaponType)

    useless_elemntal = get_useless_elements(weapon, weaponType)

    for every in range(len(useless_elemntal)):
        weapon_useless_skills.append(useless_elemntal[every])

    for every in range(len(weapon_useless_skills)):
        skillsprevious.append(weapon_useless_skills[every])

    # While loop that runs until a piece of armor has been got for each piece
    while head == "bad array" or chest == "bad array" or arms == "bad array" or waist == "bad array" or legs == "bad array":

        # Gets a skill and then begins a counter for that skill to be maxed
        skill = get_random_skills()
        skillmax = skill["skill_max"]
        skillcounter = 0

        # Checks to make sure the skill hasnt been rolled for and if it already has "max" the skill the skip 
        for skillcheck in skillsprevious:
            if skillcheck == skill["skill_name"]:
                skillmax = skillcounter

        # Add the current skill to the list so we can not roll it later
        skillsprevious.append(skill["skill_name"])

        order_for_armor = [1,2,3,4,5]
        random.shuffle(order_for_armor)

        for each in order_for_armor:
            #Logic for each armor piece
            if headflag == 0 and skillmax > skillcounter and each == 1:
                head = get_random_head(skill)
                if head != "bad array":
                    if head["skill_name_1"] == skill["skill_name"]:
                        skillcounter += head["skill_1_amount"]
                    if head["skill_name_2"] == skill["skill_name"]:
                        skillcounter += head["skill_1_amount"]
                if head != "bad array":
                    headflag = 1

            #Logic for each armor piece
            if chestflag == 0 and skillmax > skillcounter and each == 1:
                chest = get_random_chest(skill)
                if chest != "bad array":
                    if chest["skill_name_1"] == skill["skill_name"]:
                        skillcounter += chest["skill_1_amount"]
                    if chest["skill_name_2"] == skill["skill_name"]:
                        skillcounter += chest["skill_1_amount"]
                if chest != "bad array":
                    chestflag = 1

            #Logic for each armor piece
            if armsflag == 0 and skillmax > skillcounter and each == 1:
                arms = get_random_arms(skill)
                if arms != "bad array":
                    if arms["skill_name_1"] == skill["skill_name"]:
                        skillcounter += arms["skill_1_amount"]
                    if arms["skill_name_2"] == skill["skill_name"]:
                        skillcounter += arms["skill_1_amount"]
                if arms != "bad array":
                    armsflag = 1

            #Logic for each armor piece
            if waistflag == 0 and skillmax > skillcounter and each == 1:
                waist = get_random_waist(skill)
                if waist != "bad array":
                    if waist["skill_name_1"] == skill["skill_name"]:
                        skillcounter += waist["skill_1_amount"]
                    if waist["skill_name_2"] == skill["skill_name"]:
                        skillcounter += waist["skill_1_amount"]
                if waist != "bad array":
                    waistflag = 1

            #Logic for each armor piece
            if legsflag == 0 and skillmax > skillcounter and each == 1:
                legs = get_random_legs(skill)
                if legs != "bad array":
                    if legs["skill_name_1"] == skill["skill_name"]:
                        skillcounter += legs["skill_1_amount"]
                    if legs["skill_name_2"] == skill["skill_name"]:
                        skillcounter += legs["skill_1_amount"]
                if legs != "bad array":
                    legsflag = 1

     #Gets Bad skills for weapon
    for every in range(len(weapon_useless_skills)):
        charmskills.append(weapon_useless_skills[every])

    #Gets all skills on armor pieces
    if head["skill_name_1"] != "None":
        charmskills.append(head["skill_name_1"])
    if head["skill_name_2"] != "None":
        charmskills.append(head["skill_name_2"])

    if chest["skill_name_1"] != "None":
        charmskills.append(chest["skill_name_1"])
    if chest["skill_name_2"] != "None":
        charmskills.append(chest["skill_name_2"])

    if arms["skill_name_1"] != "None":
        charmskills.append(arms["skill_name_1"])
    if arms["skill_name_2"] != "None":
        charmskills.append(arms["skill_name_2"])

    if waist["skill_name_1"] != "None":
        charmskills.append(waist["skill_name_1"])
    if waist["skill_name_2"] != "None":
        charmskills.append(waist["skill_name_2"])

    if legs["skill_name_1"] != "None":
        charmskills.append(legs["skill_name_1"])
    if legs["skill_name_2"] != "None":
        charmskills.append(legs["skill_name_2"])

    while charm == "bad array" or charmflag != 0:
        
        charmflag = 0
        charmsList = get_charm_list()

        #Grabs a random charm
        charm = random.choice(charmsList)
        
        #Checks to see if that charm's skills were already gathered
        for skillnamecharm in (charmskills):
            if charm["skill_name_1"] == skillnamecharm:
                charmflag = charmflag + 1
            if charm["skill_name_2"] == skillnamecharm:
                charmflag = charmflag + 1


    #Printing Each Piece Into Console
    print(f"Helm: {head["name"]} | Slots: {head["slot_1"]}, {head["slot_2"]}, {head["slot_3"]} | Skills:", end=" ")
    if head["skill_name_1"] != "None":
        print(f"{head["skill_name_1"]}", end="")
    if head["skill_name_2"] != "None":
        print(f", {head["skill_name_2"]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Chest: {chest["name"]} | Slots: {chest["slot_1"]}, {chest["slot_2"]}, {chest["slot_3"]} | Skills:", end=" ")
    if chest["skill_name_1"] != "None":
        print(f"{chest["skill_name_1"]}", end="")
    if chest["skill_name_2"] != "None":
        print(f", {chest["skill_name_2"]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Arms: {arms["name"]} | Slots: {arms["slot_1"]}, {arms["slot_2"]}, {arms["slot_3"]} | Skills:", end=" ")
    if arms["skill_name_1"] != "None":
        print(f"{arms["skill_name_1"]}", end="")
    if arms["skill_name_2"] != "None":
        print(f", {arms["skill_name_2"]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Waist: {waist["name"]} | Slots: {waist["slot_1"]}, {waist["slot_2"]}, {waist["slot_3"]} | Skills:", end=" ")
    if waist["skill_name_1"] != "None":
        print(f"{waist["skill_name_1"]}", end="")
    if waist["skill_name_2"] != "None":
        print(f", {waist["skill_name_2"]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Legs: {legs["name"]} | Slots: {legs["slot_1"]}, {legs["slot_2"]}, {legs["slot_3"]} | Skills:", end=" ")
    if legs["skill_name_1"] != "None":
        print(f"{legs["skill_name_1"]}", end="")
    if legs["skill_name_2"] != "None":
        print(f", {legs["skill_name_2"]}")
    else:
        print()

    print("Charm: ", charm["charm_name"])
    print("The skills rolled and banned for the weapon: ", skillsprevious)

    global_weapon = weapon["weapon_name"]
    global_head = head["name"]
    global_chest = chest["name"]
    global_arms = arms["name"]
    global_waist = waist["name"]
    global_legs = legs["name"]
    global_charm = charm["charm_name"]
    global_weapon_type = weaponType

    return(weapon["weapon_name"],head["name"],chest["name"],arms["name"],waist["name"],legs["name"],charm["charm_name"],weaponType)

def save(num):

    global global_weapon
    global global_head
    global global_chest
    global global_arms
    global global_waist
    global global_legs
    global global_charm
    global global_weapon_type

    if global_weapon != "" and global_head != "" and global_chest != "" and global_arms != "" and global_waist != "" and global_legs != "" and global_charm != "" and global_weapon_type != "":
        f = open("Monster_Hunter_World_ERP/save{}.txt".format(num), "w")
        f.write(global_weapon)
        f.write("\n")
        f.write(global_head)
        f.write("\n")
        f.write(global_chest)
        f.write("\n")
        f.write(global_arms)
        f.write("\n")
        f.write(global_waist)
        f.write("\n")
        f.write(global_legs)
        f.write("\n")
        f.write(global_charm)
        f.write("\n")
        f.write(global_weapon_type)
        f.close()

def load(num):

    global global_weapon
    global global_head
    global global_chest
    global global_arms
    global global_waist
    global global_legs
    global global_charm
    global global_weapon_type

    names = []

    f = open("Monster_Hunter_World_ERP/save{}.txt".format(num), "r")

    for line in f:
        names.append(line.strip())

    f.close()

    global_weapon = names[0]
    global_head = names[1]
    global_chest = names[2]
    global_arms = names[3]
    global_waist = names[4]
    global_legs = names[5]
    global_charm = names[6]
    global_weapon_type = names[7]

    return names