#! /usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                  Παραγγελίες Ιταλία
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.1
# -------------------------------------------------------------------------------
import sys
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_html import HTML
from settings import root_logger, credentials
import yaml
from yaml import CLoader as Loader
import traceback

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info

"""
ITALIA
"""

with open(credentials, "r", encoding='utf8') as cred:
    cred_obj = yaml.load(cred, Loader=Loader)

ital_login_url = cred_obj["ital_login_url"]["url"]
ital_payload = cred_obj['ital_payload']

ital_session = requests.Session()
# headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/81.0.4044.141 Safari/537.36"}


def get_ital_price(ital_code):
    try:
        retry = Retry(connect=3)
        adapter = HTTPAdapter(max_retries=retry)
        ital_session.mount('http://', adapter)
        ital_session.mount('https://', adapter)
        ital_response = ital_session.post(ital_login_url, data=ital_payload)
        ital_requests_url = f'https://www.itrip.it/default.php?t=ecomm&act=personal&search=1&codice={ital_code}'
        with ital_session.get(ital_requests_url) as ital_html:
            ital_html_data = ital_html.text
            ital_data = HTML(html=ital_html_data)
            ital_price = ital_data.find(".col5")
            return ital_price[0].text
    except Exception:
        print(traceback.print_exc())


# ital_session = requests.Session()
# ital_response = ital_session.post(ital_login_url, data=ital_payload)
# ital_html = ital_session.get(ital_requests_url)
# ital_html_data = ital_html.text
# ital_data = HTML(html=ital_html_data)
#
# ital_availability = ital_data.find(".productAvail")
# ital_model = ital_data.find(".td_modello")
# print(ital_model[0].text)
# print(ital_availability[0].text)
# print(ital_price[0].text)



"""
ASYNC
"""
# import aiohttp
# import asyncio
# async def get_price(session, url, ital=True):
#     async with session.get(url) as resp:
#         price = await resp.content_disposition
#         print("Price.read()", price)
#         data = HTML(html=price)
#         if ital:
#             ital_price = data.find(".col5")
#             print("Italia")
#             print(datetime.now().strftime("%H:%M:%S"))
#             print("get_price", ital_price[0].text)
#             return ital_price[0].text
#         else:
#             info_price = data.find(".m_nb")
#             print("INFO-Copy")
#             print(datetime.now().strftime("%H:%M:%S"))
#             clean_info_price = info_price[1].text[-8:].splitlines()
#             print("Clean Info Price", clean_info_price[-1])
#             return clean_info_price[-1]
#
#
# async def main(ital_code=None, info_site_code=None):
#     async with aiohttp.ClientSession() as session:
#
#         tasks = []
#         ital_login = False
#         info_login = False
#         if ital_code is not None:
#             if not ital_login:
#                 await session.post(ital_login_url, data=ital_payload)
#                 ital_login = True
#             ital_url = f'https://www.itrip.it/default.php?t=ecomm&act=personal&search=1&codice={ital_code}'
#             tasks.append(asyncio.ensure_future(get_price(session, ital_url, ital=True)))
#         if info_site_code is not None:
#             if not info_login:
#                 await session.post(info_login_url, data=info_payload)
#                 info_login = True
#             info_product_url = f"http://www.infocopy.gr/index.php?com=products1&id={info_site_code}"
#             tasks.append(asyncio.ensure_future(get_price(session, info_product_url, ital=False)))
#
#         original_price = await asyncio.gather(*tasks)
#         for price in original_price:
#             return price