import updater_lib as ul

def fresh_install_lc_mods():
    lc_path = ul.find_lc()
    ul.overwrite_resources_directory()

    # The code below should be refactored into a function since it's basically
    # a copy of update_mods
    bepin_url = ul.get_most_recent_bepin_url()
    lc_api_url = ul.get_current_dl_link("https://thunderstore.io/c/lethal-company/p/2018/LC_API/")
    bigger_lobbies_url = ul.get_current_dl_link("https://thunderstore.io/c/lethal-company/p/bizzlemip/BiggerLobby/")

    bepin_zip_name = "BepinEx.zip"
    lc_api_zip_name = "LC_API.zip"
    bigger_lobbies_zip_name = "BiggerLobbies.zip"

    ul.download_mod(bepin_url, bepin_zip_name)
    ul.download_mod(lc_api_url, lc_api_zip_name)
    ul.download_mod(bigger_lobbies_url, bigger_lobbies_zip_name)

    b_zip_p =  ul.get_path_of_file("BepinEx.zip")

    ul.unzip(b_zip_p)
    b_raw_path = ul.get_path_of_folder("BepInEx")
    b_plugins_path = ul.create_plugins_folder(b_raw_path)
    
    raws_path = ul.get_raws_path()

    ul.unzip_dlls_to_path(ul.get_path_of_file(lc_api_zip_name), b_plugins_path)
    ul.unzip_dlls_to_path(ul.get_path_of_file(bigger_lobbies_zip_name), b_plugins_path)

    ul.copy_contents(raws_path, lc_path)
