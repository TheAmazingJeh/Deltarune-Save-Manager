import configparser, os

class CaseSensitiveConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

class IniParser:
    def __init__(self, file, chapter, slot):
        self.chapter = chapter
        self.slot = slot
        self.file = file
        self.config = CaseSensitiveConfigParser()
        self.config.read(file)

    
    def read_ini_file(self) -> dict:
        # Read the ini file
        config = CaseSensitiveConfigParser()
        config.read(self.file)
        # Get the sections
        sections = config.sections()
        # Create a dictionary for the sections
        sections_dict = {}
        # Loop through the sections
        for section in sections:
            # Get the options for the section
            options = config.options(section)
            # Create a dictionary for the options
            options_dict = {}
            # Loop through the options
            for option in options:
                # Get the value for the option
                value = config.get(section, option)
                # Add the option to the options dictionary
                options_dict[option] = value
            # Add the options dictionary to the sections dictionary
            sections_dict[section] = options_dict
        # Return the sections dictionary
        return sections_dict

    def create_ini_key(self, chapter:int, slot:int) -> str:
        if chapter == 1:
            return f"G{slot}"
        else:
            return f"G_{chapter}_{slot}"
            

    def duplicate_to(self, fileout, chapter:int=None, slot=0):
        # If no chapter is specified, use the current chapter
        if chapter == None: chapter = self.chapter
        # Create the ini key for the chapter and slot
        ini_key = self.create_ini_key(self.chapter, self.slot)
        # Read the specified chapter and slot
        data = self.read_ini_file()[ini_key]
        # Create a new ini file
        config = CaseSensitiveConfigParser()
        # Add the data to the new ini file
        config[self.create_ini_key(chapter, slot)] = data
        # Check if the file exists
        if not os.path.exists(fileout):
            # If it doesn't, create it
            open(fileout, "w").close()

        # If the file has data in it, read it
        if os.path.getsize(fileout) > 0:
            config.read(fileout)
        # Write the new ini file with the new data added
        with open(fileout, "w") as f:
            config.write(f)

if __name__ == "__main__":
    ini = IniParser(r"C:\Users\joehb\AppData\Local\DELTARUNE\dr.ini", 1, 1)
    ini.duplicate_to(r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager\paste.ini", slot=1)