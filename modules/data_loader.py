import json
import os

class ConfigLoader:
    def __init__(self, config_path="config"):
        self.config_path = config_path
    
    def load_json(self, filename):
        filepath = os.path.join(self.config_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

config_loader = ConfigLoader()
