import random
import numpy
from lists import *

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
    x = random.choice(skilllist)
    #print(x)
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
    if weaponType == "Great Sword":
        x = random.choice(greatswordList)
    elif weaponType == "Long Sword":
        x = random.choice(longswordList)
    elif weaponType == "S&S":
        x = random.choice(snsList)
    elif weaponType == "Hammer":
        x = random.choice(hammerList)
    elif weaponType == "Lance":
        x = random.choice(lanceList)
    elif weaponType == "Gunlance":
        x = random.choice(gunlanceList)
    elif weaponType == "Switch Axe":
        x = random.choice(switchaxeList)
    elif weaponType == "Charge Blade":
        x = random.choice(chargebladeList)
    elif weaponType == "Insect Glaive":
        x = random.choice(insectglaiveList)
    elif weaponType == "Dual Blades":
        x = random.choice(dualbladesList)
    elif weaponType == "Hunting Horn":
        x = random.choice(huntinghornList)
    elif weaponType == "Bow":
        x = random.choice(bowList)
    elif weaponType == "Light Bowgun":
        x = random.choice(lightbowgunList)
    elif weaponType == "Heavy Bowgun":
        x = random.choice(lightbowgunList)
    return x

def get_random_setbonus(percent):
    rand = random.random()
    if rand <= percent:
        x = random.choice(setbonuslist)
    else:
        x = []
    return x

def get_random_head(skill):
    grouping = []
    for y in range(len(armorheadlist)):
        x = armorheadlist[y]
        if skill[0] == skilllist[x[4]][0] and -1 != x[4]:
            grouping.append(y)
        if skill[0] == skilllist[x[6]][0] and -1 != x[6]:
            grouping.append(y)

    if grouping == []:
        return "bad array"
    
    value = random.choice(grouping)
    armor = armorheadlist[value]
    return armor

def get_random_chest(skill):
    grouping = []
    for y in range(len(armorheadlist)):
        x = armorchestlist[y]
        if skill[0] == skilllist[x[4]][0] and -1 != x[4]:
            grouping.append(y)
        if skill[0] == skilllist[x[6]][0] and -1 != x[6]:
            grouping.append(y)

    if grouping == []:
        return "bad array"
    
    value = random.choice(grouping)
    armor = armorchestlist[value]
    return armor

def get_random_arms(skill):
    grouping = []
    for y in range(len(armorheadlist)):
        x = armorarmslist[y]
        if skill[0] == skilllist[x[4]][0] and -1 != x[4]:
            grouping.append(y)
        if skill[0] == skilllist[x[6]][0] and -1 != x[6]:
            grouping.append(y)

    if grouping == []:
        return "bad array"
    
    value = random.choice(grouping)
    armor = armorarmslist[value]
    return armor

def get_random_legs(skill):
    grouping = []
    for y in range(len(armorheadlist)):
        x = armorlegslist[y]
        if skill[0] == skilllist[x[4]][0] and -1 != x[4]:
            grouping.append(y)
        if skill[0] == skilllist[x[6]][0] and -1 != x[6]:
            grouping.append(y)

    if grouping == []:
        return "bad array"
    
    value = random.choice(grouping)
    armor = armorlegslist[value]
    return armor

def get_random_feet(skill):
    grouping = []
    for y in range(len(armorheadlist)):
        x = armorfeetlist[y]
        if skill[0] == skilllist[x[4]][0] and -1 != x[4]:
            grouping.append(y)
        if skill[0] == skilllist[x[6]][0] and -1 != x[6]:
            grouping.append(y)

    if grouping == []:
        return "bad array"

    value = random.choice(grouping)
    armor = armorfeetlist[value]
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
        x = ["Artillery", "Horn Maestro", "Special Ammo Boost", "Spread/Power Shots,", "Piercing Shots", "Normal Shots" "Bow Charge Plus", "Capacity Boost", "Guard", "Offensive Guard", "Guard Up"]
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
        x = ["Artillery", "Power Prolonger", "Capacity Boost", "Guard", "Offensive Guard", "Focus", "Horn Maestro", "Guard Up"]
        return x
    if weapon == "Light Bowgun":
        x = ["Power Prolonger", "Capacity Boost", "Guard", "Offensive Guard", "Horn Maestro", "Bow Charge Plus", "Guard Up"]
        return x
    if weapon == "Heavy Bowgun":
        x = ["Power Prolonger", "Capacity Boost", "Horn Maestro", "Bow Charge Plus"]
        return x
    
