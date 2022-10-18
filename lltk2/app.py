import os, sys, inspect
sys.path.insert(0, os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
print(sys.path)

from config import *
from imports import *
from models import *
from views import *
from admin import *
from templates import *
from commands import *
from tests import *

# -------------------
# Expose application
# -------------------

application = run()