""" users Table """

from sqlalchemy import (
    Column,
    String,
    Integer
)
from . import (
    SESSION,
    BASE
)


class Users(BASE):
    """ Table to store the received messages """
    __tablename__ = "users"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    um_id = Column(Integer)
    mu_id = Column(Integer)
    kopp_id = Column(Integer)

    def __init__(self, message_id, chat_id, um_id, mu_id, kopp_id):
        self.message_id = message_id
        self.chat_id = str(chat_id)  # ensure string
        self.um_id = um_id
        self.mu_id = mu_id
        self.kopp_id = kopp_id

    def __repr__(self):
        return "<User %s>" % self.chat_id


Users.__table__.create(checkfirst=True)


def add_user_to_db(
    message_id: int,
    chat_id: int,
    um_id: int,
    mu_id: int,
    kopp_id: int
):
    """ add the message to the table """
    __user = Users(message_id, str(chat_id), um_id, mu_id, kopp_id)
    SESSION.add(__user)
    SESSION.commit()


def get_user_id(message_id: int):
    """ get the user_id from the message_id """
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        if s__:
            return int(s__.chat_id), s__.um_id
        return None, None
    finally:
        SESSION.close()


def get_chek_dmid(um_id: int):
    """ get the deleted user_id from the um_id """
    try:
        all_lst = SESSION.query(
            Users
        ).filter(
            Users.um_id == um_id
        ).all()
        if all_lst:
            return all_lst[-1]
    finally:
        SESSION.close()


def get_chek_mdid(kopp_id: int):
    """ get the deleted user_id from the kopp_id """
    try:
        all_lst = SESSION.query(
            Users
        ).filter(
            Users.kopp_id == kopp_id
        ).all()
        if all_lst:
            return all_lst[-1]
    finally:
        SESSION.close()


def get_chats():
    try:
        All = SESSION.query(Users).filter().all()
        return list({int(a.chat_id) for a in All})
    finally:
        SESSION.close()
