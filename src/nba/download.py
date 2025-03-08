import nba_api.stats.endpoints
import pandas as pd
import tqdm
from datetime import datetime


def download(season_start: int = 1950, season_end: int = None, output_path: str = None):
    """
    Download league leaders NBA data from the NBA API.

    Args:
        season_start (int): The first season to download data from.
        season_end (int): The last season to download data from.
        output_path (str): The path to save the data to.
    """
    season_end = season_end or datetime.now().year + 1
    seasons = [f"{n}-{str(n+1)[-2:]}" for n in range(season_start, season_end)]
    data = []
    for season in tqdm.tqdm(seasons):
        res = nba_api.stats.endpoints.leagueleaders.LeagueLeaders(season=season).league_leaders.get_data_frame()
        res['SEASON_STR'] = season
        res['SEASON'] = int(season.split('-')[0])
        data.append(res)
    data = pd.concat(data)
    if output_path is not None:
        data.to_csv(output_path, index=False)
    return data