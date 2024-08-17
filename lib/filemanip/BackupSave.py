import os
from tkinter.messagebox import showwarning, showerror
from lib.filemanip.IniFile import IniParser

"""

{
    "active": {int},                             # The active save slot (to backup)
    "active_exists": {bool},                     # Unused
    "backup": {int},                             # Unused
    "backup_path": "{Folder path}",              # Path to the backup folder (Is created)
    "chapter": self.chapter_selector_int.get()   # The chapter that is selected
}

"""

def backup_save(info:str) -> dict:
    # Check if the backup folder exists
    if not os.path.exists(info["backup_path"]):
        # If it doesn't, create it
        os.mkdir(info["backup_path"])
    # Get the active save slot
    active_path = generate_active_path(info["chapter"], info["active"])
    # Duplicate the active save slot into the backup folder
    duplicate_file(active_path, os.path.join(info["backup_path"], f"filech{info['chapter']}_0"))
    iniparser = IniParser(os.path.join(os.getenv("LOCALAPPDATA"), "DELTARUNE", "dr.ini"), info["chapter"], info["active"])
    iniparser.duplicate_to(os.path.join(info["backup_path"], "dr.ini"))


    

def get_correct_files_from_backup(backup_files:list, chapter:int) -> list:
    # Get the correct files from the backup folder
    correct_files = []
    for file in backup_files:
        if file.startswith(f"filech{chapter}") and not file.endswith("_9"):
            correct_files.append(file)
    return correct_files

def generate_active_path(chapter:int, slot:int):
    return os.path.join(os.getenv("LOCALAPPDATA"), "Deltarune", f"filech{chapter}_{slot}")

def duplicate_file(src:str, dst:str) -> None:
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    info = {
        "active": 1,
        "backup_path": r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager\Saves\CH1\Test",
        "chapter": 1
    }
    b = backup_save(info)
    print("BackupSave.py", b)