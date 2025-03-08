from jsonargparse import auto_cli
from nba.download import download


if __name__ == '__main__':
    auto_cli({
        'download': download
    })