# -*- coding: utf-8 -*-
from datetime import datetime
from ..app import db


class Aprendizado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now())
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    active = db.Column(db.Boolean)

    def __init__(self, question, answer=None, active=None, **kwargs):
        self.question = question
        self.answer = answer
        self.active = active

    def __call__(self, question, answer=None, active=None, **kwargs):
        self.question = question
        self.answer = answer
        self.active = active

    def __repr__(self):
        return '<Aprendizado %s>' % self.answer
