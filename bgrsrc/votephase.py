# coding: utf-8
import logging

from bgrsrc import closevote
from bgrsrc import getImage
from bgrsrc import justwait
from bgrsrc import svgtimer


logger = logging.getLogger(__name__)


def vote(window):
    logger.debug('投票フェーズに入りました')
    justwait.justWait(window, 5)
    logger.debug('画像お題であればダウンロードします')
    getImage.getImage(window)
    svgtimer.svgtimerevent(window)
    closevote.close(window)
    logger.debug('投票フェーズを抜けます')
