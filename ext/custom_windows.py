import os, json, sys
from tkinter import *
import tkinter.simpledialog 
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askopenfilename
from datetime import datetime

if getattr(sys, 'frozen', False):
    exec(f"import pyi_splash as splash")
    loc = os.path.dirname(sys.executable)
    os.chdir(loc)
else:
    loc = os.path.dirname(os.path.realpath(__file__)).replace("\\ext","")

with open(loc+'\\data.json') as json_file:
    vars = json.load(json_file)

BACKSLASH = "\\"

def rename_save(save_name,chapter):
    if save_name == "": save_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if os.path.exists(loc+f"\\Saves\\CH{str(chapter)}\\"+save_name):
        if save_name[-2].isnumeric(): save_name = f"{save_name[:-2]}{int(save_name[-2])+1})"
        else: save_name = f"{save_name} (1)"
    else: return save_name
    print(save_name)
    return rename_save(save_name,chapter)

location_data = {
    "exe":"C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNEdemo",
    "data":os.getenv("LOCALAPPDATA")+"\\DELTARUNE",
    # 100 Spelling mistakes below :)
    "chapter1rooms":['Dogcheck','ROOM_INITIALIZE', 'room_krisroom', 'room_krishallway', 'room_torroom', 'room_torhouse', 'room_torbathroom', 'room_town_krisyard', 'room_town_northwest', 'room_town_north', 'room_beach', 'room_town_mid', 'room_town_apartments', 'room_town_south', 'room_town_school', 'room_town_church', 'room_graveyard', 'room_town_shelter', 'room_hospital_lobby', 'room_hospital_hallway', 'room_hospital_rudy', 'room_hospital_room', 'room_diner', 'room_townhall', 'room_flowershop_f', 'room_flowershop_f', 'room_library', 'room_alphysalley', 'room_torielclass', 'room_schoollobby', 'room_alphysclass', 'room_schooldoor', 'room_insidecloset', 'room_school_unusedroom', 'room_dark', 'room_darka', 'room_dark', 'room_dark', 'room_darka', 'room_dark_wobbles', 'room_dark_eyepuzzle', 'room_dark', 'room_dark_chase', 'room_dark_chase', 'room_castle_outskirts', 'room_castle_town', 'room_castle_front', 'room_castle_tutorial', 'room_castle_darkdoor', 'room_field_start', 'room_field_forest', 'room_field', 'room_field', 'room_fieldA', 'room_field_topchef', 'room_field_puzzle', 'room_field_maze', 'room_field_puzzle', 'room_field_getsusie', 'room_field_shop', 'room_field_puzzletutorial', 'room_field', 'room_field_boxpuzzle', 'room_field', 'room_field_secret', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers','room_field_checkersboss', 'room_forest_savepoint', 'room_forest_area', 'room_forest_area', 'room_forest_area', 'room_forest_areaA', 'room_forest_puzzle', 'room_forest_beforeclover', 'room_forest_areaA', 'room_forest_area', 'room_forest_savepoint', 'room_forest_smith', 'room_forest_area', 'room_forest_dancers', 'room_forest_sroom_forest_maze', 'room_forest_maze_deadend', 'room_forest_maze_susie', 'room_forest_maze', 'room_forest_maze_deadend', 'room_forest_savepoint', 'room_forest_fightsusie', 'room_forest_afterthrash', 'room_forest_afterthrash', 'room_forest_afterthrash', 'room_forest_castleview', 'room_forest_chase', 'room_forest_chase', 'room_forest_castlefront', 'room_cc_prison_cells', 'room_cc_prisonlancer', 'room_cc_prison_to_elevator', 'room_cc_prison', 'room_cc_prisonelevator', 'room_cc_elevator', 'room_cc_prison_prejoker', 'room_cc_joker', 'room_cc_entrance','room_cc_f', 'room_cc_rurus', 'room_cc_clover', 'room_cc_f', 'room_cc_lancer', 'room_cc_f', 'room_cc_throneroom', 'room_cc_preroof', 'room_cc_kingbattle', 'room_cc_prefountain', 'room_cc_fountain', 'room_legend', 'room_shop', 'room_shop', 'room_gameover', 'room_myroom_dark', 'room_dark', 'room_ed', 'room_empty', 'room_man', 'room_DARKempty', 'room_battletest'],
    "chapter2rooms":["PLACE_DOGCHECK2","room_intro_ch2","room_dw_mansion_fountain","room_dw_mansion_prefountain","room_debug_choicer_light","room_debug_smallface","room_debug_battleBalloon","room_debug_smallface_dark","room_debug_choicer_dark","room_gms_debug_failsafe","room_INITIALIZE","room_title_PLACEholder","room_battletest","room_cutscene_tester","room_sound_tester","room_sprite_tester","room_gif_tester","room_bullettest","room_teacup_demoauto","room_teacup_demobullets","room_shaun_puzzle","room_GMS2_test","room_cutscene_tester_b","room_debug_color","room_debug_battle","room_debug_loc","PLACE_CONTACT","room_kris","room","room_krishallway","room_tor","room","room_torhouse","room_torbath","room","room_town_krisyard","room_town_northwest","room_town_north","room_beach","room_town_mid","room_town_apartments","room_town_south","room_town_school","room_town_church","room_graveyard","room_town_shelter","room_hospital_lobby","room_hospital_hallway","room_hospital_rudy","room_hospital_","room2","room_diner","room_townhall","room_flowershop_1f","room_flowershop_2f","room_library","room_alphysalley","room_lw_computer_lab","room_lw_library_upstairs","room_lw_police","room_lw_conbini","room_lw_icee_pizza","room_torielclass","room_schoollobby","room_alphysclass","room_schooldoor","room_insidecloset","room_school_unused","room","room_castle_town","room_castle_tutorial","room_dw_castle_west_cliff_old","room_dw_castle_east_door","room_dw_castle_west_cliff","room_dw_castle_area_1","room_dw_castle_area_2","room_dw_castle_area_2_transformed","room_dw_ralsei_castle_front","room_dw_castle_restaurant","room_dw_castle_cafe","room_dw_castle_dojo","room_dw_ralsei_castle_1f","room_dw_ralsei_castle_2f","room_dw_castle_dungeon","room_dw_castle_","rooms_hallway","room_dw_castle_","rooms_kris","room_dw_castle_","rooms_susie","room_dw_castle_","rooms_lancer","room_dw_cyber_intro_1","room_dw_cyber_intro_connector","room_dw_cyber_intro_2","room_dw_cyber_rhythm_slide","room_dw_cyber_savepoint","room_dw_cyber_battle_maze_1","room_dw_cyber_music_bullet","room_dw_cyber_tasque_battle","room_dw_cyber_keyboard_puzzle_1","room_dw_cyber_queen_boxing","room_dw_cyber_musical_door","room_dw_cyber_maze_virokun","room_dw_cyber_keyboard_puzzle_2","room_dw_cyber_battle_maze_2","room_dw_cyber_music_final","room_dw_cyber_musical_shop","room_dw_cyber_teacup_final","room_dw_cyber_rollercoaster","room_dw_cyber_maze_fireworks","room_dw_cyber_maze_tasque","room_dw_cyber_maze_queenscreen","room_dw_cyber_viro_ring","room_dw_cyber_post_music_boss_slide","room_dw_cyber_keyboard_puzzle_3","room_dw_cyber_battle_maze_3","room_dw_cyber_teacup_2","room_dw_cyber_shaunsmusicalbullettunnel","room_dw_cyber_maze_rhythm","room_dw_cyber_escalator_slide","room_dw_cyber_nuberts_treasure","room_dw_cyber_music_fight","room_dw_cyber_keyboardexample","room_dw_city_prototype_01","room_dw_city_prototype_02","room_dw_city_spamton_shop_exterior","room_dw_city_spamton_house","room_dw_city_intro","room_dw_city_split","room_dw_city_entrance","room_dw_city_traffic_1","room_dw_city_roadblock","room_dw_city_hacker","room_dw_city_mice","room_dw_city_big_1","room_dw_city_traffic_2","room_dw_city_big_2","room_dw_city_queen_drunk","room_dw_city_savepoint","room_dw_city_big_3","room_dw_city_traffic_3","room_dw_city_mice2","room_dw_city_cheesemaze","room_dw_city_mice3","room_dw_city_poppup","room_dw_city_berdly","room_dw_city_traffic_4","room_dw_city_spamton_alley","room_dw_city_monologue","room_dw_city_baseball","room_dw_city_postbaseball_1","room_dw_city_postbaseball_2","room_dw_city_postbaseball_3","room_dw_city_mansion_front","room_dw_city_susie_ralsei_fun_1","room_dw_city_mirrorfriend","room_dw_city_treasure","room_dw_city_dog_traffic","room_dw_city_man","room_dw_city_moss","room_dw_city_big_3_backup_2exits","room_dw_city_traffic_3_2Entrances","room_dw_city_cheese","room_dw_city_carnival","room_dw_city_noelle_fight_intro","room_dw_city_spamton_shop_interior","room_dw_city_monologue_old","room_dw_mansion_kris","room","room_dw_mansion_susie","room","room_dw_mansion_lightner_hallway","room_dw_mansion_darkbulb_1","room_dw_mansion_darkbulb_2","room_dw_mansion_darkbulb_3","room_dw_mansion_dining_a","room_dw_mansion_entrance","room_dw_mansion_fire_paintings","room_dw_mansion_single_pot","room_dw_mansion_potBalance","room_dw_mansion_tasquePaintings","room_dw_mansion_traffic","room_dw_mansion_east_1f_e","room_dw_mansion_east_1f_secret","room_dw_mansion_east_teacup","room_dw_mansion_east_teacup_4","room_dw_mansion_east_teacup_3","room_dw_mansion_east_teacup_2","room_dw_mansion_b_entrance","room_dw_mansion_b_stairs","room_dw_mansion_b_central","room_dw_mansion_b_west_1f","room_dw_mansion_b_west_1f_a","room_dw_mansion_b_west_1f_b","room_dw_mansion_b_west_2f","room_dw_mansion_b_east","room_dw_mansion_b_east_a","room_dw_mansion_b_east_b","room_dw_mansion_b_east_transformed","room_dw_mansion_east_2f_a","room_dw_mansion_east_2f_transformed_new","room_dw_mansion_east_2f_shortcut","room_dw_mansion_kitchen","room_dw_mansion_east_2f_c","room_dw_mansion_east_2f_c_a","room_dw_mansion_east_2f_d","room_dw_mansion_east_3f","room_dw_mansion_east_3f_projection","room_dw_mansion_east_3f_toilet","room_dw_mansion_acid_tunnel","room_dw_mansion_acid_tunnel_puzzle_entrance","room_dw_mansion_acid_tunnel_loop_rouxls","room_dw_mansion_acid_tunnel_exit","room_dw_mansion_east_4f_b","room_dw_mansion_east_4f_c","room_dw_mansion_east_4f_d","room_dw_mansion_top","room_dw_mansion_top_post","room_dw_mansion_ferris_wheel","room_dw_mansion_ferris_wheel_post","room_dw_mansion_noelle_","room","room_dw_mansion_bridges","room_dw_mansion_bridges_funny","room_dw_mansion_mouseLottery","room_dw_mansion_hands","room_dw_mansion_dining3","room_dw_mansion_dininghall","room_dw_mansion_dining_storage","room_dw_mansion_east_1f_b","room_dw_mansion_east_2f_c_b","room_dw_mansion_traffic_original","room_dw_mansion_east_1f_a","room_dw_mansion_east_2f_teacup","room_dw_mansion_east_4f_e","room_dw_mansion_east_4f_a","room_dw_mansion_east_2f_ufo_old","room_dw_mansion_east_1f_d","room_dw_mansion_east_1f_c","room_dw_mansion_sparks","room_dw_mansion_acid_tunnel_old","room_dw_mansion_top_post_old","room_dw_mansion_elevator","PLACE_DOG","room_legend","room_legend_neo","room_shop1","room_shop_ch2_music","room_shop_ch2_swatch","room_shop_ch2_spamton","room_gameover","PLACE_LOGO","PLACE_FAILURE","PLACE_NAMING_JIKKEN","PLACE_MENU","room_ed","room_empty","room_DARKempty","room_DARKbase_GMS2","room_dw_cyber_battle_maze_2_old","room_dw_cyber_keyboard_puzzle_1_old","room_dw_cyber_tasque_battle_og","room_dw_cyber_savepoint_original","room_dw_cyber_battle_maze_1_Original","room_dw_cyber_music_bullet_original","room_dw_cyber_maze_virokun_backuo","room_dw_cyber_battle_maze_2_toby","room_dw_city_big_1_original","room_dw_city_traffic_2_old","room_dw_city_big_2_OG","room_dw_city_mice2_og","room_dw_mansion_east_teacup_4_old","room_dw_cyber_teacup_1","room_dw_cyber_viromaze2","room_dw_city_traffic_5_old","room_dw_mansion_dining_storage_old","room_dw_cyber_virovirokun_fight","room_dw_mansion_east_2f_d_backup","room_dw_city_traffic_3_backup","room_cc_lancer","room_cc_clover","room_cc_fountain","room_dw_city_big_3_og","room_dw_mansion_bridgesold","room_dw_city_sidewayscars","room_transformation_sequence","room_dw_mansion_gigaqueen"]
}


class BackupSave(tkinter.simpledialog.Dialog):
    def body(self, master):
        Label(master, text="File Name:").grid(row=0)
        self.chapterSelect = Entry(master)
        self.chapterSelect.grid(row=0, column=1)

        Label(master, text="Chapter").grid(row=1)
        self.e2 = Spinbox(master, from_=1, to=vars['MAXCHAPTER'], wrap=True)
        self.e2.grid(row=1, column=1)

        Label(master, text="Slot:").grid(row=2)
        self.e3 = Spinbox(master, from_=1, to=vars['MAXSLOT'], wrap=True)
        self.e3.grid(row=2, column=1)

        return

    def apply(self):
        chapterNum = int(self.e2.get())
        chapterNum = 1 if chapterNum == 0 else chapterNum
        chapterNum = vars['MAXCHAPTER'] if chapterNum >= vars['MAXCHAPTER'] else chapterNum

        slotNum = int(self.e3.get())
        slotNum = 1 if slotNum == 0 else slotNum                              # Fix silly user input 0
        slotNum = vars['MAXSLOT'] if slotNum >= vars['MAXSLOT'] else slotNum
        saveName = self.chapterSelect.get()
        saveName = rename_save(saveName,slotNum)
        # Returns the new name (always valid), the chapter and the slot
        self.result = [saveName, chapterNum, slotNum]

class WriteSave(tkinter.simpledialog.Dialog):
    def update_saves(self, chapter):
        global writeChapter, writeSlot
        folder = loc+f"\\Saves\\CH{str(chapter)}"
        if not os.path.exists(folder):
            return []
        save_names = [ f.path.replace(loc+f"\\Saves\\CH{str(chapter)}\\","") for f in os.scandir(folder) if f.is_dir() ]
        writeChapter = chapter
        self.listbox.delete(0,END)
        for items in save_names:
            self.listbox.insert(END,items)
        self.listbox.selection_set(0)

    def GetSelectedSave(self):
        return str((self.listbox.get(ACTIVE)))
    def body(self, master):
        global writeChapter, writeSlot
        writeChapter = 1
        writeSlot = 1

        Label(master, text="Show chapter").grid(row=0)
        self.chapterSelect = Spinbox(master, from_=1, to=vars['MAXCHAPTER'], wrap=True, command=lambda: self.update_saves(self.chapterSelect.get()))
        self.chapterSelect.grid(row=0, column=1)    
        self.listbox_frame = Frame(master)
        self.listbox_frame.grid(row=1, column=0, columnspan=2)

        self.listbox = Listbox(self.listbox_frame, height=5, width=30)
        self.listbox.pack(side=LEFT, fill=BOTH)

        self.scrollbar = Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)

        Label(master, text="Load to slot:").grid(row=2)
        self.slotSelect = Spinbox(master, from_=1, to=vars['MAXSLOT'], wrap=True)
        self.slotSelect.grid(row=2, column=1)
        
        self.update_saves(1)
        self.resizable(False, False)
        return

    def apply(self):
        global writeChapter, writeSlot
        writeSlot = self.slotSelect.get()
        writeSlot = int(self.slotSelect.get())
        writeSlot = 1 if writeSlot == 0 else writeSlot
        writeSlot = vars['MAXSLOT'] if writeSlot >= vars['MAXSLOT'] else writeSlot

        self.result = [self.GetSelectedSave(), writeChapter, writeSlot]
        return

