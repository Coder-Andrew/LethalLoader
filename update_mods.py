import updater_lib as ul

def update_lc_mods():
    ul.overwrite_resources_directory()
    lc_bepin_path = ul.find_bepin(ul.find_lc())

    lc_api_base = "https://thunderstore.io/c/lethal-company/p/2018/LC_API/"
    lobbies_base = "https://thunderstore.io/c/lethal-company/p/bizzlemip/BiggerLobby/"

    lc_api_file = ul.get_current_dl_link(lc_api_base)
    lobbies_file = ul.get_current_dl_link(lobbies_base)

    ul.download_mod(lc_api_file, "lc_api.zip")
    ul.download_mod(lobbies_file, "bigger_lobbies.zip")

    ul.unzip_dlls("lc_api.zip")
    ul.unzip_dlls("bigger_lobbies.zip")


    ul.update_current_plugins(lc_bepin_path)
