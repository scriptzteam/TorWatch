#!/usr/bin/env python3
import logging
import os
import sys
import urllib.request


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)


def download_file(url: str, filename: str) -> bool:
    '''
    Download a file from a URL and save it locally
    :param url: URL to download from
    :param filename: Local filename to save as
    '''
    try:
        logging.info(f'Attempting to download {url}')
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
        logging.info(f'Writing content to {filename}')
        with open(filename, 'w') as f:
            f.write(content)
            
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            logging.info(f'Successfully wrote {size} bytes to {filename}')
            return True
        else:
            logging.error(f'File {filename} was not created')
            return False
            
    except Exception as e:
        logging.error(f'Failed to download {url}: {str(e)}')
        return False


def main() -> None:
    '''Main entry point for the script'''
    sources = {
        'exits.txt': 'https://tor-relays.0xc0d3.cc/exits.txt',
        'exits-ipv4.txt': 'https://tor-relays.0xc0d3.cc/exits-ipv4.txt',
        'exits-ipv6.txt': 'https://tor-relays.0xc0d3.cc/exits-ipv6.txt',
        'relays.txt': 'https://tor-relays.0xc0d3.cc/relays.txt',
        'relays-ipv4.txt': 'https://tor-relays.0xc0d3.cc/relays-ipv4.txt',
        'relays-ipv6.txt': 'https://tor-relays.0xc0d3.cc/relays-ipv6.txt',
    }

    success = True
    for filename, url in sources.items():
        logging.info(f'Processing {filename}')
        if not download_file(url, filename):
            success = False
            logging.error(f'Failed to process {filename}')
        else:
            logging.info(f'Successfully processed {filename}')

    if not success:
        logging.error('Script failed to complete successfully')
        sys.exit(1)
    else:
        logging.info('Script completed successfully')


if __name__ == '__main__':
    main() 
