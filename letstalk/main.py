
from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
env2 = jinja2.Environment(loader=jinja2.FileSystemLoader("NewTopicTemplate"))

def get_category_id(category_name):
    if category_name=='politics':
        n=100
    elif category_name== 'sexism':
        n=124
    elif category_name=='racism':
        n=300
    elif category_name=='world hunger':
        n=400
    elif category_name=='police brutality':
        n=500
    elif category_name== 'gun laws':
        n=600
    elif category_name=='student loans':
        n=700
    elif category_name== 'sexual assault':
        n=800
    elif category_name=='homelessness':
        n=900

    return n
        
 
class DTopic(ndb.Model):
	#Topic = ndb.StringProperty(required=True)
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
            template = env.get_template('mainindex.html') 
            login = users.create_login_url('/')
            greeting = '<a href="%s">Sign in or register</a>.' % login
            data = {"LogIn" : greeting}
            self.response.out.write(template.render(data))
        # datatwo = {}
        # self.response.write(template.render(datatwo))



class SetTopicHandler(webapp2.RequestHandler):
    def get(self):
        templates=env2.get_template('newTopic.html')  #render's the form for creating new topics
        self.response.out.write(templates.render())

    def post(self):
    	#self.response.out.write("submitted")
    	##results_template = env2.get_template('Talk.html')
        #self.response.out.write(results_template.render(top))
        n=get_category_id(self.request.get("Category"))
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
        
#user.get_current_user##############################################################################

class ListTopicHandler(webapp2.RequestHandler):
    def get(self):
        templates=env.get_template('topics.html')
        n=get_category_id(self.request.get("category"))
        top = DTopic.query().filter(DTopic.TheId == n).get()
        if top is None:
            my_comments = []
            t = DTopic(
                TheId=n,
                Category =self.request.get("Category"))
            t.put()
            #'Category'=(self.request.get("category"))
        else:
            my_comments = top.Comments

        data={
            'topic': self.request.get('category'),
            'comments':my_comments
        }
        results_template = env.get_template('topics.html') 
        self.response.out.write(results_template.render(data))
        
    def post(self): ## here's the new POST method in the MainHandler
        n=get_category_id(self.request.get("category"))
        top=DTopic.query().filter(DTopic.TheId == n).get()
        top.Comments.append(self.request.get('newCom'))
        top.put()
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

class WorkHandler(webapp2.RequestHandler):
    def get(self):
        templates=env2.get_template('mainindex.html')  #render's the form for creating new topics
        self.response.out.write(templates.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/webpage', WebPageHandler),
    ('/newtopic', SetTopicHandler),
    ('/talkpage', TalkPageHandler),
    ('/workpage', WorkHandler),
    ('/listtopic', ListTopicHandler)
], debug=True)
