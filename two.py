import rquests as rq
from bs4 import BeautifulSoup as Bu

page_info=rq.get("http://katmoviehd.to/")
page_data=Bu()
