import re
import sys
import logging
from pathlib import Path
from bs4 import BeautifulSoup


if __name__ == '__main__':

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    buildfolder = Path('./')

    for inputfile in buildfolder.rglob('*.html'):
        try:
            with open(inputfile) as f:
                soup = BeautifulSoup(f.read(), 'lxml')
                
            # Remove unnecessary scripts
            for script in soup.select('body script, head script'):
                script.decompose()
                
            # Remove that stupid `opendigitaltwins-dtdl` title on every page
            if (dummy_title := soup.select_one('body h1:first-of-type')) is not None:
                dummy_title.decompose()
            
            for h2 in soup.select('body h2'):
                try:
                    if h2.string is None:
                        continue
                    # Don't insert an TOC entry for the TOC
                    if h2['id'] in ('table-of-contents', 'contents'):
                        continue
                    # remove any "emoji" references like :dart:
                    h2.string.replace_with(re.sub(r'^:.*: ', '', h2.string, count=1))
                    # Add the docset toc reference
                    h2.string.wrap(soup.new_tag('a', attrs={'name': f"//apple_ref/cpp/Entry/{h2.string}", 'class':"dashAnchor"}))
                except Exception as e:
                    logging.warning(f'While processing H2: {e!r}')
            with open(inputfile, 'w') as f:
                f.write(soup.prettify())
        except Exception as e:
            logging.warning(f'Failed to process {inputfile.name}: {e!r}')