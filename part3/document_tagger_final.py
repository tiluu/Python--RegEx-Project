import sys
import os
import re
 
# supply path to directory housing PG docs at run time
directory = sys.argv[1]
 
# we're getting the keywords via sys.argv and
# what a dictionary comprhension.
# dictionary comprehensions are a lot like list comprehensions,
# which you've already learned about.
# Dictionary comprehensions have the following form:
#
#   d = {key: value for (key, value) in sequence}
#
# Source: http://stackoverflow.com/a/1747827/1264950
#
keywords =  {kw: re.compile(r'\b' + kw + r'\b') for kw in sys.argv[2:]}
 
title_search = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

def make_path(directory, fl):
    return os.path.join(directory, fl) 

def path_open(book_path):
    with open(book_path, 'r') as f: 
        return f.read()

for book in (os.listdir(directory)):
    if os.path.splitext(book)[-1] != ".txt": 
        continue
    book_path = make_path(directory, book)
    text_full = path_open(book_path)

    print book_path
    title = re.search(title_search, text_full).group('title')
    author = re.search(author_search, text_full)
    translator = re.search(translator_search, text_full)
    illustrator = re.search(illustrator_search, text_full)
    
    if author: 
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')
    print "***" * 25
    print "Here's the info for doc {}:".format(book)
    print "Title:  {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "\n"
    
    print "***" * 25
    for kw in keywords:
        print "Here's the keyword info for doc {}:".format(i)

