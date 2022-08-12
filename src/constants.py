#####################################################
# TOKEN types
#####################################################

from gzip import READ


T_IDENTIFIER            = 0xa01
T_KEYWORD               = 0xa02
T_TOKEN                 = 0xa03
T_BUILTIN_FUNCTION      = 0xa04
T_EXTERN_FUNCTION       = 0xa05
T_SECTION               = 0xa06
T_START                 = 0xa07
T_END                   = 0xa08
T_HIVE                  = 0xa09
T_GT                    = 0xa10
T_LT                    = 0xa11
T_FLOAT                 = 0xa12
T_INT                   = 0xa13
T_STRING                = 0xa14
T_BOOL                  = 0xa15
T_COMMENT               = 0xa16
T_COMMA                 = 0xa17
T_COLON                 = 0xa18
T_QUOTE                 = 0xa19
T_SYMBOL                = 0xa20
T_NEWLINE               = 0xa21
T_WHITESPACE            = 0xa22
T_ADD                   = 0xa23

#####################################################
# NODE types
#####################################################

N_TOKEN                 = 0xb01
N_FUNCTION              = 0xb02
N_SECTION               = 0xb03
N_START                 = 0xb04
N_END                   = 0xb05
N_HIVE                  = 0xb06
N_VALUE                 = 0xb07
N_PARAM                 = 0xb08
N_LIB                   = 0xb09
N_ADDTOKEN              = 0xb10

#####################################################
# NODE properties
#####################################################

MEADOW_MEMBER           = 0xc01
HIVE_START              = 0xc02
HIVE_END                = 0xc03
INV                     = 0xc04
FLYOUT                  = 0xc05
FLYTO                   = 0xc06
STING                   = 0xc07
HONEY                   = 0xc08
TAKE                    = 0xc09
WAX                     = 0xc10
FLOAT                   = 0xc11
INT                     = 0xc12
BOOL                    = 0xc13
STRING                  = 0xc14
TOKEN                   = 0xc15
BUILTIN                 = 0xc16
EXTERN                  = 0xc17
HONEYCOMB               = 0xc18
PYTHON                  = 0xc19
FUNCTIONPTR             = 0xc20
SRC                     = 0xc21
MEADOW                  = 0xc22
END                     = 0xc23
TRACE                   = 0xc24
HIVE                    = 0xc25
HONEYPOT                = 0xc26
STICK                   = 0xc27
LIST                    = 0xc28
IDENTIFIER              = 0xc29
SECTION                 = 0xc30
LOADED                  = 0xc31
ALWAYS_TRUE             = 0xc32
ALWAYS_FALSE            = 0xc33
OBJECT                  = 0xc34
OTHER                   = 0xc35
ADDTOKEN                = 0xc36
ONETIME                 = 0xc37
THREADED                = 0xc38
READONLY                = 0xc39
AWAIT                   = 0xc40

#####################################################
# ERROR codes
#####################################################

