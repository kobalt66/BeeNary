from constants import *
from classes import *
import io


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
    except:
        print("An error occured while reading from a file.")

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
        self.expression_types       = [T_IDENTIFIER, T_KEYWORD, T_BUILTIN_FUNCTION, T_EXTERN_FUNCTION]
        self.section_types          = [T_SECTION, T_START]
        self.token_types            = [T_TOKEN, T_HIVE, T_END]
        self.member_value_types     = [TOKEN, INT, FLOAT, STRING, BOOL]
        self.variable_value_types   = [EXTERN, IDENTIFIER, TOKEN, INT, FLOAT, STRING, BOOL]
        self.inv_condition_types    = [N_VALUE]
        self.valid_operators        = ["is", "not", "in"]
        self.valid_param_types      = [IDENTIFIER, INT, FLOAT, STRING, BOOL]

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
                return self.extern_function(tokens)
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
            elif currToken.typeof(T_NEWLINE):
                return None
        except:
            return None

    def section(self, tokens):
        section = tokens[self.idx]
        properties = []
        type = N_START if section.typeof(T_START) else N_SECTION
        value = self.string(section.str_value, section.ln)
        return node(type, section.ln, properties, value=value)

    def keyword(self, tokens):
        keyword = tokens[self.idx]
        properties = [BUILTIN]
        if keyword.has_value("honey"):      properties.append(HONEY)
        
        if keyword.has_value("honeypot"):   
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

    def extern_function(self, tokens):
        try:
            function = tokens[self.idx]
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
            if not expr:
                sys.error_system.create_error(INVALID_EXPRESSION_EXCEPTION, PARSING, f"The inv-statement cannot be left without a following expression.", inv.ln)

            properties = [BUILTIN, INV]

            return node(N_FUNCTION, inv.ln, properties, [left, right], expr, operators = operators)        
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)

    def flyout(self, tokens):
        try:
            flyout = tokens[self.idx]

            self.idx += 1
            value = self.expr(tokens)
            if not value or not value.typeof(N_VALUE):
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
                    elif not any(item in self.variable_value_types for item in value.properties) or value.has_property(BUILTIN):
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

                    properties = [BUILTIN, STICK, IDENTIFIER]
                    return node(N_FUNCTION, identifier.ln, properties, value = value)

            n = node(N_VALUE, identifier.ln, [IDENTIFIER])
            n.set_ptr(identifier.str_value)
            return n
        except Exception as e:
            sys.error_system.create_silent_from_exception(e, PARSING)


class Sortout:
    def __init__(self, nodes):
        self.nodes = nodes
        self.valid_meadow_properties = [WAX, FUNCTIONPTR, HONEYCOMB, PYTHON, FUNCTIONPTR, MEADOW]
        self.tokens_with_parmas = [PYTHON, SRC]
        self.used_var_names = {}

    def Phase1(self):
        nodes = self.Sortout_param_check(self.nodes)
        nodes = self.libraries(nodes)
        nodes = self.Sortout_used(nodes)
        nodes = self.Sortout_inv(nodes)
        nodes = self.Sortout_unused(nodes)
        nodes = self.Sortout_loops(nodes)
        nodes = self.Sortout_others(nodes)
        self.nodes = nodes
        return self.nodes

    def Sortout_param_check(self, nodes):
        for n in nodes:
            if n.has_property(TOKEN):
                if not n.params and n.has_property(HONEYCOMB):
                    sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, SORTOUT, "A honeycomb token has to have at least one argument.", n.ln)
                elif n.params and n.has_property(HONEYCOMB):
                    if not all(param.has_property(IDENTIFIER) for param in n.params):
                        sys.error_system.create_error(FALSE_SYNTAX_EXCEPTION, SORTOUT, "A honeycomb token can only have identifiers as arguments.", n.ln)
                elif not n.params and any(p in self.tokens_with_parmas for p in n.properties):
                    sys.error_system.create_error(MISSING_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] has to have one argument.", n.ln)
                elif n.params and len(n.params) > 1 and any(p in self.tokens_with_parmas for p in n.properties):
                    sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] can only have one argument.", n.ln)
                elif n.params and not any(p in self.tokens_with_parmas for p in n.properties) and not n.has_property(HONEYCOMB):
                    sys.error_system.create_error(TOO_MANY_ARGUMENTS_EXCEPTION, SORTOUT, "A token with the properties [" + ' '.join(get_node_property_to_str(p) for p in n.properties) + "] cannot have arguments.", n.ln)

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def libraries(self, nodes):
        updated_nodes = []

        for n in nodes:
            if n.has_property(SRC):
                params = n.params
                lib_path = params[0].value
                code = get_code(lib_path)
                if not code:
                    sys.error_system.create_error(LIBRARY_NOT_FOUND_EXCEPTION, SORTOUT, f"The meadow at '{params[0].value}' does not exist.", n.ln)

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
        sys.error_system.throw_silent()
        return updated_nodes

    def Sortout_used(self, nodes):
        for n in nodes:
            if n.has_property(HONEY):
                if not n.child.ptr in self.used_var_names.keys():
                    self.used_var_names[n.child.ptr] = "variable"
                elif self.used_var_names[n.child.ptr] == "list":
                    sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, f"The identifier '{n.child.ptr}' is already used by a list.", n.ln)
            elif n.has_property(LIST):
                if not n.value.ptr in self.used_var_names:
                    self.used_var_names[n.value.ptr] = "list"
                else:
                    sys.error_system.create_error(INVALID_LIST_USAGE_EXCEPTION, SORTOUT, f"The identifier '{n.value.ptr}' is already used by some other variable!", n.ln)
            
        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def Sortout_inv(self, nodes):
        updated_nodes = []

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def Sortout_unused(self, nodes):
        updated_nodes = []

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def Sortout_loops(self, nodes):
        updated_nodes = []

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def Sortout_others(self, nodes):
        updated_nodes = []

        # if start exists
        # ...

        sys.error_system.throw_errors()
        sys.error_system.throw_warnings()
        sys.error_system.throw_silent()
        return nodes

    def Phase2(self):
        return self.nodes