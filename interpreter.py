from locale import currency
from multiprocessing import Condition
from constants import *
from classes import *
import io

sys = None

def run(code, script):
    global sys
    sys = system(code, script)

    lexer = Lexer(code)
    tokens = lexer.Phase1()

    for token in tokens:
        print(token.to_str())

def get_code(path):
    file = io.open(path, "r")
    code = file.read()
    file.close()
    return code


######################################################################################################


class Lexer:
    def __init__(self, code):
        self.ln = 1
        self.idx = -1
        self.currChar = '\0'
        self.code = code
        self.tokens = []
        self.eof = False

    def advance(self):
        if (self.idx + 1) < len(self.code):
            self.idx += 1
            self.currChar = self.code[self.idx]                
        else:
            self.eof = True 

        return self.eof

    def advance_condition(self, condition):
        if self.advance():
            return False

        if condition():
            return True
        return False

    def Phase1(self):
        global sys

        while True:
            if self.eof: break
            if self.currChar == ':':
                self.tokens.append(token(T_COLON, ':', self.ln))
                if self.advance(): break
            elif self.currChar == ',':
                self.tokens.append(token(T_COMMA, ',', self.ln))
                if self.advance(): break
            elif self.currChar == '<':
                self.tokens.append(token(T_LT, '<', self.ln))
                if self.advance(): break
            elif self.currChar == '>':
                self.tokens.append(token(T_GT, '>', self.ln))
                if self.advance(): break
            elif self.currChar == '#':
                self.tokens.append(self.comment())
            elif self.currChar == '"':
                self.tokens.append(self.string())
                if self.advance(): break
            elif self.currChar in IDENTIFIER_CHARS:
                self.tokens.append(self.word())
            elif self.currChar in NUMBER_CHARS:
                self.tokens.append(self.number())
            elif not self.currChar in ' \0\n\t\r':
                self.tokens.append(token(T_SYMBOL, self.currChar, self.ln))
                if self.advance(): break
            elif self.currChar == '\n':
                self.ln += 1
                if self.advance(): break
            elif self.advance(): break
        
        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        return self.tokens

    def word(self):
        str_value = self.currChar
        condition = lambda: True if self.currChar in IDENTIFIER_CHARS else False

        while self.advance_condition(condition):
            str_value += self.currChar
        
        type = T_KEYWORD if str_value in KEYWORDS else T_IDENTIFIER
        type = T_TOKEN if str_value in TOKENS else type
        type = T_BOOL if str_value in BOOLEAN else type
        type = T_BUILTIN_FUNCTION if str_value in BUILTIN_FUNCTION else type
        return token(type, str_value, self.ln)

    def comment(self):
        self.advance()
        str_value = self.currChar
        condition = lambda: True if self.currChar != "\n" else False 

        while self.advance_condition(condition):
            str_value += self.currChar

        type = T_COMMENT
        return token(type, str_value, self.ln)
    
    def string(self):
        self.advance()
        str_value = self.currChar
        condition = lambda: True if not self.currChar in '"\n' else False

        while self.advance_condition(condition):
            str_value += self.currChar

        type = T_STRING
        return token(type, str_value, self.ln)

    def number(self):
        global sys
        str_value = self.currChar
        condition = lambda: True if self.currChar in NUMBER_CHARS else False
        dot_count = 0

        while self.advance_condition(condition):
            if self.currChar == '.':
                if dot_count == 0:
                    dot_count = 1
                else:
                    sys.error_system.create_error(INVALID_NUMBER_EXCEPTION, LEXING, "A floating point number can only have on dot.", self.ln)
            str_value += self.currChar

        type = T_INT if dot_count == 0 else T_FLOAT
        return token(type, str_value, self.ln)
