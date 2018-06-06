# coding: utf-8
import logging

from bgrsrc import phase
from bgrsrc import justwait


logger = logging.getLogger(__name__)


def waiting(window):
    logger.debug('待ち状態')
    while True:
        phase_name = phase.getPhaseName(window)
        if phase_name is None:
            justwait.justWait(window, 5)
            continue
        else:
            logger.info('待ち状態を抜けます')
            break
