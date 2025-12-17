import os
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_2?adgrpid=59261129979&dib=eyJ2IjoiMSJ9.n5Fg6tNe2GLbuNkXW5ia15rNuM-sTVBnbHxTYcRdXzsOu9eYhwWx_GSFBFNXg3tFBsfEkTdyMwwNHHnHS1H2RJBJ27tBjS9JXriDDasCpM4GC9keoERN1U7nevql8uQZPvw9yoqW0lNW_dL2XmXMtTiwdVXw2S589Y1QB2DzixlOmYM0SOygJ2PDFCXmlehkwbk1W5FL_pGMDTg7JFWu0jizUIRjf6HM73URomxwSoU.t2GgurRrMVfYaV3Sr0wPfrXC7y30YzSu2lTJJB2siiU&dib_tag=se&ext_vrnc=hi&hvadid=294122343962&hvdev=c&hvlocphy=9299927&hvnetw=g&hvqmt=e&hvrand=16352349303279500213&hvtargid=kwd-299883671737&hydadcr=17102_1793592&keywords=ps5&mcid=5d496097c5733e3e99c1751043421bed&qid=1751715034&sr=8-2"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}

response = requests.get(url=url,headers=header)

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

price = soup.find(class_ = "a-price-whole").get_text()
price_without_currency = price.split(".")[0].replace(",", "")
print(price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 52000

if BUY_PRICE > int(price_without_currency):
    message = f"{title} is on sale for {price}!"

    with SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

