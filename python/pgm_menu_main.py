# -- coding: UTF-8 --

from menu_main import MainMenu
from menu_export_ra_files import Menu_ExportRaFiles

from quit import Quit
from r_sam_roms_check import RSamRoms_CheckCrc32, RSamRoms_CheckTitles

# from wii_export_all import Wii_ExportAll


if __name__ == "__main__":
    main_menu = MainMenu.instance()

    Menu_ExportRaFiles.add_cmds(main_menu)

    # Wii_ExportAll.add_cmds(main_menu)

    RSamRoms_CheckCrc32.add_cmds(main_menu)
    RSamRoms_CheckTitles.add_cmds(main_menu)

    Quit.add_cmds(main_menu)

    main_menu.show()
