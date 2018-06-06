# coding: utf-8
import logging

from selenium import webdriver

from bgrsrc import answerphase
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


logging.basicConfig(filename='test.log', format='%(levelname)s:%(message)s')
logging.getLogger("src").setLevel(level=logging.DEBUG)


def init():
    driver = webdriver.Firefox()
    driver.get('https://bigiri.oogiri.org/')
    # driver.maximize_window()

    justwait.justWait(driver, 5)

    createroom.create(driver)
    signin.signin(driver)
    options.setting(driver)

    enter.enter(driver)
    waitphase.waiting(driver)
    while True:
        answerphase.answer(driver)
        if leaveflag.flag(driver):
            csvfiledownload.csvDL(driver)
            break
        if '回答フェーズ' == phase.getPhaseName(driver):
            newroomcreate.create__cannot_voting(driver)
        votephase.vote(driver)
        resultphase.result(driver)
        newroomcreate.create__cannot_questioning(driver)
    leave.leave(driver)
    deleteroom.delete(driver)

    driver.close()
