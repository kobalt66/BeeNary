from constants import get_exclamation_type_str, get_exclamation_code_str

class ErrorSystem:
    def __init__(self, script):
        self.errors = []
        self.warnings = []
        self.script

    def throw_errors(self):
        exit_program = False

        for e in self.errors:
            if e.code in [None]:
                exit_program = True
            print(e.get_msg())

        self.execute_exit(exit_program)

    def throw_warnings(self):
        exit_program = False
        
        for w in self.warnings:
            if w.code in [None]:
                exit_program = True
            print(w.get_msg())

        self.execute_exit(exit_program)

    def create_error(self, type, msg, ln):
        error = exclamation(type, msg, ln)
        self.errors.append(error, self.script)

    def create_warning(self, type, msg, ln):
        warning = exclamation(type, msg, ln)
        self.warnings.append(warning, self.script)

    def execute_exit(exit_program):
        if exit_program: 
            print("The program seems to have some fatal issues...")
            exit(1)


class exclamation:
    def __init__(self, code, type, msg, ln, script):
        self.code = code
        self.type = type
        self.msg = msg
        self.ln = ln
        self.script = script

    def get_msg(self):
        return f"\n{get_exclamation_code_str(self.code)}:\n\t[{get_exclamation_type_str(self.type)}] {self.msg} ({self.script}, line: {self.ln})"