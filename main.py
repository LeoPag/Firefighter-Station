from grid import GridGUI

def main():

    """
    Define GridGUI parameters
    """
    alpha = 1
    max_iter = 10000
    epsilon  = 1e-2

    """
    Get and run GridGUI object
    """
    grid_gui = GridGUI(alpha, max_iter,epsilon)
    grid_gui.run()



if (__name__ == '__main__'):
    main()
