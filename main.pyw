import sys, os

# Gets the current directory that the program is running in
def get_current_dir():
    # If the program is frozen, get the directory of the executable
    if getattr(sys, 'frozen', False):
        loc = os.path.dirname(sys.executable)
        # Change the working directory to the executable directory
        os.chdir(loc)
    else:
        # Get the directory of the script
        loc = os.path.dirname(os.path.realpath(__file__))
    return loc

# Import the main window and run it
from lib.DeltaruneSaveManager import DeltaruneSaveManager

def main():
    # Create the main window
    w = DeltaruneSaveManager(get_current_dir())
    # Run the main loop
    w.mainloop()


if __name__ == "__main__":
    main()