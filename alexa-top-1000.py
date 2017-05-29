#!env python

import alexa_top_1000


def main(number_sites=5):
    '''
    main
    '''
    site_list = alexa_top_1000.get_top_list(number_sites)

    # Get sites ordered
    sorted_site_list = alexa_top_1000.sort_sites_by_words(site_list)

    rank = 1
    total_word_count = 0
    for site in sorted_site_list:
        print('{}) {}'.format(rank, site))
        total_word_count += site.word_count
        rank += 1

    average_word_count = total_word_count / len(sorted_site_list)
    print('\n\nAverage Word count: {}'.format(average_word_count))


if __name__ == '__main__':
    main()
