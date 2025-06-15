import re
import sys
import logging
from pathlib import Path
from bs4 import BeautifulSoup


junk_content = ['#article-header',
                '#article-metadata',
                '#center-doc-outline',
                '#site-user-feedback-footer',
                '#ms--additional-resources-mobile',
                "div.inlineEditButton"
                ]

if __name__ == '__main__':

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    buildfolder = Path('./')

    for inputfile in buildfolder.rglob('*.html'):
        try:
            with open(inputfile) as f:
                soup = BeautifulSoup(f.read(), 'lxml')

            # Extract the main content
            main_content = soup.select_one('#main').extract()
            # Remove unnecessary content
            for junk in junk_content:
                try:
                    for tag in main_content.select(junk):
                        tag.decompose()
                except:
                    logging.warning(f'Junk removal: {e!r}')
            
            # Remove unnecessary head entries (e.g. non-local references)
            for head_tag in soup.select('head > meta[content], head > link[href^="https://"], head > script[src^="https://"]'):
                head_tag.decompose()

            body = soup.select_one('body')
            # Remove the classes from the body tag 
            body['class'] = None
            # Empty all content from body and insert modified content
            body.clear()
            _ = body.append(main_content)
            
            with open(inputfile, 'w') as f:
                f.write(soup.prettify())
        except Exception as e:
            logging.warning(f'Failed to process {inputfile.name}: {e!r}')
