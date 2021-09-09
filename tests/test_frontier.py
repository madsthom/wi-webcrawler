import unittest

from Frontier import Frontier


class FrontierTests(unittest.TestCase):
    def test_front_queue(self):
        test_seeds = ["https://www.aau.dk/", "https://www.humanrisks.com/"]
        frontier = Frontier(test_seeds)
        self.assertEqual(len(frontier), 2)

        frontier.add(["https://www.dr.dk/"])

        self.assertEqual(len(frontier), 3)

        url = frontier.get_url()

        self.assertEqual(url, "https://www.aau.dk/")
        self.assertEqual(len(frontier), 2)


if __name__ == '__main__':
    unittest.main()
