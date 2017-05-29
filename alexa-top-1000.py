#!env python

import alexa_top_1000
import argparse
from datetime import datetime
import logging
from logging.config import fileConfig
import os.path

dirname = os.path.dirname(__file__)
logging_conf = os.path.join(dirname, 'logging.conf')
fileConfig(logging_conf, disable_existing_loggers=False)
if os.environ.get('DEBUG'):
    logging.root.setLevel(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def main(number_sites, number_headers):
    '''
    main
    '''
    scan_time_start = datetime.now()
    site_list = alexa_top_1000.get_top_list(number_sites)
    scan_time_end = datetime.now()

    # Get sites ordered
    sorted_site_list = alexa_top_1000.sort_sites_by_words(site_list)

    # Header info.
    headers = alexa_top_1000.get_header_list(sorted_site_list)
    top_headers = alexa_top_1000.get_top_headers(headers, number_headers)

    rank = 1
    number_of_sites = len(sorted_site_list)
    print('\n\n==Header Info==')
    for header in top_headers:
        header_name = header[0]
        header_percent = (header[1] / number_of_sites) * 100
        print('{}) {} in {}% of sites'.format(rank,
                                              header_name,
                                              header_percent))
        rank += 1

    # Word Count
    rank = 1
    total_word_count = 0
    print('\n\n==Word Count Info==')
    for site in sorted_site_list:
        if site.scanned:
            print('{}) {}'.format(rank, site))
            total_word_count += site.word_count
            rank += 1
        else:
            print('{}) {} not scanned'.format(rank, site))

    average_word_count = total_word_count / len(sorted_site_list)
    print('\nAverage Word count: {}'.format(average_word_count))
    print('Scanned in: {}'.format((scan_time_end - scan_time_start)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s',
                        '--sites',
                        dest='number_sites',
                        type=int,
                        default=1000,
                        help='Number of sites')
    parser.add_argument('-H',
                        '--headers',
                        dest='number_headers',
                        type=int,
                        default=20,
                        help='Number of headers')
    args = parser.parse_args()

    main(args.number_sites, args.number_headers)
