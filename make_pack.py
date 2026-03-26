import shutil
import zipfile
import os
from PIL import Image

BASE_FOLDER = "textures"
ITEMS_FOLDER = "gui/items"
TERRAIN_FOLDER = "terrain"
TEMP_FOLDER = "temp"

ATLAS_SIZE = 256
TILE_SIZE = 16

terrainMap = {
    "grass_top_base": [0,0],
    "stone": [1,0],
    "dirt": [2,0],
    "grass_side_base": [3,0],
    "planks": [4,0],
    "stone_slab_side": [5,0],
    "stone_slab_top": [6,0],
    "bricks": [7,0],
    "tnt_side": [8,0],
    "tnt_top": [9,0],
    "tnt_bottom": [10,0],
    "cobwebs": [11,0],
    "rose": [12,0],
    "dandelion": [13,0],
    "portal_placeholder": [14,0],
    "oak_sapling": [15,0],
    "cobblestone": [0,1],
    "bedrock": [1,1],
    "sand": [2,1],
    "gravel": [3,1],
    "oak_log_side": [4,1],
    "log_top": [5,1],
    "iron_block": [6,1],
    "gold_block": [7,1],
    "diamond_block": [8,1],
    "chest_top": [9,1],
    "chest_side": [10,1],
    "chest_front": [11,1],
    "red_mushroom": [12,1],
    "brown_mushroom": [13,1],
    "fire_placeholder_0": [15,1],
    "gold_ore": [0,2],
    "iron_ore": [1,2],  
    "coal_ore": [2,2],
    "bookshelf": [3,2],
    "mossy_cobblestone": [4,2],
    "obsidian": [5,2],
    "grass_side_overlay": [6,2],
    "tallgrass": [7,2],
    "grass_top_overlay": [8,2],
    "double_chest_front_left": [9,2],
    "double_chest_front_right": [10,2],
    "crafting_table_top": [11,2],
    "furnace_front": [12,2],
    "furnace_side": [13,2],
    "dispenser_front": [14,2],
    "fire_placeholder_1": [15,2],
    "sponge": [0,3],
    "glass": [1,3],
    "diamond_ore": [2,3],
    "redstone_ore": [3,3],
    "oak_leaves_transparent": [4,3],
    "oak_leaves_opaque": [5,3],
    "deadbush": [7,3],
    "fern": [8,3],
    "double_chest_back_left": [9,3],
    "double_chest_back_right": [10,3],
    "crafting_table_side": [11,3],
    "crafting_table_front": [12,3],
    "lit_furnace_front": [13,3],
    "furnace_top": [14,3],
    "spruce_sapling": [15,3],
    "white_wool": [0,4],
    "monster_spawner": [1,4],
    "snow": [2,4],
    "ice": [3,4],
    "grass_side_snow": [4,4],
    "cactus_top": [5,4],
    "cactus_side": [6,4],
    "cactus_bottom": [7,4],
    "clay": [8,4],
    "sugarcane": [9,4],
    "noteblock": [10,4],
    "jukebox_top": [11,4],
    "birch_sapling": [15,4],
    "torch": [0,5],
    "wooden_door_top": [1,5],
    "iron_door_top": [2,5],
    "ladder": [3,5],
    "trapdoor": [4,5],
    "farmland_wet": [6,5],
    "farmland_dry": [7,5],
    "wheat_stage_0": [8,5],
    "wheat_stage_1": [9,5],
    "wheat_stage_2": [10,5],
    "wheat_stage_3": [11,5],
    "wheat_stage_4": [12,5],
    "wheat_stage_5": [13,5],
    "wheat_stage_6": [14,5],
    "wheat_stage_7": [15,5],
    "lever": [0,6],
    "wooden_door_bottom": [1,6],
    "iron_door_bottom": [2,6],
    "redstone_torch_on": [3,6],
    "pumpkin_top": [6,6],
    "netherrack": [7,6],
    "soul_sand": [8,6],
    "glowstone": [9,6],
    "sticky_piston_front": [10,6],
    "piston_front": [11,6],
    "piston_side": [12,6],
    "piston_buttom": [13,6],
    "piston_front_inside": [14,6],
    "rail_turn": [0,7],
    "black_wool": [1,7],
    "gray_wool": [2,7],
    "redstone_torch_off": [3,7],
    "spruce_log_side": [4,7],
    "birch_log_side": [5,7],
    "pumpkin_side": [6,7],
    "pumpkin_front": [7,7],
    "jack_o_lantern_front": [8,7],
    "cake_top": [9,7],
    "cake_outside": [10,7],
    "cake_inside": [11,7],
    "cake_bottom": [12,7],
    "rail_straight": [0,8],
    "red_wool": [1,8],
    "pink_wool": [2,8],
    "redstone_repeated_off": [3,8],
    "spruce_leaves_transparent": [4,8],
    "spruce_leaves_opaque": [5,8],
    "bed_top_foot": [6,8],
    "bed_top_head": [7,8],
    "cake_item": [12,8],
    "lapis_lazuli_block": [0,9],
    "green_wool": [1,9],
    "lime_wool": [2,9],
    "redstone_repeater_on": [3,9],
    "bed_bottom_foot": [4,9],
    "bed_side_foot": [5,9],
    "bed_side_head": [6,9],
    "bed_bottom_head": [7,9],
    "lapis_lazuli_ore": [0,10],
    "brown_wool": [1,10],
    "yellow_wool": [2,10],
    "powered_rail_off": [3,10],
    "redstone_dust_cross": [4,10],
    "redstone_dust_line": [5,10],
    "sandstone_top": [0,11],
    "blue_wool": [1,11],
    "light_blue_wool": [2,11],
    "powered_rail_on": [3,11],
    "sandstone_side": [0,12],
    "purple_wool": [1,12],
    "magenta_wool": [2,12],
    "activator_rail": [3,12],
    "sandstone_bottom": [0,13],
    "cyan_wool": [1,13],
    "orange_wool": [2,13],
    "light_gray_wool": [1,14],
    "breaking_stage_0": [0,15],
    "breaking_stage_1": [1,15],
    "breaking_stage_2": [2,15],
    "breaking_stage_3": [3,15],
    "breaking_stage_4": [4,15],
    "breaking_stage_5": [5,15],
    "breaking_stage_6": [6,15],
    "breaking_stage_7": [7,15],
    "breaking_stage_8": [8,15],
    "breaking_stage_9": [9,15],
}

