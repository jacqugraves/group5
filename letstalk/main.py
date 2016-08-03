
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
        string1 = self.request.get("SideOne")
        string2 = self.request.get("SideTwo")
        t = DTopic(
        	TheId=124,
        	Topic=(string1 + " vs "+ string2),
        	Category =self.request.get("Cat"),
        	Comments =[self.request.get("FirstComment")])	

        t.put()
        self.redirect('/listtopic')


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
       Titledata = {'topic': self.request.get('category')}
       self.response.out.write(templates.render(Titledata)) 


       category = self.request.get('category')
       self.response.out.write(category)
       top = DTopic.query().filter(DTopic.TheId == 124).get()
       print top.Comments
       data={
        'comments':top.Comments
       }
       results_template = env.get_template('topics.html') 
       self.response.out.write(results_template.render(data))

    def post(self): ## here's the new POST method in the MainHandler
        top=DTopic.query().filter(DTopic.TheId == 124).get()
        top.Comments.append(self.request.get('newCom'))
        top.put()
        
        print ""
        print "the category is"
        print self.request.get('category')
        data = {
        'topic' : self.request.get('category'),
        'comments':top.Comments
        } 
        results_template = env.get_template('topics.html')
        self.response.out.write(results_template.render(data))
        self.response.out.write("Comment") 
         

        self.response.out.write(results_template.render())
        self.redirect('/listtopic')

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
