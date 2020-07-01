import requests #Import python requests library
from bs4 import BeautifulSoup #Create Beatiful Soup object that takes scraped HTML content as input

print("va-webscraper has started\n") #Statement to let user know the program has started

my_url = 'https://www.va.gov/disability' #GET DISABILITY URL
page = requests.get(my_url) #Perform HTTP request
soup = BeautifulSoup(page.content, 'html.parser') #Parse file and call it soup

links_section = soup.findAll(id_='homepage-benefits') #Get info from HTML id
"""
#Opens connection to VA website through Function uReq
uVA = uReq(my_url)
#offloads info into a variable and closes the client
page_html = uVA.read()
uVA.close()
#html parsing
page_soup = soup(page_html, "html.parser")

claim = page_soup.find(id"72dea966a4245dd56a892f22b70f6c8a").text.strip()
    print(claim)
"""
