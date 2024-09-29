# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest
from a03_02_inheritance import Movie, RomCom, ActionMovie

class TestMovieInheritance(unittest.TestCase):

    def test_movie_initialization(self):
        """Test that Movie initializes correctly."""
        movie = Movie(1994, "Forrest Gump")
        self.assertEqual(movie.year, 1994)
        self.assertEqual(movie.title, "Forrest Gump")
        self.assertEqual(str(movie), "Movie: Forrest Gump (1994)")

    def test_romcom_inheritance(self):
        """Test that RomCom inherits from Movie correctly."""
        romcom = RomCom(2020, "Romantic Getaway")
        self.assertEqual(romcom.year, 2020)
        self.assertEqual(romcom.title, "Romantic Getaway")
        self.assertEqual(str(romcom), "Movie: Romantic Getaway (2020)")

    def test_action_movie_initialization(self):
        """Test that ActionMovie initializes correctly with default PG."""
        action_movie = ActionMovie(2022, "Explosive Chase")
        self.assertEqual(action_movie.year, 2022)
        self.assertEqual(action_movie.title, "Explosive Chase")
        self.assertEqual(action_movie.pg, 13)  # Default PG is 13
        self.assertEqual(str(action_movie), "Movie: Explosive Chase (2022)  PG: 13")

    def test_action_movie_custom_pg(self):
        """Test that ActionMovie accepts custom PG rating."""
        action_movie = ActionMovie(2022, "Explosive Chase", pg=18)
        self.assertEqual(action_movie.pg, 18)
        self.assertEqual(str(action_movie), "Movie: Explosive Chase (2022)  PG: 18")


if __name__ == '__main__':
    unittest.main()
