from __future__ import print_function

import os
import urllib2
import re

DILBERT_URL_PATTERN = "http://www.dilbert.com/strip/%s-%s-%s/"
DILBERT_IMG_URL = "http://assets.amuniversal.com/"

URL_FILE = os.path.join(os.path.dirname(__file__), 'img_urls.txt')
img_pattern = re.compile('<meta property="og:image" content="http://assets.amuniversal.com/([0-9a-fA-F]*)"/>')


def urlcrawler():

    with open(URL_FILE, 'w') as url_file:

        for year in range(2009, 2015):
            for month in range(1, 13):
                for day in range(1, 31):
                    try:
                        url_to_dilbert_page = DILBERT_URL_PATTERN % (year, month, day)
                        page_contents = urllib2.urlopen(url_to_dilbert_page).read()
                        image_hash = img_pattern.search(page_contents).group(1)
                        print(image_hash, file=url_file)
                        print('wrote hash for {0}-{1}-{2}'.format(year, month, day))
                    except Exception as e:
                        print('error', e)

if __name__ == "__main__":
    urlcrawler()