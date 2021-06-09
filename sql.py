#! /usr/bin/python3
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                  Παραγγελίες Ιταλία
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.1
# -------------------------------------------------------------------------------
import datetime
import sys
import traceback
import pandas as pd
from settings import database, root_logger, book, sheet

from sqlalchemy import create_engine, Column, Integer, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info

ital_engine = create_engine(f"sqlite:///{database}")
Ital_Session = sessionmaker(bind=ital_engine)()
Ital_Base = declarative_base()
ital_metadata = Ital_Base.metadata


# Μηχανήματα
class Machine(Ital_Base):
    __tablename__ = 'machines'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(Text)
    prices_date = Column(Text)

    def __repr__(self):
        return "<machine(id='%i', model='%s')>" % (self.ID, self.model)

    def __str__(self):
        return f"{self.model}"


# Ανταλλακτικά
class SparePart(Ital_Base):
    __tablename__ = 'spare_parts'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    machine = Column(Integer, ForeignKey('machines.ID'))
    machine_ref = relationship("Machine", backref=backref("spare_part"))

    part_nr = Column(Text)
    description = Column(Text)
    ml_code = Column(Text)
    ital_code = Column(Text)
    ital_price = Column(Text)
    info_code = Column(Text)
    info_site_code = Column(Text)
    info_price = Column(Text)

    def __repr__(self):
        return "<SparePart(id='%i', machine='%s', part_nr='%s', description='%s', ml_code='%s', ital_code='%s', " \
               "info_code='%s', info_site_code='%s')>" \
               % (self.ID, self.machine, self.part_nr, self.description, self.ml_code, self.ital_code, self.info_code,
                  self.info_site_code)

    def __str__(self):
        return f"{self.machine} {self.part_nr} {self.description} {self.ml_code} {self.ital_code} {self.ital_price}" \
               f" {self.info_code} {self.info_site_code} {self.info_price}"


# Καλάθι
class Basket(Ital_Base):
    __tablename__ = 'basket'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    machine = Column(Integer, ForeignKey('machines.ID'))
    machine_ref = relationship("Machine", backref=backref("basket"))

    ml_code = Column(Text)

    spare_part = Column(Integer, ForeignKey('spare_parts.ID'))
    spare_part_ref = relationship("SparePart", backref=backref("basket"))

    price = Column(Text)
    pieces = Column(Integer)
    total = Column(Text)

    def __str__(self):
        return f"{self.machine} {self.ml_code} {self.spare_part} {self.price} {self.pieces} {self.total}"


# Παραγγελίες
class Order(Ital_Base):
    __tablename__ = 'orders'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Text)
    machine = Column(Integer, ForeignKey('machines.ID'))
    machine_ref = relationship("Machine", backref=backref("order"))

    spare_part = Column(Integer, ForeignKey('spare_parts.ID'))
    spare_part_ref = relationship("SparePart", backref=backref("order"))

    price = Column(Text)
    pieces = Column(Integer)
    total = Column(Text)

    def __repr__(self):
        return "<Orders(id='%i', date='%s', machine='%s', spare_part='%s', price='%i', pieces='%f', total='%f')>" \
               % (self.ID, self.date, self.machine, self.spare_part, self.price, self.pieces, self.total)

    def __str__(self):
        return f"{self.date} {self.machine} {self.spare_part} {self.price} {self.pieces} {self.total}"


# Αποκόμηση δεδομένων απο τον πίνακα
def get_spare_parts(machine_id):
    try:
        data = Ital_Session.query(SparePart).filter(SparePart.machine == machine_id).order_by(
            SparePart.description).all()

        return data
    except Exception:
        print(traceback.print_exc())
        return


