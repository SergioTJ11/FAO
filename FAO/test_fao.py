from unittest import TestCase
import FAO


class TestFao(TestCase):
    def setUp(self):
        self.data = FAO.FAOdata()

    def test_countries(self):
        countries = self.data.countries()
        self.assertEqual(len(countries), 174)
        self.assertEqual(countries[0], "Afghanistan")
        self.assertEqual(countries[100], "Malta")
        self.assertEqual(countries[-1], "Zimbabwe")

    def test_products(self):
        countries = self.data.countries()
        self.assertEqual(self.data.products(countries[0])[0], "Alcoholic Beverages")
        self.assertEqual(self.data.products(countries[0])[-1], "Wine")
        self.assertEqual(self.data.products(countries[-1])[-1], "Wine")

    def test_min(self):
        countries = self.data.countries()
        yearRange = [2010, 2013]
        self.assertEqual(self.data.min([countries[0]], yearRange)[countries[0]][0], ["Beer", "Y2010", 3])
        self.assertEqual(self.data.min([countries[-1]], yearRange)[countries[-1]][-1], ["Sugar beet", "Y2010", 0])

    def test_max(self):
        countries = self.data.countries()
        yearRange = [2010, 2013]
        self.assertEqual(self.data.max([countries[0]], yearRange)[countries[0]][-1], 5495)
        self.assertEqual(self.data.max([countries[-1]], yearRange)[countries[-1]][-1], 2016)

    def test_av(self):
        countries = self.data.countries()
        yearRange = [1961, 1965]
        self.assertEqual(self.data.av([countries[0], countries[5]], yearRange, "Wheat and products"), {"Afghanistan":1889.8,"Argentina":1437.4})
        self.assertEqual(self.data.av([countries[100], countries[105]], yearRange, "Wheat and products"), {"Malta":50,"Montenegro":0})

        

