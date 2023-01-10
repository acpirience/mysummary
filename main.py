"""
        My Summary
"""
from config import Config

CONFIG_DIR = "./"
CONFIG_FILE = "config.cfg"

if __name__ == "__main__":
    # Main Entry
    config = Config(CONFIG_DIR, CONFIG_FILE)
    config.load_config()
