"""
Includes all the required modules to include
"""

# tornado modules
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.gen import coroutine
from tornado.options import define, options

# external modules
import os
import numpy as np
import uuid
from oct2py import octave
from collections import defaultdict
from pymongo import MongoClient

db = MongoClient()["data"]
octave.addpath('matlab/')
