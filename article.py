#! /usr/bin/python3
from newspaper import Article
import sys



myUrl = sys.argv[1]

first_article = Article(url=myUrl, language='en',  keep_article_html=True)

first_article.download()
first_article.parse()

# Open file in write mode, create if not exist
myFile = open(first_article.title + ".html", "w")
myFile.write("<title>" + first_article.title + "</title>")
myFile.write("<h1>" + first_article.title + "</h1>")
myFile.write("<h3>" + first_article.authors[0] + "</h3>")
myFile.write("<a href='" + myUrl + "'>" + myUrl + "</a>")
myFile.write("<hr><br>")
myFile.write(first_article.article_html)
myFile.close()
