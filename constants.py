#####################################################
# TOKEN types
#####################################################

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
INVALID_MATH_OPPERATION                 = 0xd15
INVALID_LIST_USAGE_EXCEPTION            = 0xd16
INVALID_NUMBER_EXCEPTION                = 0xd17
MULTI_HIVE_EXCEPTION                    = 0xd18
MULTI_START_EXCEPTION                   = 0xd19
WRONG_TOKEN_TYPE_EXCEPTION              = 0xd20
TERMINAL_EXCEPTION                      = 0xd21
SILENT_EXCEPTION                        = 0xd22
TOO_MANY_ARGUMENTS_EXCEPTION            = 0xd23

#####################################################
# WARNING codes
#####################################################

STUNG_INVINCIBLE_MEMBER                 = 0xe01
UNUSED_VARIABLE                         = 0xe02
MEMBER_NAME_COLLISION                   = 0xe03
INFINITE_LOOP                           = 0xe04

#####################################################
# WARNING codes
#####################################################

LEXING                  = 0xf01
SIMPLIFYING             = 0xf02
PARSING                 = 0xf03
SORTOUT                 = 0xf04
INTERPRETING            = 0xf05
TERMINAL                = 0xf06

#####################################################
# TO STRING functions
#####################################################

def get_exclamation_type_str(type):
    if type is PARSING:      return "PARSER"
    if type is SIMPLIFYING:  return "SIMPLIFYING"
    if type is LEXING:       return "LEXER"
    if type is SORTOUT:      return "SORTOUT"
    if type is INTERPRETING: return "INTERPRETER"
    if type is TERMINAL:     return "TERMINAL"

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
    if code is INVALID_MATH_OPPERATION:                 return "INVALID_MATH_OPPERATION"            
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

def get_node_type_to_str(type):
    if type is N_TOKEN:                 return "TOKEN"    
    if type is N_FUNCTION:              return "FUNCTION" 
    if type is N_SECTION:               return "SECTION"  
    if type is N_START:                 return "START"    
    if type is N_END:                   return "END"      
    if type is N_HIVE:                  return "HIVE"     
    if type is N_VALUE:                 return "VALUE"    
    if type is N_PARAM:                 return "PARAM"    

def get_node_property_to_str(property):
    if property is MEADOW_MEMBER:       return "MEADOW_MEMBER"
    if property is HIVE_START:          return "HIVE_START"   
    if property is HIVE_END:            return "HIVE_END"     
    if property is INV:                 return "INV"          
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

def get_node_property_by_value(str_value):
    if str_value == "honeycomb":        return HONEYCOMB   
    if str_value == "python":           return PYTHON      
    if str_value == "functionptr":      return FUNCTIONPTR 
    if str_value == "src":              return SRC         
    if str_value == "meadow":           return MEADOW      
    if str_value == "end":              return END         
    if str_value == "trace":            return TRACE       
    if str_value == "hive":             return HIVE        

#####################################################
# INTERPRETER stuff
#####################################################

IDENTIFIER_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
NUMBER_CHARS = '0123456789.'
VALID_CHARS = IDENTIFIER_CHARS + NUMBER_CHARS + '\0\n\t<>:,#\" '
KEYWORDS = [
    "true",
    "false",
    "is",
    "in",
    "honey",
    "stick",
    "honeypot",
    "not"
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
    "div",
    "add",
    "mul",
    "sub",
    "inv",
    "flyto",
    "flyout",
    "wax",
    "sting",
    "take"
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
    INVALID_EXPRESSION_EXCEPTION,       
    INVALID_PARAM_DECLARATION_EXCEPTION,
    INVALID_MATH_OPPERATION,            
    INVALID_LIST_USAGE_EXCEPTION,       
    INVALID_NUMBER_EXCEPTION,
    INVALID_CHARACTER_EXCEPTION,           
    MULTI_HIVE_EXCEPTION,               
    MULTI_START_EXCEPTION,              
    WRONG_TOKEN_TYPE_EXCEPTION,
    TERMINAL_EXCEPTION   
]