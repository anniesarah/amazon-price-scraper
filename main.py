import requests
from bs4 import BeautifulSoup
import smtplib

ITEM_NAME = "Mielle Rosemary Mint Scalp and Hair Strengthening Oil" # Only for the email
URL = ("https://www.amazon.de/-/en/Mielle-Organics-Rosemary-Strengthening-Healthy/dp/B07N7PK9QK/ref"
       "=zg_bs_c_beauty_d_sccl_1/260-5431014-4375759?pd_rd_w=MUDjB&content-id=amzn1.sym.23b89adb-9909-4f81-be6e"
       "-d852030876a5&pf_rd_p=23b89adb-9909-4f81-be6e-d852030876a5&pf_rd_r=QX7BZQ4HT0CT8VVHHAZA&pd_rd_wg=iAXIq"
       "&pd_rd_r=d2ffc6e3-18c5-4123-8777-3e44a14e843f&pd_rd_i=B07N7PK9QK&psc=1")
LOW_PRICE_POINT = 13 # You can find your item's low price point on camelcamelcamel

page = requests.get(URL, headers={"User-Agent": "Defined"})
soup = BeautifulSoup(page.content, "html.parser")
price_data = soup.find(name="span", class_="a-price")
price = price_data.get_text().split("€")[1]
if float(price) < LOW_PRICE_POINT:
    my_email = "your email"
    my_password = "your password"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:{ITEM_NAME} is now only {price}\n\n"
                f"Buy your item now at {URL}".encode("utf-8")
        )