itemMap = {
    "leather_helmet": [0,0],
    "chainmail_helmet": [1,0],
    "iron_helmet": [2,0],
    "diamond_helmet": [3,0],
    "gold_helmet": [4,0],
    "flint_and_steel": [5,0],
    "flint": [6,0],
    "coal": [7,0],
    "string": [8,0],
    "seeds": [9,0],
    "apple": [10,0],
    "golden_apple": [11,0],
    "egg": [12,0],
    "sugar": [13,0],
    "snowball": [14,0],
    "leather_chestplate": [0,1],
    "chainmail_chestplate": [1,1],
    "iron_chestplate": [2,1],
    "diamond_chestplate": [3,1],
    "gold_chestplate": [4,1],
    "bow": [5,1],
    "brick": [6,1],
    "iron_ingot": [7,1],
    "feather": [8,1],
    "wheat": [9,1],
    "painting": [10,1],
    "sugar_cane": [11,1],
    "bone": [12,1],
    "cake": [13,1],
    "slimeball": [14,1],
    "leather_leggings": [0,2],
    "chainmail_leggings": [1,2],
    "iron_leggings": [2,2],
    "diamond_leggings": [3,2],
    "gold_leggings": [4,2],
    "arrow": [5,2],
    "quiver": [6,2],
    "gold_ingot": [7,2],
    "gunpowder": [8,2],
    "bread": [9,2],
    "sign": [10,2],
    "wooden_door": [11,2],
    "iron_door": [12,2],
    "bed": [13,2],
    "leather_boots": [0,3],
    "chainmail_boots": [1,3],
    "iron_boots": [2,3],
    "diamond_boots": [3,3],
    "gold_boots": [4,3],
    "stick": [5,3],
    "compass": [6,3],
    "diamond": [7,3],
    "redstone_dust": [8,3],
    "clay_ball": [9,3],
    "paper": [10,3],
    "book": [11,3],
    "map": [12,3],
    "wooden_sword": [0,4],
    "stone_sword": [1,4],
    "iron_sword": [2,4],
    "diamond_sword": [3,4],
    "gold_sword": [4,4],
    "fishing_rod": [5,4],
    "clock": [6,4],
    "bowl": [7,4],
    "mushroom_stew": [8,4],
    "glowstone_dust": [9,4],
    "bucket": [10,4],
    "water_bucket": [11,4],
    "lava_bucket": [12,4],
    "milk_bucket": [13,4],
    "black_dye": [14,4],
    "gray_dye": [15,4],
    "wooden_shovel": [0,5],
    "stone_shovel": [1,5],
    "iron_shovel": [2,5],
    "diamond_shovel": [3,5],
    "gold_shovel": [4,5],
    "fishing_rod_cast": [5,5],
    "redstone_repeater": [6,5],
    "raw_porkchop": [7,5],
    "cooked_porkchop": [8,5],
    "raw_fish": [9,5],
    "cooked_fish": [10,5],
    "cookie": [12,5],
    "shears": [13,5],
    "red_dye": [14,5],
    "pink_dye": [15,5],
    "wooden_pickaxe": [0,6],
    "stone_pickaxe": [1,6],
    "iron_pickaxe": [2,6],
    "diamond_pickaxe": [3,6],
    "gold_pickaxe": [4,6],
    "leather": [9,6],
    "saddle": [10,6],
    "green_dye": [14,6],
    "lime_dye": [15,6],
    "wooden_axe": [0,7],
    "stone_axe": [1,7],
    "iron_axe": [2,7],
    "diamond_axe": [3,7],
    "gold_axe": [4,7],
    "brown_dye": [14,7],
    "yellow_dye": [15,7],
    "wooden_hoe": [0,8],
    "stone_hoe": [1,8],
    "iron_hoe": [2,8],
    "diamond_hoe": [3,8],
    "gold_hoe": [4,8],
    "minecart": [9,8],
    "boat": [10,8],
    "blue_dye": [14,8],
    "light_blue_dye": [15,8],
    "minecart_with_chest": [9,9],
    "purple_dye": [14,9],
    "magenta_dye": [15,9],
    "minecart_with_furnace": [9,10],
    "cyan_dye": [14,10],
    "orange_dye": [15,10],
    "light_gray_dye": [14,11],
    "white_dye": [15,11],
    "record_13": [0,15],
    "record_cat": [1,15],
}

