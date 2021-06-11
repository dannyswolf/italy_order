#! /usr/bin/python3
# -*- coding: utf-8 -*-

# ---------------------------------------------------------
#                  Παραγγελίες Ιταλία
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.4
# ----------------------------------------------------------

import logging
import os
import sys
import datetime


version = "V 0.4"
credentials = "credentials.yml"
database = "italia.db"
ml_db = "3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"
book = 'ΙΤΑΛΙΑ - Copy.xlsx'
today = datetime.datetime.today().strftime("%d.%m.%Y")
sheet = f'ΠΑΡΑΓΓΕΛΙΑ ΜΑΚΗΣ {today}'
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE και Ημερομηνία ------------------
today = datetime.datetime.today().strftime("%d %m %Y")
log_dir = "logs" + "/" + today + "/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
else:
    pass

log_file_name = today + ".log"
log_file = os.path.join(log_dir, log_file_name)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # or whatever

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(log_file, 'a', 'utf-8')  # or whatever

handler.setFormatter(formatter)  # Pass handler as a parameter, not assign
root_logger.addHandler(handler)
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
