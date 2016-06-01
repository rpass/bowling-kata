import unittest
from tenpin import Game


class MyTestCase(unittest.TestCase):

    def test_game_of_ones(self):
        game = Game()
        for i in range(20):
            game.roll(1)

        self.assertEqual(game.score(), 20)

    def test_game_with_spare_scored_correctly(self):
        game = Game()
        game.roll(2)
        game.roll(8)
        game.roll(4)
        game.roll(2)

        self.assertEqual(game.score(), 20)


if __name__ == '__main__':
    unittest.main()
