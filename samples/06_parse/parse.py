import sys

import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

book = epub.read_epub(sys.argv[1])

debug(book.metadata)
debug(book.spine)
debug(book.toc)

for x in book.get_items_of_type(ebooklib.ITEM_COVER):
    debug(x)

for x in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    debug(x)

for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    debug(x)

# if __name__ == '__main__':
#     book = epub.read_epub('/home/mi/Git/kindlepush/bot/resources/BQADBQADUAADD1ypVMO-7rK9oDMQAg.epub')
#     for x in book.get_items_of_type(ebooklib.ITEM_COVER):
#         debug(x)
