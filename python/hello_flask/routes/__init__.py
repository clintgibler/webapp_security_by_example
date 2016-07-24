from flask import Blueprint
routes = Blueprint('routes', __name__)

#from .index import *
from .xss import *
from .client_side import *
