import os, json, ctypes, sys
from tkinter import *
import tkinter
from tkinter.simpledialog import askinteger, askstring
from tkinter.messagebox import askyesno, showwarning, showerror

from configparser import ConfigParser

from ext.custom_windows import BackupSave, GameTypeSelect, WriteSave, Settings    # Import tk windows
from ext.custom_windows import loc, vars, location_data, rename_save # Import Variables & Functions

if getattr(sys, 'frozen', False): 
    exec(f"import pyi_splash")
    def kill_splash(): exec("pyi_splash.close()")
else:
    def kill_splash(): pass

class CaseConfigParser(ConfigParser): # Creates a config parser that is case sensitive (Default isn't)
    def optionxform(self, optionstr):
        return optionstr

def open_file(file_name):      # Simple File opener
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
def save_file(file_name, data):# Simple File saver
    with open(file_name, 'w') as file:
        file.write(data)
def read_file(file_name):      # Simple File reader
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content
def try_to_delete(file_name):  # Simple File deleter
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

def makeinikey(chapter,slot):  # Constructs the key for the .ini file
    if chapter == 1: chapter = "G"
    else: chapter = f"G_{chapter}_"
    return str(chapter)+str(slot)

def readini(path,key):         # Reads a specified key in a .ini file and returns the data as dictionary
    config = CaseConfigParser()
    config.read(path)
    iniData = {}
    for item in config[key]: iniData[item] = config[key][item]
    return iniData

def writeini(writePath, iniData, section, existing=None):   # Writes data to a .ini file (existing is a path to an existing .ini file)
    config = CaseConfigParser()
    if existing == None: pass
    else: config.read(existing)
    keys = list(iniData.keys())
    if not config.has_section(section): config.add_section(section)
    for item in keys: config[section][item] = iniData[item]
    with open(writePath, 'w') as configfile: config.write(configfile)

def backup_save(chapter=None,slot=None):  # Backup save function
    if chapter == None and slot == None:
        d = BackupSave(w)
        if d == None:
            return
        d = d.result
        d[2] = d[2]-1 # Fix for slot (List index starts at 0)

        if not os.path.exists(location_data["data"]+f"\\filech{d[1]}_{d[2]}"):
            showerror("Error",f"Save does not exist!\n\nChapter {d[1]} Slot {d[2]+1}")
            backup_save()
    else:
        new = askstring(" ",f"What do you want to name the backup?")
        new = rename_save(new,chapter)
        d = [new,chapter,slot]
    
    if not os.path.exists(loc+f'\\Saves\\CH{d[1]}\\{d[0]}'):
        os.makedirs(loc+f'\\Saves\\CH{d[1]}\\{d[0]}')
    save_file(loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save",open_file(location_data["data"]+f"\\filech{d[1]}_{d[2]}"))
    iniData = readini(location_data["data"]+"\\dr.ini",makeinikey(d[1],d[2]))
    writeini(loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save.ini", iniData, "DATA")

def write_save():         # Write save function
    d = WriteSave(w)
    d = d.result
    if d == None:
        return
    d[2] = d[2]-1 # Fix for slot (List index starts at 0)

    if os.path.exists(location_data["data"]+f'\\filech{d[1]}_{d[2]}'):
        doBackup = askyesno("Warning","File already exists!\nDo you want to back up existing save? (y/n)")
        match doBackup:
            case True: backup_save(chapter=d[1],slot=d[2])
            case False: pass
    
    writeini(
        location_data["data"]+"\\dr.ini", 
        readini(
            loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save.ini",
            "DATA"
            ), 
        makeinikey(d[1],d[2]), 
        existing= location_data["data"]+"\\dr.ini")

    try_to_delete(location_data["data"]+f'\\filech{d[1]}_{d[2]}')

    save_file(location_data["data"] + f"\\filech{d[1]}_{d[2]}",open_file(loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save"))
    visibleSlot = int(d[2])+1
    print(f"Save '{d[0]}' written to chapter {d[1]} slot {visibleSlot}\n",location_data["data"])

def get_game_type(w):     # Gets the game launch type from the user
    global launchGameText
    d = GameTypeSelect(w)
    d = d.result
    if d == None:
        return vars
    vars["GAMETYPE"] = d
    with open(loc+'\\data.json', 'w') as f:
        json.dump(vars, f, indent=4)
    launchGameText.set(update_game_button())
    return vars
def settings():           # Settings menu
    d = Settings(w)
    d = d.result
    launchGameText.set(update_game_button())
    return
def open_game():          # Opens the game
    global vars
    if not "GAMETYPE" in vars:
        vars = get_game_type(w)
    else:
        os.system(vars["GAMETYPE"][1])

def update_game_button(): # Updates the game button text to display the current game launch type
    global gameL
    match "GAMETYPE" in vars:
        case True: gameL = f" ({vars['GAMETYPE'][0]})"
        case _: gameL = ""
    return "Launch Game"+gameL
def setwindowmiddle(wd,width, height): # Sets the window to the middle of the screen
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    middle = screensize[0] // 2, screensize[1] // 2
    add = middle[0] - width // 2, middle[1] - height // 2
    wd.geometry(f"{width}x{height}+{add[0]}+{add[1]}")

w = Tk()
w.title("Save Manager")
if os.path.exists(loc+"\\DELTARUNE.ico"):
    w.iconbitmap(w, loc+"\\DELTARUNE.ico")
    
w.configure()
setwindowmiddle(w,250,180)
w.resizable(False, False)

launchGameText = StringVar()
launchGameText.set(update_game_button())
Button(w, text="Backup Saves", command=backup_save).pack(padx=5, pady=5)
Button(w, text="Load Save", command=write_save).pack(padx=5, pady=5)

Button(w, textvariable=launchGameText, command=open_game).pack(pady=5)
Button(w, text="Settings", command=settings).pack(padx=5, pady=5)

Button(w, text="Quit", command=sys.exit).pack(padx=5, pady=5)



if __name__ == "__main__":
    kill_splash()
    w.mainloop()