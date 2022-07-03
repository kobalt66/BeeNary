#####################################################
# TOKEN types
#####################################################

T_IDENTIFIER            = 0xa01
T_KEYWORD               = 0xa01
T_TOKEN                 = 0xa02
T_BUILTIN_FUNCTION      = 0xa03
T_EXTERN_FUNCTION       = 0xa04
T_SECTION               = 0xa05
T_START                 = 0xa06
T_END                   = 0xa07
T_HIVE                  = 0xa08
T_GT                    = 0xa09
T_LT                    = 0xa10
T_FLOAT                 = 0xa11
T_INT                   = 0xa12
T_STRING                = 0xa13
T_BOOL                  = 0xa14
T_COMMENT               = 0xa15
T_COMMA                 = 0xa16
T_COLON                 = 0xa17
T_QUOTE                 = 0xa18
T_HASH                  = 0xa19
T_SYMBOL                = 0xa20

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
WAX                     = 0xc08
FLOAT                   = 0xc09
INT                     = 0xc10
BOOL                    = 0xc11
STRING                  = 0xc12
TOKEN                   = 0xc13
BUILTIN                 = 0xc14
EXTERN                  = 0xc15

HONEYCOMB               = 0xc16
PYTHON                  = 0xc17
FUNCTIONPTR             = 0xc18
SRC                     = 0xc19
MEADOW                  = 0xc20
END                     = 0xc21
TRACE                   = 0xc22
HIVE                    = 0xc23

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
MULTI_HIVE_EXCEPTION                    = 0xd17
MULTI_START_EXCEPTION                   = 0xd18

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
PARSING                 = 0xf02
SORTOUT                 = 0xf03
INTERPRETING            = 0xf04

#####################################################
# TO STRING functions
#####################################################

def get_exclamation_type_str(type):
    if type is PARSING:      return "PARSER"
    if type is LEXING:       return "LEXER"
    if type is SORTOUT:      return "SORTOUT"
    if type is INTERPRETING: return "INTERPRETER"

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