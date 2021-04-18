"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
    'bird',
    ### TODO: define the fields that are in the json.
    Field('bird', requires=IS_NOT_EMPTY()),
    Field('weight', 'float', requires=IS_NOT_EMPTY() and IS_FLOAT_IN_RANGE(0, 1e6)),
    Field('diet', requires=IS_NOT_EMPTY()),
    Field('habitat', requires=IS_NOT_EMPTY()),
    Field('bird_count', 'integer', requires=IS_INT_IN_RANGE(0, 1e6)),
    Field('seen_by', default=get_user_email),
)

db.bird.seen_by.readable = db.bird.seen_by.writable = False

db.commit()
