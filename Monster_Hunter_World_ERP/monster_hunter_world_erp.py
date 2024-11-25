import tkinter as tk
from tkinter import ttk
import definitions

#Functions

def selector_greatsword():
    if definitions.get_greatsword() == True:
        great_button.configure(bg='#cccccc')
    if definitions.get_greatsword() == False:
        great_button.configure(bg='#2E2E2E')
    definitions.set_greatsword()

def selector_longsword():
    if definitions.get_longsword() == True:
        longsword_button.configure(bg='#cccccc')
    if definitions.get_longsword() == False:
        longsword_button.configure(bg='#2E2E2E')
    definitions.set_longsword()

def selector_sns():
    if definitions.get_sns() == True:
        sns_button.configure(bg='#cccccc')
    if definitions.get_sns() == False:
        sns_button.configure(bg='#2E2E2E')
    definitions.set_sns()

def selector_db():
    if definitions.get_db() == True:
        db_button.configure(bg='#cccccc')
    if definitions.get_db() == False:
        db_button.configure(bg='#2E2E2E')
    definitions.set_db()

def selector_hammer():
    if definitions.get_hammer() == True:
        hammer_button.configure(bg='#cccccc')
    if definitions.get_hammer() == False:
        hammer_button.configure(bg='#2E2E2E')
    definitions.set_hammer()

def selector_hh():
    if definitions.get_hh() == True:
        hh_button.configure(bg='#cccccc')
    if definitions.get_hh() == False:
        hh_button.configure(bg='#2E2E2E')
    definitions.set_hh()

def selector_lance():
    if definitions.get_lance() == True:
        lance_button.configure(bg='#cccccc')
    if definitions.get_lance() == False:
        lance_button.configure(bg='#2E2E2E')
    definitions.set_lance()

def selector_glance():
    if definitions.get_glance() == True:
        glance_button.configure(bg='#cccccc')
    if definitions.get_glance() == False:
        glance_button.configure(bg='#2E2E2E')
    definitions.set_glance()

def selector_sa():
    if definitions.get_sa() == True:
        sa_button.configure(bg='#cccccc')
    if definitions.get_sa() == False:
        sa_button.configure(bg='#2E2E2E')
    definitions.set_sa()

def selector_cb():
    if definitions.get_cb() == True:
        cb_button.configure(bg='#cccccc')
    if definitions.get_cb() == False:
        cb_button.configure(bg='#2E2E2E')
    definitions.set_cb()

def selector_ig():
    if definitions.get_ig() == True:
        ig_button.configure(bg='#cccccc')
    if definitions.get_ig() == False:
        ig_button.configure(bg='#2E2E2E')
    definitions.set_ig()

def selector_lb():
    if definitions.get_lb() == True:
        lb_button.configure(bg='#cccccc')
    if definitions.get_lb() == False:
        lb_button.configure(bg='#2E2E2E')
    definitions.set_lb()

def selector_hb():
    if definitions.get_hb() == True:
        hb_button.configure(bg='#cccccc')
    if definitions.get_hb() == False:
        hb_button.configure(bg='#2E2E2E')
    definitions.set_hb()

def selector_bow():
    if definitions.get_bow() == True:
        bow_button.configure(bg='#cccccc')
    if definitions.get_bow() == False:
        bow_button.configure(bg='#2E2E2E')
    definitions.set_bow()

def rollem():
    x = definitions.roll_that_shiz()
    weapon_name.configure(text=x[0])
    head_name.configure(text=x[1])
    chest_name.configure(text=x[2])
    arms_name.configure(text=x[3])
    waist_name.configure(text=x[4])
    legs_name.configure(text=x[5])
    charm_name.configure(text=x[6])
    if x[7] == "Great Sword":
        weapon_label.configure(image=great)
    if x[7] == "Long Sword":
        weapon_label.configure(image=longsword)
    if x[7] == "S&S":
        weapon_label.configure(image=sns)
    if x[7] == "Hunting Horn":
        weapon_label.configure(image=hh)
    if x[7] == "Dual Blades":
        weapon_label.configure(image=db)
    if x[7] == "Lance":
        weapon_label.configure(image=lance)
    if x[7] == "Gunlance":
        weapon_label.configure(image=glance)
    if x[7] == "Switch Axe":
        weapon_label.configure(image=switch)
    if x[7] == "Charge Blade":
        weapon_label.configure(image=charge)
    if x[7] == "Hammer":
        weapon_label.configure(image=hammer)
    if x[7] == "Insect Glaive":
        weapon_label.configure(image=ig)
    if x[7] == "Bow":
        weapon_label.configure(image=bow)
    if x[7] == "Light Bowgun":
        weapon_label.configure(image=lb)
    if x[7] == "Heavy Bowgun":
        weapon_label.configure(image=hb)
    
