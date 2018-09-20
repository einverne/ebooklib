import sys

import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

if __name__ == '__main__':
    if len(sys.argv) > 1:
        book = epub.read_epub(sys.argv[1])
    else:
        print('provide parameter')
        sys.exit()

    debug(book.metadata)
    debug(book.spine)
    debug(book.toc)

    for x in book.get_items_of_type(ebooklib.ITEM_COVER):
        debug(x)

    for x in book.get_items_of_type(ebooklib.ITEM_IMAGE):
        debug(x)

    for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        debug(x)