VARIABLE_NOT_FOUND_EXCEPTION            = 0xd01
NO_VALUE_EXCEPTION                      = 0xd02
INDEX_OUT_OF_RANGE_EXCEPTION            = 0xd03
FALSE_SYNTAX_EXCEPTION                  = 0xd04
FALSE_LIB_USAGE_EXCEPTION               = 0xd05
LIBRARY_NOT_FOUND_EXCEPTION             = 0xd06
FALSE_LIB_FUNCTION_USAGE_EXCEPTION      = 0xd07
INVALID_MEMBER_VALUE_EXCEPTION          = 0xd08
MISSING_START_SECTION_EXCEPTION         = 0xd09
INVALID_CHARACTER_EXCEPTION             = 0xd10
EXPECTED_HIVE_SECTION_EXCEPTION         = 0xd11
MISSING_ARGUMENTS_EXCEPTION             = 0xd12
INVALID_EXPRESSION_EXCEPTION            = 0xd13
INVALID_PARAM_DECLARATION_EXCEPTION     = 0xd14
INVALID_MATH_OPERATION                  = 0xd15
INVALID_LIST_USAGE_EXCEPTION            = 0xd16
INVALID_NUMBER_EXCEPTION                = 0xd17
MULTI_HIVE_EXCEPTION                    = 0xd18
MULTI_START_EXCEPTION                   = 0xd19
WRONG_TOKEN_TYPE_EXCEPTION              = 0xd20
TERMINAL_EXCEPTION                      = 0xd21
SILENT_EXCEPTION                        = 0xd22
TOO_MANY_ARGUMENTS_EXCEPTION            = 0xd23
INVALID_OPERATION_EXCEPTION             = 0xd24
INVALID_TYPE_EXCEPTION                  = 0xd25
INVALID_SECTION_EXCEPTION               = 0xd26
INVALID_ARGUMENT_EXCEPTION              = 0xd27
PYTHON_EXCEPTION                        = 0xd28

#####################################################
# WARNING codes
#####################################################

STUNG_INVINCIBLE_MEMBER                 = 0xe01
UNUSED_VARIABLE                         = 0xe02
MEMBER_NAME_COLLISION                   = 0xe03
INFINITE_LOOP                           = 0xe04
USELESS_INV_EXPRESSION                  = 0xe05
MISSING_END_TOKEN_EXCEPTION             = 0xe06

#####################################################
# WARNING codes
#####################################################

LEXING                  = 0xf01
SIMPLIFYING             = 0xf02
PARSING                 = 0xf03
SORTOUT                 = 0xf04
INTERPRETING            = 0xf05
TERMINAL                = 0xf06
STACK                   = 0xf07
SYSTEM                  = 0xf08
LIBRARY                 = 0xf09

#####################################################
# LIBRARY stuff (python)
#####################################################

# arg types
L_INT                   = 0xfa01
L_FLOAT                 = 0xfa02
L_STRING                = 0xfa03
L_BOOL                  = 0xfa04
L_OBJECT                = 0xfa05
L_LIST                  = 0xfa06
L_ANY                   = 0xfa07
L_NUMBER                = 0xfa08

#####################################################
# TO STRING functions
#####################################################

def get_exclamation_type_str(type):
    if type is PARSING:         return "PARSER"
    if type is SIMPLIFYING:     return "SIMPLIFYING"
    if type is LEXING:          return "LEXER"
    if type is SORTOUT:         return "SORTOUT"
    if type is INTERPRETING:    return "INTERPRETER"
    if type is TERMINAL:        return "TERMINAL"
    if type is STACK:           return "STACK"
    if type is SYSTEM:          return "SYSTEM"
    if type is LIBRARY:         return "LIBRARY"

