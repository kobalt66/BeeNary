import interpreter as BeeNary
import sys


code = BeeNary.get_code(sys.argv[1])
BeeNary.run(code, sys.argv[1])
#code = BeeNary.get_code("test.b")
#BeeNary.run(code, "test.b")