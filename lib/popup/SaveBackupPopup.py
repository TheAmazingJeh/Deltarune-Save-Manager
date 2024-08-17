from tkinter import Tk, Listbox, Scrollbar, Frame, Entry, StringVar, Button, Menu
from tkinter.simpledialog import Dialog
from tkinter.messagebox import showerror
from tkinter.filedialog import askdirectory


import os, sys
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)


from lib.filemanip.BackupFolderNav import BackupFolderNav

def has_illegal_chars(string:str):
    illegal_chars = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
    for char in illegal_chars:
        if char in string:
            return True
    return False

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class NewFolderPopup(Dialog):
    def __init__(self, parent, config:str, current_folder, title="New Folder"):
        # Set the config
        self.config = config
        self.current_folder = current_folder
        self.entry_placeholder = "Folder Name"
        # Create a backup folder navigator

        # Initialize the dialog
        super().__init__(parent, title)

    def body(self, master):
        self.base_frame = Frame(self)
        self.entry = EntryWithPlaceholder(self.base_frame, placeholder=self.entry_placeholder)
        self.entry.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        self.base_frame.pack(side="top", fill="both", expand=True)

    def validate(self) -> bool:
        # Check if the entry is empty
        if self.entry.get() == "" or self.entry.get() == self.entry_placeholder:
            showerror("Error", "You must enter a folder name.")
            return False
        # Check if the entry has illegal characters
        if has_illegal_chars(self.entry.get()):
            showerror("Error", "You cannot use any of the following characters in a folder name: \\ / : * ? \" < > |")
            return False
        # Check if the folder already exists
        if os.path.isdir(os.path.join(self.current_folder, self.entry.get())):
            showerror("Error", "That folder already exists.")
            return False
        return True

    def apply(self):
        self.result = os.path.join(self.current_folder, self.entry.get())

