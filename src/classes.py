try:        import error_system as e
except:     import src.error_system as e
try:        import virtual_stack as v
except:     import src.virtual_stack as v
try:        from constants import IDENTIFIER, SYSTEM, VARIABLE_NOT_FOUND_EXCEPTION, get_token_type_str, get_node_type_to_str, get_node_property_to_str, N_START, T_NEWLINE, T_WHITESPACE, N_VALUE, TERMINAL_EXCEPTION, TERMINAL
except:     from src.constants import IDENTIFIER, SYSTEM, VARIABLE_NOT_FOUND_EXCEPTION, get_token_type_str, get_node_type_to_str, get_node_property_to_str, N_START, T_NEWLINE, T_WHITESPACE, N_VALUE, TERMINAL_EXCEPTION, TERMINAL

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

    def to_str(self, sys):
        if self.typeof(T_WHITESPACE):
            if sys.tokens_show_space:
                return '" "'
        elif self.typeof(T_NEWLINE):
            if sys.tokens_show_nl:
                return f"\\n"
        elif self.params:
            return f"{self.str_value} ({self.ln}) params: [" + ' '.join(e.str_value for e in self.params) + "]" 
        elif not self.type in [T_WHITESPACE, T_NEWLINE]:
            return f"TOKEN: <{get_token_type_str(self.type)}>, {self.str_value} ({self.ln})"
        else:
            return f'NO TOKEN REPRESENTATION FOUND ({self.ln})'

class node:
    def __init__(self, type, ln, properties, child = None, value = None, params = None, operators = None):
        self.type = type
        self.ln = ln
        self.properties = properties
        self.child = child
        self.value = value
        self.params = params
        self.operators = operators
        self.ptr = "" # Pointer address to a node on the stack
        self.idx = 0

    def get_param_to_str(self, param):
        if param.has_property(IDENTIFIER):
            return param.ptr
        return param.value

    def get_member_properties(self, member):
        if isinstance(member, node):
            return ' '.join(get_node_property_to_str(p) for p in member.properties)
        return ''

    def get_value_to_str(self):
        if not self.value: return self.ptr
        
        if hasattr(self.value, '__call__'):
            return f"[python_function]: {self.value.__name__}"
        elif self.value.has_property(IDENTIFIER):
            return self.value.ptr

        if self.typeof(N_START):
            return f"Starting the code from here"
        elif self.value.typeof(N_VALUE):
            return f"{get_node_property_to_str(self.value.properties[0])} » {self.value.value}"
        else:
            return f"{get_node_type_to_str(self.value.type)} » SOME VALUE..."

    def typeof(self, type):
        return True if type is self.type else False

    def has_property(self, property):
        return True if property in self.properties else False
    
    def has_operator(self, operator):
        return True if any(op.str_value == operator for op in self.operators) else False
    
    def operator_count(self, operator):
        count = 0
        if self.has_operator(operator):
            for op in self.operators:
                if op.str_value == operator:
                    count += 1
        return count    

    def add_property(self, property):
        if not self.has_property(property):
            self.properties.append(property)

    def pop_property(self, property):
        if self.has_property(property):
            self.properties.remove(property)
    
    def set_ptr(self, str_value):
        if str_value: self.ptr = str_value

    def to_str(self, sys):
        if sys.nodes_show_properties:
            if sys.nodes_show_child_properties:
                return f"NODE: <{get_node_type_to_str(self.type)}>, [{self.get_value_to_str()} ({self.get_member_properties(self.value)})], [" + ' '.join(get_node_property_to_str(p) for p in self.properties) + f"] ({self.ln})"
            elif sys.nodes_show_parameters and self.params:
                return f"NODE: <{get_node_type_to_str(self.type)}>, [{self.get_value_to_str()}], params: [" + ' '.join(self.get_param_to_str(p) for p in self.params) + "], [" + ' '.join(get_node_property_to_str(p) for p in self.properties) + f"] ({self.ln})"
            return f"NODE: <{get_node_type_to_str(self.type)}>, [{self.get_value_to_str()}], [" + ' '.join(get_node_property_to_str(p) for p in self.properties) + f"] ({self.ln})"
        elif not sys.nodes_show_parameters and not sys.nodes_show_properties:
            return f"NODE: <{get_node_type_to_str(self.type)}>, [{self.get_value_to_str()}] ({self.ln})"
        else:
            return f"NO NODE REPRESENTATION FOUND ({self.ln})"

    def copy(self):
        n = node(self.type, self.ln, self.properties, self.child, self.value, self.params, self.operators)
        n.set_ptr(self.ptr)
        n.idx = self.idx
        return n

