#!env python

import alexa_top_1000


def main(number_sites=5):
    '''
    main
    '''
    site_list = alexa_top_1000.get_top_list(number_sites)

    # Get sites ordered
    sorted_site_list = alexa_top_1000.sort_sites_by_words(site_list)

    # Header info.
    headers = alexa_top_1000.get_header_list(sorted_site_list)
    top_headers = alexa_top_1000.get_top_headers(headers)

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
        print('{}) {}'.format(rank, site))
        total_word_count += site.word_count
        rank += 1

    average_word_count = total_word_count / len(sorted_site_list)
    print('\nAverage Word count: {}'.format(average_word_count))


if __name__ == '__main__':
    main()