class SaveBackupPopup(Dialog):
    def __init__(self, parent, config:str, chapter:int, title="Backup Save"):
        # Set the config
        self.config_ = config
        # Create a backup folder navigator
        self.backup_folder_nav = BackupFolderNav(self.config_, chapter, default_chapter=chapter)
        # Listbox select colour
        self.BACKGROUND_COL = self.config_["colours"]["listboxSelect"]
        
        # Initialize the dialog
        super().__init__(parent, title)

    def body(self, master):
        self.base_frame = Frame(self)
        self.place_path_label(self.base_frame, 0, 0)
        self.place_listbox(self.base_frame, 0, 1)
        self.base_frame.pack(side="top", fill="both", expand=True)

        self.place_menubar()

        # Update the current folder
        self.path_label_update()
        # Update the listbox
        self.update_listbox()

        # Bind double click to move to folder
        self.saves.bind("<Double-Button-1>", self.move_to_folder)
        # Bind backspace to go back a folder
        self.saves.bind("<BackSpace>", self.back_folder)

        # Bind enter to move to folder
        self.saves.bind("<Return>", self.move_to_folder)
        # Set focus to the listbox

    def place_menubar(self):
        menubar = Menu(self)
        menubar.add_command(label="Open", command=lambda: self.move_to_folder(None))
        menubar.add_command(label="Back", command=lambda: self.back_folder(None))
        menubar.add_command(label="New Folder", command=lambda: self.new_folder(None))
        self.config(menu=menubar)


    def buttonbox(self):
        '''
        Overriding the buttonbox method to remove focus & bind enter to the ok button
        '''

        box = Frame(self)

        self.fnm_entry = EntryWithPlaceholder(box, width=45, placeholder="Backup Name")
        self.fnm_entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        box2 = Frame(box)

        ok_button = Button(box2, text="OK", width=8, command=self.ok)
        ok_button.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        cl_button = Button(box2, text="Cancel", width=8, command=self.cancel)
        cl_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        

        self.bind("<Escape>", self.cancel)

        box2.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="e")
        box.pack()

    def validate(self) -> bool:
        # Check if there is a name in the entry
        if self.fnm_entry.get() == "":
            showerror("Error", "You must enter a name for the backup.")
            return False
        # Check if the name has illegal characters
        if has_illegal_chars(self.fnm_entry.get()):
            showerror("Error", "You cannot use any of the following characters in a backup name: \\ / : * ? \" < > |")
            return False
    
        # Check if the folder already exists
        if os.path.isdir(os.path.join(self.backup_folder_nav.current_folder, self.fnm_entry.get())):
            showerror("Error", "That save already exists.")
            return False
        
        return True

    def apply(self):
        # Check if there is a selection
        if len(self.saves.curselection()) == 1:
            # Get the selected index
            index = self.saves.curselection()[0]
            # Move to the folder
            self.backup_folder_nav.move_to_folder_index(index)
        # Get the name of the backup
        self.result = os.path.join(self.backup_folder_nav.current_folder, self.fnm_entry.get())

    def place_path_label(self, frame, x, y):
        # Make frame
        self.path_label_frame = Frame(frame)
        # Make label, as an entry
        self.path_label = Entry(self.path_label_frame, width=50, state="disabled")
        # Make stringvar and bind it to the entry
        self.path_label_var = StringVar(value="Waiting for update...")
        self.path_label.config(textvariable=self.path_label_var)
        # Pack label
        self.path_label.pack(side="left", fill="both", expand=True)
        # Pack frame
        self.path_label_frame.grid(row=y, column=x, sticky="w", padx=(6,0), pady=(5, 0))

    def place_listbox(self, frame, x, y):
        # Make frame
        self.list_box_frame = Frame(frame)
        # Make listbox
        self.saves = Listbox(self.list_box_frame, selectmode="single", width=50, exportselection=False, selectbackground=self.BACKGROUND_COL)
        self.saves.pack(side="left", fill="both", expand=True)
        # Make scrollbar
        self.saves_scrollbar = Scrollbar(self.list_box_frame)
        self.saves_scrollbar.pack(side="right", fill="y", padx=(0, 5))
        # Configure scrollbar
        self.saves.config(yscrollcommand=self.saves_scrollbar.set)
        self.saves_scrollbar.config(command=self.saves.yview)
        # Pack frame
        self.list_box_frame.grid(row=y, column=x, sticky="w", padx=(5, 0), pady=(5, 0))

    def update_listbox(self):
        self.saves.delete(0, "end")
        for save in self.backup_folder_nav.get_folder_contents(self.backup_folder_nav.current_folder)["folders"]:
            self.saves.insert("end", save)

    def path_label_update(self):
        self.path_label_var.set(str(self.backup_folder_nav.current_folder.replace(self.config_["loc"],"").replace("\\Saves", "Saves:\\", 1)))

    def place_current_directory(self):
        pass

    def move_to_folder(self, event):
        # Check if there is a selection
        if len(self.saves.curselection()) == 0:
            return
        # Check if there is more than one selection
        if len(self.saves.curselection()) > 1:
            showerror("Error", "You can only select one folder at a time.")
        # Get the selected index
        index = self.saves.curselection()[0]
        # Move to the folder
        self.backup_folder_nav.move_to_folder_index(index)
        # Update the listbox
        self.update_listbox()
        # Update the path label
        self.path_label_update()
    
    def back_folder(self, event):
        # Go back a folder
        self.backup_folder_nav.back_folder()
        # Update the listbox
        self.update_listbox()
        # Update the path label
        self.path_label_update()

    def new_folder(self, event):
        new_folder_popup = NewFolderPopup(self, self.config, self.backup_folder_nav.current_folder)
        if new_folder_popup.result != None:
            # Make the folder
            os.mkdir(new_folder_popup.result)
            # Update the listbox
            self.update_listbox()

if __name__ == "__main__":
    # Create the main window
    


    #try:

    example_config = {
        "savesFolderCONST": r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager\Saves",
        "loc": r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager",
        "colours": {
            "text":None,
            "background":None,
            "listboxSelect":"steel blue"
        }
    }

    w = SaveBackupPopup(Tk(), example_config, 2)
    print(w.result)

    #except TclError as e:
    #    print(e)