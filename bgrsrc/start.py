# coding: utf-8
import logging

from selenium import webdriver

from src.bgrsrc import answerphase
from src.bgrsrc import createroom
from src.bgrsrc import csvfiledownload
from src.bgrsrc import deleteroom
from src.bgrsrc import enter
from src.bgrsrc import justwait
from src.bgrsrc import leave
from src.bgrsrc import leaveflag
from src.bgrsrc import options
from src.bgrsrc import resultphase
from src.bgrsrc import signin
from src.bgrsrc import votephase
from src.bgrsrc import waitphase
from src.bgrsrc import newroomcreate
from src.bgrsrc import phase


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
