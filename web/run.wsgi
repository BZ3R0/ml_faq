import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/../src")

from chatbot.app import app as application
application.secret_key = 'w4\x06\x12\x94\\t\xb3\xe0@\x13>\xea\xa49\x97\x92av\xc0*\xe9x}'
