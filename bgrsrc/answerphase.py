# coding: utf-8
import logging

from bgrsrc import access
from bgrsrc import closeanswer
from bgrsrc import justwait
from bgrsrc import svgtimer


logger = logging.getLogger(__name__)


def answer(window):
    logger.debug('回答フェーズに入りました')
    justwait.justWait(window, 5)
    access.permission(window)
    svgtimer.svgtimerevent(window)
    closeanswer.close(window)