guiFiles = [
    "background",
    "container",
    "crafting",
    "furnace",
    "gui",
    "icons",
    "inventory",
    "logo",
    "particles",
    "slot",
    "trap",
    "unknown_pack",
]

def get_texture_path(texture_name, folder):
    return os.path.join(BASE_FOLDER, folder, f"{texture_name}.png")

# Create empty atlas
def generate_atlas(mapping, atlas_name):
    missing = 0
    atlas = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE))

    for name, (x, y) in mapping.items():
        path = get_texture_path(name, atlas_name)

        if not os.path.exists(path):
            #print(f"Missing: {path}")
            missing += 1
            continue

        tile = Image.open(path).convert("RGBA")

        if tile.size != (TILE_SIZE, TILE_SIZE):
            print(f"Wrong size: {path} -> {tile.size}")
            continue

        atlas.paste(tile, (x * TILE_SIZE, y * TILE_SIZE))

    print(f"{atlas_name}.png progress: {len(mapping) - missing}/{len(mapping)}")

    # Save atlas
    atlas.save(os.path.join(TEMP_FOLDER, f"{atlas_name}.png"))

def copy_files(file_list, base_folder):
    missing = 0
    for file in file_list:
        src_path = os.path.join(BASE_FOLDER, base_folder, f"{file}.png")
        dst_path = os.path.join(TEMP_FOLDER, base_folder, f"{file}.png")

        if not os.path.exists(src_path):
            #print(f"Missing: {src_path}")
            missing += 1
            continue

        shutil.copy(src_path, dst_path)

    print(f"{base_folder} progress: {len(file_list) - missing}/{len(file_list)}")

# Create temp folder
if not os.path.exists(TEMP_FOLDER):
    os.mkdir(TEMP_FOLDER)
if not os.path.exists(os.path.join(TEMP_FOLDER, "gui")):
    os.mkdir(os.path.join(TEMP_FOLDER, "gui"))

# Generate atlases
generate_atlas(terrainMap, TERRAIN_FOLDER)
generate_atlas(itemMap, ITEMS_FOLDER)

# Copy raw files
copy_files(guiFiles, "gui")

# Create texture pack zip
with zipfile.ZipFile("LibreProg.zip", "w") as zipf:
    for root, dirs, files in os.walk(TEMP_FOLDER):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, TEMP_FOLDER)
            zipf.write(full_path, rel_path)

# Cleanup temp folder
#shutil.rmtree(TEMP_FOLDER)