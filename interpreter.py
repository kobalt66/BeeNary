from constants import *
from classes import *
import io

sys = None

def run(code, script):
    global sys
    sys = system(code, script)

    lexer = Lexer(code)
    tokens = lexer.Phase1()
    tokens = lexer.Phase2()

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
            elif self.currChar == '\n':
                self.tokens.append(token(T_NEWLINE, '\\n', self.ln))
                self.ln += 1
                if self.advance(): break
            elif self.currChar == ' ':
                self.tokens.append(token(T_WHITESPACE, "' '", self.ln))
                if self.advance(): break
            elif self.currChar in IDENTIFIER_CHARS:
                self.tokens.append(self.word())
            elif self.currChar in NUMBER_CHARS:
                self.tokens.append(self.number())
            elif not self.currChar in '\0\n\t':
                self.tokens.append(token(T_SYMBOL, self.currChar, self.ln))
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

    def Phase2(self):
        idx = 0
        while idx < len(self.tokens):
            token = self.tokens[idx]

            if token.typeof(T_COLON):
                self.tokens = self.simplify_token(self.tokens, idx)
            elif token.typeof(T_IDENTIFIER):
                self.tokens = self.simplify_identifier(self.tokens, idx)

            idx += 1

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        return self.tokens

    def simplify_token(self, token_list, idx):
        colon = token_list[idx]
        identifier = token_list[idx + 1]

        if not colon.same_ln(identifier):
            sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"':' is at weird place.", colon.ln)

        if not identifier.typeof(T_TOKEN):
            sys.error_system.create_error(WRONG_TOKEN_TYPE_EXCEPTION, SIMPLIFYING, f"The token '{identifier.str_value}' is not a valid token.", identifier.ln)
        
        type = T_END if identifier.has_value("end") else T_TOKEN
        type = T_HIVE if identifier.has_value("hive") else type
        new_token = token(type, identifier.str_value, identifier.ln)


        currToken = token_list[idx + 2]
        if currToken.typeof(T_LT): 
            token_list, params = self.simplify_params(token_list, idx + 2)
            new_token = token(type, identifier.str_value, identifier.ln, params)


        currToken = token_list[idx + 2]
        if not currToken.typeof(T_COLON):
            sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"Expected ':' instead of '{currToken.str_value}'.", currToken.ln)

        token_list.pop(idx)
        token_list[idx] = new_token
        token_list.pop(idx + 1)

        return token_list
    
    def simplify_identifier(self, token_list, idx):
        identifier = token_list[idx]
        followed_by = token_list[idx + 1]

        if followed_by.typeof(T_COLON) and identifier.same_ln(followed_by):
            type = T_START if identifier.str_value == "start" else T_SECTION
            new_token = token(type, identifier.str_value, identifier.ln)

            token_list[idx] = new_token
            token_list.pop(idx + 1)
        elif followed_by.typeof(T_LT):
            type = T_EXTERN_FUNCTION
            token_list, params = self.simplify_params(token_list, idx + 1)
            new_token = token(type, identifier.str_value, identifier.ln, params)

            token_list[idx] = new_token

        return token_list
    
    def simplify_params(self, token_list, idx):
        currToken = token_list[idx]
        if not currToken.typeof(T_LT):
            sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"Expected '<' instead of '{currToken.str_value}'.", currToken.ln)

        params = []
        param_idx = 0

        param_token = token_list[idx + 1 + param_idx]
        if param_token.typeof(T_COMMA):
            sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"Expected parameter value instead of '{param_token.str_value}'.", param_token.ln)

        more_params = False
        while True:
            param_token = token_list[idx + 1 + param_idx]
            if param_token.typeof(T_COMMA):
                param_idx += 1
                more_params = True
                continue    

            if param_token.typeof(T_GT): 
                if more_params:
                    sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"Expected parameter value instead of '{param_token.str_value}'.", param_token.ln)
                break

            if not more_params and len(params) > 0:
                if not param_token.typeof(T_GT):
                    sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SIMPLIFYING, f"Expected '>' instead of '{param_token.str_value}'.", param_token.ln)
                break

            if param_token.type in [T_IDENTIFIER, T_INT, T_FLOAT, T_STRING, T_BOOL]:
                params.append(param_token)
                more_params = False
            elif not param_token.type in [T_COMMA, T_WHITESPACE]:
                sys.error_system.create_error(INVALID_PARAM_DECLARATION_EXCEPTION, SIMPLIFYING, f"The parameter type of '{get_token_type_str(param_token.type)}' is invalid!", param_token.ln)

            param_idx += 1

        for i in range(param_idx + 2):
            token_list.pop(idx)

        return token_list, params
