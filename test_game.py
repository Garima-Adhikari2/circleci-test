import unittest
import rock_paper_scissors


class TestDetermineWinner(unittest.TestCase):
    
    def test_tie_rock(self):
        result = rock_paper_scissors.determine_winner('rock', 'rock')
        self.assertEqual(result, "It's a tie!")
    
    def test_tie_paper(self):
        result = rock_paper_scissors.determine_winner('paper', 'paper')
        self.assertEqual(result, "It's a tie!")
    
    def test_tie_scissors(self):
        result = rock_paper_scissors.determine_winner('scissors', 'scissors')
        self.assertEqual(result, "It's a tie!")
    
    def test_user_wins_rock_scissors(self):
        result = rock_paper_scissors.determine_winner('rock', 'scissors')
        self.assertEqual(result, "You win!")
    
    def test_user_wins_paper_rock(self):
        result = rock_paper_scissors.determine_winner('paper', 'rock')
        self.assertEqual(result, "You win!")
    
    def test_user_wins_scissors_paper(self):
        result = rock_paper_scissors.determine_winner('scissors', 'paper')
        self.assertEqual(result, "You win!")
    
    def test_computer_wins_rock_paper(self):
        result = rock_paper_scissors.determine_winner('rock', 'paper')
        self.assertEqual(result, "Computer wins!")
    
    def test_computer_wins_paper_scissors(self):
        result = rock_paper_scissors.determine_winner('paper', 'scissors')
        self.assertEqual(result, "Computer wins!")
    
    def test_computer_wins_scissors_rock(self):
        result = rock_paper_scissors.determine_winner('scissors', 'rock')
        self.assertEqual(result, "Computer wins!")


if __name__ == "__main__":
    unittest.main()