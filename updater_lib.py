import os
import shutil
import requests
from bs4 import BeautifulSoup
import zipfile
import tempfile

def find_lc():
    print("Looking for Lethal Company folder")

    parent_path = os.path.dirname(os.getcwd())

    steam_path = os.path.join(parent_path,"Steam","steamapps","common","Lethal Company")
    steam_lib_path = os.path.join(parent_path,"SteamLibrary","steamapps","common","Lethal Company")

    if (not os.path.exists(steam_path) and not os.path.exists(steam_lib_path)):
        print(f"Could not find Lethal Company at either {steam_path} or {steam_lib_path}")
        print("Could not find Lethal Company")
        finish_program()
        raise ValueError("Lethal Company not found")
    elif(os.path.exists(steam_path)):
        path = steam_path
    else:
        path = steam_lib_path

    print(f"Found Lethal Company at: {path}")
    return path

def overwrite_directory():
    print("Setting up updater resource files")

    resources_path = os.path.join(os.getcwd(), "resources")
    zips_path = os.path.join(resources_path, "zips")
    raws_path = os.path.join(resources_path, "raws")
    
    if os.path.exists(resources_path):
        print("Resource files exist, removing...")
        shutil.rmtree(resources_path)
    
    print("Making resource folders")

    os.makedirs(resources_path)
    os.makedirs(zips_path)
    os.makedirs(raws_path)

def finish_program():
    input("Press Enter to Exit...")

def get_most_recent_bepin_url(git_url = "https://api.github.com/repos/BepInEx/BepInEx/releases"):
    print(f"Looking for Bepinex at: {git_url}")
    response = requests.get(git_url)

    if response.status_code == 200:
        print(f"Found Bepinex at: {git_url}")
        return response.json()[0]['assets'][1]['browser_download_url']
    else:
        print(f"Error, could not find bepinex at: {git_url}")
        return
    
def get_current_dl_link(mod_url):
    print(f"Searching for mods at: {mod_url}")
    
    response = requests.get(mod_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")
    i_tag = soup.find('i', class_='fa fa-download mr-2')
    a_tag = i_tag.find_parent('a') if i_tag else None

    mod_link = a_tag["href"] if a_tag else None

    if mod_link:
        print(f"Found mod at: {mod_url}")
        return mod_link
    else:
        print(f"Could not find mod at: {mod_url}")
        return

def download_mod(mod_url, fileName):
    print(f"Requesting {fileName} at: {mod_url}")
    response = requests.get(mod_url, stream=True)

    if (response.status_code == 200):
        print(f"Downloading {fileName} at: {mod_url}")
        with open(os.path.join(os.getcwd(), "resources", "zips",fileName), 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    else:
        print(f"Could not get {fileName} at: {mod_url}")
        finish_program()
        raise ValueError(f"Could not get {fileName}")

def find_bepin(lc_path):
    plugins_path = os.path.join(lc_path, "BepinEx", "plugins")
    print("Looking for BepinEx plugins at: {plugins_path}")

    if (not os.path.exists(plugins_path)):
        print(f"Please run fresh_install in order to install BepinEx and mods. Could not find BepinEx at: {plugins_path}")
        finish_program()
        raise ValueError("BepinEx plugins not found")
    
    print(f"BepinEx plugins found at: {plugins_path}")
    return plugins_path

def update_current_plugins(plugins):
    print("Removing existing BepinEx plugins folder")
    resources_path = os.path.join(os.getcwd(), "resources", "raws")

    if (not os.path.exists(resources_path)):
        print(f"Could not find resources at: {resources_path}")
        finish_program()
        raise ValueError("Could not find resources")
    
    shutil.rmtree(plugins)

    print("Updated plugins")
    shutil.copytree(resources_path, plugins)

def unzip(filename):
    print(f"Unzipping zip file: {filename}")
    file_path = os.path.join(os.getcwd(), "resources", "zips", filename)
    dir_name = os.path.join(os.getcwd(), "resources", "raws")
    try:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith('.dll'):
                    with tempfile.TemporaryDirectory() as tmpdirname:
                        zip_ref.extract(file, tmpdirname)
                        shutil.move(os.path.join(tmpdirname, file), os.path.join(dir_name, os.path.basename(file)))
        print("Extraction successful.")
    except FileNotFoundError:
        print(f"Error: {filename} does not exist.")
    except zipfile.BadZipFile:
        print("Error: Bad zip file.")