def get_exclamation_code_str(code):
    if code is VARIABLE_NOT_FOUND_EXCEPTION:            return "VARIABLE_NOT_FOUND_EXCEPTION"                  
    if code is NO_VALUE_EXCEPTION:                      return "NO_VALUE_EXCEPTION"                  
    if code is INDEX_OUT_OF_RANGE_EXCEPTION:            return "INDEX_OUT_OF_RANGE_EXCEPTION"          
    if code is FALSE_SYNTAX_EXCEPTION:                  return "FALSE_SYNTAX_EXCEPTION"              
    if code is FALSE_LIB_USAGE_EXCEPTION:               return "FALSE_LIB_USAGE_EXCEPTION"            
    if code is LIBRARY_NOT_FOUND_EXCEPTION:             return "LIBRARY_NOT_FOUND_EXCEPTION"        
    if code is FALSE_LIB_FUNCTION_USAGE_EXCEPTION:      return "FALSE_LIB_FUNCTION_USAGE_EXCEPTION"  
    if code is INVALID_MEMBER_VALUE_EXCEPTION:          return "INVALID_MEMBER_VALUE_EXCEPTION"      
    if code is MISSING_START_SECTION_EXCEPTION:         return "MISSING_START_SECTION_EXCEPTION"    
    if code is INVALID_CHARACTER_EXCEPTION:             return "INVALID_CHARACTER_EXCEPTION"        
    if code is EXPECTED_HIVE_SECTION_EXCEPTION:         return "EXPECTED_HIVE_SECTION_EXCEPTION"    
    if code is MISSING_ARGUMENTS_EXCEPTION:             return "MISSING_ARGUMENTS_EXCEPTION"
    if code is TOO_MANY_ARGUMENTS_EXCEPTION:            return "TOO_MANY_ARGUMENTS_EXCEPTION"        
    if code is INVALID_EXPRESSION_EXCEPTION:            return "INVALID_EXPRESSION_EXCEPTION"          
    if code is INVALID_PARAM_DECLARATION_EXCEPTION:     return "INVALID_PARAM_DECLARATION_EXCEPTION"
    if code is INVALID_MATH_OPERATION:                  return "INVALID_MATH_OPERATION"            
    if code is INVALID_LIST_USAGE_EXCEPTION:            return "INVALID_LIST_USAGE_EXCEPTION"          
    if code is MULTI_HIVE_EXCEPTION:                    return "MULTI_HIVE_EXCEPTION"                  
    if code is MULTI_START_EXCEPTION:                   return "MULTI_START_EXCEPTION"
    if code is STUNG_INVINCIBLE_MEMBER:                 return "STUNG_INVINCIBLE_MEMBER"
    if code is UNUSED_VARIABLE:                         return "UNUSED_VARIABLE"        
    if code is MEMBER_NAME_COLLISION:                   return "MEMBER_NAME_COLLISION"  
    if code is INFINITE_LOOP:                           return "INFINITE_LOOP"                      
    if code is INVALID_NUMBER_EXCEPTION:                return "INVALID_NUMBER_EXCEPTION"
    if code is WRONG_TOKEN_TYPE_EXCEPTION:              return "WRONG_TOKEN_TYPE_EXCEPTION"
    if code is TERMINAL_EXCEPTION:                      return "TERMINAL_EXCEPTION"
    if code is SILENT_EXCEPTION:                        return "SILENT_EXCEPTION"
    if code is USELESS_INV_EXPRESSION:                  return "USELESS_INV_EXPRESSION"
    if code is INVALID_OPERATION_EXCEPTION:             return "INVALID_OPERATION_EXCEPTION"
    if code is INVALID_TYPE_EXCEPTION:                  return "INVALID_TYPE_EXCEPTION"
    if code is INVALID_SECTION_EXCEPTION:               return "INVALID_SECTION_EXCEPTION"
    if code is INVALID_ARGUMENT_EXCEPTION:              return "INVALID_ARGUMENT_EXCEPTION"
    if code is PYTHON_EXCEPTION:                        return "PYTHON_EXCEPTION"
    if code is MISSING_END_TOKEN_EXCEPTION:             return "MISSING_END_TOKEN_EXCEPTION"

def get_token_type_str(type):
    if type is T_IDENTIFIER:            return "IDENTIFIER"        
    if type is T_KEYWORD:               return "KEYWORD"           
    if type is T_TOKEN:                 return "TOKEN"             
    if type is T_BUILTIN_FUNCTION:      return "BUILTIN_FUNCTION"  
    if type is T_EXTERN_FUNCTION:       return "EXTERN_FUNCTION"   
    if type is T_SECTION:               return "SECTION"           
    if type is T_START:                 return "START"             
    if type is T_END:                   return "END"               
    if type is T_HIVE:                  return "HIVE"              
    if type is T_GT:                    return "GT"                
    if type is T_LT:                    return "LT"                
    if type is T_FLOAT:                 return "FLOAT"             
    if type is T_INT:                   return "INT"               
    if type is T_STRING:                return "STRING"            
    if type is T_BOOL:                  return "BOOL"              
    if type is T_COMMENT:               return "COMMENT"           
    if type is T_COMMA:                 return "COMMA"             
    if type is T_COLON:                 return "COLON"             
    if type is T_QUOTE:                 return "QUOTE"             
    if type is T_SYMBOL:                return "SYMBOL" 
    if type is T_NEWLINE:               return "NEWLINE"
    if type is T_WHITESPACE:            return "WHITESPACE"
    if type is T_ADD:                   return "ADD"           

