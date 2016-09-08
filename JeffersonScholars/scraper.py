# Jack Morris 09/06/16

from bs4 import BeautifulSoup
import urllib


all_scholars_url = "http://www.jeffersonscholars.org/scholars"
scholar_link_base = "http://www.jeffersonscholars.org"

# get lists of links
r = urllib.urlopen(all_scholars_url).read()
soup = BeautifulSoup(r, "lxml")
full_list = soup.find_all("div", class_="people-list")[0]
lists_by_year = full_list.find_all("div", class_="people-sublist-year")
scholar_links = []

# get all people links from lists
for scholar_list in lists_by_year:
  #
  people_links = [header.find_all("a")[0] for header in scholar_list.find_all("h3", class_="field-name")]
  scholar_links.extend( [a["href"] for a in people_links] )
  #
#


# grab data from each link
scholars = []
for scholar_link in scholar_links:
  #
  r = urllib.urlopen(scholar_link_base + scholar_link).read()
  soup = BeautifulSoup(r, "lxml")
  #
  scholar = {}
  scholar["name"] = soup.find_all("h1", class_="title")[0].get_text().strip()
  scholar["age"]  = soup.find_all("div", class_="field-class")[0].get_text().strip()
  scholar["town"] = soup.find_all("div", class_="field-hometown")[0].get_text().strip()
  print scholar
  #
#
