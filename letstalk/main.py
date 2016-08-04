
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
    topics = {'politics': 'politics',
          'sexism': 'sexism',
          'racism': 'racism',
          'world hunger': 'worldhunger',
          'police brutality':'policebrutality',
          'gun laws': 'gun',
          'student loans': 'studentloans',
          'sexual assault': 'sexualassault',
          'homelessness': 'homelessness'}
    
    def get(self):     
        user = users.get_current_user()
        if user:  #if the user is logged in it will render the main webpage
            data = {'topics': self.topics}
            template = env.get_template('index.html') 
            self.response.out.write(template.render(data))
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
        if self.request.get('Category')=='politics':
            n=100
        if self.request.get('Category')== 'sexism':
            n=124
        if self.request.get('Category')=='racism':
            n=300
        if self.request.get('Category')== 'world hunger':
            n=400
        if self.request.get('Category')=='police brutality':
            n=500
        if self.request.get('Category')== 'gun laws':
            n=600
        if self.request.get('Category')=='student loans':
            n=700
        if self.request.get('Category')== 'sexual assault':
            n=800
        if self.request.get('Category')=='homelessness':
            n=900
        string1 = self.request.get("SideOne")
        string2 = self.request.get("SideTwo")
        t = DTopic(
        	TheId=n,
        	Topic=(string1 + " vs "+ string2),
        	Category =self.request.get("Category"),
        	Comments =[self.request.get("FirstComment")])	

        t.put()
        self.redirect('/listtopic')




class TalkPageHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/listtopic?category=' + self.request.get('category'))
        #templates=env2.get_template('Talk.html')
        #self.response.out.write(templates.render())
        #top = DTopic.query().filter(DTopic.TheId == 124).get()
        #for comment in top:
        #print top.Comments
        #data={
        #'comments':top.Comments
        #}

        #results_template = env2.get_template('Talk.html')
        #self.response.out.write(results_template.render(data))

    #def post(self):
     #   top=DTopic.query().filter(DTopic.TheId == 124).get()
      #  top.Comments.append(self.request.get('newCom'))
       # top.put()
       
        #results_template = env2.get_template('Talk.html')
        


class ListTopicHandler(webapp2.RequestHandler):
    def get(self):
        templates=env.get_template('topics.html')
        if self.request.get('category')=='politics':
            DTopic.query().filter(DTopic.TheId == 100).get()
            n=100
        if self.request.get('category')== 'sexism':
            DTopic.query().filter(DTopic.TheId == 124).get()
            n=124
        if self.request.get('category')=='racism':
            DTopic.query().filter(DTopic.TheId == 300).get()
            n=300
        if self.request.get('category')== 'world hunger':
            DTopic.query().filter(DTopic.TheId == 400).get()
            n=400
        if self.request.get('category')=='police brutality':
            DTopic.query().filter(DTopic.TheId == 500).get()
            n=500
        if self.request.get('category')== 'gun laws':
            DTopic.query().filter(DTopic.TheId == 600).get()
            n=600
        if self.request.get('category')=='student loans':
            DTopic.query().filter(DTopic.TheId == 700).get()
            n=700
        if self.request.get('category')== 'sexual assault':
            DTopic.query().filter(DTopic.TheId == 800).get()
            n=800
        if self.request.get('category')=='homelessness':
            DTopic.query().filter(DTopic.TheId == 900).get()
            n=900
        top = DTopic.query().filter(DTopic.TheId == n).get()
        data={
            'topic': self.request.get('category'),
            'comments':top.Comments
        }
        results_template = env.get_template('topics.html') 
        self.response.out.write(results_template.render(data))

    def post(self): ## here's the new POST method in the MainHandler
        if self.request.get('category')=='politics':
            DTopic.query().filter(DTopic.TheId == 100).get()
            n=100
        if self.request.get('category')== 'sexism':
            DTopic.query().filter(DTopic.TheId == 124).get()
            n=124
        if self.request.get('category')=='racism':
            DTopic.query().filter(DTopic.TheId == 300).get()
            n=300
        if self.request.get('category')== 'world hunger':
            DTopic.query().filter(DTopic.TheId == 400).get()
            n=400
        if self.request.get('category')=='police brutality':
            DTopic.query().filter(DTopic.TheId == 500).get()
            n=500
        if self.request.get('category')== 'gun laws':
            DTopic.query().filter(DTopic.TheId == 600).get()
            n=600
        if self.request.get('category')=='student loans':
            DTopic.query().filter(DTopic.TheId == 700).get()
            n=700
        if self.request.get('category')== 'sexual assault':
            DTopic.query().filter(DTopic.TheId == 800).get()
            n=800
        if self.request.get('category')=='homelessness':
            DTopic.query().filter(DTopic.TheId == 900).get()
            n=900
        top=DTopic.query().filter(DTopic.TheId == n).get()
        top.Comments.append(self.request.get('newCom'))
        top.put()
        
        #print ""
        #print "the category is"
        #print self.request.get('category')
        #data = {
        #'topic' : self.request.get('category'),
        #'comments':top.Comments
        #} 
       # results_template = env.get_template('topics.html')
        #self.response.out.write(results_template.render(data))
        self.redirect('/listtopic?category=' + self.request.get('category'))
        #self.redirect('/talkpage')
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
