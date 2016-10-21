import urllib.request as request
from bs4 import BeautifulSoup
import re

team_name_dict = {'bos':'Boston Celtics',
                  'bkn':'Brooklyn Nets',
                  'nyk':'New York Knicks',
                  'phi':'Philadelphia 76ers',
                  'tor':'Toronto Raptors',
                  'gsw':'Golden State Warriors',
                  'lac':'Los Angeles Clippers',
                  'lal':'Los Angeles Lakers',
                  'pho':'Phoenix Suns',
                  'sac':'Sacramento Kings',
                  'chi':'Chicago Bulls',
                  'cle':'Cleveland Cavaliers',
                  'det':'Detroit Pistons',
                  'ind':'Indiana Pacers',
                  'mil':'Milwaukee Bucks',
                  'dal':'Dallas Mavericks',
                  'hou':'Houston Rockets',
                  'mem':'Memphis Grizzlies',
                  'nor':'New Orleans Pelicans',
                  'sas':'San Antonio Spurs',
                  'atl':'Atlanta Hawks',
                  'cha':'Charlotte Hornets',
                  'mia':'Miami Heat',
                  'orl':'Orlando Magic',
                  'was':'Washington Wizards',
                  'den':'Denver Nuggets',
                  'min':'Minnesota Timberwolves',
                  'okc':'Oklahoma City Thunder',
                  'por':'Portland Trail Blazers',
                  'uth':'Utah Jazz'
                  }

base_url = 'http://espn.go.com'

teams_url = 'http://espn.go.com/nba/teams'
html_teams = request.urlopen(teams_url)

soup_teams = BeautifulSoup(html_teams)

urls = soup_teams.find_all(href=re.compile('/nba/teams/stats'))
team_urls = [base_url+url['href'] for url in urls]
print(team_urls)

for team in team_urls:
  html_ind_teams = request.urlopen(team)
  soup_team = BeautifulSoup(html_ind_teams)
  
  roster = soup_team.find_all('tr', class_=re.compile('player'))
  roster_game_stats = roster[:int(len(roster)/2)]
  
  players = []
  for row in roster_game_stats:
    for data in row:
      players.append(data.get_text())
  for i in players:
    print(i.encode('utf-8'))
