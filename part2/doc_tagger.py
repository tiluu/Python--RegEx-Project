import sys, os, re

directory = sys.argv[1]

keywords = {}
for kw in sys.argv[2:]:
	 keywords[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

title_search = re.compile(r'(title:\s*)(?P<title>([\s\S](?!\n.+:))*)', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

for book in (os.listdir(directory)):
	if os.path.splitext(book)[-1] != ".txt": 
		continue
	book_path = os.path.join(directory, book)
	with open(book_path, 'r') as book_text:
		text = book_text.read()

	print book_path
	title = re.search(title_search, text).group('title')
	author = re.search(author_search, text)
	translator = re.search(translator_search, text)
	illustrator = re.search(illustrator_search, text)
	
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

		def make_path(directory, fl):
    return os.path.join(directory, fl) 

def path_open(make_path_val):
with open(make_path_val, 'r') as f: 
    full_text = f.read()
