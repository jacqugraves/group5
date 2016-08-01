#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import webapp2

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
 emails= [{'subject':'Lunch?', 'unread' : True, 'spam': False },
         {'subject':'Google+ notification', 'unread' : False, 'spam': False},
         {'subject':'Help! send me money from your account!', 'unread': True, 'spam': True},
         {'subject':'Meeting on Thursday', 'unread' : False, 'spam': False}]
 def get(self):
     template = env.get_template('main.html')
     variables = {'name':self.request.get('name'),
                 'emails':self.emails}

     self.response.write(template.render(variables))

app = webapp2.WSGIApplication([
   ('/', MainHandler)
], debug=True)