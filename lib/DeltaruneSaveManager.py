import os, sys
from tkinter import Tk, Frame, Button, Listbox, Scrollbar, StringVar, END, ACTIVE, E, W, N, S, PhotoImage
from tkinter.messagebox import  askyesnocancel, showinfo, showerror
from tkinter.simpledialog import askstring

from lib.filemanip.ConfigFile import load_config, save_config
from lib.windowmanip.SetWindowMiddle import set_window_middle
from lib.PyinstallerExeUtils import close_splash, get_icon

from lib.frames.SavesFrame import SavesFrame
from lib.frames.ButtonsFrame import ButtonsFrame


class DeltaruneSaveManager(Tk):
    def __init__(self, loc:str):
        # Initialize the window
        super().__init__()
        
        # Hide the window until it's ready to be shown
        self.withdraw()

        # Get the current directory
        self.loc = loc
        # Load the config file, and save it to a temporary variable so it can be accessed later
        self.temp_config = load_config(self.loc)

        # Set the program data
        self.program_data = {
            # Location of the Deltarune data folder that contains the active save
            "data":os.path.join(os.getenv("LOCALAPPDATA"), "DELTARUNE"),
            # Location of the folder that contains the backup saves
            "savesFolder": os.path.join(self.loc, "Saves"),
            # Constant location of the folder that contains the backup saves
            "savesFolderCONST": os.path.join(self.loc, "Saves"),
            # Location of the Deltarune executable
            "exe": self.temp_config["exe"],
            # Base path of program
            "loc": self.loc,
            # Set colours (I spelled colours the correct way)
            "colours": {
                "text":None,
                "background":None,
                "listboxSelect":"steel blue"
            }
        }
        # If the game type is in the config file, set it to the temporary gane type variable
        if "GAMETYPE" in self.temp_config:
            self.program_data["GAMETYPE"] = self.temp_config["GAMETYPE"]
        if "hideAppdata" in self.temp_config:
            self.program_data["hideAppdata"] = self.temp_config["hideAppdata"]
        
        # Delete the temporary config variable
        del self.temp_config

        save_config(self.loc, self.program_data)

        self.pre_start()
        self.create_window()
        self.reload_config()

        # Show the window
        self.deiconify()

    # Creates the window
    def create_window(self):
        # Set the window title and icon
        self.title("Save Manager")
        icon = get_icon()
        if icon[0] == "base64":
            self.wm_iconphoto(True, PhotoImage(data=icon[1]))
        elif icon[0] == "path":
            self.iconbitmap(icon[1])

        # Set the window size and make it unresizable
        set_window_middle(self, 500, 330)
        #self.resizable(False, False)

        # Set the window background colour
        self.config(bg=self.program_data["colours"]["background"])

        # Create the frames
        self.saves_frame = SavesFrame(self, self.program_data)
        self.saves_frame.pack(side="left", fill="both")

        # Create the buttons frame
        self.buttons_frame = ButtonsFrame(self, self.program_data, self.saves_frame)
        self.buttons_frame.pack(side="left", fill="both")

    # Assorted Functions that need to be run before the window is created
    def pre_start(self):
        # Checks if the data folder exists
        if not os.path.exists(self.program_data["data"]):
            # If it doesn't, show an error and exit
            close_splash()
            showerror("Error","No save file found.\nPlease make sure you have installed Deltarune & have ran it at least once.")
            sys.exit()
        # Checks if the saves folder exists
        if not os.path.exists(self.program_data["savesFolder"]):
            # If it doesn't, create it
            os.makedirs(self.program_data["savesFolder"])
        
        # Close the splash screen
        close_splash()

    def reload_config(self):
        self.program_data = load_config(self.loc)
        self.buttons_frame.reload_launch_button()