def save(num):
    definitions.save(num)

def load(num):
    x = definitions.load(num)

    weapon_name.configure(text=x[0])
    head_name.configure(text=x[1])
    chest_name.configure(text=x[2])
    arms_name.configure(text=x[3])
    waist_name.configure(text=x[4])
    legs_name.configure(text=x[5])
    charm_name.configure(text=x[6])
    if x[7] == "Great Sword":
        weapon_label.configure(image=great)
    if x[7] == "Long Sword":
        weapon_label.configure(image=longsword)
    if x[7] == "S&S":
        weapon_label.configure(image=sns)
    if x[7] == "Hunting Horn":
        weapon_label.configure(image=hh)
    if x[7] == "Dual Blades":
        weapon_label.configure(image=db)
    if x[7] == "Lance":
        weapon_label.configure(image=lance)
    if x[7] == "Gunlance":
        weapon_label.configure(image=glance)
    if x[7] == "Switch Axe":
        weapon_label.configure(image=switch)
    if x[7] == "Charge Blade":
        weapon_label.configure(image=charge)
    if x[7] == "Hammer":
        weapon_label.configure(image=hammer)
    if x[7] == "Insect Glaive":
        weapon_label.configure(image=ig)
    if x[7] == "Bow":
        weapon_label.configure(image=bow)
    if x[7] == "Light Bowgun":
        weapon_label.configure(image=lb)
    if x[7] == "Heavy Bowgun":
        weapon_label.configure(image=hb)

#root window
root = tk.Tk()
root.title("Monster Hunter ERP")
root.configure(bg="#2E2E2E")
root.geometry("500x500")
root.pack_propagate(0)
root.resizable(0,0)

#Weapon Images
great = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunGreat.png")
great = great.subsample(2,2)
longsword = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunLong.png")
longsword = longsword.subsample(2,2)
sns = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunSNS.png")
sns = sns.subsample(2,2)
hh = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunHH.png")
hh = hh.subsample(2,2)
db = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunDB.png")
db = db.subsample(2,2)
lance = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunLance.png")
lance = lance.subsample(2,2)
glance = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunGunlance.png")
glance = glance.subsample(2,2)
hammer = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunHammer.png")
hammer = hammer.subsample(2,2)
switch = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunSwitch.png")
switch = switch.subsample(2,2)
charge = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunCharge.png")
charge = charge.subsample(2,2)
ig = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunInsect.png")
ig = ig.subsample(2,2)
bow = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunBow.png")
bow = bow.subsample(2,2)
lb = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunLB.png")
lb = lb.subsample(2,2)
hb = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\MonHunHB.png")
hb = hb.subsample(2,2)

#Armor Images
head = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Helmet_Icon_White.png")
chest = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Chest_Icon_White.png")
arm= tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Arm_Icon_White.png")
waist = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Waist_Icon_White.png")
legs = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Leg_Icon_White.png")
charm = tk.PhotoImage(file ="Monster_Hunter_World_ERP\Images\Talisman_Icon_White.png")

#Generate Set Button
btn = tk.Button(root, text="Generate a Random Build", bg='#808080', font='Helvetica 16 bold', command=rollem)
btn.place(x = 10, y = 10)

#Set Stuff
set_frame = tk.Frame(root,bg='#2E2E2E')
set_frame.place(x = 5, y = 60)

weapon_label = tk.Label(set_frame, image=great, bg='#2E2E2E')
weapon_label.grid(row=0,column=0,sticky="w")

head_label = tk.Label(set_frame, image=head, bg='#2E2E2E')
head_label.grid(row=1,column=0,sticky="w")

chest_label = tk.Label(set_frame, image=chest, bg='#2E2E2E')
chest_label.grid(row=2,column=0,sticky="w")

arms_label = tk.Label(set_frame, image=arm, bg='#2E2E2E')
arms_label.grid(row=3,column=0,sticky="w")

waist_label = tk.Label(set_frame, image=waist, bg='#2E2E2E')
waist_label.grid(row=4,column=0,sticky="w")

