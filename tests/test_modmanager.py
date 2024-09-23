import pytest
from dmodmanager.modmanager import ModManager
import os

@pytest.fixture
def modmanager() -> ModManager:
    return ModManager("/GameFolder", "/AppDataFolder")


@pytest.mark.parametrize("folders_exist_map,expected_result", [
    ([("/GameFolder/dmm_bin", False)], False),
    ([("/GameFolder/dmm_bin", True), ("/GameFolder/dmm_Data", False)], False),
    ([("/GameFolder/dmm_bin", True), ("/GameFolder/dmm_Data", True), ("/AppDataFolder/dmm_Mods", False)], False),
    ([("/GameFolder/dmm_bin", True), ("/GameFolder/dmm_Data", True), ("/AppDataFolder/dmm_Mods", True)], True),
    ])
def test_managed_folders_when_dont(monkeypatch, modmanager: ModManager, folders_exist_map, expected_result):
    monkeypatch.setattr(os.path, "exists", lambda search_path: next((exists for path, exists in folders_exist_map if path == search_path), None) )
        
    managed_folders_exists = modmanager.managed_folders_exists()
    assert managed_folders_exists == expected_result