import io, os, threading
import sys as s
from time import sleep

try:        from constants import *
except:     from src.constants import *
try:        from classes import *
except:     from src.classes import *

s.path.insert(1, os.getcwd())

sys = None

def run(code, argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10):
    global sys
    sys = system(code, argv1)

    if argv1 == "-help":
        sys.process_help_flag(argv2)
        exit(0)

    sys.process_argv(argv2)
    sys.process_argv(argv3)
    sys.process_argv(argv4)
    sys.process_argv(argv5)
    sys.process_argv(argv6)
    sys.process_argv(argv7)
    sys.process_argv(argv8)
    sys.process_argv(argv9)
    sys.process_argv(argv10)

    lexer = Lexer(code)
    tokens = lexer.Phase1()
    tokens = lexer.Phase2()
    tokens_final = lexer.get_final_token_list(tokens)

    parser = Parser(tokens_final)
    nodes = parser.Parse()

    sortout = Sortout(nodes)
    sorted_nodes = sortout.Phase1()
    sorted_nodes = sortout.Phase2()
    sorted_nodes = sortout.Phase3()
    sorted_nodes = sortout.Finish()

    interpreter = Interpreter(sorted_nodes)
    interpreter.execute()
    sys.stdout.flush()

    if sys.show_tokens:
        print("\n\nTOKENS:")
        for token in tokens:
            str = token.to_str(sys)
            if str: print(str)
        print("\n")

    if sys.show_nodes:
        print("\n\nNODES:")
        for node in nodes:
            str = node.to_str(sys)
            if str: print(str)
        print("\n")
    
    if sys.show_sorted_nodes:
        print("\n\nSORTED NODES:")
        for node in sorted_nodes:
            str = node.to_str(sys)
            if str: print(str)
        print("\n")
    
    if sys.show_stack_objects:
        print("\n\nVIRTUAL STACK:")
        for ptr in sys.virtual_stack.stack.keys():
            str = sys.virtual_stack.stack[ptr].to_str(sys)
            if str: print(str)
        print("\n")
    

def run_compiled(code, argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10):
    global sys
    sys = system(code, argv1)

    if argv1 == "-help":
        sys.process_help_flag(argv2)
        exit(0)

    sys.process_argv(argv2)
    sys.process_argv(argv3)
    sys.process_argv(argv4)
    sys.process_argv(argv5)
    sys.process_argv(argv6)
    sys.process_argv(argv7)
    sys.process_argv(argv8)
    sys.process_argv(argv9)
    sys.process_argv(argv10)

    lexer = Lexer(code)
    tokens = lexer.Phase1()
    tokens = lexer.Phase2()
    tokens_final = lexer.get_final_token_list(tokens)

    parser = Parser(tokens_final)
    nodes = parser.Parse()

    sortout = Sortout(nodes)
    sorted_nodes = sortout.Phase1()
    sorted_nodes = sortout.Phase2()
    sorted_nodes = sortout.Phase3()
    sorted_nodes = sortout.Finish()

    compiler = Compiler(sorted_nodes)
    compiler.compile()

    if sys.show_tokens:
        print("\n\nTOKENS:")
        for token in tokens:
            str = token.to_str(sys)
            if str: print(str)
        print("\n")

    if sys.show_nodes:
        print("\n\nNODES:")
        for node in nodes:
            str = node.to_str(sys)
            if str: print(str)
        print("\n")
    
    if sys.show_sorted_nodes:
        print("\n\nSORTED NODES:")
        for node in sorted_nodes:
            str = node.to_str(sys)
            if str: print(str)
        print("\n")


