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
import traceback
from settings import root_logger, credentials
import yaml
from yaml import CLoader as Loader

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info

"""
INFO COPY
"""


with open(credentials, "r", encoding='utf8') as cred:
    cred_obj = yaml.load(cred, Loader=Loader)

info_login_url = cred_obj["info_login_url"]["url"]
info_payload = cred_obj['info_payload']


def get_info_price(info_site_code):
    try:
        info_session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        info_session.mount('http://', adapter)
        info_session.mount('https://', adapter)
        info_response = info_session.post(info_login_url, data=info_payload)

        info_product_url = f"http://www.infocopy.gr/index.php?com=products1&id={info_site_code}"
        info_html = info_session.get(info_product_url)
        info_html_data = info_html.text
        info_data = HTML(html=info_html_data)
        info_price = info_data.find(".m_nb")
        clean_info_price = info_price[1].text[-8:].splitlines()
        return clean_info_price[-1]
    except Exception:
        print(traceback.print_exc())

