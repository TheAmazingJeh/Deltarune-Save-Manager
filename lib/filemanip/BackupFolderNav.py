import os


class BackupFolderNav:
    def __init__(self, config, max_chapter, default_chapter=1):
        self.config = config # Expects folder with folders, CH1, CH2, etc.
        self.BASE_FOLDER = config["savesFolderCONST"]
        self.max_chapter = max_chapter
        self.change_chapter(default_chapter)

    def change_chapter(self, chapter):
        if chapter > self.max_chapter:
            raise ValueError(f"Chapter {chapter} is greater than the maximum chapter of {self.max_chapter}")
        
        if not os.path.exists(os.path.join(self.BASE_FOLDER, f"CH{str(chapter)}")):
            os.mkdir(os.path.join(self.BASE_FOLDER, f"CH{str(chapter)}"))

        self.current_folder = os.path.join(self.BASE_FOLDER, f"CH{str(chapter)}")
        self.current_chapter = chapter

    def move_to_folder_index(self, index):
        # Get the contents of the current folder
        contents = self.get_folder_contents(self.current_folder)
        # Check if the index is in the folders
        if index < len(contents["folders"]):
            # Move to the folder
            self.move_to_folder(contents["folders"][index])

    def get_selected_save(self, index):
        # Get the contents of the current folder
        contents = self.get_folder_contents(self.current_folder)
        # Subtract the length of the folders from the index
        index = index - len(contents["folders"])
        # Check if the index is < 0
        if index < 0:
            return None
        # Check if the index is in the saves
        if index < len(contents["saves"]):
            # Return the save
            return contents["saves"][index]
        else:
            return None

    def move_to_folder(self, folder):
        if os.path.exists(os.path.join(self.current_folder, folder)):
            if not self.is_save_folder(os.path.join(self.current_folder, folder)):
                self.current_folder = os.path.join(self.current_folder, folder)
        else:
            raise FileNotFoundError(f"Folder {folder} does not exist in {self.current_folder}")

    def back_folder(self):
        if self.current_folder == os.path.join(self.BASE_FOLDER, f"CH{str(self.current_chapter)}"):
            return
        else:
            self.current_folder = os.path.dirname(self.current_folder)

    def get_folder_contents(self, folder):
        current_folder_structure = {
            "folders": [],
            "saves": []
        }
        # Check if the folder exists
        if not os.path.exists(folder):
            return {"folders": [], "saves": []}
        # Get the contents of the folder
        contents = os.listdir(folder)
        # Loop through the contents
        for item in contents:
            # Check if the item is a folder or a save
            if self.is_save_folder(os.path.join(folder, item)):
                current_folder_structure["saves"].append(item)
            else:
                current_folder_structure["folders"].append(item)

        return current_folder_structure
    
    def is_save_folder(self, folder):
        # Check if the folder only contains files
        if len(os.listdir(os.path.join(self.current_folder, folder))) == 0:
            return False
        for file in os.listdir(os.path.join(self.current_folder, folder)):
            if os.path.isdir(os.path.join(folder, file)):
                return False
        return True
    
if __name__ == "__main__":
    b = BackupFolderNav({"savesFolderCONST": r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager\Saves"}, 3)
    print(b.get_folder_contents(b.current_folder))
    b.move_to_folder("saves")
    print(b.get_folder_contents(b.current_folder))
    b.back_folder()
    print(b.get_folder_contents(b.current_folder))
    try:
        b.move_to_folder("Error")
    except FileNotFoundError as e:
        print(e)