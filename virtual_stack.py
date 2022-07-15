from constants import HONEY, LIST, SECTION, TERMINAL_EXCEPTION, VARIABLE_NOT_FOUND_EXCEPTION, WAX
from constants import STACK
import classes

class VirtualStack:
    def __init__(self, script):
        self.script = script
        self.stack = {}
        self.sys = classes.system(script = script, no_stack = True)

    def isset(self, pointer):
        check = True if pointer.ptr in self.stack.keys() else False
        if not check:
            self.sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, STACK, f"The variable pointer '{pointer.ptr}' does not exist on the stack.", pointer.ln)
        
        return check

    def reset(self):
        self.sys.error_system.create_warning(TERMINAL_EXCEPTION, STACK, f"The virtual stack got reset.")
        self.stack = {}

    def get_var(self, pointer):
        if self.isset(pointer):
            return self.stack[pointer.ptr]

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()
    
    def set_var(self, variable):
        if self.isset(variable.child):
            self.stack[variable.child.ptr] = variable

        self.sys.error_system.throw_errors()
        self.sys.error_system.throw_warnings()
        self.sys.error_system.throw_silent()

    def del_var(self, pointer):
        if self.isset(pointer):
            self.stack.pop(pointer.ptr)
        
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
