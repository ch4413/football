import numpy as np
import pandas as pd

from footballanalysis.transform.transform import results_points, get_points_by_week


def prob_result(hw, aw, d):
    """Convert encoding to Win, Lose, draw"""
    
    value = np.argmax(np.array([hw, aw, d])
                                )
    if value == 0:
        return 'HomeWin'
    if value == 1:
        return 'AwayWin'
    if value == 2:
        return 'Draw'
    else:
        return ValueError


def predict_match(homeid, awayid, gameweek, results_df):
    """ Take Home and Away IDs for a fixture and
    predict the result from the means of the simulated goals.
    Assign W, L, D and return dict
    """
    goals_1 = results_df[homeid]
    goals_2 = results_df[awayid]

    win = np.mean(goals_1 > goals_2)
    lose = np.mean(goals_1 < goals_2)
    draw = np.mean(goals_1 == goals_2)

    results = {'Gameweek': gameweek,'HomeTeamID': homeid, 'AwayTeamID': awayid,
               'HomeWin': win, 'AwayWin': lose, 'Draw': draw}
    return results


def create_sim_season(fixtures, sim_results, i):
    """Combine the base fixtures with a set of simulation
    results for goals scored. Get points per team by week using
     results_points, get_points_by_week
     """
    sim_fixtures = fixtures[['Gameweek', 'HomeTeamID', 'AwayTeamID']].copy()
    sim_fixtures['HomeScore'] = sim_results[:, 0, i]
    sim_fixtures['AwayScore'] = sim_results[:, 1, i]
    sim_fixtures['Points'] = sim_fixtures.apply(lambda row: results_points(row['HomeScore'], row['AwayScore']), axis=1)
    sim_fixtures[['HomePoints', 'AwayPoints']] = pd.DataFrame(sim_fixtures['Points'].tolist(), index=sim_fixtures.index)

    return get_points_by_week(sim_fixtures)


def get_probs(homeid, awayid, gameweek, trace):
    """Given goals prediction from posterior samples in trace,
    calculate the probabilities of each result
    """
    home_goals, away_goals = get_match_predictions(homeid, awayid, trace)

    win = np.mean(home_goals > away_goals)
    lose = np.mean(home_goals < away_goals)
    draw = np.mean(home_goals == away_goals)

    results = {'Gameweek': gameweek,'HomeTeamID': homeid, 'AwayTeamID': awayid,
               'HomeWinPred': win, 'AwayWinPred': lose, 'DrawPred': draw}
    return results

def get_match_predictions(home_id, away_id, trace):
    """
    Use ids with trace to generate match outcomes
    """
    # Samples
    team_effect_samples = trace.posterior['team_effect'].values
    opponent_effect_samples = trace.posterior['opponent_effect'].values
    home_adv_effect_samples = trace.posterior['home_adv_effect'].values
    # Home
    mu_samples = (team_effect_samples[..., home_id-1] -
                opponent_effect_samples[..., away_id-1] +
                1 * home_adv_effect_samples)
    home_goal_predictions = np.random.poisson(lam=np.exp(mu_samples)).flatten()
    # Away
    mu_samples = (team_effect_samples[..., away_id-1] -
                opponent_effect_samples[..., home_id-1] +
                0 * home_adv_effect_samples)
    away_goal_predictions = np.random.poisson(lam=np.exp(mu_samples)).flatten()

    return home_goal_predictions, away_goal_predictions