def get_node_type_to_str(type):
    if type is N_TOKEN:                 return "TOKEN"  
    if type is N_FUNCTION:              return "FUNCTION" 
    if type is N_SECTION:               return "SECTION"  
    if type is N_START:                 return "START"    
    if type is N_END:                   return "END"      
    if type is N_HIVE:                  return "HIVE"     
    if type is N_VALUE:                 return "VALUE"    
    if type is N_PARAM:                 return "PARAM"
    if type is N_LIB:                   return "LIB"    
    if type is N_ADDTOKEN:              return "ADDTOKEN"

def get_node_property_to_str(property):
    if property is MEADOW_MEMBER:       return "MEADOW_MEMBER"
    if property is HIVE_START:          return "HIVE_START"   
    if property is HIVE_END:            return "HIVE_END"     
    if property is INV:                 return "INV"   
    if property is OTHER:               return "OTHER"       
    if property is FLYOUT:              return "FLYOUT"       
    if property is FLYTO:               return "FLYTO"        
    if property is STING:               return "STING"        
    if property is HONEY:               return "HONEY"        
    if property is TAKE:                return "TAKE"         
    if property is WAX:                 return "WAX"          
    if property is FLOAT:               return "FLOAT"        
    if property is INT:                 return "INT"          
    if property is BOOL:                return "BOOL"         
    if property is STRING:              return "STRING"       
    if property is TOKEN:               return "TOKEN"        
    if property is BUILTIN:             return "BUILTIN"      
    if property is EXTERN:              return "EXTERN"       
    if property is HONEYCOMB:           return "HONEYCOMB"    
    if property is PYTHON:              return "PYTHON"       
    if property is FUNCTIONPTR:         return "FUNCTIONPTR"  
    if property is SRC:                 return "SRC"          
    if property is MEADOW:              return "MEADOW"       
    if property is END:                 return "END"          
    if property is TRACE:               return "TRACE"        
    if property is HIVE:                return "HIVE"         
    if property is HONEYPOT:            return "HONEYPOT"     
    if property is STICK:               return "STICK"
    if property is LIST:                return "LIST"
    if property is IDENTIFIER:          return "IDENTIFIER"   
    if property is SECTION:             return "SECTION"
    if property is LOADED:              return "LOADED"        
    if property is ALWAYS_TRUE:         return "ALWAYS_TRUE"  
    if property is ALWAYS_FALSE:        return "ALWAYS_FALSE" 
    if property is OBJECT:              return "OBJECT"  
    if property is ADDTOKEN:            return "ADDTOKEN"   
    if property is READONLY:            return "READONLY"   
    if property is THREADED:            return "THREADED"   
    if property is ONETIME:             return "ONETIME"
    if property is AWAIT:               return "AWAIT"

def get_node_property_by_value(str_value):
    if str_value == "honeycomb":        return HONEYCOMB   
    if str_value == "python":           return PYTHON      
    if str_value == "functionptr":      return FUNCTIONPTR 
    if str_value == "src":              return SRC         
    if str_value == "meadow":           return MEADOW      
    if str_value == "end":              return END         
    if str_value == "trace":            return TRACE       
    if str_value == "hive":             return HIVE 

def get_addtoken_property_by_value(str_value):
    if str_value == "readonly":         return READONLY
    if str_value == "threaded":         return THREADED
    if str_value == "onetime":          return ONETIME
    if str_value == "await":            return AWAIT