def get_code(path):
    global sys
    if path == "-help": return ""

    try:
        file = io.open(path, "r")
        code = file.read()
        file.close()
        return code
    except Exception as e:
        sys = system("", no_stack = True)
        sys.error_system.create_error_from_exception(e, PYTHON_EXCEPTION, TERMINAL, -1)
        sys.error_system.throw_errors()


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
            if not self.currChar in VALID_CHARS:
                sys.error_system.create_error(INVALID_CHARACTER_EXCEPTION, LEXING, f"The character '{self.currChar}' is invalid!", self.ln)
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
            elif self.currChar == '@':
                self.tokens.append(token(T_ADD, '>', self.ln))
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
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return self.tokens

    def word(self):
        str_value = self.currChar
        condition = lambda: True if self.currChar in IDENTIFIER_CHARS + NUMBER_CHARS else False

        while self.advance_condition(condition):
            str_value += self.currChar
        
        type = T_KEYWORD if str_value in KEYWORDS else T_IDENTIFIER
        type = T_TOKEN if str_value in TOKENS else type
        type = T_BOOL if str_value in BOOLEAN else type
        type = T_BUILTIN_FUNCTION if str_value in BUILTIN_FUNCTION else type
        return token(type, str_value, self.ln)

    def comment(self):
        self.advance()
        condition = lambda: True if not self.currChar == "\n" else False
        if self.currChar == "\n": return token(T_COMMENT, '', self.ln)
    
        str_value = self.currChar
        while self.advance_condition(condition):
            str_value += self.currChar

        return token(T_COMMENT, str_value, self.ln)
    
    def string(self):
        self.advance()
        condition = lambda: True if not self.currChar in '"\n' else False
        if self.currChar in '"\n': return token(T_STRING, '', self.ln)
    
        str_value = self.currChar
        while self.advance_condition(condition):
            str_value += self.currChar

        type = T_STRING
        return token(type, str_value, self.ln)

    def number(self):
        global sys
        str_value = self.currChar
        condition = lambda: True if self.currChar in NUMBER_CHARS + '.' else False
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
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return self.tokens

    def simplify_token(self, token_list, idx):
        try:
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
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, SIMPLIFYING)

        return token_list

    def simplify_identifier(self, token_list, idx):
        try:
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
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, SIMPLIFYING)

        return token_list

    def simplify_identifier_arg(self, token_list, idx):
        try:
            identifier = token_list[idx]
            followed_by = token_list[idx + 1]

            if followed_by.typeof(T_LT):
                type = T_EXTERN_FUNCTION
                token_list, params = self.simplify_params(token_list, idx + 1)
                new_token = token(type, identifier.str_value, identifier.ln, params)

                token_list[idx] = new_token
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, SIMPLIFYING)

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

            if param_token.typeof(T_IDENTIFIER):
                token_list = self.simplify_identifier_arg(token_list, idx + 1 + param_idx)
                param_token = token_list[idx + 1 + param_idx]
                params.append(param_token)
                more_params = False
            elif param_token.type in [T_INT, T_FLOAT, T_STRING, T_BOOL]:
                params.append(param_token)
                more_params = False
            elif not param_token.type in [T_COMMA, T_WHITESPACE]:
                sys.error_system.create_error(INVALID_PARAM_DECLARATION_EXCEPTION, SIMPLIFYING, f"The parameter type of '{get_token_type_str(param_token.type)}' is invalid!", param_token.ln)

            param_idx += 1

        for i in range(param_idx + 2):
            token_list.pop(idx)

        return token_list, params

    def get_final_token_list(self, token_list):
        final_token_list = []
        for token in self.tokens:
            if token.type in [T_COMMENT, T_WHITESPACE]:
                continue
            final_token_list.append(token)

        return final_token_list


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.expression_types       = [T_IDENTIFIER, T_STRING, T_BOOL, T_INT, T_FLOAT, T_KEYWORD, T_ADD, T_BUILTIN_FUNCTION, T_EXTERN_FUNCTION]
        self.section_types          = [T_SECTION, T_START]
        self.token_types            = [T_TOKEN, T_HIVE, T_END]
        self.member_value_types     = [TOKEN, INT, FLOAT, STRING, BOOL]
        self.variable_value_types   = [EXTERN, IDENTIFIER, TOKEN, INT, FLOAT, STRING, BOOL, TAKE]
        self.inv_condition_types    = [N_VALUE, N_FUNCTION]
        self.inv_expr_properties    = [BUILTIN, EXTERN]
        self.valid_operators        = ["is", "not", "in"]
        self.valid_param_types      = [IDENTIFIER, INT, FLOAT, STRING, BOOL, EXTERN]

        self.node_list = []
        self.idx = 0

    def Parse(self):
        
        while self.idx < len(self.tokens):
            currToken = self.tokens[self.idx]

            if currToken.type in self.expression_types:
                expr = self.expr(self.tokens)
                if expr: self.node_list.append(expr)
            elif currToken.type in self.section_types:
                self.node_list.append(self.section(self.tokens))
            elif currToken.type in self.token_types:
                self.node_list.append(self.token(self.tokens))
            elif not currToken.str_value in " \\n\\t\\r":
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The token '{currToken.str_value}' is invalid at it's current position.", currToken.ln)

            self.idx += 1

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return self.node_list

    def expr(self, tokens = None, token = None):
        try:
            currToken = tokens[self.idx] if not token else token

            if currToken.typeof(T_BUILTIN_FUNCTION):
                if currToken.has_value("inv"):
                    return self.inv(tokens)
                if currToken.has_value("other"):
                    return self.other(tokens)
                if currToken.has_value("flyout"):
                    return self.flyout(tokens)
                if currToken.has_value("flyto"):
                    return self.flyto(tokens)
                if currToken.has_value("wax"):
                    return self.wax(tokens)
                if currToken.has_value("sting"):
                    return self.sting(tokens)
                if currToken.has_value("take"):
                    return self.take(tokens)

                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, PARSING, f"The expression '{currToken.str_value}' is invalid.", currToken.ln)
                return None
            elif currToken.typeof(T_EXTERN_FUNCTION):
                return self.extern_function(tokens, token)
            elif currToken.typeof(T_STRING):
                return self.string(currToken.str_value, currToken.ln)
            elif currToken.type in [T_INT, T_FLOAT]:
                return self.number(currToken.type, currToken.str_value, currToken.ln)
            elif currToken.typeof(T_BOOL):
                return self.boolean(currToken.str_value, currToken.ln)
            elif currToken.typeof(T_IDENTIFIER):
                if token: return self.simple_identifier(token)
                return self.identifier(tokens)
            elif currToken.typeof(T_TOKEN):
                return self.token(tokens)
            elif currToken.typeof(T_KEYWORD):
                return self.keyword(tokens)
            elif currToken.typeof(T_ADD):
                return self.addToken(tokens)
            elif currToken.typeof(T_NEWLINE):
                return None
        except:
            return None

    def section(self, tokens):
        section = tokens[self.idx]
        properties = [SECTION]
        type = N_START if section.typeof(T_START) else N_SECTION
        value = self.simple_identifier(section)
        return node(type, section.ln, properties, value=value)

    def addToken(self, tokens):
        try:
            add = tokens[self.idx]

            self.idx += 1
            followed_by = self.expr(tokens)
            if not followed_by or not followed_by.has_property(IDENTIFIER):
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "A valid identifier must follow an '@' character", add.ln)
            elif not followed_by.ptr in ADDTOKENS:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The addtoken of type '{followed_by.ptr}' is not valid.", add.ln)

            properties = [BUILTIN, ADDTOKEN]
            return node(N_ADDTOKEN, add.ln, properties, value = followed_by)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def keyword(self, tokens):
        keyword = tokens[self.idx]
        properties = []
        if keyword.has_value("honey"):      properties.append(HONEY)
        if keyword.has_value("stick"):      properties.append(STICK)
        
        if keyword.has_value("honeypot"):   
            properties.append(BUILTIN)
            properties.append(HONEYPOT)
            properties.append(LIST)

            self.idx += 1
            list = self.expr(tokens)
            if not list or not list.has_property(IDENTIFIER) or list.has_property(BUILTIN):
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "A honeycomb can only be defined with an identifier.", keyword.ln)

            return node(N_FUNCTION, keyword.ln, properties, value = list) 
        return node(N_FUNCTION, keyword.ln, properties, value = keyword.str_value)

    def token(self, tokens):
        token = tokens[self.idx]
        type = N_END if token.typeof(T_END) else N_TOKEN
        type = N_HIVE if token.typeof(T_HIVE) else type

        params = None
        if token.params:
            params = self.params(token)
        
        properties = [BUILTIN, TOKEN]
        properties.append(get_node_property_by_value(token.str_value))
        return node(type, token.ln, properties, params = params )

    def extern_function(self, tokens, token = None):
        try:
            function = tokens[self.idx] if not token else token
            params = self.params(function)
            properties = [EXTERN, IDENTIFIER]
            
            n = node(N_FUNCTION, function.ln, properties, params = params) 
            n.set_ptr(function.str_value)
            return n       
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def params(self, token):
        try:
            params = []
            for p in token.params:
                param = self.expr(token = p)
                params.append(param)
            
            return params
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)
        
    def operators(self, tokens):
        try:
            ops = []
            op_idx = 0
            while True:
                op = tokens[self.idx + op_idx]

                if op_idx == 0:
                    if not op.typeof(T_KEYWORD) or not op.str_value in self.valid_operators:
                        sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "Expected a valid operator (" + ' '.join(op for op in self.valid_operators) + ").", op.ln)
                elif not op.typeof(T_KEYWORD) or not op.str_value in self.valid_operators:
                    break

                ops.append(op)
                op_idx += 1

            self.idx += op_idx - 1
            return ops
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def inv(self, tokens):
        try:
            inv = tokens[self.idx]
            
            self.idx += 1
            left = self.expr(tokens)
            if not left:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The left condition element is missing.", inv.ln)
            elif not left.type in self.inv_condition_types:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The condition element of type '{get_node_type_to_str(left.type)}' is invalid.", inv.ln)
        
            self.idx += 1
            operators = self.operators(tokens)
            
            self.idx += 1
            right = self.expr(tokens)
            if not right:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The right condition element is missing.", inv.ln)
            elif not right.type in self.inv_condition_types:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, f"The condition element of type '{get_node_type_to_str(right.type)}' is invalid.", inv.ln)
        
            self.idx += 1
            expr = self.expr(tokens)
            if not expr or expr.has_property(TOKEN) or not any(p in self.inv_expr_properties for p in expr.properties):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, PARSING, f"The inv-statement cannot be left without a following expression.", inv.ln)

            other = None
            followed_by = tokens[self.idx + 2]
            if followed_by and followed_by.has_value("other"):
                self.idx += 2
                other = self.expr(tokens)

            properties = [BUILTIN, INV]
            if other: properties.append(OTHER)

            return node(N_FUNCTION, inv.ln, properties, [left, right, other], expr, operators = operators)        
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def other(self, tokens):
        try:
            other = tokens[self.idx]

            self.idx += 1
            expr = self.expr(tokens)
            if not expr or expr.has_property(TOKEN) or not any(p in self.inv_expr_properties for p in expr.properties):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, PARSING, f"The other-statement cannot be left without a following expression.", other.ln)

            properties = [BUILTIN, OTHER]
            return node(N_FUNCTION, other.ln, properties, value = expr)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def flyout(self, tokens):
        try:
            flyout = tokens[self.idx]

            self.idx += 1
            value = self.expr(tokens)
            if not value or not value.type in [N_VALUE, N_FUNCTION]:
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "Expected a value (string, number,...).", flyout.ln)

            properties = [BUILTIN, FLYOUT]

            return node(N_FUNCTION, flyout.ln, properties, value = value)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def flyto(self, tokens):
        try:
            flyto = tokens[self.idx]

            self.idx += 1
            section = self.expr(tokens)
            if not section or not section.has_property(IDENTIFIER) or section.has_property(BUILTIN):
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "Expected an identifier of a section.", flyto.ln)

            properties = [BUILTIN, FLYTO]

            return node(N_FUNCTION, flyto.ln, properties, value = section)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def wax(self, tokens):
        try:
            wax = tokens[self.idx]

            self.idx += 1
            name = self.expr(tokens)
            if not name or not name.has_property(IDENTIFIER):
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, PARSING, "Expected an identifier as the member's name.", wax.ln)

            self.idx += 1
            value = self.expr(tokens)
            if not value:
                sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "The meadow member must have a value!", wax.ln)
            elif not any(item in self.member_value_types for item in value.properties):
                sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, PARSING, f"A meadow member cannot hold a value of type '{get_node_type_to_str(value.type)}' with properties like [" + ' '.join(get_node_property_to_str(p) for p in value.properties) + "]", wax.ln)

            properties = [BUILTIN, WAX, MEADOW_MEMBER]

            return node(N_FUNCTION, wax.ln, properties, name, value)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def sting(self, tokens):
        try:
            sting = tokens[self.idx]

            self.idx += 1
            value = self.expr(tokens)
            if not value or not all(item is IDENTIFIER for item in value.properties):
                sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "Expected a valid identifier.", sting.ln)

            properties = [BUILTIN, STING]

            return node(N_FUNCTION, sting.ln, properties, value = value)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def take(self, tokens):
        try:
            take = tokens[self.idx]

            self.idx += 1
            list = self.expr(tokens)
            if not list or not all(item is IDENTIFIER for item in list.properties):
                sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "Expected a valid identifier of a list.", take.ln)

            self.idx += 1
            idx = self.expr(tokens)
            if not idx or not all(item is INT for item in idx.properties):
                sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "Expected an idx.", take.ln)

            properties = [BUILTIN, TAKE]

            return node(N_FUNCTION, take.ln, properties, list, idx)
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def string(self, str_value, ln):
        return node(N_VALUE, ln, [STRING], value=str_value)
    
    def number(self, type, number, ln):
        property = INT if type is T_INT else FLOAT
        return node(N_VALUE, ln, [property], value=number)

    def boolean(self, boolean, ln):
        return node(N_VALUE, ln, [BOOL], value=boolean)
    
    def simple_identifier(self, token):
        try:
            identifier = token
            n = node(N_VALUE, identifier.ln, [IDENTIFIER])
            n.set_ptr(identifier.str_value)
            return n
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def identifier(self, tokens):
        try:
            identifier = tokens[self.idx]

            if len(tokens) >= self.idx + 2: 
                following = tokens[self.idx + 1]
                if following.typeof(T_KEYWORD) and following.has_value("honey"):
                    self.idx += 2
                    value = self.expr(tokens)
                    if not value:
                        sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "The variable must have a value!", identifier.ln)
                    elif not any(item in self.variable_value_types for item in value.properties):
                        sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, PARSING, f"A variable cannot hold a value of type '{get_node_type_to_str(value.type)}' with properties like [" + ' '.join(get_node_property_to_str(p) for p in value.properties) + "]", identifier.ln)

                    name = self.simple_identifier(identifier)
                    properties = [BUILTIN, HONEY, IDENTIFIER]
                    return node(N_FUNCTION, identifier.ln, properties, name, value)
                elif following.typeof(T_KEYWORD) and following.has_value("stick"):
                    self.idx += 2
                    value = self.expr(tokens)
                    if not value:
                        sys.error_system.create_error(NO_VALUE_EXCEPTION, PARSING, "Some value is requiered in order to push something to a list.", identifier.ln)
                    elif not any(item in self.variable_value_types for item in value.properties) or value.has_property(BUILTIN):
                        sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, PARSING, f"A list cannot hold a value of type '{get_node_type_to_str(value.type)}' with properties like [" + ' '.join(get_node_property_to_str(p) for p in value.properties) + "]", identifier.ln)

                    name = self.simple_identifier(identifier)
                    properties = [BUILTIN, STICK, IDENTIFIER]
                    return node(N_FUNCTION, identifier.ln, properties, name, value)

            n = node(N_VALUE, identifier.ln, [IDENTIFIER])
            n.set_ptr(identifier.str_value)
            return n
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)


