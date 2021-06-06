#! /usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                  Παραγγελίες Ιταλία
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.1
# -------------------------------------------------------------------------------
import sys
from settings import  ml_db

from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import root_logger
import traceback

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


ml_engine = create_engine(f"sqlite:///{ml_db}")
Ml_Session = sessionmaker(bind=ml_engine)()
Ml_Base = declarative_base()
ml_metadata = Ml_Base.metadata


# Konica απο 3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ
class Konica(Ml_Base):
    __tablename__ = 'KONICA'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Konica(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


# Sharp απο 3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ
class Sharp(Ml_Base):
    __tablename__ = 'SHARP'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Sharp(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


def get_ml_konica_pieces(ml_code):
    try:
        data = Ml_Session.query(Konica).filter(Konica.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
        Ml_Session.close()
        return data
    except Exception:
        print(traceback.print_exc())


def get_ml_sharp_pieces(ml_code):
    try:
        data = Ml_Session.query(Sharp).filter(Sharp.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
        Ml_Session.close()
        return data
    except Exception:
        print(traceback.print_exc())