def get_addtoken_property_to_str(type):
    if type is READONLY:                return "readonly"
    if type is THREADED:                return "threaded"
    if type is ONETIME:                 return "onetime"
    if type is AWAIT:                   return "await"

def get_value_type_to_lib_value_type(type):
    if type is INT:                     return L_INT
    if type is FLOAT:                   return L_FLOAT
    if type is STRING:                  return L_STRING
    if type is BOOL:                    return L_BOOL  
    if type is OBJECT:                  return L_OBJECT   
    if type is LIST:                    return L_LIST
    if type is EXTERN:                  return EXTERN

def get_lib_value_type_to_str(type):    
    if type == L_NUMBER:                return "NUMBER"
    if type == L_INT:                   return "INT"
    if type == L_FLOAT:                 return "FLOAT"
    if type == L_STRING:                return "STRING"
    if type == L_BOOL:                  return "BOOL"
    if type == L_OBJECT:                return "OBJECT"
    if type == L_LIST:                  return "LIST"
    if type == L_ANY:                   return "ANY"

def get_value_of_node(value):
    if value.has_property(INT):
        return int(value.value)
    if value.has_property(FLOAT):
        return float(value.value)
    if value.has_property(BOOL):
        return True if value.value == "true" else False
    if value.has_property(STRING):
        return value.value
        
#####################################################
# INTERPRETER stuff
#####################################################

IDENTIFIER_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜabcdefghijklmnopqrstuvwxyzäöü_'
NUMBER_CHARS = '-0123456789'
VALID_CHARS = IDENTIFIER_CHARS + NUMBER_CHARS + '\0\n\t<>:,#@\" '
KEYWORDS = [
    "true",
    "false",
    "is",
    "in",
    "honey",
    "stick",
    "honeypot",
    "not",
]
TOKENS = [
   "honeycomb",
   "python",
   "functionptr",
   "src",
   "meadow",
   "end",
   "trace",
   "hive"
]
BOOLEAN = [
    "true",
    "false"
]
BUILTIN_FUNCTION = [
    "inv",
    "other",
    "flyto",
    "flyout",
    "wax",
    "sting",
    "take"
]
ADDTOKENS = [
    "readonly",
    "threaded",
    "onetime",
    "await"
]
FATAL_ERRORS = [
    VARIABLE_NOT_FOUND_EXCEPTION,       
    NO_VALUE_EXCEPTION,                 
    INDEX_OUT_OF_RANGE_EXCEPTION,       
    FALSE_SYNTAX_EXCEPTION,             
    FALSE_LIB_USAGE_EXCEPTION,          
    LIBRARY_NOT_FOUND_EXCEPTION,        
    FALSE_LIB_FUNCTION_USAGE_EXCEPTION,
    INVALID_MEMBER_VALUE_EXCEPTION,    
    MISSING_START_SECTION_EXCEPTION,        
    EXPECTED_HIVE_SECTION_EXCEPTION,    
    MISSING_ARGUMENTS_EXCEPTION,
    TOO_MANY_ARGUMENTS_EXCEPTION,        
    INVALID_EXPRESSION_EXCEPTION,       
    INVALID_PARAM_DECLARATION_EXCEPTION,
    INVALID_MATH_OPERATION,            
    INVALID_LIST_USAGE_EXCEPTION,       
    INVALID_NUMBER_EXCEPTION,
    INVALID_CHARACTER_EXCEPTION,           
    MULTI_HIVE_EXCEPTION,               
    MULTI_START_EXCEPTION,              
    WRONG_TOKEN_TYPE_EXCEPTION,
    TERMINAL_EXCEPTION,
    INVALID_OPERATION_EXCEPTION,
    INVALID_TYPE_EXCEPTION,
    INVALID_SECTION_EXCEPTION,
    INVALID_ARGUMENT_EXCEPTION,
    PYTHON_EXCEPTION
]