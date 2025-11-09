import unittest
from problem1 import *

class TestIPLAnalysis(unittest.TestCase):
     
    def setUp(self):
        self.matches=[
               {"id": "1", "season": "2015", "team1": "MI", "team2": "CSK", "winner": "MI"},
            {"id": "2", "season": "2015", "team1": "RCB", "team2": "SRH", "winner": "RCB"},
            {"id": "3", "season": "2016", "team1": "MI", "team2": "RCB", "winner": "RCB"},
            {"id": "4", "season": "2016", "team1": "KKR", "team2": "SRH", "winner": "SRH"},
            {"id": "5", "season": "2017", "team1": "CSK", "team2": "RCB", "winner": "CSK"},
          ]
        self.deliveries=[
            {"match_id": "1", "batting_team": "MI", "bowling_team": "CSK", "bowler": "Bumrah", "extra_runs": "1", "total_runs": "5"},
            {"match_id": "1", "batting_team": "MI", "bowling_team": "CSK", "bowler": "Malinga", "extra_runs": "0", "total_runs": "4"},
            {"match_id": "2", "batting_team": "RCB", "bowling_team": "SRH", "bowler": "Starc", "extra_runs": "2", "total_runs": "6"},
            {"match_id": "3", "batting_team": "RCB", "bowling_team": "MI", "bowler": "Chahal", "extra_runs": "0", "total_runs": "2"},
        ]

    def test_matches_per_year(self):
        result=matches_per_year(self.matches)
        self.assertEqual(result,{"2015": 2, "2016": 2, "2017": 1})
    def test_matches_won_per_teams(self):
        result=matches_won_per_teams(self.matches)
        expected = {"MI": 1, "RCB": 2, "SRH": 1, "CSK": 1}
        self.assertEqual(result, expected)
        
    def test_extra_runs_2016_per_team(self):
        result=extra_runs_2016_per_team(self.matches,self.deliveries)
        expected={"MI": 0}
        self.assertEqual(result,expected)

    def test_top_economical_bowlers_2015(self):
        result=top_economical_bowlers_2015(self.matches,self.deliveries)
        self.assertIn("Bumrah", result)
        self.assertTrue(result["Bumrah"] > 0)
if __name__=="__main__":
    unittest.main()