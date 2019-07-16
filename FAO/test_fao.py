from unittest import TestCase
from FAO import FAO


class TestFao(TestCase):
    def setUp(self):
        self.data = FAO()

    def test_countries(self):
        self.assertEqual(len(self.data.countries()), 174)
        self.assertEqual(self.data.countries()[0], "Afghanistan")
        self.assertEqual(self.data.countries()[100], "Malta")
        self.assertEqual(self.data.countries()[-1], "Zimbabwe")

    def test_products(self):
        self.assertEqual(self.data.products("Afghanistan")[0], "Wheat and products")

    def test_min(self):
        self.assertEqual(self.data.min(["Afghanistan"], [2010, 2013])["Afghanistan"][0][-1], 0)

    def test_max(self):
        self.assertEqual(self.data.max(["Afghanistan"], [2010, 2013])["Afghanistan"][-1], 5495)

    def test_av(self):
        self.assertEqual(self.data.av(["Afghanistan","Cyprus"], ['Y1961', 'Y1965'], "Wheat and products"), ["Afghanistan:1889.8","Cyprus:67.4"])


        

