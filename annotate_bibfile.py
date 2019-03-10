# -*- coding: utf-8 -*-
"""Bibfile cleanup script.

This module parses the list of publications, to apply
fixes before CV generation. First, it adds an annotation
to the script author's name, to allow biblatex highlighting.
Second, it takes the Zotero date format of YYYY-MM-DD, and strips
it down to YYYY.

Requires the `bibtexparser` library.

Example:
    This generates an annotated bibfile:

        $ python annotate_bibfile.py publications.bib publications_annotated.bib

"""

import sys
import bibtexparser


def check_author(author):
    """
    Check if I'm the author

    Parameters
    ----------

    author : string
        Last name, first name
    """
    return author.startswith('Kahn')


def highlight_author(entry):
    """
    Highlight the author in a block
    
    Parameters
    ----------

    entry : dict
        bibtex entry
    """

    # This separates out the authors
    bibtexparser.customization.author(entry)
    
    # Find the index that matches
    authors = entry['author']
    author_index = [check_author(x) for x in authors].index(True) + 1
    entry['author+an'] = "{index}=highlight".format(index=author_index)
    entry['author'] = '\n and '.join(authors)


def fix_date(entry):
    """
    Changes Y-M-D to Y
    
    Parameters
    ----------

    entry : dict
        bibtex entry
    """
    entry['date'] = entry['date'].split('-')[0]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of args.")
        print("Usage: python annotate_bibfile.py in.bib out.bib")
        exit(1)
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

        with open(in_file) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)

        for entry in bib_database.entries:
            highlight_author(entry)
            fix_date(entry)

        with open(out_file, 'w') as bibtex_file:
            bibtexparser.dump(bib_database, bibtex_file)