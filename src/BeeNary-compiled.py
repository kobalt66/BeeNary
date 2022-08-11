try:        from interpreter import get_code, run_compiled
except:     from src.interpreter import get_code, run_compiled
try:        from classes import system
except:     from src.classes import system
import sys as s

def main():
    sys = system()
    argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10 = sys.process_argv_list(s.argv)

    code = get_code(argv1)
    run_compiled(code, argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10)

if __name__ == "__main__":
    main()