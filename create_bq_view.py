#!/usr/bin/env python

import webapp2
from bqviewinit import BQView


class MainHandler(webapp2.RequestHandler):
    def get(self):
        bq_view = BQView()
        bq_view.init_view()

        self.response.write('ok')




app = webapp2.WSGIApplication([
    ('/tasks/create_bq_view', MainHandler)
], debug=True)