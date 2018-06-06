# coding: utf-8
import logging

from selenium.common.exceptions import NoSuchElementException
from src.bgrsrc import justwait
from src.bgrsrc import config


logger = logging.getLogger(__name__)


def signin(window):
    try:
        logger.debug('サインインしようとした')
        justwait.justWait(window, 1)
        window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/input').send_keys(config.MY_NAME)
    except NoSuchElementException:
        logger.warning('サインインに失敗した')
    try:
        logger.debug('サインイン確認しようとした')
        justwait.justWait(window, 1)
        window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        logger.warning('サインイン確認に失敗した')