legs_label = tk.Label(set_frame, image=legs, bg='#2E2E2E')
legs_label.grid(row=5,column=0,sticky="w")

charm_label = tk.Label(set_frame, image=charm, bg='#2E2E2E')
charm_label.grid(row=6,column=0,sticky="w")

weapon_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
weapon_name.grid(row=0,column=1,sticky="w")

head_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
head_name.grid(row=1,column=1,sticky="w")

chest_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
chest_name.grid(row=2,column=1,sticky="w")

arms_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
arms_name.grid(row=3,column=1,sticky="w")

waist_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
waist_name.grid(row=4,column=1,sticky="w")

legs_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
legs_name.grid(row=5,column=1,sticky="w")

charm_name = tk.Label(set_frame, text= "", font='Helvetica 12 bold', bg='#2E2E2E', fg='#cccccc', padx = 5)
charm_name.grid(row=6,column=1,sticky="w")

#Weapon selector buttons
weapon_frame = tk.Frame(root)
weapon_frame.place(x = 380, y = 45)

great_button = tk.Button(weapon_frame, image=great, bg='#2E2E2E', command=selector_greatsword)
great_button.grid(row=0,column=1)

longsword_button = tk.Button(weapon_frame, image=longsword, bg='#2E2E2E', command=selector_longsword)
longsword_button.grid(row=0,column=2)

sns_button = tk.Button(weapon_frame, image=sns, bg='#2E2E2E', command=selector_sns)
sns_button.grid(row=1,column=1,)

db_button = tk.Button(weapon_frame, image=db, bg='#2E2E2E', command=selector_db)
db_button.grid(row=1,column=2,)

hammer_button = tk.Button(weapon_frame, image=hammer, bg='#2E2E2E', command=selector_hammer)
hammer_button.grid(row=2,column=1,)

hh_button = tk.Button(weapon_frame, image=hh, bg='#2E2E2E', command=selector_hh)
hh_button.grid(row=2,column=2,)

lance_button = tk.Button(weapon_frame, image=lance, bg='#2E2E2E', command=selector_lance)
lance_button.grid(row=3,column=1,)

glance_button = tk.Button(weapon_frame, image=glance, bg='#2E2E2E', command=selector_glance)
glance_button.grid(row=3,column=2,)

sa_button = tk.Button(weapon_frame, image=switch, bg='#2E2E2E', command=selector_sa)
sa_button.grid(row=4,column=1,)

cb_button = tk.Button(weapon_frame, image=charge, bg='#2E2E2E', command=selector_cb)
cb_button.grid(row=4,column=2,)

ig_button = tk.Button(weapon_frame, image=ig, bg='#2E2E2E', command=selector_ig)
ig_button.grid(row=5,column=1,)

lb_button = tk.Button(weapon_frame, image=lb, bg='#2E2E2E', command=selector_lb)
lb_button.grid(row=5,column=2,)

hb_button = tk.Button(weapon_frame, image=hb, bg='#2E2E2E', command=selector_hb)
hb_button.grid(row=6,column=1,)

bow_button = tk.Button(weapon_frame, image=bow, bg='#2E2E2E', command=selector_bow)
bow_button.grid(row=6,column=2,)

#save button
save_frame = tk.Frame(root, bg='#2E2E2E')
save_frame.place(x = 60, y = 465)

save1 = tk.Button(save_frame, text="Save 1", bg='#808080', font='Helvetica 10 bold', command=lambda: save(1))
save1.grid(row=0,column=0)

load1 = tk.Button(save_frame, text="Load 1", bg='#808080', font='Helvetica 10 bold', command=lambda: load(1))
load1.grid(row=0,column=1)

save2 = tk.Button(save_frame, text="Save 2", bg='#808080', font='Helvetica 10 bold', command=lambda: save(2))
save2.grid(row=0,column=2, padx=(25,0))

load2 = tk.Button(save_frame, text="Load 2", bg='#808080', font='Helvetica 10 bold', command=lambda: load(2))
load2.grid(row=0,column=3)

save3 = tk.Button(save_frame, text="Save 3", bg='#808080', font='Helvetica 10 bold', command=lambda: save(3))
save3.grid(row=0,column=4, padx=(25,0))

load3 = tk.Button(save_frame, text="Load 3", bg='#808080', font='Helvetica 10 bold', command=lambda: load(3))
load3.grid(row=0,column=5)

root.mainloop()