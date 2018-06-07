# coding: utf-8
import logging
from bgrsrc import start

logging.basicConfig(filename='test.log', format='%(levelname)s:%(message)s')
logging.getLogger("src").setLevel(level=logging.DEBUG)

start.init()
