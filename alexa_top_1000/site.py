'''
Alexa Site module
'''

from bs4 import BeautifulSoup
from datetime import datetime
import logging
import requests

_logger = logging.getLogger(__name__)

class Site(object):
    '''
    An Alexa Site
    '''
    def __init__(self, name):
        time_start = datetime.now()
        self.name = name

        self.word_list, self.headers, self.scanned, self.status_code = self._get_site_first_page_data()
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

        # FIXME: Do we for speed:
        # * Just assume https?
        # * assume www?
        url = '{}{}'.format('http://', self.name)
        try:
            resp = requests.get(url, timeout=15)
            soup = BeautifulSoup(resp.text, 'html.parser')

            # FIXME: this could be better
            word_list = soup.get_text().split()
            headers = resp.headers
            scanned = True
            status_code = resp.status_code
        except requests.exceptions.ConnectionError as e:
            _logger.debug('Scan for {} failed: {}'.format(self.name, e))
            word_list = []
            headers = {}
            scanned = False
            status_code = 0 # Not a valid status code.

        return (word_list, headers, scanned, status_code)

