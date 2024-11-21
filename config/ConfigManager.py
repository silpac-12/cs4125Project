import pandas as pd
import re
from googletrans import Translator

# Singleton Pattern: Configuration Manager
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config = {"language": "en"}
        return cls._instance

