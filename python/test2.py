from graphics import *

def main():
    win = GraphWin("My Circle", 640, 450, True)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse()
    win.close() 

if __name__ == "__main__":
    main()