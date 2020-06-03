import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL/"
rPage = requests.get(url)
soup = BeautifulSoup(rPage.content, "html.parser")
soup = soup.find("div",{"class":"Bxz(bb) D(ib) Va(t) Mih(250px)--lgv2 W(100%) Mt(-6px) Mt(0px)--mobp Mt(0px)--mobl W(50%)--lgv2 Mend(20px)--lgv2 Pend(10px)--lgv2 BdEnd--lgv2 Bdendc($seperatorColor)--lgv2"})
# soup = soup.find("div",{"class":"main-container"})
# for image in soup.find_all("img"):
#     image.decompose()
print(soup.prettify())