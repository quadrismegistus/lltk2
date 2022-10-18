from imports import *

# -------------------
# Template tags
# -------------------

@template.simple_tag
def say_hello(name):
    return 'Hello, {}!'.format(name)
