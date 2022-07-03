from locale import currency
from multiprocessing import Condition
from constants import *
from classes import *

sys = None

def run(code, script):
    global sys
    sys = system(code, script)

    lexer = Lexer(code)
    tokens = lexer.Phase1()

    for token in tokens:
        print(token.to_str())
    
######################################################################################################

class Lexer:
    def __init__(self, code):
        self.ln = 1
        self.idx = -1
        self.currChar = '\0'
        self.code = code
        self.tokens = []

    def advance(self):
        eof = False

        if (self.idx + 1) <= len(self.code):
            self.idx += 1
            self.currChar = self.code[self.idx]
            if self.currChar is '\n':
                self.ln += 1
                self.advance()
        else:
            eof = True 

        return eof

    def advance_condition(self, condition):
        self.advance()

        if condition(self.currChar):
            return True
        return False

    def Phase1(self):
        global sys

        while True:
            if self.currChar is ':':
                self.tokens.append(token(T_COLON, ':', self.ln))
                if self.advance(): break
            if self.currChar is ',':
                self.tokens.append(token(T_COMMA, ',', self.ln))
                if self.advance(): break
            if self.currChar is '<':
                self.tokens.append(token(T_LT, '<', self.ln))
                if self.advance(): break
            if self.currChar is '>':
                self.tokens.append(token(T_GT, '>', self.ln))
                if self.advance(): break
            if self.currChar in '#':
                self.tokens.append(self.comment())
            if self.currChar in '"':
                self.tokens.append(self.string())
            if self.currChar in IDENTIFIER_CHARS:
                self.tokens.append(self.word())
            if self.currChar in NUMBER_CHARS:
                self.tokens.append(self.number())
            else:
                self.tokens.append(token(T_SYMBOL, self.currChar, self.ln))
                if self.advance(): break
        
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
        condition = lambda: True if not self.currChar is '\n' else False 

        while self.advance_condition(condition):
            str_value += self.currChar

        type = T_COMMENT
        return token(type, str_value, self.ln)
    
    def string(self):
        self.advance()
        str_value = self.currChar
        condition = lambda: True if not self.currChar is '"' else False

        while self.advance_condition(condition):
            str_value += self.currChar

        type = T_STRING
        return token(type, str_value, self.ln)

    def number(self):
        global sys
        self.advance()
        str_value = self.currChar
        condition = lambda: True if self.currChar in NUMBER_CHARS else False
        dot_count = 0

        while self.advance_condition(condition):
            if self.currChar is '.':
                if dot_count is 0:
                    dot_count = 1
                else:
                    sys.error_system.create_error(INVALID_NUMBER_EXCEPTION, LEXING, "A floating point number can only have on dot.", self.ln)
            str_value += self.currChar

        type = T_INT if dot_count is 0 else T_FLOAT
        return token(type, str_value, self.ln)
