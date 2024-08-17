from tkinter import Frame, Listbox, Scrollbar, Spinbox, Label, Button, Entry
from tkinter import IntVar, StringVar
from tkinter.constants import N, S, W, E, END, LEFT, RIGHT, TOP, BOTTOM, ALL, ACTIVE, DISABLED
from tkinter.messagebox import showerror, showwarning

from lib.filemanip.BackupFolderNav import BackupFolderNav

import os, json


class SavesFrame(Frame):
    def __init__(self, master, config) -> None:
        super().__init__(master)
        self.master = master
        self.config = config
        self.active_saves = []
        self.MIN_CHAPTERS = 1
        self.MAX_CHAPTERS = 3
        self.DEFAULT_CHAPTER = 1
        self.SELECT_HIGHLIGHT = self.config["colours"]["listboxSelect"]
        self.BACKGROUND_COL = self.config["colours"]["background"]
        self.configure(bg=self.BACKGROUND_COL)

        self.folder_nav = BackupFolderNav(self.config, self.MAX_CHAPTERS, default_chapter=self.DEFAULT_CHAPTER)

        self.place_widgets()    
        self.configure_binds()
        self.refresh_active_saves(ch=self.DEFAULT_CHAPTER)
        self.refresh_backup_saves()

    def place_widgets(self) -> None:
        self.place_active_listbox(0, 0)
        self.place_backup_listbox(0, 1)
        self.place_chapter_selector(0, 2, self)
        self.place_backup_controls(1, 2)

    def place_active_listbox(self, x, y) -> None:
        # Create a frame to hold the active saves listbox and scrollbar
        self.active_saves_frame = Frame(self, bg=self.BACKGROUND_COL)
        # Create a disabled entry to label the frame with the backup saves location
        self.active_saves_label = Entry(self.active_saves_frame, width=50, state=DISABLED)
        # String variable to hold the backup saves location
        self.active_saves_label_str = StringVar(value="")
        self.active_saves_label.config(textvariable=self.active_saves_label_str)
        # Place the entry at the top of the frame
        self.active_saves_label.grid(row=0, column=0, sticky=W, padx=(10,0), pady=(10,2))
        # Create the listbox that contains the active saves
        self.active_saves_widget = Listbox(self.active_saves_frame, width=50, height=3, exportselection=False, selectbackground=self.SELECT_HIGHLIGHT)
        # Create the scrollbar for the listbox
        self.active_saves_widget_scrollbar = Scrollbar(self.active_saves_frame)
        # Set the scrollbar to the listbox
        self.active_saves_widget.config(yscrollcommand=self.active_saves_widget_scrollbar.set)
        self.active_saves_widget_scrollbar.config(command=self.active_saves_widget.yview)
        # Place the listbox and scrollbar
        self.active_saves_widget.grid(row=1, column=0, sticky=N+S+E+W, pady=(0,2), padx=(10,0))
        self.active_saves_widget_scrollbar.grid(row=1, column=1, sticky=N+S+E+W, pady=(0,2))
        # Place the frame
        self.active_saves_frame.grid(row=y, column=x, sticky=E, columnspan=2)

    def place_backup_listbox(self, x, y) -> None:
        # Create a frame to hold the backup saves listbox and scrollbar
        self.backup_saves_frame = Frame(self, bg=self.BACKGROUND_COL)
        # Create a disabled entry to label the frame with the backup saves location
        self.backup_saves_label = Entry(self.backup_saves_frame, width=50, state=DISABLED)
        # String variable to hold the backup saves location
        self.backup_saves_label_str = StringVar(value="")
        self.backup_saves_label.config(textvariable=self.backup_saves_label_str)
        # Place the entry at the top of the frame
        self.backup_saves_label.grid(row=0, column=0, sticky=W, padx=(10,0), pady=(10,2))
        # Create the listbox that contains the backups
        self.backup_saves_widget = Listbox(self.backup_saves_frame, width=50, exportselection=False, selectbackground=self.SELECT_HIGHLIGHT)
        # Create the scrollbar for the listbox
        self.backup_saves_widget_scrollbar = Scrollbar(self.backup_saves_frame)
        # Set the scrollbar to the listbox
        self.backup_saves_widget.config(yscrollcommand=self.backup_saves_widget_scrollbar.set)
        self.backup_saves_widget_scrollbar.config(command=self.backup_saves_widget.yview)
        # Place the listbox and scrollbar
        self.backup_saves_widget.grid(row=1, column=0, sticky=N+S+E+W, pady=2, padx=(10,0))
        self.backup_saves_widget_scrollbar.grid(row=1, column=1, sticky=N+S+E+W, pady=2)
        # Place the frame
        self.backup_saves_frame.grid(row=y, column=x, sticky=E, columnspan=2)

    def place_backup_controls(self, x, y) -> None:
        self.backup_controls_frame = Frame(self, bg=self.BACKGROUND_COL)
        Button(self.backup_controls_frame, text="Refresh", command=self.backup_controls_refresh).grid(row=0, column=0, sticky=E, pady=2)
        Button(self.backup_controls_frame, text="Open Folder", command=self.backup_controls_open_folder).grid(row=0, column=1, sticky=W, pady=2)
        Button(self.backup_controls_frame, text="Back", command=self.backup_controls_back_folder).grid(row=0, column=2, sticky=E, pady=2)
        self.backup_controls_frame.grid(row=y, column=x, sticky=E, padx=(0, 15))

    def place_chapter_selector(self, x, y, root) -> None:
        # Create a frame to hold the chapter selector
        self.chapter_selector_frame = Frame(root, bg=self.BACKGROUND_COL)
        # Label the frame
        self.chapter_selector_label = Label(self.chapter_selector_frame, text="Chapter:", bg=self.BACKGROUND_COL, fg=self.config["colours"]["text"])
        # Place the label
        self.chapter_selector_label.pack(side=LEFT)
        # Create integer variable to hold the chapter number
        self.chapter_selector_int = IntVar(value=self.DEFAULT_CHAPTER)
        # Create the chapter selector
        self.chapter_selector = Spinbox(self.chapter_selector_frame, 
                                        from_=1, to=self.MAX_CHAPTERS, wrap=True,
                                        width=2, textvariable=self.chapter_selector_int,
                                        command=self.chapter_selector_update
                                        )
        # Bind the enter key to chapter selector update while the chapter selector is focused
        self.chapter_selector.bind("<Return>", lambda e: self.chapter_selector_update())
        # Place the chapter selector
        self.chapter_selector.pack(side=RIGHT)
        # Place the frame
        self.chapter_selector_frame.grid(row=y, column=x, sticky=W, padx=15)

    def get_appdata_visual(self) -> str:
        if not self.config["hideAppdata"]: return self.config["data"]
        else: return "C:\\Users\\{USER}\\AppData\\Local\\DELTARUNE"

    def configure_binds(self) -> None:
        # Bind backspace to the back folder function
        self.master.bind("<BackSpace>", lambda e: self.backup_controls_back_folder())
        # Bind enter to the open folder function
        self.master.bind("<Return>", lambda e: self.backup_controls_open_folder())
        # Bind double click to the open folder function
        self.backup_saves_widget.bind("<Double-Button-1>", lambda e: self.backup_controls_open_folder())

    def chapter_selector_update(self) -> None:
        # Get the chapter number from the chapter selector
        if not self.validate(chapter_selector=True): return
        chapter = self.chapter_selector_int.get()
        # Refresh the active saves
        self.folder_nav.change_chapter(chapter)
        self.refresh_active_saves(ch=chapter)
        self.refresh_backup_saves()

    def backup_controls_refresh(self) -> None:
        self.refresh_backup_saves()
        self.refresh_active_saves(ch=self.chapter_selector_int.get())

    def backup_controls_open_folder(self) -> None:
        # Check if a backup save is selected
        if len(self.backup_saves_widget.curselection()) == 0: return
        # Get the selected backup save
        selected_backup_save = self.backup_saves_widget.curselection()[0]
        # Get the length of the folders seccion
        folders_length = len(self.folder_nav.get_folder_contents(self.folder_nav.current_folder)["folders"])
        # Check if the selected backup save is a folder
        if selected_backup_save < folders_length:
            # Move to the folder
            self.folder_nav.move_to_folder_index(selected_backup_save)
            # Refresh the backup saves
            self.refresh_backup_saves()

    def backup_controls_back_folder(self) -> None:
        self.folder_nav.back_folder()
        self.refresh_backup_saves()

    def validate(self, 
                chapter_selector:bool = False, # Return True if the chapter selector is valid
                active_choice:bool = False,    # Return True if the active choice is valid
                backup_choice:bool = False     # Return True if the backup choice is valid
                )-> bool:


        if chapter_selector: # Validate the chapter selector
            # Try to get the chapter selector value
            try: chapter_selector_value = self.chapter_selector_int.get()
            except:
                # If the chapter selector value is invalid, show an error and return False
                showerror("Invalid Chapter", "The selected chapter is invalid.")
                return False
            # Check if the chapter selector value is out of range
            if chapter_selector_value < self.MIN_CHAPTERS or chapter_selector_value > self.MAX_CHAPTERS:
                showerror("Invalid Chapter", f"The selected chapter '{chapter_selector_value}' is out of range. ({self.MIN_CHAPTERS} - {self.MAX_CHAPTERS})")
                return False
        if active_choice:
            try: active_choice_value = self.active_saves_widget.curselection()[0]
            except:
                showerror("Invalid Active Save", "Please select an active save.")
                return False            
        if backup_choice:
            try: backup_choice_value = self.backup_saves_widget.curselection()[0]
            except:
                showerror("Invalid Backup Save", "Please select a backup save.")
                return False
            
            selected_save = self.folder_nav.get_selected_save(backup_choice_value)
            if selected_save is None:
                showerror("Invalid Backup Save", "Please select a backup save.")
                return False


        return True # Return True if the function reaches the end without returning False

    def get_info(self, include_active=False, include_backup=False) -> dict:
        if not self.validate(chapter_selector=True, active_choice=include_active, backup_choice=include_backup): return False
        info_dict = {
            "active": None,
            "active_exists": None,
            "backup": None,
            "backup_path": None,
            "chapter": self.chapter_selector_int.get()
        }
        if include_active:
            if len(self.active_saves_widget.curselection()) == 0: return
            info_dict["active"] = self.active_saves_widget.curselection()[0]
            info_dict["active_exists"] = False if self.active_saves_widget.get(info_dict["active"]).endswith("[Empty]") else True
        if include_backup:
            if len(self.backup_saves_widget.curselection()) == 0: return
            info_dict["backup"] = self.backup_saves_widget.curselection()[0]
            info_dict["backup_path"] = os.path.join(self.folder_nav.current_folder, self.folder_nav.get_selected_save(info_dict["backup"]))
        return info_dict

    def refresh_backup_saves(self) -> None:
        # Clear the listbox
        self.backup_saves_widget.delete(0, END)
        # Get the backup saves
        backup_saves = self.get_backup_saves()
        # Add the backup saves to the listbox
        backup_saves = self.format_backup_saves(backup_saves)
        # Loop through the backup saves
        for save in backup_saves:
            self.backup_saves_widget.insert(END, save)

        self.backup_saves_label_str.set(str(self.folder_nav.current_folder.replace(self.config["loc"],"").replace("\\Saves", "Saves:\\", 1)))
        self.active_saves_label_str.set(str(self.get_appdata_visual()))

    def get_backup_saves(self) -> list:
        # Get the backup saves from the folder nav
        self.backup_saves = self.folder_nav.get_folder_contents(self.folder_nav.current_folder)
        # Return the backup saves
        return self.backup_saves
    
    def format_backup_saves(self, backup_saves:list) -> list:
        formatted_saves = []
        # Loop through the backup folders
        for folder in backup_saves["folders"]:
            # Format the folder name
            folder = f"[{folder}]"
            # Add the folder to the listbox
            formatted_saves.append(folder)
        
        # Loop through the backup saves
        for save in backup_saves["saves"]:
            # Format the save name
            save = f"{save}"
            # Add the save to the listbox
            formatted_saves.append(save)

        return formatted_saves

    def refresh_active_saves(self, ch=None) -> None:
        # Clear the listbox
        self.active_saves_widget.delete(0, END)
        # Get the active saves
        active_saves = self.get_active_saves()
        # Remove any saves that aren't from the selected chapter
        if ch is not None: active_saves = [save for save in active_saves if save.startswith(f"filech{ch}")]
        # Add the active saves to the listbox
        active_saves = self.format_active_saves(active_saves, ch, populate=True if ch is not None else False)

        # Loop through the active saves
        for save in active_saves:
            self.active_saves_widget.insert(END, save)

    def get_active_saves(self) -> list:
        # Get the active saves from directory
        self.active_saves = os.listdir(self.config["data"])
        # Remove anything that doesn't start with "filech"
        self.active_saves = [save for save in self.active_saves if save.startswith("filech")]
        # Ignore slot nine from any chapter (as it is a copy of the most recent save)
        self.active_saves = [save for save in self.active_saves if not save.endswith("_9")]
        # Return the active saves
        return self.active_saves

    def format_active_saves(self, active_saves:list, chapter, populate:bool=True) -> list:
        formatted_saves = []
        # Loop through the active saves
        for save in active_saves:
            chapter, slot = self.get_chapter_and_slot_from_save(save)
            room_id = self.get_room_id_from_save(save)
            room_id = self.fix_room_id(room_id, chapter)
            room_name = self.get_str_from_room_id(room_id, ch=chapter, slt=slot, fancy=True)
            # Format the save name
            save = f"{slot+1} {room_name}"

            formatted_saves.append(save)

        # If the listbox is being populated, add the empty saves to the listbox in slots that are empty in the right order
        if populate:
            # Loop through the slots
            for slot in range(0, 3):
                # If the slot is empty, add it to the listbox
                if f"filech{chapter}_{slot}" not in active_saves:
                    formatted_saves.insert(slot, f"{slot+1} [Empty]")
        
        return formatted_saves

    def get_chapter_and_slot_from_save(self, save_name:str) -> int:
        # Remove the "filech" from the save name
        save_name = save_name.replace("filech", "")
        # Split the save name by _
        save_name = save_name.split("_")
        # return the chapter number & slot
        return int(save_name[0]), int(save_name[1])

    def get_room_id_from_save(self, save_name:str) -> int:
        save_path = os.path.join(self.config["data"], save_name)
        # Open the save file, and read lines
        with open(save_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Get the room id from the save file, 2nd to last line
        room_id = lines[-2]
        # Remove the newline character from the room id
        room_id = room_id.replace("\n", "")
        # Convert the room id to an integer
        room_id = int(room_id)
        # Return the room id
        return room_id

    def fix_room_id(self, room_id:int, chapter:int) -> int:
        # Fix offset for chapter 1
        if chapter == 1:
            if room_id - 281 > 0:
                room_id -= 281
        
        # Effectively hard code correct room for "kris room" in chapter 2
        if chapter == 2 and room_id == 30:
            return 26
        
        # Fix offset for chapter 2
        if chapter == 2 and room_id > 10:
            room_id -= 2
        
        return room_id

    def get_str_from_room_id(self, rid:int, ch:int = 1, slt:int = 1, fancy:bool = True) -> str:
        if not os.path.exists(os.path.join(self.config["loc"], "Data")):
            os.path.mkdir(os.path.join(self.config["loc"], "Data"))
        if not os.path.exists(os.path.join(self.config["loc"], "Data", f"ch{ch}_rooms_id_to_name.json")):
            return f"{rid}"
        
        with open(os.path.join(self.config["loc"], "Data", f"ch{ch}_rooms_id_to_name.json"), "r", encoding="utf-8") as f:
            save_list = json.load(f)
        
        # Check the ids either side of the room id to see if it is a named room
        if len(save_list[rid]) == 1:
            if len(save_list[rid+1]) == 1:
                if len(save_list[rid-1]) == 1:
                    pass
                else:
                    rid -= 1
            else:
                rid += 1

        # If the room id is a named room, return the name
        if fancy: room_name = save_list[rid][1] if len(save_list[rid]) > 1 else save_list[rid][0]
        # If the room id is not a named room, return the room id
        else: room_name = save_list[rid][0]    
            
        return f"{room_name}"
