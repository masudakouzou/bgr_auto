# coding: utf-8
import logging
from selenium.common.exceptions import NoSuchElementException
from bgrsrc import justwait


logger = logging.getLogger(__name__)


def delete(window):
    
    try:
        logger.debug('部屋消去開始')
        justwait.justWait(window, 3)
        window.find_element_by_css_selector('.btn-secondary').click()
    except NoSuchElementException:
        logger.warning('部屋消し失敗continue')
    else:
        logger.info('部屋消し準備ok')

    try:
        logger.debug('部屋消し確認します')
        justwait.justWait(window, 3)
        window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        logger.warning('部屋消し確認失敗、部屋消しは手動で行ってください')
    else:
        logger.info('部屋を削除しました')
