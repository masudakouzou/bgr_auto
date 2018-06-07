# coding: utf-8
# standard library
import logging

# third-party library
from selenium import webdriver

# local library
from bgrsrc import answerphase
from bgrsrc import config
from bgrsrc import createroom
from bgrsrc import csvfiledownload
from bgrsrc import deleteroom
from bgrsrc import enter
from bgrsrc import justwait
from bgrsrc import leave
from bgrsrc import leaveflag
from bgrsrc import options
from bgrsrc import resultphase
from bgrsrc import signin
from bgrsrc import votephase
from bgrsrc import waitphase
from bgrsrc import newroomcreate
from bgrsrc import phase


logger = logging.getLogger(__name__)

def init():
    driver = webdriver.Firefox()
    logger.info("connect bigiri-ch")
    driver.get(config.BIGIRI_URL)
    # driver.maximize_window()

    justwait.justWait(driver, 5)

    logger.info("create room")
    createroom.create(driver)
    signin.signin(driver)
    options.setting(driver)

    logger.info("enter room")
    enter.enter(driver)
    logger.info("waiting...")
    waitphase.waiting(driver)
    while True:
        logger.info("answer phase")
        answerphase.answer(driver)
        if leaveflag.flag(driver):
            logger.info("post process")
            csvfiledownload.csvDL(driver)
            break
        if '回答フェーズ' == phase.getPhaseName(driver):
            logger.info("recreate room")
            newroomcreate.create__cannot_voting(driver)
        logger.info("vote phase")
        votephase.vote(driver)
        logger.info("result phase")
        resultphase.result(driver)
        newroomcreate.create__cannot_questioning(driver)
    logger.info("leave room")
    leave.leave(driver)
    logger.info("delete room")
    deleteroom.delete(driver)

    driver.close()
