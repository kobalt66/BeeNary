import error_system as e
from constants import get_token_type_str

class token:
    def __init__(self, type, str_value, ln, params = None):
        self.type = type
        self.str_value = str_value
        self.ln = ln
        self.params = params

    def typeof(self, type):
        return True if self.type is type else False
    
    def to_str(self):
        return f"TOKEN: <{get_token_type_str(self.type)}>, {self.str_value} ({self.ln})"

class system:
    def __init__(self, code, script):
        self.code = code
        self.error_system = e.ErrorSystem(script)
        