def save_prices(data):
    try:
        for index in range(len(data)):
            spare_part = Ital_Session.query(SparePart).get(data[index]["ID"])
            spare_part.part_nr = data[index]["part_nr"]
            spare_part.ml_code = data[index]["ml_code"]
            spare_part.ital_code = data[index]["ital_code"]
            spare_part.ital_price = data[index]["ital_price"]
            spare_part.info_code = data[index]["info_code"]
            spare_part.info_site_code = data[index]["info_site_code"]
            spare_part.info_price = data[index]['info_price']
            Ital_Session.commit()

            machine_id = spare_part.machine
            machine = Ital_Session.query(Machine).get(machine_id)
            machine.prices_date = datetime.datetime.today().strftime("%d/%m/%Y")
            Ital_Session.commit()

        return True
    except Exception:
        print(traceback.print_exc())
        return False


# Αποκόμηση μοντέλου απο τον πίνακα
def get_model(machine_id):
    try:
        data = Ital_Session.query(Machine).get(machine_id)

        return data.model
    except Exception:
        print(traceback.print_exc())
        return


def save_to_basket(part_id=None, pieces=None):
    spare_part = Ital_Session.query(SparePart).get(part_id)
    machine_id = spare_part.machine
    ml_code = spare_part.ml_code
    # Ελεγχος αν υπάρχει ο κωδικός ιδη στο καλάθι
    item = Ital_Session.query(Basket).filter_by(ml_code=ml_code).one_or_none()
    if item:
        return f"Ο κωδικός {ml_code} υπάρχει στο καλάθι"
    price = spare_part.ital_price.replace(" €", "").replace(",", ".")
    total = "{:.2f}".format(float(price) * int(pieces))
    machine_model = spare_part.machine_ref
    item_to_basket = Basket(machine=machine_id, ml_code=ml_code, spare_part=part_id, price=price, pieces=pieces,
                            total=total)
    Ital_Session.add(item_to_basket)
    Ital_Session.commit()


def get_basket():
    data = Ital_Session.query(Basket).order_by(Basket.machine).all()

    return data


def save_basket(items_to_save=None, items_ids=None):
    try:
        for index in range(len(items_to_save)):
            spare_part = Ital_Session.query(Basket).get(items_to_save[index]["ID"])
            spare_part.ml_code = items_to_save[index]["ml_code"]
            spare_part.price = items_to_save[index]["price"]
            spare_part.pieces = items_to_save[index]["pieces"]
            spare_part.total = items_to_save[index]["total"]
            Ital_Session.commit()

        # Αφου αποθηκεύσουμε αυτά να σβήσουμε τα υπολποπα items που ειναι στο καλάθι
        all_items = Ital_Session.query(Basket).all()
        for item in all_items:
            if item.ID not in items_ids:
                Ital_Session.delete(item)
                Ital_Session.commit()
        return True
    except Exception:
        print(traceback.print_exc())
        return traceback.print_exc()


def get_prices_date(machine_id):
    try:
        data = Ital_Session.query(Machine).get(machine_id)

        return data.prices_date
    except Exception:
        print(traceback.print_exc())
        return


def colorized(v):
    sharp_color = '#C4BD97'
    konica_color = '#8EB4E3'
    overall_total_color = '#92d050'

    if 'Sharp' in str(v):
        color = sharp_color

    elif 'Konica' in str(v):
        color = konica_color

    elif 'Τελικό σύνολο' in str(v):
        color = overall_total_color

    else:
        return

    return 'background-color: %s' % f'{color}'


