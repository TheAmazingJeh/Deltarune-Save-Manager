import os
from tkinter.messagebox import showwarning
from lib.filemanip.IniFile import IniParser
"""

{
    "active": {int},                             # Which save is active
    "active_exists": {bool},                     # If the active save exists
    "backup": {int},                             # Unused
    "backup_path": "{Folder path}",              # Path to the backup folder
    "chapter": self.chapter_selector_int.get()   # The chapter that is selected
}

"""

def load_save(info:str) -> dict:
    if info['active_exists']:
        showwarning("Warning", "Overwriting an existing save is not supported yet. Skill Issue")
        return None

    # List files in backup folder
    backup_files = os.listdir(info["backup_path"])
    backup_files = get_correct_files_from_backup(backup_files, info["chapter"])
    for file in backup_files:
        if file.endswith("_9"):
            backup_files.remove(file)
        duplicate_file(os.path.join(info["backup_path"], file), generate_active_path(info["chapter"], info["active"]))
        iniparser = IniParser(os.path.join(info["backup_path"], "dr.ini"), info["chapter"], 0)
        iniparser.duplicate_to(os.path.join(os.getenv("LOCALAPPDATA"), "DELTARUNE", "dr.ini"), info["chapter"], info["active"])

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