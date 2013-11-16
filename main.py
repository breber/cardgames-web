#!/usr/bin/env python
from google.appengine.api import users
from webapp2_extras import jinja2
import datetime
import models
import webapp2
import logging

class MainHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, template_args):
          self.response.write(self.jinja2.render_template(filename, **template_args))

    def get(self):
        path = 'welcome.html'

        self.render_template(path, {})

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
