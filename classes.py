from cgi import parse_multipart
import error_system as e
from constants import T_WHITESPACE, get_token_type_str, T_NEWLINE, TERMINAL_EXCEPTION, TERMINAL

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

    def to_str(self, show_nl = False, show_space = False, show_tokens = False):
        if not show_tokens: return None
        if self.typeof(T_WHITESPACE):
            if show_space:
                return '" "'
        elif self.typeof(T_NEWLINE):
            if show_nl:
                return f"\\n"
        elif self.params:
            return f"{self.str_value} ({self.ln}) params: [" + ' '.join(e.str_value for e in self.params) + "]" 
        elif not self.type in [T_WHITESPACE, T_NEWLINE]:
            return f"TOKEN: <{get_token_type_str(self.type)}>, {self.str_value} ({self.ln})"
        else:
            return f'NO TOKEN REPRESENTATION FOUND ({self.ln})'

class node:
    def __init__(self, type, ln, properties, child = None, value = None, params = None):
        self.type = type
        self.ln = ln
        self.properties = properties
        self.child = child
        self.value = value
        self.params = params
        self.ptr = "" # Pointer address to a node on the stack

    def has_property(self, property):
        return True if property in self.properties else False
    
    def add_property(self, property):
        if not self.has_property(property):
            self.properties.append(property)

    def pop_property(self, property):
        if self.has_property(property):
            self.properties.remove(property)

class system:
    def __init__(self, code = "", script = "<terminal>"):
        self.code = code
        self.error_system = e.ErrorSystem(script)
        self.show_tokens = False
        self.tokens_show_nl = False
        self.tokens_show_space = False
        self.show_silent_warnings = False

    def process_argv(self, argv):
        if argv == "-t":
            self.show_tokens = True
        elif argv == "-n":
            self.tokens_show_nl = True
        elif argv == "-w":
            self.tokens_show_space = True
        elif argv == "-sw":
            self.show_silent_warnings = True 

    def process_argv_list(self, argv):
        # Error handling 
        if len(argv) == 1:
            self.error_system.create_error(TERMINAL_EXCEPTION, TERMINAL, "A path to a valid BeeNary script is required!")

        self.error_system.throw_errors()
        self.error_system.throw_warnings()

        # Extract argvs
        argv1   = argv[1]  if len(argv) > 1  else ""
        argv2   = argv[2]  if len(argv) > 2  else ""
        argv3   = argv[3]  if len(argv) > 3  else ""
        argv4   = argv[4]  if len(argv) > 4  else ""
        argv5   = argv[5]  if len(argv) > 5  else ""
        argv6   = argv[6]  if len(argv) > 6  else ""
        argv7   = argv[7]  if len(argv) > 7  else ""
        argv8   = argv[8]  if len(argv) > 8  else ""
        argv9   = argv[9]  if len(argv) > 9  else ""
        argv10  = argv[10] if len(argv) > 10 else ""

        return argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10