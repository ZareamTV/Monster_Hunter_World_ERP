# Monster_Hunter_World_ERP
This is a Equipment Randomizer Program (ERP) for Monster Hunter: World.

As it currently stands this program only rolls Master Rank Armor and the last weapons of each tree.

This program is made to make random build within Monster Hunter World using some logic. The program is intended to explore options in Monster Hunter: World that may not be strong, but are never the less possible.

The build will select set bonuses (if it rolls one) and skills to focus on obtaining and get gear to achieve those skills and set bonuses. It will not focus any skills that are useless for a weapon. It may focus skills that are bad for them, but not useless. Examples being, Great Sword may get offensive guard because it can use it but Dual Blades cannot. You however can get a skill the is useless on a weapon **IF** the armor has a second skill that was useful and the program focused that instead.

# Setup (With the .exe):

*As a note, windows or your antivirus may flag the .exe as a suspicious file when you run it. You always run .exe's at your own risk on the internet. Be smart, be safe and do your research. Always scan your PC if you are unsure after running an .exe.*

*For your knowledge, the files were compiled using Pyinstaller. https://pyinstaller.org/en/stable/*

1. Download the files provided as a .zip
2. Pull out the folder anwhere on your pc. (Do **NOT** move any files in this folder as the image files bundled are in set locations for it to locate.)
3. Run the monster_hunter_erp.exe

# Setup (Without the .exe):

*This setup will take some knowledge of coding to do, but is viable*

1. This code was written in Python 3.13.0 https://www.python.org/downloads/release/python-3130/
   - Install this to your PC
   - I would verify that Python is working if you are new by opening your CMD and running "python --version" to verify the installed version. If you have issues with this, the internet is full of reasons on why.
2. Download the files provided as a zip and pull out the folder "Monster_Hunter_World_ERP-main". (Do **NOT** move any files in this folder as the image files bundled are in set locations for it to locate.)
3. You will neeed the following modules as dependencies:
   - Numpy
     
   To Install these modules, open up the CMD and run "pip install -r [a copied path to the requirements.txt document downloaded]"

   *I will note because numpy is the only install for this program you can also just run "pip install numpy==2.1.2"*
4. Open up the cmd and change the directory to the Monster_Hunter_World_ERP-main folder containing all of the files including the .exe.
   - To do this, type "cd .../.../" where the .../.../ is the path to the folder.
5. Finally type "python Monster_Hunter_World_ERP/monster_hunter_world_erp.py"

# Running the Program

Once you have the program up it works as follows:

- Pressing the "Generate a Random Build" button will generate your build.
- Selecting any of the weapon on the right side will make the generation use the selected weapons only.