class Sortout:
    def __init__(self, nodes, library = False, preset_unused_vars = None, preset_used_var_names = None, sections = None):
        self.nodes = nodes

        self.valid_meadow_properties = [WAX, FUNCTIONPTR, HONEYCOMB, PYTHON, FUNCTIONPTR, MEADOW]
        self.valid_meadow_value_properties = [PYTHON, HONEYCOMB]
        self.stack_objects = [SECTION, WAX]
        self.valid_expressions = [FLYTO, FLYOUT, INV, TAKE, STING, WAX, HONEY, STICK, TOKEN, SECTION, EXTERN, HONEYPOT]
        self.valid_addtoken_expressions = [FLYOUT, INV, HONEY, STICK, EXTERN]
        self.valid_onetime_expressions = [HONEY]
        self.valid_threaded_expressions = [FLYOUT, INV, HONEY, STICK, EXTERN]
        self.valid_await_expressions = [FLYOUT, INV, HONEY, STICK, EXTERN]
        self.valid_readonly_expressions = [HONEY]
        self.tokens_with_parmas = [PYTHON, SRC]
        self.tokens_only_string_args = [PYTHON, SRC, END]
        self.constant_values = [INT, FLOAT, STRING, BOOL]
        
        self.used_var_names = {} if not preset_used_var_names else preset_used_var_names
        self.used_sections = ["start"]
        self.sections = [] if not sections else sections
        self.unused_variables = [] if not preset_unused_vars else preset_unused_vars
        self.currSection = ""
        self.idx = 0
        self.end = False
        self.library = library

    def Phase1(self):
        nodes = self.Sortout_param_check(self.nodes)
        nodes = self.libraries(nodes)
        nodes = self.Sortout_inv(nodes)
        nodes = self.Sortout_addtoken(nodes)
        nodes = self.Sortout_others(nodes)
        self.nodes = nodes
        return self.nodes

    def Sortout_param_check(self, nodes):
        for n in nodes:
            if n.has_property(TOKEN):
                has_params = True if n.params else False
                if has_params: param_len = len(n.params)
                
                if has_params:
                    if param_len > 1:
                        if n.has_property(END):
                            sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT,  "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] can only have one argument.", n.ln)
                        elif any(p in self.tokens_with_parmas for p in n.properties):
                            sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] can only have one argument.", n.ln)
                    elif not n.has_property(END) and not n.has_property(HONEYCOMB) and not any(p in self.tokens_with_parmas for p in n.properties):
                        sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] cannot have arguments.", n.ln)
                elif any(p in self.tokens_with_parmas for p in n.properties):
                    sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] has to have one argument.", n.ln)

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return nodes

    def libraries(self, nodes):
        updated_nodes = []

        for n in nodes:
            if n.has_property(SRC):
                params = n.params
                lib_path = params[0].value
                lib_path = lib_path.replace("[CURRDIR]", os.getcwd())
                code = get_code(lib_path)
                if not code:
                    sys.error_system.create_error(LIBRARY_NOT_FOUND_EXCEPTION, SORTOUT, f"The meadow at '{params[0].value}' does not exist.", n.ln)
                    break

                script = sys.error_system.script
                sys.error_system.script = lib_path

                lexer = Lexer(code)
                tokens = lexer.Phase1()
                tokens = lexer.Phase2()
                tokens_final = lexer.get_final_token_list(tokens)

                parser = Parser(tokens_final)
                meadow = parser.Parse()

                idx = 0
                for member in meadow:
                    if idx == 0 and not member.typeof(N_TOKEN) and not member.has_property(MEADOW):
                        sys.error_system.create_error(FALSE_LIB_USAGE_EXCEPTION, SORTOUT, "The script you are trying to use as a meadow does not fulfill all meadow-definition-standards.", member.ln)
                    elif not any(p in self.valid_meadow_properties for p in member.properties):
                        sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SORTOUT, "A meadow member cannot have the following property-constellation [" + ' '.join(get_node_property_to_str(p) for p in member.properties) + "]", member.ln)
                    
                    idx += 1
                
                sys.error_system.script = script
                properties = [MEADOW]
                path = parser.string(lib_path, n.ln)
                lib = node(N_LIB, n.ln, properties, meadow, path) 
                updated_nodes.append(lib)
            else:
                updated_nodes.append(n) 

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return updated_nodes

    def Sortout_inv(self, nodes):
        updated_nodes = []

        for n in nodes:
            if n.has_property(INV):
                left = n.child[0]
                right = n.child[1]

                is_op = False
                if (n.operator_count("not") % 2) == 0:
                    is_op = True

                if n.operator_count("is") > 1:
                    sys.error_system.create_error(INVALID_OPERATION_EXCEPTION, SORTOUT, "An inv-statement cannot have more than one 'is' operator.", n.ln)
                elif n.operator_count("in") > 1:
                    sys.error_system.create_error(INVALID_OPERATION_EXCEPTION, SORTOUT, "An inv-statement cannot have more than one 'in' operator.", n.ln)
                elif n.has_operator("is") and n.has_operator("in"):
                    sys.error_system.create_error(INVALID_OPERATION_EXCEPTION, SORTOUT, "An inv-statement cannot have the operator combination [is in].", n.ln)
                elif n.has_operator("not") and not n.has_operator("is") and not n.has_operator("in"):
                    sys.error_system.create_error(INVALID_OPERATION_EXCEPTION, SORTOUT, "An inv-statement cannot only have 'not' operators.", n.ln)

                if any(p in self.constant_values for p in left.properties) and any(p in self.constant_values for p in right.properties):
                    if not left.value == right.value and is_op or left.value == right.value and not is_op:
                        sys.error_system.create_warning(USELESS_INV_EXPRESSION, SORTOUT, "The left and right condition of the inv-statement will never be true.", n.ln)
                        n.add_property(ALWAYS_FALSE)
                        continue
                    else:
                        sys.error_system.create_warning(USELESS_INV_EXPRESSION, SORTOUT, "The left and right condition of the inv-statement are constant values and will never change the outcome of the statement.", n.ln)
                        n.add_property(ALWAYS_TRUE)

            updated_nodes.append(n)

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return updated_nodes

    def Sortout_addtoken(self, nodes):
        updated_nodes = []
        
        addtoken = None
        type = None
        valid = True
        for n in nodes:
            if addtoken:
                type = get_addtoken_property_by_value(addtoken.value.ptr)
                if any(p in self.valid_addtoken_expressions for p in n.properties):                    
                    if type is ONETIME:
                        if not any(p in self.valid_onetime_expressions for p in n.properties):
                            valid = False
                            break
                    elif type is THREADED:
                        if not any(p in self.valid_threaded_expressions for p in n.properties):
                            valid = False
                            break
                    elif type is READONLY:
                        if not any(p in self.valid_readonly_expressions for p in n.properties):
                            valid = False
                            break
                    elif type is AWAIT:
                        if not any(p in self.valid_threaded_expressions for p in n.properties):
                            valid = False
                            break

                    n.add_property(type)
                else:
                    updated_nodes.append(addtoken)
                    updated_nodes.append(n)
                    
                addtoken = None

            if n.has_property(ADDTOKEN):
                addtoken = n
                continue

            updated_nodes.append(n)
            
        if not valid:
            sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, SORTOUT, f"The @-token of type '{get_addtoken_property_to_str(type)}' cannot be applied to an expression with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "].", n.ln)

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return updated_nodes

    def Sortout_others(self, nodes):
        start_section = False
        hive_start = False
        inside_hive = False
        hive_end = False
        for n in nodes:
            if n.has_property(ADDTOKEN):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, SORTOUT, "There cannot be a single @-token somewhere in the script.", n.ln)
            if n.has_property(SECTION):
                if not n.value.ptr in self.sections:
                    self.sections.append(n.value.ptr)
            if n.typeof(N_START):
                if start_section:
                    sys.error_system.create_error(MULTI_START_EXCEPTION, SORTOUT, "There can only be one start section.", n.ln)
                start_section = True
            if n.typeof(N_HIVE):
                if not hive_start:
                    hive_start = True
                    inside_hive = True
                elif hive_start:
                    if hive_end:
                        sys.error_system.create_error(MULTI_HIVE_EXCEPTION, SORTOUT, "There can only be one hive section, defined by two hive tokens.", n.ln)
                    else:
                        hive_end = True
                        inside_hive = False
                elif hive_end:
                    sys.error_system.create_error(MULTI_HIVE_EXCEPTION, SORTOUT, "There can only be one hive section, defined by two hive tokens.", n.ln)
            if n.has_property(HONEYPOT) and not inside_hive:
                sys.error_system.create_error(EXPECTED_HIVE_SECTION_EXCEPTION, SORTOUT, "A honeypot can only be defined inside a hive section.", n.ln)
            if not n.has_property(HONEYPOT) and not n.has_property(HIVE) and hive_start and not hive_end:
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, SORTOUT, "An expression with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] cannot be inside a hive section.", n.ln)
            if n.typeof(N_VALUE):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, SORTOUT, "There cannot be single values somewhere in the script.", n.ln)
            if (n.has_property(HONEY) or n.has_property(STICK)) and not n.has_property(BUILTIN):
                sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SORTOUT, "A keyword like 'honey' and 'stick' cannot stand alone in the script.", n.ln)
            if n.has_property(OTHER) and not n.has_property(INV):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, SORTOUT, "An other-statement cannot be alone in a script.", n.ln)

        if not start_section and not self.library:
            sys.error_system.create_error(MISSING_START_SECTION_EXCEPTION, SORTOUT, "There has to be a start section in a script! This will be the starting point for the interpreter.", 1)
        if hive_start and not hive_end:
            sys.error_system.create_error(EXPECTED_HIVE_SECTION_EXCEPTION, SORTOUT, "The hive section has to be closed of with another hive token.")

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return nodes

    def Phase2(self):
        idx = 0
        for n in self.nodes:
            n.idx = idx
            if any(p in self.stack_objects for p in n.properties):
                sys.virtual_stack.init_var(n)

            idx += 1
            
        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return self.nodes

    def Phase3(self):
        start = sys.virtual_stack.get_var_by_ptr("start") if not self.library else None
        skipped_vars = []
        self.unused_variables.extend([(list[0], list[1], False) if list[1] == "list" else skipped_vars.append(list) for list in self.used_var_names.items()])
        self.currSection = "start" if start else ""
        self.idx = start.idx if start else 0

        while self.idx < len(self.nodes):
            currNode = self.nodes[self.idx]

            if any(p in self.valid_expressions for p in currNode.properties):
                self.Phase3_expr(currNode)
            elif currNode.typeof(N_LIB):
                self.Phase3_lib(currNode)

            if self.end: break
            self.idx += 1

        for item in skipped_vars:
            sys.error_system.create_silent(SORTOUT, f"The variable '{item[0]} [{item[1]}]' was skipped durring Phase3 of the Sortout.")
        for item in self.unused_variables:
            if not item[1] == "member" and not item[2] and not self.library:
                sys.error_system.create_warning(UNUSED_VARIABLE, SORTOUT, f"The variable '{item[0]} [{item[1]}]' is never used in the program.")

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        return self.nodes    
        
    def Phase3_expr(self, currNode, execute_jumps = True):
        if any(p in self.valid_meadow_properties for p in currNode.properties) and not self.library:
            sys.error_system.create_error(FALSE_LIB_FUNCTION_USAGE_EXCEPTION, SORTOUT, "You cannot use library specific code inside a regular script.", currNode.ln)

        if currNode.has_property(INV):
            self.Phase3_inv(currNode)
        elif currNode.has_property(FLYOUT):
            self.Phase3_flyout(currNode)
        elif currNode.has_property(FLYTO) and execute_jumps:
            self.Phase3_flyto(currNode)
        elif currNode.has_property(HONEY):
            self.Phase3_honey(currNode)
        elif currNode.has_property(STICK):
            self.Phase3_stick(currNode)
        elif currNode.has_property(TAKE):
            self.Phase3_take(currNode)
        elif currNode.has_property(WAX):
            self.Phase3_wax(currNode)
        elif currNode.has_property(TOKEN):
            self.end = self.Phase3_token(currNode)
        elif currNode.has_property(EXTERN):
            self.Phase3_extern(currNode)
        elif currNode.has_property(STING):
            self.Phase3_sting(currNode)
        elif currNode.has_property(HONEYPOT):
            self.Phase3_list(currNode)
        elif currNode.has_property(IDENTIFIER):
            self.Phase3_identifier(currNode)

    def Phase3_inv(self, currNode):
        left = currNode.child[0]
        right = currNode.child[1]
        expr = currNode.value

        defined_left, var_left = False, None
        defined_right, var_right = False, None

        if left.has_property(IDENTIFIER): defined_left, var_left = self.Phase3_is_defined(left.ptr, currNode.ln)
        if right.has_property(IDENTIFIER): defined_right, var_right = self.Phase3_is_defined(right.ptr, currNode.ln)

        if not currNode.has_operator("in") and (defined_left and var_left[1] == "list" and (not defined_right or not var_right[1] == "list") or defined_right and var_right[1] == "list" and (not defined_left or not var_left[1] == "list")):
            sys.error_system.create_error(INVALID_TYPE_EXCEPTION, SORTOUT, "If a component of a condition is an identifier of a list, it can only be compared to another list.", currNode.ln)
        elif currNode.has_operator("in") and defined_left and defined_right and var_left[1] == "list" and var_right[1] == "list":
            sys.error_system.create_error(INVALID_TYPE_EXCEPTION, SORTOUT, "A list cannot be inside a list.", currNode.ln)
        elif currNode.has_operator("in") and defined_left and defined_right and var_left[1] == "list" and not var_right[1] == "list":
            sys.error_system.create_error(INVALID_TYPE_EXCEPTION, SORTOUT, "You can only check if a value is in a list.", currNode.ln)
    
        self.Phase3_expr(left)
        self.Phase3_expr(right)
        if currNode.has_property(ALWAYS_TRUE): self.Phase3_expr(expr, True)

    def Phase3_flyout(self, currNode):
        value = currNode.value
        self.Phase3_expr(value)

    def Phase3_take(self, currNode):
        list = currNode.child

        defined, var = self.Phase3_is_defined(list.ptr, currNode.ln)
        if defined and not var[1] == "list":
            sys.error_system.create_error(INVALID_TYPE_EXCEPTION, SORTOUT, "The provided identifier has to be one from a list.", currNode.ln)

        self.Phase3_expr(list)

    def Phase3_honey(self, currNode):
        value = currNode.value
        tuple = (currNode.child.ptr, "variable", False)
        defined, var = self.Phase3_is_defined(currNode.child.ptr, currNode.ln, True)

        self.Phase3_expr(value)
        if defined and var[1] == "list":
            sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, f"The identifier '{currNode.child.ptr}' is already taken by another object.", currNode.ln)
        elif currNode.child.ptr in self.sections:
            sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, SORTOUT, f"The pointer '{currNode.child.ptr}' is already used by a section.", currNode.ln)
        elif not defined:
            self.unused_variables.append(tuple)

        defined, var = self.Phase3_is_defined(currNode.value.ptr, currNode.ln)
        if defined and var[1] == "list" and not currNode.value.params:
            sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, "You cannot define a variable with a list.", currNode.ln)

    def Phase3_stick(self, currNode):
        defined, var = self.Phase3_is_defined(currNode.child.ptr, currNode.ln)
        if defined and not var[1] == "list":
            sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, "You can only stick a value to a valid list.", currNode.ln)

        self.Phase3_expr(currNode.child)

        defined, var = self.Phase3_is_defined(currNode.value.ptr, currNode.ln)
        if defined and var[1] == "list" and not currNode.value.params:
            sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, "You cannot add a list to a list.", currNode.ln)
        
        self.Phase3_expr(currNode.value)

    def Phase3_identifier(self, currNode):
        updated_unused_variables = []
        object_found = False

        for item in self.unused_variables:
            ptr = item[0]
            type = item[1]
            used = item[2]

            if ptr == currNode.ptr:
                object_found = True
                updated_unused_variables.append((ptr, type, True))
            else:
                updated_unused_variables.append(item)

        if not object_found:
            sys.error_system.create_error(VARIABLE_NOT_FOUND_EXCEPTION, SORTOUT, f"The data object '{currNode.ptr}' is not defined.", currNode.ln)

        self.unused_variables = updated_unused_variables

    def Phase3_wax(self, currNode):
        tuple = (currNode.child.ptr, "member", False)
        defined, var = self.Phase3_is_defined(currNode.child.ptr, currNode.ln, True)

        if defined:
            sys.error_system.create_error(MEMBER_NAME_COLLISION, SORTOUT, f"The name '{currNode.child.ptr}' seems to be already taken by another variable. Change the variable name or the meadow member name.", currNode.ln)
        elif currNode.child.ptr in self.sections:
            sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, SORTOUT, f"The pointer '{currNode.child.ptr}' is already used by a section.", currNode.ln)
        elif not defined:
            self.unused_variables.append(tuple)

        if currNode.value.typeof(N_TOKEN):
            if not any(p in self.valid_meadow_value_properties for p in currNode.value.properties):
                sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, SORTOUT, "A meadow member can only have a token as it's value, if it features one of the following properties [" + ' '.join(get_node_property_to_str(p) for p in self.valid_meadow_value_properties) + "]")

        self.Phase3_expr(currNode.value)

    def Phase3_token(self, currNode):
        if not currNode.params and currNode.has_property(HONEYCOMB):
            sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, SORTOUT, "A honeycomb token has to have at least one argument.", currNode.ln)
        elif not currNode.params and any(p in self.tokens_with_parmas for p in currNode.properties):
            sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in currNode.properties) + "] has to have one argument.", currNode.ln)
        elif currNode.params and len(currNode.params) > 1 and any(p in self.tokens_with_parmas for p in currNode.properties):
            sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in currNode.properties) + "] can only have one argument.", currNode.ln)

        if currNode.params:
            self.Phase3_params(currNode)

        if currNode.typeof(N_END):
            return True

        return False

    def Phase3_lib(self, currNode):
        if not currNode.has_property(LOADED):
            script = sys.error_system.script
            sys.error_system.script = currNode.value.value
            self.nodes[self.idx].add_property(LOADED)
            sortout = Sortout(currNode.child, True, self.unused_variables, sections = self.sections)
            sortout.Phase1()
            sortout.Phase2()
            sortout.Phase3()
            self.unused_variables = sortout.unused_variables
            sys.error_system.script = script

    def Phase3_flyto(self, currNode):
        section_ptr = currNode.value.ptr
        if not section_ptr in sys.virtual_stack.stack.keys():
            sys.error_system.create_error(INVALID_SECTION_EXCEPTION, SORTOUT, f"The section '{section_ptr}' is not defined.", currNode.ln)

        section = sys.virtual_stack.get_var_by_ptr(section_ptr)
        if not section or not section.has_property(SECTION):
            sys.error_system.create_error(INVALID_SECTION_EXCEPTION, SORTOUT, f"The section '{section_ptr}' is not a valid section.", currNode.ln)
        else:
            if not section_ptr in self.used_sections:
                self.used_sections.append(section_ptr)
                self.currSection = section_ptr
                self.idx = section.idx
            else:
                sys.error_system.create_silent(SORTOUT, "There might the chance of an infinite loop...", currNode.ln)

    def Phase3_list(self, currNode):
        tuple = (currNode.value.ptr, "list", False)
        defined, var = self.Phase3_is_defined(currNode.value.ptr, currNode.ln, True)

        if defined:
            sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, f"The identifier '{currNode.value.ptr}' is already taken by another object.", currNode.ln)
        else:
            self.unused_variables.append(tuple)

    def Phase3_sting(self, currNode):
        defined, var = self.Phase3_is_defined(currNode.value.ptr, currNode.ln)
        self.Phase3_expr(currNode.value)

        if defined and var[1] == "member":
            sys.error_system.create_warning(STUNG_INVINCIBLE_MEMBER, SORTOUT, "A meadow member is constant. Thus it cannot be destroyed.", currNode.ln)
        elif defined and not var[1] == "member":
            self.Phase3_del_defined(currNode.value.ptr)

    def Phase3_extern(self, currNode):
        self.Phase3_identifier(currNode)
        defined, var = self.Phase3_is_defined(currNode.ptr, currNode.ln)

        if defined and var[1] == "list" and len(currNode.params) > 1:
            sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A list identifier only expects one argument, which is acting as the idx.", currNode.ln)

        if currNode.params:
            self.Phase3_params(currNode)

    def Phase3_params(self, currNode):
        for param in currNode.params:
            if any(p in self.tokens_only_string_args for p in currNode.properties):
                if not currNode.params[0].has_property(STRING):
                    sys.error_system.create_error(INVALID_PARAM_DECLARATION_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in currNode.properties) + "] can only have one string message argument.", currNode.ln)
            elif currNode.has_property(HONEYCOMB):
                if not param.has_property(IDENTIFIER):
                    sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SORTOUT, "A honeycomb token can only have identifiers as arguments.", currNode.ln)
            elif currNode.params and len(currNode.params) > 1 and any(p in self.tokens_with_parmas for p in currNode.properties):
                    sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in currNode.properties) + "] can only have one argument.", currNode.ln)

            if not currNode.has_property(HONEYCOMB):
                self.Phase3_expr(param)

    def Phase3_is_defined(self, var_ptr, ln, define_var = False):
        defined = False
        var = None
        for item in self.unused_variables:
            ptr = item[0]
            type = item[1]
            used = item[2]

            if ptr == var_ptr:
                if define_var and type == "member":
                    sys.error_system.create_error(MEMBER_NAME_COLLISION, SORTOUT, f"The name '{var_ptr}' seems to be already taken by a meadow member.", ln)

                defined = True
                var = item

        return defined, var 
    
    def Phase3_del_defined(self, var_ptr):
        updated_list = []
        for item in self.unused_variables:
            if not item[0] == var_ptr:
                updated_list.append(item)
        
        self.unused_variables = updated_list

    def Finish(self):
        virtual_stack = sys.virtual_stack.stack.copy()

        for item in virtual_stack.items():
            if item[1].has_property(WAX):
                sys.virtual_stack.del_var(item[0])

        for n in self.nodes:
            if n.typeof(N_LIB) and n.has_property(LOADED):
                n.pop_property(LOADED)

        return self.nodes


