from scipy.optimize import linprog


def preapare_result(c, a, b, bounds):
    return linprog(c, A_ub=a, b_ub=b, bounds=bounds, method='highs')