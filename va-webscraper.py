import requests #Import python requests Library
from bs4 import BeautifulSoup #Import BeautifulSoup Library 

print("va-webscraper has started") #Statement to let user know the program has started

my_url = 'https://www.va.gov/' #Set variable my_url to va.gov website
page = requests.get(my_url) #Perform HTTP request
soup = BeautifulSoup(page.content, 'html.parser') #Parse file and call it soup

links_section = soup.find(id='homepage-benefits') #Get content from benefits section
links_section = str(links_section) #Turn the links_section into a string
links_section = links_section.replace("href=\"", "href=\"https://va.gov") #Route hyperlinks from rel location to absolute

#Content for HTML page
htmlpage = """<!DOCTYPE html>
<html>
	<head>
		<title>VA-Scraper Page</title>
	</head>
	<body>
""" + links_section + """
	</body>
</html>
""" 

f = open("index.html", "w") #Create or Open up a file with the name index.html and write to it
f.write(htmlpage) #Write the content to the html page
f.close() #Close file after writing

print("Website has been generated with all helpful links for veterans seeking benefits and health care")
