# coding: utf-8
import logging
from selenium.common.exceptions import NoSuchElementException

from bgrsrc import justwait


logger = logging.getLogger(__name__)


def create(window):
    while True:
        try:
            logger.debug('部屋を建てようとした')
            justwait.justWait(window, 3)
            window.find_element_by_xpath('/html/body/div/div[2]/p/button').click()
        except NoSuchElementException:
            logger.warning('部屋建てに失敗したのでもう一度')
            continue
        else:
            logger.info('部屋を立てるボタンを押した')
            break
