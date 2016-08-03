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
# limitations under the License.from google.appengine.api import users
from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
env2 = jinja2.Environment(loader=jinja2.FileSystemLoader("NewTopicTemplate"))

class DTopic(ndb.Model):
	Topic = ndb.StringProperty(required=True)
	Category = ndb.StringProperty(required=True, default='Misc')
	Comments = ndb.StringProperty(repeated=True)
	TheId= ndb.IntegerProperty()


class WebPageHandler(webapp2.RequestHandler):
 def get(self): 
    template = env.get_template('index.html')   
    #template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render())


class MainHandler(webapp2.RequestHandler):  #Page user see's first asking them to login in 
 def get(self):     
    user = users.get_current_user()
    if user:  #if the user is logged in it will render the main webpage
        template = env.get_template('index.html') 
        self.response.out.write(template.render())
    else:  #if the user is not logged in, it will ask them to login then redirect 
        login = users.create_login_url('/')
        greeting = '<a href="%s">Sign in or register</a>.' % login
        self.response.out.write('<html><body>%s</body></html>' % greeting)

class SetTopicHandler(webapp2.RequestHandler):
    def get(self):
        templates=env2.get_template('newTopic.html')  #render's the form for creating new topics
        self.response.out.write(templates.render())
    def post(self):
    	#self.response.out.write("submitted")
    	##results_template = env2.get_template('Talk.html')
        #self.response.out.write(results_template.render(top))
        string1 = self.request.get("SideOne")
        string2 = self.request.get("SideTwo")
        t = DTopic(
        	TheId=124,
        	Topic=(string1 + " vs "+ string2),
        	Category =self.request.get("Cat"),
        	Comments =[self.request.get("FirstComment")])	
        t.put()
        self.redirect('/talkpage')


class TalkPageHandler(webapp2.RequestHandler):
    def get(self):
        #templates=env2.get_template('Talk.html')
        #self.response.out.write(templates.render())
        top = DTopic.query().filter(DTopic.TheId == 124).get()
        #for comment in top:
        print top.Comments
        data={
        'comments':top.Comments
        }

        results_template = env2.get_template('Talk.html')
        self.response.out.write(results_template.render(data))

    def post(self):
        top=DTopic.query().filter(DTopic.TheId == 124).get()
        top.Comments.append(self.request.get('newCom'))
        top.put()
       
        results_template = env2.get_template('Talk.html')
        self.redirect('/talkpage')


class ListTopicHandler(webapp2.RequestHandler):
    def get(self):
       templates=env.get_template('topics.html')
       self.response.out.write(templates.render()) 
       category = self.request.get('category')
       self.response.out.write(category)
    def post(self): ## here's the new POST method in the MainHandler
        self.response.out.write("Comment") 
        results_template = env.get_template('topics.html') 
        self.response.out.write(results_template.render())

class FormatHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("format.html")
        format_query = Format.query()
        format_results = format_query.fetch()
        format_result = format_results[0]
        data = {}
        data['title'] = format_result.title
        data[''] = format_result.source
        self.response.write(template.render(data)) 


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/webpage', WebPageHandler),
    ('/newtopic', SetTopicHandler),
    ('/talkpage', TalkPageHandler),
    ('/listtopic', ListTopicHandler)
], debug=True)
