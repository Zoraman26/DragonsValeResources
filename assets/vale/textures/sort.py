import argparse
import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue
        if "screenshot" in filename:
            os.remove(os.path.join(folder_path, filename))
            
    bows_subfolder_path = os.path.join(folder_path, "bows")
    if not os.path.exists(bows_subfolder_path):
        os.makedirs(bows_subfolder_path)
        
    tools_subfolder_path = os.path.join(folder_path, "tools")
    if not os.path.exists(tools_subfolder_path):
        os.makedirs(tools_subfolder_path)
    
    food_subfolder_path = os.path.join(folder_path, "food")
    if not os.path.exists(food_subfolder_path):
        os.makedirs(food_subfolder_path)
        
    parts_subfolder_path = os.path.join(folder_path, "parts")
    if not os.path.exists(parts_subfolder_path):
        os.makedirs(parts_subfolder_path)
    
    for filename in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue
        new_filename = filename.lower().replace("_texture", "")
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        if "bow" in new_filename or "crossbow" in new_filename:
            new_file_path = os.path.join(bows_subfolder_path, new_filename)
            os.rename(old_file_path, new_file_path)
        elif "sword" in new_filename or "axe" in new_filename or "shovel" in new_filename or "hoe" in new_filename or "stick" in new_filename or "rod" in new_filename:
            new_file_path = os.path.join(tools_subfolder_path, new_filename)
            os.rename(old_file_path, new_file_path)
        elif "soup" in new_filename:
            new_file_path = os.path.join(food_subfolder_path, new_filename)
            os.rename(old_file_path, new_file_path)
        elif "essence" in new_filename:
            new_file_path = os.path.join(parts_subfolder_path, new_filename)
            os.rename(old_file_path, new_file_path)
        else:
            os.rename(old_file_path, new_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename and sort files in a folder.")
    parser.add_argument("folder_path", type=str, help="The path to the folder.")
    args = parser.parse_args()
    rename_files(args.folder_path)