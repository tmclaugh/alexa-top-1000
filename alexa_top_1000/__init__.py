'''
alexa-top-1000

The Alexa Top 1000 sites.
'''
import boto3
import io
import logging
import zipfile

from .site import Site

_logger = logging.getLogger(__name__)

ALEXA_TOP_SITES_BUCKET = 'alexa-static'
ALEXA_TOP_SITES_KEY = 'top-1m.csv.zip'
ALEXA_TOP_SITES_FILE = 'top-1m.csv'

def get_top_list(number):
    '''
    Get list of top sites from ATS S3 bucket.
    '''
    s3_client = boto3.client('s3')
    top_sites_obj = s3_client.get_object(Bucket=ALEXA_TOP_SITES_BUCKET,
                                  Key=ALEXA_TOP_SITES_KEY)
    top_sites_bytes = io.BytesIO(top_sites_obj.get('Body').read())
    top_sites_zip = zipfile.ZipFile(top_sites_bytes)
    # This gives us a value with line breaks.
    top_sites_list = []
    for line in io.BytesIO(top_sites_zip.read(ALEXA_TOP_SITES_FILE)):
        rank, site = line.decode('utf-8').strip().split(',')
        top_sites_list.append(Site(site))

        if len(top_sites_list) == number:
            break

    return top_sites_list

def sort_sites_by_words(site_list):
    '''
    Return a list of site objects sorted by word count.
    '''
    sorted_site_list = []

    for site in site_list:
        _logger.debug('Sorting: {}'.format(site))
        inserted = False
        index = 0
        if not sorted_site_list:
            sorted_site_list.append(site)
        elif not site.scanned:
            sorted_site_list.insert(0, site)
        else:
            for sorted_site in sorted_site_list:
                if site < sorted_site:
                    sorted_site_list.insert(index, site)
                    inserted = True
                    break
                else:
                    index += 1

            if not inserted:
                sorted_site_list.append(site)

    # FIXME: I sorted these incorrectly above so reverse it here.
    sorted_site_list.reverse()
    return sorted_site_list

def get_header_list(site_list):
    '''
    Return the headers and number of times they appear from a list of site
    objects.
    '''

    headers = {}
    for site in site_list:
        for header in site.headers.keys():
            # FIXME: Necessary?
            lc_header = header.lower()

            if lc_header in headers.keys():
                headers[lc_header] += 1
            else:
                headers[lc_header] = 1

    return headers

def get_top_headers(headers, number):
    '''
    Get the top header names.
    '''
    sorted_headers_list = []

    for header in headers.keys():
        inserted = False
        index = 0
        if not sorted_headers_list:
            sorted_headers_list.append((header, headers.get(header)))
        else:
            for sorted_header in sorted_headers_list:
                if headers.get(header) < sorted_header[1]:
                    sorted_headers_list.insert(index, (header, headers.get(header)))
                    inserted = True
                    break
                else:
                    index += 1

            if not inserted:
                sorted_headers_list.append((header, headers.get(header)))

    # FIXME: I sorted these incorrectly above so reverse it here.
    sorted_headers_list.reverse()
    return sorted_headers_list[:number]

