# Welcome to LethalLoader!
Lethal Loader is an **EXTREMELY crudely** put together mod loader/updater for Lethal Company. It is designed to automatically download and install BepinEx, LC-API, and the BiggerLobbies mod for Lethal Company.

# How to use:
1. Drag Lethal Loader into a folder that is next to your Steam folder. This will not work if your Steam folder is in your C drive
1. Double click the LethalLoader.exe and enjoy!

### Example Directory:
- **E Drive/**
    - **Steam/**
        - **steamapps/**
            - **common/**
                - ...
    - **LethalLoader/**
        - `LethalLoader.exe`


# Notes:
- You CANNOT have Lethal Company in your C drive
- Currently only downloads 64-bit version of BepinEx only
- `LethalLoader.exe` will most likely be detected by Anti-virus software as a trojan because LethalLoader isn't registered with any Certificate Authorities (don't know how to register)
    - If you want to compile to exe yourself, you need Python, Pyinstaller, and the libraries listed at the top of [updater_lib.py](updater_lib.py) (that or you can just run the LethalLoader.py script after getting Python and the libraries)
