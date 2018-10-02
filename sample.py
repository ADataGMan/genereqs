import requests
import bs4
import pymongo
import datetime
import time
import urllib.parse
import multiprocessing
from multiprocessing import pool

import genereqs

genereqs.generate_requirements(globals())