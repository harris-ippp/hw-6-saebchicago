import requests
from bs4 import BeautifulSoup as bs

from e1 import *

link = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
for line in elect_id:
    resp = requests.get(link.replace('{}',str(line[1])))
    file_name = 'Presidential_General' + line[0] + ".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