class system:
    def __init__(self, code = "", script = "<terminal>", no_stack = False):
        self.code = code
        self.error_system = e.ErrorSystem(script)
        self.virtual_stack = None
        if not no_stack: self.virtual_stack = v.VirtualStack(script)
        self.initialized_extern_functions = {}
        self.stdout = stdout()

        self.show_tokens = False
        self.tokens_show_nl = False
        self.tokens_show_space = False
        self.show_silent_warnings = False
        self.show_nodes = False
        self.nodes_show_properties = False
        self.nodes_show_child_properties = False
        self.nodes_show_parameters = False
        self.show_sorted_nodes = False
        self.show_stack_objects = False

        self.flags = {
            "-t"  : "-t\tToggle token printing.", 
            "-nl" : "-nl\tToggle newline printing.",
            "-ws" : "-ws\tToggle whitespace printing.",
            "-sw" : "-sw\tShow silent warnings.",
            "-n"  : "-n\tToggle node printing.",
            "-np" : "-np\tToggle node property printing.",
            "-cp" : "-cp\tToggle property printing of a child node.",
            "-pa" : "-pa\tToggle node parameter printing.",
            "-sn" : "-sn\tToggle sorted node printing.",
            "-vs" : "-vs\tToggle virtual stack printing."
        }

    def cast_all_exceptions(self):
        self.error_system.throw_errors()
        self.error_system.throw_warnings()

    def process_help_flag(self, argv2 = None):
        if not argv2:
            print("\n\n" + '-' * 50)
            for k, v in self.flags.items():
                print("\n" + v)
            print("\n" + '-' * 50)
        else:
            try:
                description = self.flags[argv2]
                print(f"Description - {argv2}:\n\t{description}")
            except KeyError:
                self.error_system.create_warning(TERMINAL_EXCEPTION, TERMINAL, f"The flag '{argv2}' does not exist.")

        self.error_system.throw_errors()
        self.error_system.throw_warnings()

    def process_argv(self, argv):
        if argv == "-help":
            self.error_system.create_error(TERMINAL_EXCEPTION, TERMINAL, "Invalid flag combination.")

        if argv == "-t":
            self.show_tokens = True
        elif argv == "-nl":
            self.tokens_show_nl = True
        elif argv == "-ws":
            self.tokens_show_space = True
        elif argv == "-sw":
            self.show_silent_warnings = True
        elif argv == "-n":
            self.show_nodes = True
        elif argv == "-np":
            self.nodes_show_properties = True
        elif argv == "-cp":
            self.nodes_show_child_properties = True
        elif argv == "-pa":
            self.nodes_show_parameters = True
        elif argv == "-sn":
            self.show_sorted_nodes = True
        elif argv == "-vs":
            self.show_stack_objects = True

        self.error_system.throw_errors()
        self.error_system.throw_warnings()

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
    
    def init_extern_function(self, name, arg_count, arg_types):
        self.initialized_extern_functions[name] = (arg_count, arg_types)

    def get_function_arg_count(self, name):
        if name in self.initialized_extern_functions.keys():
            return self.initialized_extern_functions[name][0]
        self.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, SYSTEM, f"The function called '{name}' is not initialized.")

    def get_function_arg_types(self, name):
        if name in self.initialized_extern_functions.keys():
            return self.initialized_extern_functions[name][1]
        self.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, SYSTEM, f"The function called '{name}' is not initialized.")

class stdout:
    def __init__(self):
        self.stash = []

    def write(self, str):
        self.stash.append(str)
    
    def flush(self):
        for str in self.stash:
            print(str)
        self.stash = []