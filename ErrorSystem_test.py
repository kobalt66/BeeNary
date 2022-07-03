import error_system as e
import constants as c

system = e.ErrorSystem("Test.b")
system.create_error(c.INVALID_CHARACTER_EXCEPTION, c.LEXING, "The character '|' is invalid!", 1)
system.create_error(c.INVALID_EXPRESSION_EXCEPTION, c.PARSING, "honey a 10? nope...", 100)
system.create_error(c.INVALID_MATH_OPPERATION, c.SORTOUT, "div div div a add 1", 19)
system.create_error(c.INVALID_PARAM_DECLARATION_EXCEPTION, c.INTERPRETING, "<a, b,>", 12)

system.create_warning(c.MEMBER_NAME_COLLISION, c.PARSING)
system.create_warning(c.MEMBER_NAME_COLLISION, c.PARSING)
system.create_warning(c.MEMBER_NAME_COLLISION, c.PARSING)
system.create_warning(c.MEMBER_NAME_COLLISION, c.PARSING)

system.throw_errors()
system.throw_warnings()