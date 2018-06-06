# coding: utf-8
import logging

from src.bgrsrc import closevote
from src.bgrsrc import getImage
from src.bgrsrc import justwait
from src.bgrsrc import svgtimer


logger = logging.getLogger(__name__)


def vote(window):
    logger.debug('投票フェーズに入りました')
    justwait.justWait(window, 5)
    logger.debug('画像お題であればダウンロードします')
    getImage.getImage(window)
    svgtimer.svgtimerevent(window)
    closevote.close(window)
    logger.debug('投票フェーズを抜けます')
