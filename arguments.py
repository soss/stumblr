import sys
import argparse

def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="MarkDown project documentation")
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%{prog}s 0.1'
    )
    parser.add_argument(
        '-o', '--output',
        default=sys.stdout,
        type=argparse.FileType('w'),
        help="The file to output to (default stdout)"
    )
    parser.add_argument(
        '--css',
        nargs='*',
        type=argparse.FileType('r'),
        help="CSS files to use instead of the default"
    )
    parser.add_argument(
        '-f', '--force-generate',
        action='store_true',
        help="Ignore the cache and force regeneration of all documentation."
    )
    parser.add_argument(
        '--autocreate',
        action='store_true',
        help="If there is no index.md file in a directory, make a blank one."
    )
    parser.add_argument(
        'root',
        nargs=1,
        help="The root directory for the project"
    )

    return parser.parse_args(argv)