def save_order():
    all_bask_obj = Ital_Session.query(Basket).join(SparePart).all()

    today = datetime.datetime.today().strftime("%d.%m.%Y")
    writer = pd.ExcelWriter(f'{book}', mode="a", engine='openpyxl')
    machines_list = []
    final_df = {}
    d = {'Μηχάνημα': [], 'Κωδικός': [], 'Κωδικός Ιταλίας': [], 'Περιγραφή': [], 'Τεμάχια': [], 'Τιμή': [], "Σύνολο": []}
    all_totals = []
    try:
        for item in all_bask_obj:
            # κενές γραμμές
            if item.machine_ref.model in machines_list:
                d['Μηχάνημα'].append("")

            else:
                # Αν δεν είναι στην λίστα να βαλει  κενες γραμμές και μετα τα δεδομένα
                machines_list.append(item.machine_ref.model)
                d['Μηχάνημα'].append("")
                d['Κωδικός'].append("")
                d['Κωδικός Ιταλίας'].append("")
                d['Περιγραφή'].append("")
                d['Τεμάχια'].append("")
                d['Τιμή'].append("")
                d['Σύνολο'].append("")

                d['Μηχάνημα'].append(item.machine_ref.model)
                d['Κωδικός'].append("")
                d['Κωδικός Ιταλίας'].append("")
                d['Περιγραφή'].append("")
                d['Τεμάχια'].append("")
                d['Τιμή'].append("")
                d['Σύνολο'].append("")

                d['Μηχάνημα'].append("")
                d['Κωδικός'].append(item.ml_code)
                d['Κωδικός Ιταλίας'].append(item.spare_part_ref.ital_code)
                d['Περιγραφή'].append(item.spare_part_ref.description)
                d['Τεμάχια'].append(item.pieces)
                d['Τιμή'].append(item.price + ' €')
                d['Σύνολο'].append(item.total + ' €')
                all_totals.append(float(item.total))
                order_item = Order(date=today, machine=item.machine, spare_part=item.spare_part,
                                   price=item.price, pieces=int(item.pieces), total=item.total)
                Ital_Session.add(order_item)
                continue

            d['Κωδικός'].append(item.ml_code)
            d['Κωδικός Ιταλίας'].append(item.spare_part_ref.ital_code)
            d['Περιγραφή'].append(item.spare_part_ref.description)
            d['Τεμάχια'].append(item.pieces)
            d['Τιμή'].append(str(item.price) + ' €')
            d['Σύνολο'].append(str(item.total) + ' €')
            all_totals.append(float(item.total))
            order_item = Order(date=today, machine=item.machine, spare_part=item.spare_part,
                               price=item.price, pieces=int(item.pieces), total=item.total)
            Ital_Session.add(order_item)

        # Γραμμή Τελίκό Σύνολο
        d['Μηχάνημα'].append("")
        d['Κωδικός'].append("")
        d['Κωδικός Ιταλίας'].append("")
        d['Περιγραφή'].append("")
        d['Τεμάχια'].append("")
        d['Τιμή'].append("")
        d['Σύνολο'].append('')

        d['Μηχάνημα'].append("Τελικό σύνολο")
        d['Κωδικός'].append("")
        d['Κωδικός Ιταλίας'].append("")
        d['Περιγραφή'].append("")
        d['Τεμάχια'].append("")
        d['Τιμή'].append("")
        d['Σύνολο'].append(str("{:.2f}".format(sum(all_totals))) + ' €')
        df = pd.DataFrame(data=d)
        styled = df.style.applymap(colorized)
        # print("df.Μηχάνημα", df.Μηχάνημα)
        # styled.to_excel('styled.xlsx', engine='openpyxl', index=False)
        print("sheet", sheet)
        styled.to_excel(writer, sheet_name=f'{sheet}', startcol=1, startrow=2, index=False)
        writer.save()
        # Ital_Session.commit()
        # Αδειασμα πίνακα καλαθιού - basket
        Ital_Session.query(Basket).delete()
        Ital_Session.commit()
        return True
    except Exception:
        print(traceback.print_exc())
        return traceback.print_exc()


def get_orders_dates():
    orders_obj = Ital_Session.query(Order).order_by(Order.date).all()
    dates = []
    for order in orders_obj:
        if order.date not in dates:
            dates.append(order.date)
    dates.sort(key=lambda date: datetime.datetime.strptime(date, '%d.%m.%Y'))
    return dates


def get_history(selected_date=None):
    data = Ital_Session.query(Order).filter(Order.date == selected_date).all()
    return data

    # Create Tables
# Base.metadata.create_all(engine)

# Insert data
# pay1 = Payments(supplier_id=9, amount=20, date=datetime.date.today())
# Session.add(pay1)
# Session.commit()