class Interpreter:
    def __init__(self, nodes):
        self.function_properties = [FLYTO, FLYOUT, INV, TAKE, STING]
        self.invalid_expression = [PYTHON, HONEYCOMB]
        self.regular_values = [INT, FLOAT, BOOL, STRING]
        self.nodes = nodes
        self.idx = 0
        self.should_exit = False
        self.init_functionptr = False
        self.in_library = False
        self.every_data = False

    def execute(self):
        start = sys.virtual_stack.get_var_by_ptr("start")
        self.idx = start.idx
        self.ln = -1

        while self.idx < len(self.nodes):
            self.idx += 1
            if self.idx >= len(self.nodes):
                sys.error_system.create_warning(MISSING_END_TOKEN_EXCEPTION, INTERPRETING, "Unexpected eof! Use an end token to exit properly.", self.ln)
                break

            currNode = self.nodes[self.idx]
            self.ln = currNode.ln
            
            if any(p in self.invalid_expression for p in currNode.properties):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, INTERPRETING, "A expression with the properties [" + ' '.join(p in self.invalid_expression for p in currNode.properties) + "] is invalid.", currNode.ln)
                break

            self.expression(currNode)
            if self.should_exit: break
        
        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.create_silent(sys.show_silent_warnings)

    def expression(self, currNode):
        if any(p in self.function_properties for p in currNode.properties):
            if currNode.has_property(THREADED) or currNode.has_property(AWAIT):
                threading.Thread(target=self.functions, args=[currNode]).start()
                return
            self.functions(currNode)
        elif currNode.has_property(TOKEN):
            self.tokens(currNode)
        elif currNode.has_property(HONEY):
            if currNode.has_property(THREADED) or currNode.has_property(AWAIT):
                threading.Thread(target=self.honey, args=[currNode]).start()
                return
            self.honey(currNode)
        elif currNode.has_property(STICK):
            if currNode.has_property(THREADED) or currNode.has_property(AWAIT):
                threading.Thread(target=self.stick, args=[currNode]).start()
                return
            self.stick(currNode)
        elif currNode.has_property(HONEYPOT):
            self.honeypot(currNode)
        elif currNode.has_property(EXTERN):
            if currNode.has_property(THREADED) or currNode.has_property(AWAIT):
                threading.Thread(target=self.extern, args=[currNode]).start()
                return
            self.extern(currNode)
        elif currNode.typeof(N_LIB):
            if not currNode.has_property(LOADED):
                self.library(currNode)
                self.nodes[self.idx].add_property(LOADED)

    def functions(self, currNode):
        if currNode.has_property(FLYOUT):
            value = self.extract_value(currNode.value, True if currNode.has_property(AWAIT) else False)
            if not value:
                sys.error_system.create_error(NO_VALUE_EXCEPTION, INTERPRETING, f"The object you tried to flyout to doesn't carry a value. Thus you cannot use the object as a value.", currNode.ln)
                self.should_exit = True
            else: print(value.value)
        elif currNode.has_property(FLYTO):
            section = sys.virtual_stack.get_var(currNode.value)
            self.idx = section.idx
        elif currNode.has_property(STING):
            var = currNode.value
            sys.virtual_stack.del_var(var)
        elif currNode.has_property(TAKE):
            self.take(currNode)
        elif currNode.has_property(INV):
            self.inv(currNode)

    def extern(self, currNode):
        value = sys.virtual_stack.get_var(currNode)
        params = currNode.params

        if value.has_property(LIST):
            if not len(params) == 1:
                sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, "A list identifier only excepts one argument, which is the idx.", currNode.ln)
                self.should_exit = True

            valid, idx = self.validate_list_idx(value.child, params[0], currNode.ln)
            if valid:
                value = value.child[idx]
                return self.extract_value(value)
        elif value.has_property(FUNCTIONPTR):
            function = value.value
            func_name = function.__name__
            arg_count = sys.get_function_arg_count(func_name)

            if not arg_count == -1: 
                if len(params) < arg_count:
                    sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, INTERPRETING, f"The extern function '{func_name}' expects {arg_count} arguments instead of just {len(params)} arguments.", currNode.ln)
                    self.should_exit = True
                    return None
                elif len(params) > arg_count:
                    sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, INTERPRETING, f"The extern function '{func_name}' expects only {arg_count} arguments instead of {len(params)} arguments.", currNode.ln)
                    self.should_exit = True
                    return None

            check = self.validate_arg_types(func_name, params, currNode.ln, True if currNode.has_property(AWAIT) else False)
            if not check: return None

            final_params = self.translate_params_to_lib_format(currNode)
            return_value = function(final_params)
            return_value = self.translate_return_to_node_format(return_value, currNode.ln)

            return return_value
        elif value.has_property(WAX):
            value = self.extract_value(value)
            if not len(params) == len(value.params):
                sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, f"The honeycomb identifier expects {len(value.params)} argument.", currNode.ln)
                self.should_exit = True
            
            final_params = [self.extract_value(v) for v in currNode.params]
            final_params = [self.extract_lib_value(v) for v in final_params]
            return self.translate_return_to_node_format(final_params, currNode.ln)
        elif value.value and value.value.has_property(OBJECT):
            if not len(params) == 1:
                sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, "An honeycomb identifier only excepts one argument, which is the idx.", currNode.ln)
                self.should_exit = True

            valid, idx = self.validate_list_idx(value.value.child, params[0], currNode.ln)
            if valid:
                value = value.value.child[idx]
                return self.extract_value(value)

    def honey(self, currNode):
        honey = currNode.copy()
        value = self.extract_value(honey.value, True if currNode.has_property(AWAIT) else False)
        ptr = honey.child.ptr
        honey.value = value

        if not value:
            sys.error_system.create_error(NO_VALUE_EXCEPTION, INTERPRETING, f"The object you tried to asign to {ptr} doesn't carry a value. Thus you cannot use the object as a value.", honey.ln)
            self.should_exit = True
        elif value.has_property(OBJECT):
            honey.add_property(EXTERN)

        if sys.virtual_stack.isset(ptr):
            if sys.virtual_stack.get_var_by_ptr(ptr).has_property(READONLY):
                sys.error_system.create_error(INVALID_OPERATION_EXCEPTION, STACK, f"The variable '{ptr}' is marked as readonly and thus a constant.", currNode.ln)
                return
            sys.virtual_stack.set_var(honey)
        else:
            sys.virtual_stack.init_var(honey)

    def stick(self, currNode):
        value = self.extract_value(currNode.value, True if currNode.has_property(AWAIT) else False)
        ptr = currNode.child.ptr
        currNode.value = value
        sys.virtual_stack.stack[ptr].child.append(value)

    def wax(self, currNode):
        value = None
        if self.init_functionptr:
            if not currNode.value.has_property(PYTHON):
                sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, INTERPRETING, "This member is initialized as a function pointer. It can only hold the python-token.", currNode.ln)
                self.should_exit = True
                return

            value = self.functionptr(currNode)
            currNode.add_property(FUNCTIONPTR)
            self.init_functionptr = False
        elif not self.init_functionptr and currNode.value.has_property(PYTHON):
            sys.error_system.create_error(INVALID_MEMBER_VALUE_EXCEPTION, INTERPRETING, "Did not expect a function pointer! First the member has to be initialized as a function pointer via the functionptr-token.", currNode.ln)
            self.should_exit = True
            return
        else:
            value = self.extract_value(currNode.value)
        
        ptr = currNode.child.ptr
        currNode.value = value

        if sys.virtual_stack.isset(ptr):
            sys.virtual_stack.set_var(currNode)
        else:
            sys.virtual_stack.init_var(currNode)

    def honeypot(self, currNode):
        ptr = currNode.value.ptr
        currNode.child = []
        sys.virtual_stack.init_var(currNode)

    def take(self, currNode):
        list = sys.virtual_stack.get_var(currNode.child)

        valid, idx = self.validate_list_idx(list.child, currNode.value.value, currNode.ln)
        if valid:
            del list.child[idx]
            sys.virtual_stack.set_var(list)

    def inv(self, currNode):
        not_condition = False
        if currNode.has_operator("not"):
            op_count = currNode.operator_count("not")
            not_condition = False if (op_count % 2) == 0 else True

        left = currNode.child[0]
        right = currNode.child[1]

        self.every_data = True
        value_left = self.extract_lib_value(self.extract_value(left, True if currNode.has_property(AWAIT) else False))
        value_right = self.extract_lib_value(self.extract_value(right, True if currNode.has_property(AWAIT) else False))
        self.every_data = False

        if not value_left:
            sys.error_system.create_error(NO_VALUE_EXCEPTION, INTERPRETING, "The left condition value doesn't carry any value. Thus it cannot be compared to the right condition value.", currNode.ln)
            self.should_exit = True
            return
        if not value_right:
            sys.error_system.create_error(NO_VALUE_EXCEPTION, INTERPRETING, "The right condition value doesn't carry any value. Thus it cannot be compared to the left condition value.", currNode.ln)
            self.should_exit = True
            return

        condition_succeded = False
        if currNode.has_operator("is"):
            if not_condition:
                if not value_left == value_right:
                    if currNode.has_property(AWAIT): currNode.value.add_property(AWAIT)
                    self.expression(currNode.value)
                    condition_succeded = True
            else:
                if value_left == value_right:
                    if currNode.has_property(AWAIT): currNode.value.add_property(AWAIT)
                    self.expression(currNode.value)
                    condition_succeded = True
        elif currNode.has_operator("in"):
            if not_condition:
                if not any(item is value_left for item in value_right):
                    if currNode.has_property(AWAIT): currNode.value.add_property(AWAIT)
                    self.expression(currNode.value)
                    condition_succeded = True
            else:
                if any(item is value_left for item in value_right):
                    if currNode.has_property(AWAIT): currNode.value.add_property(AWAIT)
                    self.expression(currNode.value)
                    condition_succeded = True

        if not condition_succeded and currNode.has_property(OTHER):
            if currNode.has_property(AWAIT): currNode.child[2].value.add_property(AWAIT)
            self.expression(currNode.child[2].value)

    def validate_list_idx(self, list, param, ln):
        idx = -1
        check = True
        idx_value = param.value if not param.has_property(IDENTIFIER) else self.extract_value(param).value
        try: idx = int(idx_value) 
        except Exception as e:
            sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, "A list identifier only excepts a number as it's parameter.", ln)
            self.should_exit = True
            check = False
        
        if idx > (len(list) - 1) or idx < 0:
            sys.error_system.create_error(INDEX_OUT_OF_RANGE_EXCEPTION, INTERPRETING, "The idx was outside the range of the list you tried to access.", ln)
            self.should_exit = True
            check = False
        
        return check, idx

    def validate_arg_types(self, func_name, params, ln, _await=False):
        check = True
        arg_count = sys.get_function_arg_count(func_name)
        arg_types = sys.get_function_arg_types(func_name)

        if arg_count == -1:
            param_types = []
            for p in params:
                if p.has_property(IDENTIFIER):
                    p = self.extract_value(p, _await)

                for property in p.properties:
                    type = get_value_type_to_lib_value_type(property)
                    if type: param_types.append(type)

            if not arg_types[0] == L_ANY:
                if not all(type == arg_types[0] for type in param_types):
                    sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, f"All parameters have to be of type {get_lib_value_type_to_str(arg_types[0])}.", ln)
                    self.should_exit = True
                    check = False
            return check

        idx = 0
        for p in params:
            if arg_types[idx] == L_ANY: continue

            if p.has_property(IDENTIFIER):
                p = self.extract_value(p, _await)

            param_types = []
            for property in p.properties:
                type = get_value_type_to_lib_value_type(property)
                if type: param_types.append(type)

            if arg_types[idx] == L_NUMBER:
                if not any(type in [L_INT, L_FLOAT] for type in param_types):
                    sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, f"The {idx + 1}. parameter has to be of type {get_lib_value_type_to_str(arg_types[idx])}.", ln)
                    self.should_exit = True
                    check = False
            else:
                if not any(type == arg_types[idx] for type in param_types):
                    sys.error_system.create_error(INVALID_ARGUMENT_EXCEPTION, INTERPRETING, f"The {idx + 1}. parameter has to be of type {get_lib_value_type_to_str(arg_types[idx])}.", ln)
                    self.should_exit = True
                    check = False

            idx += 1
        
        return check

    def translate_params_to_lib_format(self, currNode):
        types = self.regular_values
        types.append(LIST)
        types.append(OBJECT)
        types
        final_params = []
        for p in currNode.params:
            value = None
            if p.has_property(IDENTIFIER):
                if p.has_property(EXTERN):
                    value = self.extract_value(p)
                else:
                    value = sys.virtual_stack.get_var(p)
            else:
                value = self.extract_value(p)
            
            if any(p in types for p in value.properties):
                final_params.append(self.extract_lib_value(value))
            else:
                value = self.extract_value(value)
                final_params.append(self.extract_lib_value(value))

        return final_params

    def translate_return_to_node_format(self, return_value, ln):
        if isinstance(return_value, (int, float, str, bool)):
            return self.regular_value_to_node(return_value, ln)
        if isinstance(return_value, list) or isinstance(return_value, tuple):
            final_list = [self.regular_value_to_node(v, ln) for v in list(return_value)]
            object = node(N_VALUE, ln, [OBJECT], child = final_list)
            object.value = "[ <object> honeycomb ]"
            return object

    def regular_value_to_node(self, return_value, ln):
        parser = Parser(None)
        if str(return_value) in ["True", "False"]:
            return parser.boolean(str(return_value).lower(), ln)
        if isinstance(return_value, int):
            return parser.number(T_INT, str(return_value), ln)
        if isinstance(return_value, float):
            return parser.number(T_FLOAT, str(return_value), ln)
        if isinstance(return_value, str):
            return parser.string(str(return_value), ln)

    def extract_value(self, value, _await=False):
        if hasattr(value, "__call__"):
            return Parser(None).string(f"{value.__name__}: [ <object> function ]", -1)

        if value.has_property(HONEY):
            if value.has_property(ONETIME):
                sys.virtual_stack.del_var(value.child)
            return value.value
        elif value.has_property(HONEYPOT):
            if not value.params and not self.every_data:
                return Parser(None).string(f"{value.value.ptr}: [ <object> honeypot ]", value.ln)
            return value
        elif value.has_property(EXTERN):
            if _await: value.add_property(AWAIT)
            return self.extern(value)
        elif value.has_property(WAX):
            return self.extract_value(value.value)
        elif value.has_property(IDENTIFIER):
            if _await:
                while (True):
                    if sys.virtual_stack.isset(value): break            
                    sleep(.25)

            value = sys.virtual_stack.get_var(value)
            value = self.extract_value(value, _await)
            return value
        elif value.has_property(TOKEN):
            token = self.tokens(value)
            return token
        elif value.has_property(OBJECT):
            return value
        elif any(p in self.regular_values for p in value.properties):
            return value

    def extract_lib_value(self, value):
        if value.has_property(INT):
            return int(value.value)
        if value.has_property(FLOAT):
            return float(value.value)
        if value.has_property(BOOL):
            return True if value.value == "true" else False
        if value.has_property(STRING):
            return value.value
        if value.has_property(LIST) or value.has_property(OBJECT):
            return [self.extract_lib_value(v) for v in value.child]

    def tokens(self, currNode):
        if currNode.typeof(N_END):
            self.should_exit = True
            if currNode.params:
                msg = currNode.params[0].value
                print(msg)
        elif currNode.has_property(TRACE):
            print(f"[INTERPRETER] executing line {self.ln}...")
        elif currNode.has_property(FUNCTIONPTR):
            self.init_functionptr = True
        elif currNode.has_property(MEADOW):
            self.in_library = True
        elif currNode.has_property(HONEYCOMB):
            currNode.value = "[ <object> honeycomb ]"
            return currNode
        
    def functionptr(self, currNode):
        if not currNode.value.has_property(PYTHON):
            sys.error_system.create_error(WRONG_TOKEN_TYPE_EXCEPTION, INTERPRETING, "A function pointer was expected. Make sure the provided value of the member points to an extern python function.", currNode.ln)

        try:
            python_module = currNode.value.params[0].value
            sub_modules = python_module.split('.')
            del sub_modules[0]

            module = __import__(python_module)
            for sub in sub_modules:
                module = getattr(module, sub)

            function = getattr(module, currNode.child.ptr)
            arg_count = getattr(module, f"{currNode.child.ptr}_arg_count")
            arg_types = getattr(module, f"{currNode.child.ptr}_arg_types")
            sys.init_extern_function(currNode.child.ptr, arg_count, arg_types)
            return function
        except Exception as e:
            sys.error_system.create_error_from_exception(e, PYTHON_EXCEPTION, INTERPRETING, currNode.ln)

    def library(self, currNode):
        script = sys.error_system.script
        sys.error_system.script = currNode.value.value

        self.init_functionptr = False
        for member in currNode.child:
            if member.has_property(WAX):
                self.wax(member)
            elif member.has_property(PYTHON) or member.has_property(HONEYCOMB):
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, INTERPRETING, "Tokens with the properties [PYTHON | HONEYCOMB] can only act as a member value and cannot act as an expression.", currNode.ln)
                self.should_exit = True
                break
            elif member.has_property(TOKEN):
                self.tokens(member)
        
        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent(sys.show_silent_warnings)
        sys.error_system.script = script
        self.in_library = False


class Compiler:
    def __init__(self, nodes):
        self.nodes = nodes
        self.script = ""
        self.script_path = "./a.asm"
        self.obj_path = "./a.bin"

    def create_script(self):
        if os.path.exists(self.script_path):
            os.remove(self.script_path)

        with open(self.script_path, "x") as file:
            file.write(self.script)
            file.close()

        os.system("nasm -f bin a.asm -o a.bin")
        os.system("chmod +x a.bin")
        os.system("./a.bin")

        #if os.path.exists(self.obj_path):
        #    os.remove(self.obj_path)

    def compile(self):
        self.script = """section .data
    text db "Hello, World!",10
 
section .text
    global _start
 
_start:
    mov ah, 0x0e
    mov al, [text]
    int 0x10
        """
        self.create_script()
