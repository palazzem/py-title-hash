""" 
Title hash calculator with git

Usage:
  hash_calculator.py [--version] [--help] <title>

Options:
  -h --help               See this help message and exit
  -v --version            See builder version and exit

This is a title hash calculator to print pretty SHA1 link for my blog
"""

from hashlib import sha1
from docopt import docopt


# git hash-object binding
def git_hash(data):
    s = sha1()
    s.update("blob {}\0".format(len(data) + 1))
    s.update(data)
    s.update("\n")
    return s.hexdigest()


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0', options_first=True)
    title = args['<title>']

    hash = git_hash(title)
    print "Complete hash: {}".format(hash)
    print "Short hash: {}".format(hash[:7])
