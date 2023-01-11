"""
        My Summary
"""
from config import Config
from events import Events

CONFIG_DIR = "./"
CONFIG_FILE = "config.cfg"

if __name__ == "__main__":
    config = Config(CONFIG_DIR, CONFIG_FILE)
    config.load_config()

    events = Events()
    events.load_events(config.prefs["DATA_SOURCE_TYPE"], config.prefs["DATA_SOURCE"])
