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
	book_path = os.path.join(directory, book)
	with open('book_path', 'r') as book_text:
		text = book_text.read()

	title = re.search(title_search, doc).group('title')
	author = re.search(author_search, doc)
	translator = re.search(translator_search, doc)
	illustrator = re.search(illustrator_search, doc)
	
	if author: 
		author = author.group('author')
	if translator:
		translator = translator.group('translator')
	if illustrator:
		illustrator = illustrator.group('illustrator')
	print "***" * 25
	print "Here's the info for doc {}:".format(i)
	print "Title:  {}".format(title)
	print "Author(s): {}".format(author)
	print "Translator(s): {}".format(translator)
	print "Illustrator(s): {}".format(illustrator)
	print "\n"
	
	print "***" * 25

	for kw in keywords:
		print "Here's the keyword info for doc {}:".format(i)