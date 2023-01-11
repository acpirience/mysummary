"""
    Class containing all events
"""
from loguru import logger


class Events:
    """Class containing all events"""

    def __init__(self) -> None:
        self.events: dict[str, str] = {}

    def load_events(self, events_src_type: str, events_source: str) -> None:
        """Load all events for the datasource"""
        match events_src_type:
            case "TXT":
                self.events = self.load_events_from_txt(events_source)
            case "SQLITE":
                self.events = self.load_events_from_sqlite(events_source)
            case _:
                logger.error(f"Event source type not recognised {events_src_type}")

    def load_events_from_txt(self, events_source: str) -> dict[str, str]:
        """Load all events from text file"""
        logger.info(f"Loading text file from {events_source}")
        return {}

    def load_events_from_sqlite(self, events_source: str) -> dict[str, str]:
        """Load all events from sqlite database"""
        logger.info(f"Loading sqlite database from {events_source}")
        return {}
