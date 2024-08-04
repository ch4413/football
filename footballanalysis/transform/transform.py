import pandas as pd

def results_points(a, b):
    """
    Returns the points for team a and b, based off their
    scores (W3, D1, L0)

    Parameters
    ----------
    a : int
    b : int
    goals of team a and goals of team b

    Returns
    -------
    list int
    List of values

    Examples
    --------
    results_points(1, 1) # reults [1, 1]
    """
    if a > b:
        return [3, 0]
    if b > a:
        return [0, 3]
    if b == a:
        return [1, 1]
    else:
        return ValueError


def get_points_by_week(df):
    """
    
    """
    new_df = df.copy()
    home = new_df[['Gameweek', 'HomeTeamID', 'HomePoints', 'HomeScore', 'AwayScore']].copy()
    away = new_df[['Gameweek', 'AwayTeamID', 'AwayPoints', 'AwayScore', 'HomeScore']].copy()
    cols = ['Gameweek', 'ID', 'Points', 'For', 'Against']
    home.columns = cols
    away.columns = cols
    points_by_week = pd.concat([home, away])
    return points_by_week

def print_a_string(string_to_print):
    """
    Prints an input string to the console, and also returns the string.

    Parameters
    ----------
    string_to_print : str
    The string to be printed to the console

    Returns
    -------
    string_to_print : str
    The string that was printed to the console

    Examples
    --------
    print_a_string('Hello Mango!')

    """

    print(string_to_print)

    return string_to_print