def get_useless_elements(weapon, weaponType):

    x = ["Fire Attack", "Ice Attack", "Dragon Attack", "Thunder Attack", "Water Attack", "Blast Attack", "Sleep Attack", "Poison Attack", "Paralysis Attack", "Free Elem/Ammo Up", "Elderseal Boost", "Blast Functionality", "Paralysis Functionality", "Posion Functionality", "Sleep Functionality"]

    #BowGun
    if weaponType == "Light Bowgun" or weaponType == "Heavy Bowgun":
        x.remove("Free Elem/Ammo Up")
        if weapon[4] == 1:
            x.remove("Fire Attack")
        if weapon[5] == 1:
            x.remove("Water Attack")
        if weapon[6] == 1:
            x.remove("Thunder Attack")
        if weapon[7] == 1:
            x.remove("Ice Attack")
        if weapon[8] == 1:
            x.remove("Dragon Attack")
        if weapon[9] == 1:
            x.remove("Poison Attack")
        if weapon[10] == 1:
            x.remove("Sleep Attack")
        if weapon[11] == 1:
            x.remove("Paralysis Attack")

    else:

        #Fire
        if weapon[4] == 1:
            x.remove("Fire Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Water
        if weapon[4] == 2:
            x.remove("Water Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Thunder
        if weapon[4] == 3:
            x.remove("Thunder Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Ice
        if weapon[4] == 4:
            x.remove("Ice Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Dragon
        if weapon[4] == 5:
            x.remove("Dragon Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
            if weapon[6] == 1 or weapon[6] == 2:
                x.remove("Elderseal Boost")
        #Poison
        if weapon[4] == 6:
            x.remove("Poison Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Sleep
        if weapon[4] == 7:
            x.remove("Sleep Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Para
        if weapon[4] == 8:
            x.remove("Paralysis Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")
        #Blast
        if weapon[4] == 9:
            x.remove("Blast Attack")
            if weapon[5] == 0:
                x.remove("Free Elem/Ammo Up")

        #Double ELement Check
        if weaponType == "Dual Blades" or weaponType == "Hunting Horn":
            if weapon[7] == 1:
                x.remove("Fire Attack")

            if weapon[7] == 2:
                x.remove("Water Attack")

            if weapon[7] == 3:
                x.remove("Thunder Attack")

            if weapon[7] == 4:
                x.remove("Ice Attack")

            if weapon[7] == 5:
                x.remove("Dragon Attack")

            if weapon[7] == 6:
                x.remove("Poison Attack")

            if weapon[7] == 7:
                x.remove("Sleep Attack")

            if weapon[7] == 8:
                x.remove("Paralysis Attack")

            if weapon[7] == 9:
                x.remove("Blast Attack")
        
        #Bow Coatings
        if weaponType == "Bow":
            
            if weapon[7] == 0:
                x.remove("Paralysis Functionality")
            elif weapon[4] != 8:
                x.remove("Paralysis Attack")
            if weapon[8] == 0:
                x.remove("Posion Functionality")
            elif weapon[4] != 6:
                x.remove("Poison Attack")
            if weapon[9] == 0:
                x.remove("Sleep Functionality")
            elif weapon[4] != 7:
                x.remove("Sleep Attack")
            if weapon[10] == 0:
                x.remove("Blast Functionality")
            elif weapon[4] != 9:
                x.remove("Blast Attack")


    return x

#############################################################################################################################

def roll_that_shiz():

    # Defining the armor pieces
    head = "bad array"
    chest = "bad array"
    arms = "bad array"
    legs = "bad array"
    feet = "bad array"
    charm = "bad array"

    # Flags to Mark a piece has been slotted
    headflag = 0
    chestflag = 0
    armsflag = 0
    legsflag = 0
    feetflag = 0
    charmflag = 1

    print("")
    print("")
    print("")

    # Getting weapons
    weaponType = get_random_weapontype()
    weapon = get_random_weapon(weaponType)

    print(weaponType, weapon)

    # Array for what skills have already been rolled to use
    skillsprevious = []
    charmskills = []

    # Rolling for a set bonus
    set_bonus_percentage = .25
    set_bonus = get_random_setbonus(set_bonus_percentage)
    needed_set = 0

    #Sees if it should do 1 level of set bonus or 2
    if set_bonus != []:
        print(set_bonus)
        if set_bonus[2] != -1:
            if random.random() >= .5:
                needed_set = set_bonus[2]
            else:
                needed_set = set_bonus[1]
        else:
            needed_set = set_bonus[1]

    #Rolling for what set pieces to grab
    set_bonus_pieces = set()
    while len(set_bonus_pieces) < needed_set:
        set_bonus_pieces.add(random.randint(1, 5))

    #Checks for each armor piece if it rolled to do it
    if needed_set != 0:
        if 1 in set_bonus_pieces:
            if set_bonus[4] != -1 and random.random() >= .5:
                head = armorheadlist[set_bonus[4]]
            else:
                head = armorheadlist[set_bonus[3]]
            headflag = 1
        if 2 in set_bonus_pieces:
            if set_bonus[4] != -1 and random.random() >= .5:
                chest = armorchestlist[set_bonus[4]]
            else:
                chest = armorchestlist[set_bonus[3]]
            chestflag = 1
        if 3 in set_bonus_pieces:
            if set_bonus[4] != -1 and random.random() >= .5:
                arms = armorarmslist[set_bonus[4]]
            else:
                arms = armorarmslist[set_bonus[3]]
            armsflag = 1
        if 4 in set_bonus_pieces:
            if set_bonus[4] != -1 and random.random() >= .5:
                legs = armorlegslist[set_bonus[4]]
            else:
                legs = armorlegslist[set_bonus[3]]
            legsflag = 1
        if 5 in set_bonus_pieces:
            if set_bonus[4] != -1 and random.random() >= .5:
                feet = armorfeetlist[set_bonus[4]]
            else:
                feet = armorfeetlist[set_bonus[3]]
            feetflag = 1

    # Getting Useless skills
    weapon_useless_skills = get_useless_skills(weaponType)

    useless_elemntal = get_useless_elements(weapon, weaponType)

    for every in range(len(useless_elemntal)):
        weapon_useless_skills.append(useless_elemntal[every])

    for every in range(len(weapon_useless_skills)):
        skillsprevious.append(weapon_useless_skills[every])

    # While loop that runs until a piece of armor has been got for each piece
    while head == "bad array" or chest == "bad array" or arms == "bad array" or legs == "bad array" or feet == "bad array":

        # Gets a skill and then begins a counter for that skill to be maxed
        skill = get_random_skills()
        skillmax = skill[1]
        skillcounter = 0

        # Checks to make sure the skill hasnt been rolled for and if it already has "max" the skill the skip 
        for skillcheck in skillsprevious:
            if skillcheck == skill[0]:
                skillmax = skillcounter

        # Add the current skill to the list
        skillsprevious.append(skill[0])

        order_for_armor = [1,2,3,4,5]
        random.shuffle(order_for_armor)

        for each in order_for_armor:
            #Logic for each armor piece
            if headflag == 0 and skillmax > skillcounter and each == 1:
                head = get_random_head(skill)
                if head != "bad array":
                    if skill[0] == skilllist[head[4]][0]:
                        skillcounter += head[5]
                    if skill[0] == skilllist[head[6]][0]:
                        skillcounter += head[7]
                if head != "bad array":
                    headflag = 1

            #Logic for each armor piece
            if chestflag == 0 and skillmax > skillcounter and each == 1:
                chest = get_random_chest(skill)
                if chest != "bad array":
                    if skill[0] == skilllist[chest[4]][0]:
                        skillcounter += chest[5]
                    if skill[0] == skilllist[chest[6]][0]:
                        skillcounter += chest[7]
                if chest != "bad array":
                    chestflag = 1

            #Logic for each armor piece
            if armsflag == 0 and skillmax > skillcounter and each == 1:
                arms = get_random_arms(skill)
                if arms != "bad array":
                    if skill[0] == skilllist[arms[4]][0]:
                        skillcounter += arms[5]
                    if skill[0] == skilllist[arms[6]][0]:
                        skillcounter += arms[7]
                if arms != "bad array":
                    armsflag = 1

            #Logic for each armor piece
            if legsflag == 0 and skillmax > skillcounter and each == 1:
                legs = get_random_legs(skill)
                if legs != "bad array":
                    if skill[0] == skilllist[legs[4]][0]:
                        skillcounter += legs[5]
                    if skill[0] == skilllist[legs[6]][0]:
                        skillcounter += legs[7]
                if legs != "bad array":
                    legsflag = 1

            #Logic for each armor piece
            if feetflag == 0 and skillmax > skillcounter and each == 1:
                feet = get_random_feet(skill)
                if feet != "bad array":
                    if skill[0] == skilllist[feet[4]][0]:
                        skillcounter += feet[5]
                    if skill[0] == skilllist[feet[6]][0]:
                        skillcounter += feet[7]
                if feet != "bad array":
                    feetflag = 1

    #Gets Bad skills for weapon
    for every in range(len(weapon_useless_skills)):
        charmskills.append(weapon_useless_skills[every])

    #Gets all skills on armor pieces
    if head[4] != -1:
        charmskills.append(skilllist[head[4]][0])
    if head[6] != -1:
        charmskills.append(skilllist[head[6]][0])

    if chest[4] != -1:
        charmskills.append(skilllist[chest[4]][0])
    if chest[6] != -1:
        charmskills.append(skilllist[chest[6]][0])

    if arms[4] != -1:
        charmskills.append(skilllist[arms[4]][0])
    if arms[6] != -1:
        charmskills.append(skilllist[arms[6]][0])

    if legs[4] != -1:
        charmskills.append(skilllist[legs[4]][0])
    if legs[6] != -1:
        charmskills.append(skilllist[legs[6]][0])

    if feet[4] != -1:
        charmskills.append(skilllist[feet[4]][0])
    if feet[6] != -1:
        charmskills.append(skilllist[feet[6]][0])

    while charm == "bad array" or charmflag != 0:
        charmflag = 0

        #Grabs a random charm
        charm = random.choice(charmsList)
        charmname = charm[0]
        
        #Checks to see if that charm's skills were already gathered
        for skillnamecharm in (charmskills):
            if skilllist[charm[1]][0] == skillnamecharm:
                charmflag = charmflag + 1
            if skilllist[charm[3]][0] == skillnamecharm:
                charmflag = charmflag + 1

    #Printing Each Piece Into Console
    print(f"Helm: {head[0]} | Slots: {head[1]}, {head[2]}, {head[3]} | Skills:", end=" ")
    if head[4] != -1:
        print(f"{skilllist[head[4]][0]}", end="")
    if head[6] != -1:
        print(f", {skilllist[head[6]][0]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Chest: {chest[0]} | Slots: {chest[1]}, {chest[2]}, {chest[3]} | Skills:", end=" ")
    if chest[4] != -1:
        print(f"{skilllist[chest[4]][0]}", end="")
    if chest[6] != -1:
        print(f", {skilllist[chest[6]][0]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Arms: {arms[0]} | Slots: {arms[1]}, {arms[2]}, {arms[3]} | Skills:", end=" ")
    if arms[4] != -1:
        print(f"{skilllist[arms[4]][0]}", end="")
    if arms[6] != -1:
        print(f", {skilllist[arms[6]][0]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Hips: {legs[0]} | Slots: {legs[1]}, {legs[2]}, {legs[3]} | Skills:", end=" ")
    if legs[4] != -1:
        print(f"{skilllist[legs[4]][0]}", end="")
    if legs[6] != -1:
        print(f", {skilllist[legs[6]][0]}")
    else:
        print()

    #Printing Each Piece Into Console
    print(f"Legs: {feet[0]} | Slots: {feet[1]}, {feet[2]}, {feet[3]} | Skills:", end=" ")
    if feet[4] != -1:
        print(f"{skilllist[feet[4]][0]}", end="")
    if feet[6] != -1:
        print(f", {skilllist[feet[6]][0]}")
    else:
        print()

    print("Charm: ", charmname)
    print("The skills rolled and banned for the weapon: ", skillsprevious)

    return(weapon[0],head[0],chest[0],arms[0],legs[0],feet[0],charm[0],weaponType)
