import sys, os

try:        from constants import FATAL_ERRORS, SILENT_EXCEPTION, get_exclamation_type_str, get_exclamation_code_str
except:     from src.constants import FATAL_ERRORS, SILENT_EXCEPTION, get_exclamation_type_str, get_exclamation_code_str

class ErrorSystem:
    def __init__(self, script):
        self.errors = []
        self.warnings = []
        self.silent = []
        self.script = script
        self.constants_module = None
        self.show_warnings = True
        self.show_errors = True

    def throw_errors(self):
        exit_program = False

        for e in self.errors:
            if e.code in FATAL_ERRORS:
                exit_program = True

            if not self.show_errors: continue
            print("(Error) " + e.get_msg() + "\n")

        self.errors = []
        self.execute_exit(exit_program)

    def throw_warnings(self):
        exit_program = False
        
        for w in self.warnings:
            if w.code in [None]:
                exit_program = True

            if not self.show_warnings: continue
            print("(Warning) " + w.get_msg() + "\n")

        self.warnings = []
        self.execute_exit(exit_program)

    def throw_silent(self, show=False):
        if not show: return
        exit_program = False
        
        for s in self.silent:
            if s.code in [None]:
                exit_program = True
            print("(Silent warning) " + s.get_msg() + "\n")

        self.silent = []
        self.execute_exit(exit_program)

    def create_error(self, code, type, msg = "Something went wrong...", ln = -1):
        error = exclamation(code, type, msg, ln, self.script, self.constants_module)
        self.errors.append(error)

    def create_error_from_exception(self, e, code, type, ln):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self.create_error(code, type, f"{exc_type} {e} ({fname}:{exc_tb.tb_lineno})", ln)

    def create_warning(self, code, type, msg = "Something went wrong...", ln = -1):
        warning = exclamation(code, type, msg, ln, self.script, self.constants_module)
        self.warnings.append(warning)
    
    def create_warning_from_exception(self, e, code, type, ln):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self.create_warning(code, type, f"{exc_type} {e} ({fname}:{exc_tb.tb_lineno})", ln)

    def create_silent(self, type, msg = "Something went wrong...", ln = -1):
        error = exclamation(SILENT_EXCEPTION, type, msg, ln, self.script, self.constants_module)
        self.silent.append(error)
    
    def create_silent_from_exception(self, e, type):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        self.create_silent(type, f"{exc_type} {e} ({fname}:{exc_tb.tb_lineno})")

    def execute_exit(self, exit_program):
        if exit_program: 
            print("\n\nThe program seems to have some fatal issues...")
            exit(1)


class exclamation:
    def __init__(self, code, type, msg, ln, script, constants_module):
        self.code = code
        self.type = type
        self.msg = msg
        self.ln = ln
        self.script = script
        self.constants_module = constants_module

    def get_msg(self):
        code = get_exclamation_code_str(self.code) if not self.constants_module else self.constants_module.get_exclamation_code_str(self.code)
        type = get_exclamation_type_str(self.type) if not self.constants_module else self.constants_module.get_exclamation_type_str(self.type)
        return f"\n{code}:\n\t[{type}] {self.msg} ({self.script}, line: {self.ln})"