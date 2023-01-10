""" Unit tests for config.py.py """
import os

from config import Config


def test_default_prefs_loaded():
    """default prefs are loaded at startup"""
    test_config = Config("", "")
    assert test_config.prefs is not None


def test_dir_and_filename_are_ok():
    """validate good transmission of dir and filename"""
    test_config = Config("/.", "config.cfg")
    assert test_config.save_dir == "/."
    assert test_config.save_file == "config.cfg"


def test_file_not_found_does_default():
    """if file not found create default"""
    test_config = Config("./", "12345.cfg")
    test_config.load_config()
    assert test_config.prefs == test_config.default_prefs
    # cleanup
    os.remove("./12345.cfg")


def test_file_found_after_new_creation():
    """create new file then read form it"""
    test_config = Config("./", "12345.cfg")
    test_config.load_config()

    test_config2 = Config("./", "12345.cfg")
    test_config2.load_config()
    assert test_config.prefs == test_config.default_prefs

    # cleanup
    os.remove("./12345.cfg")


def test_corrupted_json_creates_new_file():
    with open("./56789.cfg", "a") as corrupted_json:
        corrupted_json.write("<begin><end>")

    test_config = Config("./", "56789.cfg")
    test_config.load_config()
    assert test_config.prefs == test_config.default_prefs

    # cleanup
    os.remove("./56789.cfg")
