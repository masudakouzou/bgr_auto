# coding: utf-8
import logging

from src.bgrsrc import access
from src.bgrsrc import closeanswer
from src.bgrsrc import justwait
from src.bgrsrc import svgtimer


logger = logging.getLogger(__name__)


def answer(window):
    logger.debug('回答フェーズに入りました')
    justwait.justWait(window, 5)
    access.permission(window)
    svgtimer.svgtimerevent(window)
    closeanswer.close(window)
