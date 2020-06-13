import unittest
from scrape_data import Data


def string_to_int(string):
    """
    Convert string to int
    :param string: An instance of type string
    :return: Integer
    """
    return int(string.replace(',', ''))


class TestScrapeData(unittest.TestCase):

    def setUp(self):
        self.data = Data('https://www.worldometers.info/coronavirus/')

    def test_get_data(self):
        print("Test get_data dictionary keys")

        data_total = self.data.get_data()
        data_keys = tuple(data_total.keys())
        data_total_keys = tuple(data_total['total'].keys())

        self.assertTupleEqual(('total', 'country'),
                              data_keys,
                              msg='Dictionary keys are not "total" and "country"')

        self.assertTupleEqual(('name', 'total_cases', 'total_deaths'),
                              data_total_keys,
                              msg='Dictionary keys are not "name", "total_cases", and "total_deaths"')

    def test_get_total_cases(self):
        print("Test if get_total_cases is an integer")
        total_cases = self.data.get_total_cases()
        self.assertIsInstance(string_to_int(total_cases), int, msg="Total cases is not an integer")

    def test_get_total_deaths(self):
        print("Test if get_total_deaths is an integer")
        total_deaths = self.data.get_total_deaths()
        self.assertIsInstance(string_to_int(total_deaths), int, msg="Total deaths is not an integer")

    def test_get_country_data(self):
        print("Test if USA exist")
        usa = self.data.get_country_data(country='usa')['name']
        self.assertEqual("USA", usa, msg="USA does not exist. Possible data corruption")

    def test_get_list_of_countries(self):
        print("Test if get_list_of_countries is a list")
        countries_ls = self.data.get_list_of_countries()
        self.assertIsInstance(countries_ls, list, msg="List of countries is not of type list")


if __name__ == '__main__':
    unittest.main()
