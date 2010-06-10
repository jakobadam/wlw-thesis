import os
import cgi

from webob.multidict import MultiDict

from google.appengine.ext import webapp
from google.appengine.api import users

from django.utils import simplejson 

from helpers.decorators import require_login

class RestController(webapp.RequestHandler):
    """Route HTTP requests to the corresponding method wrt. the HTTP method and argument.
    
    In addition to supporting usual PUT and DELETE, PUT and DELETE are also handled by use of 
    overloaded POST:
        resource/{id}/?_method=PUT
        resource/{id}/?_method=DELETE
    
    Args:
        **kwargs
            id: if specefied taken to be the id of a concrete resource
    returns:
        response - HTTP response 
    """
    def doIndex(self, *args):
        self.error(405)

    def doShow(self, *args):
        self.error(405)
        
    def doPost(self, *args):
        self.error(405)
                    
    def doGet(self, *args):
        self.error(405)

    def doDelete(self, *args):
        self.error(405)


    # overwritten get, put, post
    def get(self, key=None):
        if key:
            # GET the concrete item
            return self.doShow(key)
        else:
            # GET the items
            return self.doIndex()

    @require_login
    def put(self, *args):
        self._load_post_data()
        return self.doPut(*args)

    @require_login
    def post(self, *args):
        self._load_post_data()
        method = self.request.get('_method')
        if method:
            try:
                callback = getattr(self, 'do%s' % method.capitalize())
                return callback(*args)
            except ValueError:
                self.error(405)
        else:
            return self.doPost()
    
    def _load_post_data(self):
        content_type = self.request.content_type
        if content_type == 'application/json':
            self.data = simplejson.loads(self.request.body)
        elif content_type == 'application/x-www-form-urlencoded':
            # LOOK INTO THIS
            fs = cgi.FieldStorage(fp=self.request.body_file,
                                  environ=self.request.environ.copy(),
                                  keep_blank_values=True)
            self.data = MultiDict.from_fieldstorage(fs) 
        else:
            raise "Unsupported content type: %s" % content_type
        
            

          


