import tkinter as tk
from minimizers import compute_centroid, compute_geometric_median

class GridGUI:
    def __init__(self, alpha = 0.01, max_iter = 1000000, epsilon = 1e-2):

        """
        Gradient descent hyperparameters
        """
        self.alpha = alpha
        self.max_iter = max_iter
        self.epsilon = epsilon

        self.points = []


        """
        Create grid
        """
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.canvas.create_line(50, 450, 450, 450, arrow=tk.LAST)
        self.canvas.create_line(50, 450, 50, 50, arrow=tk.LAST)
        self.canvas.create_text(250, 470, text="X", font=("Arial", 12, "bold"))
        self.canvas.create_text(20, 250, text="Y", font=("Arial", 12, "bold"))


        """
        Define events
        """
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("<Return>", self.on_enter)

    def on_click(self, event):
        x = event.x
        y = event.y
        self.points.append((x, y))
        self.draw_point(x, y,'black')

    def on_enter(self, event):
        """
        Print houses coordinates
        """
        print("Houses are located at the following points:")
        for point in self.points:
            print(point)

        """
        Compute minimizers
        """
        self.centroid = compute_centroid(self.points)
        self.geometric_median = compute_geometric_median(self.points, self.alpha, self.max_iter, self.epsilon)

        print("Geometric mean is: ", self.centroid)
        print("Geometric median is: ", self.geometric_median)

        """
        Draw minimizers
        """
        self.draw_point(self.centroid[0], self.centroid[1], "red")
        self.draw_point(self.geometric_median[0], self.geometric_median[1], "green")
        #self.root.destroy()
    """
    Draw points - The third argument defines the colour:
    'black' --> Houses
    'red'   --> Centroid
    'blue'  --> Geometric median
    """

    def draw_point(self, x, y,colour):
        x1 = x - 5
        y1 = y - 5
        x2 = x + 5
        y2 = y + 5

        self.canvas.create_oval(x1, y1, x2, y2, fill=colour)

    def run(self):
        self.root.mainloop()
