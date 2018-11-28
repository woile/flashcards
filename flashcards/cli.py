"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mflashcards` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``flashcards.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``flashcards.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse

from .flashcards import start

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def get_arguments():
    description = (
        'Flashcards is a small command line tool used to study.\n'
        'Shuffles the content for you and displays the title, once you think\n'
        'you know the answer, by pressing [Enter] you can see the content.\n\n'
        'Expected YML format (keywords are optional):\n\n'
        '-\n'
        '  topic: Python\n'
        '  content: Is a widely used high-level programming language for\n'
        '           created by Guido van Rossum and first released in 1991.\n'
        '  keywords: programming, language\n'
        '-\n'
        '  topic: Javascript\n'
        '  content: Is a dynamic, untyped, and interpreted programming lang.\n')

    formater = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='flashcards', description=description,
                                     formatter_class=formater)
    parser.add_argument('file_name', metavar='FILE_NAME',
                        help='YML file with flashcards content')
    parser.add_argument('-O', '--ordered', action="store_true", default=False,
                        help='Show cards keeping the file order')
    return parser.parse_args()


def main():
    args = get_arguments()
    start(args)
