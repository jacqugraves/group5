from google.appengine.ext import ndb

class Format(ndb.Model):
	title = ndb.StringProperty(required = True)
	 #= ndb.StringProperty(required = True)