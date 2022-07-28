from logging import exception


try:        from constants import HONEY, LIST, SECTION, TERMINAL_EXCEPTION, VARIABLE_NOT_FOUND_EXCEPTION, WAX, MEADOW_MEMBER
except:     from src.constants import HONEY, LIST, SECTION, TERMINAL_EXCEPTION, VARIABLE_NOT_FOUND_EXCEPTION, WAX, MEADOW_MEMBER
try:        from constants import STACK
except:     from src.constants import STACK
try:        import classes
except:     import src.classes as classes

class VirtualStack:
    def __init__(self, script):
        self.script = script
        self.stack = {}
        self.sys = classes.system(script = script, no_stack = True)

    def isset(self, pointer, ln = None):
        key = pointer if isinstance(pointer, str) else pointer.ptr 
        check = True if key in self.stack.keys() else False    
        return check

    def reset(self):
        self.sys.error_system.create_warning(TERMINAL_EXCEPTION, STACK, f"The virtual stack got reset.")
        self.stack = {}

    def get_var(self, pointer):
        if self.isset(pointer):
            return self.stack[pointer.ptr]
        else:
            self.sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, STACK, f"The variable pointer '{pointer.ptr}' does not exist on the stack.", pointer.ln)

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()
    
    def get_var_by_ptr(self, ptr):
        if self.isset(ptr, -1):
            return self.stack[ptr]
        else:
            self.sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, STACK, f"The variable pointer '{ptr}' does not exist on the stack.", -1)

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()

    def set_var(self, variable):
        if variable.has_property(LIST) and self.isset(variable.value):
            self.stack[variable.value.ptr] = variable
        elif self.isset(variable.child):
            self.stack[variable.child.ptr] = variable
        else:
            self.sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, STACK, f"The variable pointer '{variable.child.ptr}' does not exist on the stack.", variable.ln)

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()

    def del_var(self, pointer):
        key = pointer if isinstance(pointer, str) else pointer.ptr
        if self.isset(key):
            if not self.stack[key].has_property(MEADOW_MEMBER):
                self.stack.pop(key)
        else:
            self.sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, STACK, f"The variable pointer '{key}' does not exist on the stack.", pointer.ln if not isinstance(pointer, str) else -1)

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()

    def init_var(self, object):
        if object.has_property(HONEY) or object.has_property(WAX):
            if not self.isset(object.child):
                self.stack[object.child.ptr] = object
        elif object.has_property(LIST) or object.has_property(SECTION):
            if not self.isset(object.value):
                self.stack[object.value.ptr] = object
