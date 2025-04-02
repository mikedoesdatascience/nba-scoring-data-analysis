from dataclasses import dataclass

@dataclass
class Team:
    name: str
    abbreviation: str
    city: str
    team_color: str

teams = [
    Team(name="Hawks", abbreviation="ATL", city="Atlanta", team_color="#E03A3E"),
    Team(name="Celtics", abbreviation="BOS", city="Boston", team_color="#007A33"),
    Team(name="Nets", abbreviation="BKN", city="Brooklyn", team_color="#000000"),
    Team(name="Hornets", abbreviation="CHA", city="Charlotte", team_color="#1D1160"),
    Team(name="Bulls", abbreviation="CHI", city="Chicago", team_color="#CE1141"),
    Team(name="Cavaliers", abbreviation="CLE", city="Cleveland", team_color="#860038"),
    Team(name="Mavericks", abbreviation="DAL", city="Dallas", team_color="#00538C"),
    Team(name="Nuggets", abbreviation="DEN", city="Denver", team_color="#FEC524"),
    Team(name="Pistons", abbreviation="DET", city="Detroit", team_color="#C8102E"),
    Team(name="Warriors", abbreviation="GSW", city="Golden State", team_color="#ffc72c"),
    Team(name="Warriors", abbreviation="SFW", city="San Fransisco", team_color="#ffc72c"),
    Team(name="Rockets", abbreviation="HOU", city="Houston", team_color="#CE1141"),
    Team(name="Rockets", abbreviation="SDR", city="San Diego", team_color="#CE1141"),
    Team(name="Pacers", abbreviation="IND", city="Indiana", team_color="#002D62"),
    Team(name="Clippers", abbreviation="LAC", city="Los Angeles", team_color="#C8102E"),
    Team(name="Lakers", abbreviation="LAL", city="Los Angeles", team_color="#FDB927"),
    Team(name="Grizzlies", abbreviation="MEM", city="Memphis", team_color="#5D76A9"),
    Team(name="Heat", abbreviation="MIA", city="Miami", team_color="#98002E"),
    Team(name="Bucks", abbreviation="MIL", city="Milwaukee", team_color="#00471B"),
    Team(name="Timberwolves", abbreviation="MIN", city="Minnesota", team_color="#0C2340"),
    Team(name="Pelicans", abbreviation="NOP", city="New Orleans", team_color="#0C2340"),
    Team(name="Knicks", abbreviation="NYK", city="New York", team_color="#F58426"),
    Team(name="Thunder", abbreviation="OKC", city="Oklahoma City", team_color="#007AC1"),
    Team(name="Magic", abbreviation="ORL", city="Orlando", team_color="#0077C0"),
    Team(name="76ers", abbreviation="PHI", city="Philadelphia", team_color="#ed174c"),
    Team(name="76ers", abbreviation="PHL", city="Philadelphia", team_color="#ed174c"),
    Team(name="Warriors", abbreviation="PHW", city="Philadelphia", team_color="#006bb6"),
    Team(name="Suns", abbreviation="PHX", city="Phoenix", team_color="#1D1160"),
    Team(name="Trail Blazers", abbreviation="POR", city="Portland", team_color="#E03A3E"),
    Team(name="Kings", abbreviation="SAC", city="Sacramento", team_color="#5A2D81"),
    Team(name="Kings", abbreviation="CIN", city="Cincinnati", team_color="#5A2D81"),
    Team(name="Kings", abbreviation="KCK", city="Kansas City", team_color="#5A2D81"),
    Team(name="Spurs", abbreviation="SAS", city="San Antonio", team_color="#C4CED4"),
    Team(name="Spurs", abbreviation="SAN", city="San Antonio", team_color="#C4CED4"),
    Team(name="Raptors", abbreviation="TOR", city="Toronto", team_color="#CE1141"),
    Team(name="Jazz", abbreviation="UTA", city="Utah", team_color="#002B5C"),
    Team(name="Jazz", abbreviation="UTH", city="Utah", team_color="#002B5C"),
    Team(name="Jazz", abbreviation="NOJ", city="New Orleans", team_color="#002B5C"),
    Team(name="Wizards", abbreviation="WAS", city="Washington", team_color="#002B5C"),
    Team(name="Braves", abbreviation="BUF", city="Buffalo", team_color="#ff6314"),
    Team(name="Hawks", abbreviation="STL", city="St Louis", team_color="#E03A3E"),
]

def get_team_by_abbreviation(abbreviation: str) -> Team:
    for team in teams:
        if team.abbreviation == abbreviation:
            return team
    return None

def get_team_by_name(name: str) -> Team:
    for team in teams:
        if team.name == name:
            return team
    return None

def get_team_by_city(city: str) -> Team:
    for team in teams:
        if team.city == city:
            return team
    return None

def get_team(name: str = None, abbreviation: str = None, city: str = None) -> Team:
    if name:
        return get_team_by_name(name)
    if abbreviation:
        return get_team_by_abbreviation(abbreviation)
    if city:
        return get_team_by_city(city)
    return None

# Example: Accessing a team's color by abbreviation
team_colors = {team.abbreviation: team.team_color for team in teams}