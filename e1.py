import requests
from bs4 import BeautifulSoup as bs

website = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(election_id)
soup = bs(resp.content , "html.parser")
ID = soup.find_all("tr", "election_item")

elect_id = [[a.find("td", "year first").contents[0], a.get("id").split("-")[2]] for a in ID]

print('list:', *elect_id, sep='\n- ')
