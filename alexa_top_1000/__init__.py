#!env python

import boto3
import io
import zipfile


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
        top_sites_list.append(site)

        if len(top_sites_list) == number:
            break

    return top_sites_list

