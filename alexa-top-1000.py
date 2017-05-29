#!env python

import alexa_top_1000


def main(number_sites=5):
    '''
    main
    '''
    site_list = alexa_top_1000.get_top_list(number_sites)

    # Get sites ordered
    sorted_site_list = alexa_top_1000.sort_sites_by_words(site_list)

    print(sorted_site_list)


if __name__ == '__main__':
    main()
