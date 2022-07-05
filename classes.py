import error_system as e
from constants import get_token_type_str, T_NEWLINE

class token:
    def __init__(self, type, str_value, ln, params = None):
        self.type = type
        self.str_value = str_value
        self.ln = ln
        self.params = params

    def typeof(self, type):
        return True if self.type == type else False
    
    def has_value(self, str_value):
        return True if self.str_value == str_value else False

    def same_ln(self, token):
        return True if self.ln == token.ln else False    

    def to_str(self):
        if self.typeof(T_NEWLINE): return f"\\n" 
        if self.params: return f"{self.str_value} ({self.ln}) params: [" + ' '.join(e.str_value for e in self.params) + "]" 
        return f"TOKEN: <{get_token_type_str(self.type)}>, {self.str_value} ({self.ln})"

class system:
    def __init__(self, code, script):
        self.code = code
        self.error_system = e.ErrorSystem(script)
        