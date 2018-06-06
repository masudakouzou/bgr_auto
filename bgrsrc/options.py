# coding: utf-8

from bgrsrc import config
from bgrsrc import justwait


def setting(window):
    justwait.justWait(window, 5)
    # PW
    # window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[4]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[5]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[7]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[8]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[9]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[10]/div[3]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[12]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[13]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[14]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[15]/div[2]/label/input').click()
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[16]/div[3]/label/input').click()
    # 投票制限
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[17]/div[2]/label/input').click()
    justwait.justWait(window, 2)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[1]/input').send_keys(config.ROOM_NAME)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[2]/textarea').send_keys(config.ROOM_DESCRIPTION)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[3]/input').send_keys(config.REF_URL)
    # window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[4]/div[3]/input').send_keys(config.PASSWD)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[5]/div[3]/input').send_keys(config.PRIORITY_TIME)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[8]/div[3]/input').send_keys(config.ANSWER_TIME)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[9]/div[3]/input').send_keys(config.ANSWER_LIMIT)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[13]/div[3]/input').send_keys(config.VOTE_TIME_BASE)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[13]/div[4]/input').send_keys(config.VOTE_TIME_COEFFICIENT)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[14]/div[3]/input').send_keys(config.VOTE_LIMIT_PER_QUESTION)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[15]/div[3]/input').send_keys(config.VOTE_LIMIT_PER_ANSWER)
    justwait.justWait(window, 1)
    window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[3]/button[2]').click()
