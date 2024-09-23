import os
class ModManager:
    def __init__(self, game_folder, app_data):
        self.game_folder = game_folder
        self.managed_bin = f'{game_folder}/dmm_bin'
        self.managed_data = f'{game_folder}/dmm_Data'
        self.app_data_folder = app_data
        self.managed_mods = f'{self.app_data_folder}/dmm_Mods'
        
    def managed_folders_exists(self):
        if not os.path.exists(self.managed_bin):
            return False
        elif not os.path.exists(self.managed_data):
            return False
        elif not os.path.exists(self.managed_mods):
            return False
        return True