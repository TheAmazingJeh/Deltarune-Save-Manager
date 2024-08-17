from tkinter import Frame, Listbox, Scrollbar, Spinbox, Label, Button
from tkinter import IntVar, StringVar
from tkinter.constants import N, S, W, E, END, LEFT, RIGHT, TOP, BOTTOM, ALL
from tkinter.messagebox import showerror, showwarning, askyesnocancel

from lib.popup.SettingsMenu import Settings
from lib.popup.GameTypeSelect import GameTypeSelect
from lib.popup.SaveBackupPopup import SaveBackupPopup
from lib.filemanip.LoadSave import load_save
from lib.filemanip.BackupSave import backup_save
from lib.filemanip.ConfigFile import save_config

import os, json


class ButtonsFrame(Frame):
    def __init__(self, master, config, save_frame_reference) -> None:
        super().__init__(master)
        self.master = master
        self.config = config
        self.saves_frame = save_frame_reference

        self.place_widgets()    

    def place_widgets(self) -> None:
        self.place_backup_button(0, 0)
        self.place_load_button(0, 1)
        self.place_blank(0, 2)
        self.place_launch_game_button(0, 3)
        self.place_settings_button(0, 4)

    def place_blank(self, x, y) -> None:
        blank = Label(self, text="")
        blank.grid(row=y, column=x, padx=5, sticky=W)

    def place_backup_button(self, x, y) -> None:
        self.backup_button = Button(self, text="Backup Active Save", command=self.backup_command)
        self.backup_button.grid(row=y, column=x, padx=5, sticky=W, pady=(10, 0))

    def place_load_button(self, x, y) -> None:
        self.load_button = Button(self, text="Load Save to Slot", command=self.load_command)
        self.load_button.grid(row=y, column=x, padx=5, sticky=W)

    def place_launch_game_button(self, x, y) -> None:
        self.launch_game_button = Button(self, text="Launch Game", command=self.launch_game_command)
        self.launch_game_button.grid(row=y, column=x, padx=5, sticky=W)

    def place_settings_button(self, x, y) -> None:
        self.settings_button = Button(self, text="Settings", command=self.settings_command)
        self.settings_button.grid(row=y, column=x, padx=5, sticky=W)

    def backup_command(self) -> None:
        info = self.saves_frame.get_info(include_active=True)
        print("ButtonsFrame.py", info)
        if info == False: return
        # Check if the active save slot exists (and if it doesn't, show an error because it can't be backed up)
        if info["active_exists"] == False:
            showerror("Error", "The active save slot does not exist.")
            return
        backup_path = SaveBackupPopup(self.master, self.config, info["chapter"])
        if backup_path.result == None: return
        info["backup_path"] = backup_path.result
        backup_save(info)
        self.saves_frame.refresh_active_saves(ch=info["chapter"])

    def load_command(self) -> None:
        info = self.saves_frame.get_info(include_active=True, include_backup=True)
        if info == False: return
        # Check if the active save slot exists & prompt the user to back it up if it doesn't
        if info["active_exists"] == True:
            backup_prompt = askyesnocancel("Warning", "There is already a save in the active slot. Would you like to back it up before loading?")
            if backup_prompt == None: return
            if backup_prompt == True: self.backup_command()
            else: pass
        load_save(info)
        self.saves_frame.refresh_active_saves(ch=info["chapter"])

    def launch_game_command(self) -> None:
        if "GAMETYPE" not in self.config or self.config["GAMETYPE"] == None:
            res = GameTypeSelect(self.master, self.config)
            self.config["GAMETYPE"] = res.result
            # Save the config
            save_config(self.config["loc"], self.config)
            self.master.reload_config()
        else:
            res = self.config["GAMETYPE"]
            os.system(res[1])
    
    def settings_command(self) -> None:
        Settings(self.master, self.config)
        self.master.reload_config()

    def reload_launch_button(self) -> None:
        if "GAMETYPE" not in self.config or self.config["GAMETYPE"] == None:
            self.launch_game_button.config(text="Launch Game")
        else:
            self.launch_game_button.config(text=f"Launch Game ({self.config['GAMETYPE'][0]})")