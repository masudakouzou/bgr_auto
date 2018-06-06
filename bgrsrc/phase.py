# coding: utf-8
import logging

from selenium.common.exceptions import NoSuchElementException


logger = logging.getLogger(__name__)


def getPhaseName(window):
    try:
        pn = window.find_element_by_xpath('/html/body/div/div/div[4]/div/div[1]/span')
    except NoSuchElementException:
        logger.info("Phase Name is Nothing")
        return None
    else:
        logger.debug("Phase Name")
        return pn.text
