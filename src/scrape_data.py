from operator import itemgetter
from bs4 import BeautifulSoup
import requests

URL = 'https://www.worldometers.info/coronavirus/'


class Data:
    """
    Class that retrieves and manipulates the data from the website
    """
    def __init__(self, url):
        self.url = url
        self.data = self.get_data()

    def get_data(self):
        """
        Retrieves the data from the website
        :return: Dictionary with data
        """
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        page = soup.find('table',
                         attrs={'class': 'table table-bordered table-hover main_table_countries',
                                'id': 'main_table_countries_today'})
        body = page.tbody
        trs = body.findAll('tr')
        columns = []
        for tr in trs:
            cols = tr.findAll('td')
            cols = [x.text.strip() for x in cols]
            columns.append(itemgetter(1, 2, 4)(cols))
        names = ['name', 'total_cases', 'total_deaths']
        countries = [dict(zip(names, d)) for d in columns[8:]]
        total = {'name': columns[7][0], 'total_cases': columns[7][1], 'total_deaths': columns[7][2]}
        self.data = {'total': total, 'country': countries}
        return self.data

    def get_total_cases(self):
        """
        Retrieves the total cases from data
        :return: Number of total cases
        """
        return self.data['total']['total_cases']

    def get_total_deaths(self):
        """
        Retrieves the total deaths from data
        :return: Number of total deaths
        """
        return self.data['total']['total_deaths']

    def get_country_data(self, country):
        """
        Retrieves data for a specific country
        :param country: Country to be selected
        :return: Data for the selected country
        """
        for content in self.data['country']:
            if content['name'].lower() == country:
                return content
        return "0"

    def get_list_of_countries(self):
        """
        The list of all available countries
        :return: List of all countries
        """
        countries = []
        for country in self.data['country']:
            countries.append(country['name'].lower())

        return countries
