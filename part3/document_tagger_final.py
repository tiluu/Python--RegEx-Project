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

key_dicts = {'title':title_search, 'author': author_search, 'translator':translator_search, 'illustrator':illustrator_search}
def make_path(directory, fl):
    return os.path.join(directory, fl) 

def path_open(book_path):
    with open(book_path, 'r') as f: 
        return f.read() 


def find_key(key_dicts, text_full):
    results = {}
    for key in key_dicts:
        result = re.search(key_dicts[key], text_full)
        if result:
            results[key] = result.group(key)
        else:
            results[key] = None
    return results

for book in (os.listdir(directory)):
    if os.path.splitext(book)[-1] != ".txt": 
        continue
    book_path = make_path(directory, book)
    text_full = path_open(book_path)

    searches = find_key(key_dicts, text_full)

    print "***" * 25

    print "Here's the info for doc {}:".format(book)
    for k in searches:
        print '{0}:{1}'.format(k, searches[k]) 
    
    print "\n"
    
    print "***" * 25
    for kw in keywords:
        print "Here's the keyword info for doc {}:".format(i)

