#!/usr/bin/env python
import datetime

def get_context():
    context = {}
    context['currentYear'] = datetime.date.today().year

    return context