class GameTypeSelect(tkinter.simpledialog.Dialog):
    def sel(self):
        match self.radioVar.get():
            case 1: self.file_select.config(state=DISABLED), self.file_label_truncated.config(state=DISABLED)
            case 2: self.file_select.config(state=NORMAL), self.file_label_truncated.config(state=DISABLED)
    def select_file(self):
        self.fileName = askopenfilename(initialdir="C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNEdemo", filetypes=[("Executable", "*.exe")])
        self.file_string_truncated.set("..."+self.fileName[-32:])
    def body(self, master):
        self.minsize(width=250, height=100)
        self.fileName = ""
        Label(master,text="Please select an option.").grid(sticky=W)

        self.radioVar = IntVar()
        self.r1 = Radiobutton(master, text="Open By Using Steam Link", variable=self.radioVar, value=1,command=self.sel)
        self.r1.grid(row=1, sticky=W)

        self.r2 = Radiobutton(master, text="Open By Directly Running File", variable=self.radioVar, value=2,command=self.sel)
        self.r2.grid(row=2, sticky=W)
        self.file_select = Button(master, text="Select File", command=self.select_file)
        self.file_select.grid(row=2,column=1, sticky=W)

        self.file_string_truncated = StringVar()
        self.file_label_truncated = Entry(master, textvariable=self.file_string_truncated, width=40)
        self.file_label_truncated.grid(row=3,column=0, columnspan=2,sticky=W, pady=5)

        self.r1.invoke()
        return
    
    def apply(self):
        match self.radioVar.get():
            case 1: self.result = ["Steam","start \"\" steam://rungameid/1690940"]
            case 2: self.fileName = f'explorer.exe "{loc.replace(BACKSLASH,"/")}"' if self.fileName == "" else f'"{self.fileName}"'; self.result = ["Direct",self.fileName]
        return

class Settings(tkinter.simpledialog.Dialog):
    def reset_game_launch(self):
        if "GAMETYPE" in vars:
            del vars["GAMETYPE"]
            with open(loc+'\\data.json', 'w') as f:
                json.dump(vars, f, indent=4)
        return
    def body(self, master):
        self.minsize(width=250, height=10)
        Button(master, text="Reset Game Launch Type", command=self.reset_game_launch).grid(row=0)
        Button(master, text="Open Deltarune Saves Folder", command=lambda: os.system(f"explorer.exe {location_data['data']}")).grid(row=1)
        return
    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="Back", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()


if __name__ == "__main__":
    w = Tk()
    w.title("Test Window")
    d = BackupSave(w)
    print(d.result)

