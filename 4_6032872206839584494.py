import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], marker = '*')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Draw a line between two points')
    plt.grid(True)
    plt.show()
    
def main():
    x1 = float(input("Please Enter x of first point: "))
    y1 = float(input("Please Enter y of first point: "))
    x2 = float(input("Please Enter x of second point: "))
    y2 = float(input("Please Enter y of second point: "))
    
    draw_line(x1, y1, x2, y2)
    
if __name__ == "__main__":
    main()