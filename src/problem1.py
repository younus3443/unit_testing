import csv
from collections import defaultdict

SEASON="season"
WINNER="winner"
EXTRA_RUNS="extra_runs"
ID="id"
MATCH_ID="match_id"
BOWLING_TEAM="bowling_team"
BOWLER="bowler"
TOTAL_RUNS="total_runs"
def load_csv(file_path):
    with open(file_path,encoding="utf-8")as csv_file:
        return list(csv.DictReader(csv_file))

def matches_per_year(matches):
    result=defaultdict(int)
    for match in matches:
        result[match[SEASON]]+=1
    return dict(result)

def matches_won_per_teams(matches):
    result=defaultdict(int)
    for match in matches:
        result[match[WINNER]]+=1
    return dict(result)

def extra_runs_2016_per_team(matches,deliveries):
    id=set()
    extra_runs_team=defaultdict(int)
    for match in matches:
        if match[SEASON]=="2016":
            id.add(match[ID])
    for delivery in deliveries:
        if delivery[MATCH_ID] in id:
            extra_runs_team[delivery[BOWLING_TEAM]]+=int(delivery[EXTRA_RUNS])
    return extra_runs_team

def top_economical_bowlers_2015(matches,deliveries):
    id=set()
    runs=defaultdict(int)
    balls=defaultdict(int)
    economic_bowlers_2015={}
    for match in matches:
        if match[SEASON]=="2015":
            id.add(match[ID])
    for delivery in deliveries:
        if delivery[MATCH_ID] in id:
            runs[delivery[BOWLER]]+=int(delivery[TOTAL_RUNS])
            balls[delivery[BOWLER]]+=1
    economy={b: runs[b]/(balls[b]/6) for b in runs}
    sorted_bowler=dict(sorted(economy.items(),key=lambda x:x[1])[:5])
    return sorted_bowler



