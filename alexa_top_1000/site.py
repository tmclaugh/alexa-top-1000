'''
Alexa Site module
'''

from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Site(object):
    '''
    An Alexa Site
    '''
    def __init__(self, name):
        time_start = datetime.now()
        self.name = name

        self.word_list, self.headers = self._get_site_first_page_data()
        self.word_count = len(self.word_list)
        self.scan_time = datetime.now() - time_start

    def __gt__(self, site):
        return self.word_count > site.word_count

    def __lt__(self, site):
        return self.word_count < site.word_count

    def __str__(self):
        return "{} has {} words; scanned in {}".format(self.name,
                                                       self.word_count,
                                                       self.scan_time)


    def _get_site_first_page_data(self):
        '''
        Get the word count and headers.
        '''
        url = '{}{}'.format('http://', self.name)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # FIXME: this could be better
        word_list = soup.get_text().split()

        return (word_list, resp.headers)

