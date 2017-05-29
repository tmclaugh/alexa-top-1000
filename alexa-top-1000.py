#!env python

import alexa_top_1000


def main(number_sites=5):
    '''
    main
    '''
    site_list = alexa_top_1000.get_top_list(number_sites)

    # Get info about sites
    site_word_data = []
    headers_list = []
    for site in site_list:
        site_data = alexa_top_1000.get_site_first_page_data(site)

        site_word_data.append({'site': site,
                               'word_count': site_data.get('word_count')})
        headers_list.append(site_data.get('headers'))

    # Get sites ordered
    sorted_site_list = alexa_top_1000.sort_sites_by_words(site_word_data)


if __name__ == '__main__':
    main()
