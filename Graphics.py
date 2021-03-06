"""
@package Graphics.py
Handles all the graphical functions of the program
"""

from rpy2 import robjects
from rpy2.robjects import Formula
from rpy2.robjects.packages import importr


def display_graphics(dataset):
    """
        Displays a plot of all the data points

        Args:
            dataset :pd.DataFrame:  a dataset

        Returns:
            N/A
    """

    # The R 'print' function
    rprint = robjects.globalenv.get("print")

    lattice = importr('lattice')

    formula = Formula('id ~ value')
    formula.getenvironment()['id'] = dataset['id'].tolist()
    formula.getenvironment()['value'] = dataset['value'].tolist()

    p = lattice.xyplot(formula)
    rprint(p)

    raw_input()
