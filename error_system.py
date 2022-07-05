from constants import FATAL_ERRORS, SILENT_EXCEPTION, get_exclamation_type_str, get_exclamation_code_str
import sys, os

class ErrorSystem:
    def __init__(self, script):
        self.errors = []
        self.warnings = []
        self.silent = []
        self.script = script

    def throw_errors(self):
        exit_program = False

        for e in self.errors:
            if e.code in FATAL_ERRORS:
                exit_program = True
            print("\n(Error) " + e.get_msg())

        self.errors = []
        self.execute_exit(exit_program)

    def throw_warnings(self):
        exit_program = False
        
        for w in self.warnings:
            if w.code in [None]:
                exit_program = True
            print("\n(Warning) " + w.get_msg())

        self.warnings = []
        self.execute_exit(exit_program)

    def throw_silent(self, show=False):
        if not show: return
        exit_program = False
        
        for s in self.silent:
            if s.code in [None]:
                exit_program = True
            print("\n(Silent warning) " + s.get_msg())

        self.silent = []
        self.execute_exit(exit_program)

    def create_error(self, code, type, msg = "Something went wrong...", ln = -1):
        error = exclamation(code, type, msg, ln, self.script)
        self.errors.append(error)

    def create_warning(self, code, type, msg = "Something went wrong...", ln = -1):
        warning = exclamation(code, type, msg, ln, self.script)
        self.warnings.append(warning)
    
    def create_silent(self, type, msg = "Something went wrong...", ln = -1):
        error = exclamation(SILENT_EXCEPTION, type, msg, ln, self.script)
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
    def __init__(self, code, type, msg, ln, script):
        self.code = code
        self.type = type
        self.msg = msg
        self.ln = ln
        self.script = script

    def get_msg(self):
        return f"\n{get_exclamation_code_str(self.code)}:\n\t[{get_exclamation_type_str(self.type)}] {self.msg} ({self.script}, line: {self.ln})"