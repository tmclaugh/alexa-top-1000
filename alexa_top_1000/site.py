'''
Alexa Site
'''

from bs4 import BeautifulSoup
import requests

class Site(object):
    '''
    An Alexa Site
    '''
    def __init__(self, name):
        self.name = name
        self.word_list, self.headers = self._get_site_first_page_data()
        self.word_count = len(self.word_list)

    def __gt__(self, site):
        return self.word_count > site.word_count

    def __lt__(self, site):
        return self.word_count < site.word_count

    def __str__(self):
        return "{} has {} words".format(self.name, self.word_count)


    def _get_site_first_page_data(self):
        '''
        given a site get the word count and headers.
        '''
        url = '{}{}'.format('http://', self.name)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # FIXME: this could be better
        word_list = soup.get_text().split()

        return (word_list, resp.headers)

