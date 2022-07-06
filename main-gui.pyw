import os, configparser, json, ctypes, sys
from tkinter import *
import tkinter
from tkinter.simpledialog import askinteger, askstring
from tkinter.messagebox import askyesno, showwarning, showerror

from ext.custom_windows import BackupSave, GameTypeSelect, WriteSave, Settings    # Import tk windows
from ext.custom_windows import loc, vars, location_data # Import Variables

if getattr(sys, 'frozen', False): 
    exec(f"import pyi_splash")
    def kill_splash(): exec("pyi_splash.close()")
else:
    def kill_splash(): pass

config = configparser.ConfigParser()
config.optionxform=str

def open_file(file_name):      
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
def save_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)
def read_file(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content
def try_to_delete(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

def get_save_type_tuple():
    # Make new window and ask for slot & save
    save_type = (0,0) # TEMP
    return (str(save_type[0]),str(save_type[1]-1))

def makeinikey(chapter,slot):
    chapter, slot = str(chapter), str(slot)
    match chapter:
        case "1": chapter = "G"
        case "2": chapter = "G_2_"
        case _  : pass
    match slot:
        case "0": chapSlot = f"{chapter}0"
        case "1": chapSlot = f"{chapter}1"
        case "2": chapSlot = f"{chapter}2"
        case _: pass
    return chapSlot
def writeini(key,name,room,time):
    config.read(location_data["data"]+'\\dr.ini')
    if not config.has_section(key):
        config.add_section(key)
    if not key.__contains__("_2"):
        room == str(int(room)+281)

    config.set(key, 'Name',f'"{name.strip(" ")}"')
    config.set(key, 'Level', '"1.000000"')
    config.set(key, 'Love', '"1.000000"')
    config.set(key, 'Time', f'"{time.strip(" ")}.000000"')
    config.set(key, 'Room', f'"{room.strip(" ")}.000000"')
    config.set(key, 'InitLang', '"0.000000"')
    config.set(key, 'UraBoss', '"0.000000"')
    config.set(key, 'Version', '"1.10"')
    
    with open(location_data["data"]+'\\dr.ini', 'w') as configfile:
        config.write(configfile)

def backup_save(chapter=None,slot=None):
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
        if new == "":
            new = "Undefined"
        if os.path.exists(loc+f"\\Saves\\CH{str(chapter)}\\"+new):
            new += "-new"
        d = [new,chapter,slot]
    
    if not os.path.exists(loc+f'\\Saves\\CH{d[1]}\\{d[0]}'):
        os.makedirs(loc+f'\\Saves\\CH{d[1]}\\{d[0]}')
    save_file(loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save",open_file(location_data["data"]+f"\\filech{d[1]}_{d[2]}"))

def write_save():
    d = WriteSave(w)
    d = d.result
    if d == None:
        return
    d[2] = d[2]-1 # Fix for slot (List index starts at 0)

    print(location_data["data"]+f'\\filech{d[1]}_{d[2]}')
    if os.path.exists(location_data["data"]+f'\\filech{d[1]}_{d[2]}'):
        doBackup = askyesno("File already exists!\nDo you want to back up existing save? (y/n)")
        match doBackup:
            case True: backup_save(chapter=d[1],slot=d[2])
            case False: pass
    
    # TODO: Redo to just copy .ini file. (Only Specified Key)
    
    lines = read_file(loc+f'\\Saves\\CH{d[1]}\\{d[0]}\\save')
    data = []
    for item in lines:
        data.append(item.strip("\n"))
    if d[1] == "1":
        room = data[10316]
        time = data[10317]
    if d[1] == "2":
        room = data[3053]
        time = data[3054]
    name = "Undefined" 
    room = "1"
    time = "1"
    

    writeini(makeinikey(d[1],d[2]),name,room,time)

    # END FIXME:

    try_to_delete(location_data["data"]+f'\\filech{d[1]}_{d[2]}')

    save_file(location_data["data"] + f"\\filech{d[1]}_{d[2]}",open_file(loc+f"\\Saves\\CH{d[1]}\\{d[0]}\\save"))
    visibleSlot = int(d[2])+1
    print(f"Save '{d[0]}' written to chapter {d[1]} slot {visibleSlot}\n",location_data["data"])

def get_game_type(w):
    global launchGameText
    d = GameTypeSelect(w)
    d = d.result
    vars["GAMETYPE"] = d
    with open(loc+'\\data.json', 'w') as f:
        json.dump(vars, f, indent=4)
    launchGameText.set(update_game_button())
    return vars
def settings():
    d = Settings(w)
    d = d.result
    launchGameText.set(update_game_button())
    return
def open_game():
    global vars
    if not "GAMETYPE" in vars:
        vars = get_game_type(w)
    else:
        os.system(vars["GAMETYPE"][1])

def update_game_button():
    global gameL
    match "GAMETYPE" in vars:
        case True: gameL = f" ({vars['GAMETYPE'][0]})"
        case _: gameL = ""
    return "Launch Game"+gameL
def setwindowmiddle(wd,width, height):
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
#w.resizable(False, False)

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