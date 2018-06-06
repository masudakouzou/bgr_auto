# coding: utf-8
import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.bgrsrc import justwait

logger = logging.getLogger(__name__)


def close(window):
    while True:
        try:
            logger.debug('投票締め切り')
            window.find_element_by_xpath('/html/body/div/div/div[4]/div/div[1]/button').click()
        except NoSuchElementException:
            logger.warning('投票締め切りボタンがない')
            continue
        except TimeoutException:
            logger.warning('投票を占めきれなかった')
            continue
        else:
            logger.info('投票を締め切ろうとしている')
            break
    
    justwait.justWait(window, 1)
    try:
        logger.debug('投票締め切り確認')
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    else:
        logger.info('投票を締め切りました')
