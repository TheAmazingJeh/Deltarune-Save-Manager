import os, configparser
config = configparser.ConfigParser()
config.optionxform=str

loc = os.path.dirname(os.path.realpath(__file__))
location_data = {
    "exe":"C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNEdemo",
    "data":os.getenv("LOCALAPPDATA")+"\\DELTARUNE",
    "chapter1rooms":['not_a_room','ROOM_INITIALIZE', 'room_krisroom', 'room_krishallway', 'room_torroom', 'room_torhouse', 'room_torbathroom', 'room_town_krisyard', 'room_town_northwest', 'room_town_north', 'room_beach', 'room_town_mid', 'room_town_apartments', 'room_town_south', 'room_town_school', 'room_town_church', 'room_graveyard', 'room_town_shelter', 'room_hospital_lobby', 'room_hospital_hallway', 'room_hospital_rudy', 'room_hospital_room', 'room_diner', 'room_townhall', 'room_flowershop_f', 'room_flowershop_f', 'room_library', 'room_alphysalley', 'room_torielclass', 'room_schoollobby', 'room_alphysclass', 'room_schooldoor', 'room_insidecloset', 'room_school_unusedroom', 'room_dark', 'room_darka', 'room_dark', 'room_dark', 'room_darka', 'room_dark_wobbles', 'room_dark_eyepuzzle', 'room_dark', 'room_dark_chase', 'room_dark_chase', 'room_castle_outskirts', 'room_castle_town', 'room_castle_front', 'room_castle_tutorial', 'room_castle_darkdoor', 'room_field_start', 'room_field_forest', 'room_field', 'room_field', 'room_fieldA', 'room_field_topchef', 'room_field_puzzle', 'room_field_maze', 'room_field_puzzle', 'room_field_getsusie', 'room_field_shop', 'room_field_puzzletutorial', 'room_field', 'room_field_boxpuzzle', 'room_field', 'room_field_secret', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers', 'room_field_checkers','room_field_checkersboss', 'room_forest_savepoint', 'room_forest_area', 'room_forest_area', 'room_forest_area', 'room_forest_areaA', 'room_forest_puzzle', 'room_forest_beforeclover', 'room_forest_areaA', 'room_forest_area', 'room_forest_savepoint', 'room_forest_smith', 'room_forest_area', 'room_forest_dancers', 'room_forest_sroom_forest_maze', 'room_forest_maze_deadend', 'room_forest_maze_susie', 'room_forest_maze', 'room_forest_maze_deadend', 'room_forest_savepoint', 'room_forest_fightsusie', 'room_forest_afterthrash', 'room_forest_afterthrash', 'room_forest_afterthrash', 'room_forest_castleview', 'room_forest_chase', 'room_forest_chase', 'room_forest_castlefront', 'room_cc_prison_cells', 'room_cc_prisonlancer', 'room_cc_prison_to_elevator', 'room_cc_prison', 'room_cc_prisonelevator', 'room_cc_elevator', 'room_cc_prison_prejoker', 'room_cc_joker', 'room_cc_entrance','room_cc_f', 'room_cc_rurus', 'room_cc_clover', 'room_cc_f', 'room_cc_lancer', 'room_cc_f', 'room_cc_throneroom', 'room_cc_preroof', 'room_cc_kingbattle', 'room_cc_prefountain', 'room_cc_fountain', 'room_legend', 'room_shop', 'room_shop', 'room_gameover', 'room_myroom_dark', 'room_dark', 'room_ed', 'room_empty', 'room_man', 'room_DARKempty', 'room_battletest'],
    "chapter2rooms":["PLACE_DOGCHECK2","room_intro_ch2","room_dw_mansion_fountain","room_dw_mansion_prefountain","room_debug_choicer_light","room_debug_smallface","room_debug_battleBalloon","room_debug_smallface_dark","room_debug_choicer_dark","room_gms_debug_failsafe","room_INITIALIZE","room_title_PLACEholder","room_battletest","room_cutscene_tester","room_sound_tester","room_sprite_tester","room_gif_tester","room_bullettest","room_teacup_demoauto","room_teacup_demobullets","room_shaun_puzzle","room_GMS2_test","room_cutscene_tester_b","room_debug_color","room_debug_battle","room_debug_loc","PLACE_CONTACT","room_kris","room","room_krishallway","room_tor","room","room_torhouse","room_torbath","room","room_town_krisyard","room_town_northwest","room_town_north","room_beach","room_town_mid","room_town_apartments","room_town_south","room_town_school","room_town_church","room_graveyard","room_town_shelter","room_hospital_lobby","room_hospital_hallway","room_hospital_rudy","room_hospital_","room2","room_diner","room_townhall","room_flowershop_1f","room_flowershop_2f","room_library","room_alphysalley","room_lw_computer_lab","room_lw_library_upstairs","room_lw_police","room_lw_conbini","room_lw_icee_pizza","room_torielclass","room_schoollobby","room_alphysclass","room_schooldoor","room_insidecloset","room_school_unused","room","room_castle_town","room_castle_tutorial","room_dw_castle_west_cliff_old","room_dw_castle_east_door","room_dw_castle_west_cliff","room_dw_castle_area_1","room_dw_castle_area_2","room_dw_castle_area_2_transformed","room_dw_ralsei_castle_front","room_dw_castle_restaurant","room_dw_castle_cafe","room_dw_castle_dojo","room_dw_ralsei_castle_1f","room_dw_ralsei_castle_2f","room_dw_castle_dungeon","room_dw_castle_","rooms_hallway","room_dw_castle_","rooms_kris","room_dw_castle_","rooms_susie","room_dw_castle_","rooms_lancer","room_dw_cyber_intro_1","room_dw_cyber_intro_connector","room_dw_cyber_intro_2","room_dw_cyber_rhythm_slide","room_dw_cyber_savepoint","room_dw_cyber_battle_maze_1","room_dw_cyber_music_bullet","room_dw_cyber_tasque_battle","room_dw_cyber_keyboard_puzzle_1","room_dw_cyber_queen_boxing","room_dw_cyber_musical_door","room_dw_cyber_maze_virokun","room_dw_cyber_keyboard_puzzle_2","room_dw_cyber_battle_maze_2","room_dw_cyber_music_final","room_dw_cyber_musical_shop","room_dw_cyber_teacup_final","room_dw_cyber_rollercoaster","room_dw_cyber_maze_fireworks","room_dw_cyber_maze_tasque","room_dw_cyber_maze_queenscreen","room_dw_cyber_viro_ring","room_dw_cyber_post_music_boss_slide","room_dw_cyber_keyboard_puzzle_3","room_dw_cyber_battle_maze_3","room_dw_cyber_teacup_2","room_dw_cyber_shaunsmusicalbullettunnel","room_dw_cyber_maze_rhythm","room_dw_cyber_escalator_slide","room_dw_cyber_nuberts_treasure","room_dw_cyber_music_fight","room_dw_cyber_keyboardexample","room_dw_city_prototype_01","room_dw_city_prototype_02","room_dw_city_spamton_shop_exterior","room_dw_city_spamton_house","room_dw_city_intro","room_dw_city_split","room_dw_city_entrance","room_dw_city_traffic_1","room_dw_city_roadblock","room_dw_city_hacker","room_dw_city_mice","room_dw_city_big_1","room_dw_city_traffic_2","room_dw_city_big_2","room_dw_city_queen_drunk","room_dw_city_savepoint","room_dw_city_big_3","room_dw_city_traffic_3","room_dw_city_mice2","room_dw_city_cheesemaze","room_dw_city_mice3","room_dw_city_poppup","room_dw_city_berdly","room_dw_city_traffic_4","room_dw_city_spamton_alley","room_dw_city_monologue","room_dw_city_baseball","room_dw_city_postbaseball_1","room_dw_city_postbaseball_2","room_dw_city_postbaseball_3","room_dw_city_mansion_front","room_dw_city_susie_ralsei_fun_1","room_dw_city_mirrorfriend","room_dw_city_treasure","room_dw_city_dog_traffic","room_dw_city_man","room_dw_city_moss","room_dw_city_big_3_backup_2exits","room_dw_city_traffic_3_2Entrances","room_dw_city_cheese","room_dw_city_carnival","room_dw_city_noelle_fight_intro","room_dw_city_spamton_shop_interior","room_dw_city_monologue_old","room_dw_mansion_kris","room","room_dw_mansion_susie","room","room_dw_mansion_lightner_hallway","room_dw_mansion_darkbulb_1","room_dw_mansion_darkbulb_2","room_dw_mansion_darkbulb_3","room_dw_mansion_dining_a","room_dw_mansion_entrance","room_dw_mansion_fire_paintings","room_dw_mansion_single_pot","room_dw_mansion_potBalance","room_dw_mansion_tasquePaintings","room_dw_mansion_traffic","room_dw_mansion_east_1f_e","room_dw_mansion_east_1f_secret","room_dw_mansion_east_teacup","room_dw_mansion_east_teacup_4","room_dw_mansion_east_teacup_3","room_dw_mansion_east_teacup_2","room_dw_mansion_b_entrance","room_dw_mansion_b_stairs","room_dw_mansion_b_central","room_dw_mansion_b_west_1f","room_dw_mansion_b_west_1f_a","room_dw_mansion_b_west_1f_b","room_dw_mansion_b_west_2f","room_dw_mansion_b_east","room_dw_mansion_b_east_a","room_dw_mansion_b_east_b","room_dw_mansion_b_east_transformed","room_dw_mansion_east_2f_a","room_dw_mansion_east_2f_transformed_new","room_dw_mansion_east_2f_shortcut","room_dw_mansion_kitchen","room_dw_mansion_east_2f_c","room_dw_mansion_east_2f_c_a","room_dw_mansion_east_2f_d","room_dw_mansion_east_3f","room_dw_mansion_east_3f_projection","room_dw_mansion_east_3f_toilet","room_dw_mansion_acid_tunnel","room_dw_mansion_acid_tunnel_puzzle_entrance","room_dw_mansion_acid_tunnel_loop_rouxls","room_dw_mansion_acid_tunnel_exit","room_dw_mansion_east_4f_b","room_dw_mansion_east_4f_c","room_dw_mansion_east_4f_d","room_dw_mansion_top","room_dw_mansion_top_post","room_dw_mansion_ferris_wheel","room_dw_mansion_ferris_wheel_post","room_dw_mansion_noelle_","room","room_dw_mansion_bridges","room_dw_mansion_bridges_funny","room_dw_mansion_mouseLottery","room_dw_mansion_hands","room_dw_mansion_dining3","room_dw_mansion_dininghall","room_dw_mansion_dining_storage","room_dw_mansion_east_1f_b","room_dw_mansion_east_2f_c_b","room_dw_mansion_traffic_original","room_dw_mansion_east_1f_a","room_dw_mansion_east_2f_teacup","room_dw_mansion_east_4f_e","room_dw_mansion_east_4f_a","room_dw_mansion_east_2f_ufo_old","room_dw_mansion_east_1f_d","room_dw_mansion_east_1f_c","room_dw_mansion_sparks","room_dw_mansion_acid_tunnel_old","room_dw_mansion_top_post_old","room_dw_mansion_elevator","PLACE_DOG","room_legend","room_legend_neo","room_shop1","room_shop_ch2_music","room_shop_ch2_swatch","room_shop_ch2_spamton","room_gameover","PLACE_LOGO","PLACE_FAILURE","PLACE_NAMING_JIKKEN","PLACE_MENU","room_ed","room_empty","room_DARKempty","room_DARKbase_GMS2","room_dw_cyber_battle_maze_2_old","room_dw_cyber_keyboard_puzzle_1_old","room_dw_cyber_tasque_battle_og","room_dw_cyber_savepoint_original","room_dw_cyber_battle_maze_1_Original","room_dw_cyber_music_bullet_original","room_dw_cyber_maze_virokun_backuo","room_dw_cyber_battle_maze_2_toby","room_dw_city_big_1_original","room_dw_city_traffic_2_old","room_dw_city_big_2_OG","room_dw_city_mice2_og","room_dw_mansion_east_teacup_4_old","room_dw_cyber_teacup_1","room_dw_cyber_viromaze2","room_dw_city_traffic_5_old","room_dw_mansion_dining_storage_old","room_dw_cyber_virovirokun_fight","room_dw_mansion_east_2f_d_backup","room_dw_city_traffic_3_backup","room_cc_lancer","room_cc_clover","room_cc_fountain","room_dw_city_big_3_og","room_dw_mansion_bridgesold","room_dw_city_sidewayscars","room_transformation_sequence","room_dw_mansion_gigaqueen"]
}
def open_file(file_name):      
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
def save_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)
def read_file(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content
def try_to_delete(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

def get_save_type_tuple():
    try:
        save_type = (int(input("Which chapter? (1-2) >>>   ")),int(input("Which slot? (1-2-3) >>>   ")))
    except ValueError:
        print("Invalid input.")
        return get_save_type_tuple()
    if save_type[0] not in [1,2]:
        print("Invalid chapter.")
        return get_save_type_tuple()
    if save_type[1] not in [1,2,3]:
        print("Invalid slot.")
        return get_save_type_tuple()
    return (str(save_type[0]),str(save_type[1]-1))

def makeinikey(chapter,slot):
    match chapter:
        case "1": chapter = "G"
        case "2": chapter = "G_2_"
        case _  : pass
    match slot:
        case "0": chapSlot = f"{chapter}0"
        case "1": chapSlot = f"{chapter}1"
        case "2": chapSlot = f"{chapter}2"
        case _: pass
    return chapSlot
def writeini(key,name,room,time):
    config.read(location_data["data"]+'\\dr.ini')
    if not config.has_section(key):
        config.add_section(key)
    if not key.__contains__("_2"):
        room == str(int(room)+281)

    config.set(key, 'Name',f'"{name.strip(" ")}"')
    config.set(key, 'Level', '"1.000000"')
    config.set(key, 'Love', '"1.000000"')
    config.set(key, 'Time', f'"{time.strip(" ")}.000000"')
    config.set(key, 'Room', f'"{room.strip(" ")}.000000"')
    config.set(key, 'InitLang', '"0.000000"')
    config.set(key, 'UraBoss', '"0.000000"')
    config.set(key, 'Version', '"1.10"')
    
    with open(location_data["data"]+'\\dr.ini', 'w') as configfile:
        config.write(configfile)

def backup_save(new_name,chapter="none",slot="none"):
    if chapter == "none":
        chapter = input("Which Chapter? (1-2) >>>   ")
        if chapter != "1" or chapter != "2":
            backup_save(new_name)
        slot =     input("Which Slot? (1-2-3) >>>   ")
        if slot != "1" or slot != "2" or slot != "3":
            backup_save(new_name)
    
    if os.path.exists(location_data["data"]+f'\\filech{chapter}_{slot}'):
        if not os.path.exists(loc+f'\\Saves\\CH{chapter}\\{new_name}'):
            os.makedirs(loc+f'\\Saves\\CH{chapter}\\{new_name}')
        save_file(loc+f"\\Saves\\CH{chapter}\\{new_name}\\save",open_file(location_data["data"]+f"\\filech{chapter}_{slot}"))
    
    
    
    
    else:
        print("No save found!")
        return
def write_save(backup_name,new_save_type):
    if os.path.exists(location_data["data"]+f'\\filech{new_save_type[0]}_{new_save_type[1]}'):
        dobackup = input("File already exists!\nDo you want to back up existing save? (y/n)")
        match dobackup:
            case "y": backup_save(input("What do you want to name the backup? >>>   "),chapter=new_save_type[0],slot=new_save_type[1])
            case "n": pass

        ## Backup existing save here
    
    lines = read_file(loc+f'\\Saves\\CH{new_save_type[0]}\\{backup_name}\\save')
    data = []
    for item in lines:
        data.append(item.strip("\n"))
    if new_save_type[0] == "1":
        room = data[10316]
        time = data[10317]
    if new_save_type[0] == "2":
        room = data[3053]
        time = data[3054]
    name = data[0]
    

    writeini(makeinikey(new_save_type[0],new_save_type[1]),name,room,time)
    try_to_delete(location_data["data"]+f'\\filech{new_save_type[0]}_{new_save_type[1]}')

    save_file(location_data["data"] + f"\\filech{new_save_type[0]}_{new_save_type[1]}",open_file(loc+f"\\Saves\\CH{new_save_type[0]}\\{backup_name}\\save"))
    visibleslot = int(new_save_type[1])+1
    print(f"Save '{backup_name}' written to chapter {new_save_type[0]} slot {visibleslot}\n",location_data["data"])
def list_saves():
    try:
        chapter = int(input("Which chapter? (1-2) >>>   "))
    except ValueError:
        print("Invalid input.")
        return list_saves()
    saves = os.listdir(loc+"\\Saves\\CH"+str(chapter))
    print("\nChapter "+str(chapter)+" saves:\n")
    for i in range(len(saves)):
        print(f"• {saves[i]}")
    print("\n")


if __name__ == "__main__":
    while True:
        print("""
    1. Backup Loaded Save
    2. Load New Save
    3. List All Saves
    4. Exit
""")
        choice = input("Please enter your choice >>>   ")
        if choice == "1":
            chapslot = get_save_type_tuple()
            backup_save(input("What do you want to name the backup? >>>   "),chapslot[0],chapslot[1])
        elif choice == "2":
            chapslot = get_save_type_tuple()
            write_save(input("Please enter the name of the save to write >>>   "),chapslot)
        elif choice == "3":
            list_saves()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")




