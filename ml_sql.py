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


class Ricoh(Ml_Base):
    __tablename__ = 'RICOH'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Ricoh(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Brother(Ml_Base):
    __tablename__ = 'BROTHER'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Brother(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Canon(Ml_Base):
    __tablename__ = 'CANON'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Canon(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Epson(Ml_Base):
    __tablename__ = 'EPSON'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Epson(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Kyocera(Ml_Base):
    __tablename__ = 'KYOCERA'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Kyocera(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Lexmark(Ml_Base):
    __tablename__ = 'LEXMARK'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Lexmark(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Oki(Ml_Base):
    __tablename__ = 'OKI'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Oki(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


class Samsung(Ml_Base):
    __tablename__ = 'SAMSUNG'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    PARTS_NR = Column(Text)
    ΠΕΡΙΓΡΑΦΗ = Column(Text)
    ΚΩΔΙΚΟΣ = Column(Text)
    ΤΕΜΑΧΙΑ = Column(Text)
    ΠΑΡΑΤΗΡΗΣΗΣ = Column(Text)

    def __repr__(self):
        return "<Samsung(id='%i', code='%s')>" % (self.ID, self.ΚΩΔΙΚΟΣ)

    def __str__(self):
        return f"{self.ΤΕΜΑΧΙΑ}"


def get_ml_db_pieces(machine_model=None, ml_code=None):
    data = None

    try:
        if "konica" in machine_model.lower():
            data = Ml_Session.query(Konica).filter(Konica.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'sharp' in machine_model.lower():
            data = Ml_Session.query(Sharp).filter(Sharp.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'ricoh' in machine_model.lower():
            data = Ml_Session.query(Ricoh).filter(Ricoh.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'brother' in machine_model.lower():
            data = Ml_Session.query(Brother).filter(Brother.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'canon' in machine_model.lower():
            data = Ml_Session.query(Canon).filter(Canon.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'epson' in machine_model.lower():
            data = Ml_Session.query(Epson).filter(Epson.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'kyocera' in machine_model.lower():
            data = Ml_Session.query(Kyocera).filter(Kyocera.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'lexmark' in machine_model.lower():
            data = Ml_Session.query(Lexmark).filter(Lexmark.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'oki' in machine_model.lower():
            data = Ml_Session.query(Oki).filter(Oki.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data
        elif 'samsung' in machine_model.lower():
            data = Ml_Session.query(Samsung).filter(Samsung.ΚΩΔΙΚΟΣ == ml_code).one_or_none()
            return data

    except Exception:
        print(traceback.print_exc())

