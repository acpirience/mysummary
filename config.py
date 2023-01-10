"""
    Config object used by program
"""
import json
import os

from loguru import logger

DEFAULT_PREFS = {
    "DATA_SOURCE": "/data/summary.txt",
}


class Config:
    """Config object used by program"""

    def __init__(self, config_dir: str, config_file: str) -> None:
        self.default_prefs = DEFAULT_PREFS
        self.prefs = DEFAULT_PREFS
        self.save_dir = config_dir
        self.save_file = config_file

    def load_config(self) -> None:
        """Load config file, create it with default values if it does not exist"""
        try:
            self.prefs = self.load_existing_save()
        except FileNotFoundError:
            # No save file, so create one
            logger.error("File not found")
            self.write_save()

    def load_existing_save(self) -> dict[str, str]:
        """Load config file, when file exists"""
        logger.info(f"Loading file {self.save_file}")
        with open(
            os.path.join(self.save_dir, self.save_file), "r+", encoding="UTF_8"
        ) as file:
            try:
                save = json.load(file)
            except json.decoder.JSONDecodeError:
                logger.error(
                    f"{self.save_file} seems corrupted folding back to default prefs"
                )
                save = self.default_prefs
                self.write_save()

        return save

    def write_save(self) -> None:
        """Save config file"""
        logger.info(f"Saving file {self.save_file} in {self.save_dir}")
        with open(
            os.path.join(self.save_dir, self.save_file), "w", encoding="UTF_8"
        ) as file:
            json.dump(self.prefs, file)
