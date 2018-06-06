# coding: utf-8
from src.bgrsrc import justwait
from selenium.common.exceptions import NoSuchElementException


# 未登録リスト = []
# 登録済みリスト = []


def permission(window):
    def __find_css_selector(selector):
        try:
            window.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        else:
            return True

    def __wrapper_find_css_element(selector):
        try:
            ele = window.find_element_by_css_selector(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele

    def __wrapper_find_css_elements(selector):
        try:
            ele_list = window.find_elements_by_css_selector(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele_list

    def __wrapper_find_tag_element(selector):
        try:
            ele = window.find_element_by_tag_name(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele

    # メンバーリストを見る
    try:
        justwait.justWait(window, 2)
        window.find_element_by_xpath('/html/body/div/div/button').click()
    except NoSuchElementException:
        pass
    else:
        justwait.justWait(window, 1)

    # メンバーリストを操作する
    try:
        # ここですべての許可ボタンを得る
        allow_buttons = window.find_elements_by_css_selector('body > div > div.modal > div > div > div.modal-body > div > div > div > div.card-footer > div > button:nth-child(3)')
    except:
        pass
    else:
        for allow in allow_buttons:
            # 取り合えず全員追加
            if '追加' in allow.text:
                justwait.justWait(window, 1)
                allow.click()
        # 以下は失敗した記述
        # for handler in controller:
        #     if __find_css_selector('.btn.btn-secondary.btn-sm'):
        #         登録済みリスト.append(__wrapper_find_tag_element('p').text)
        #     else:
        #         未登録リスト.append(__wrapper_find_tag_element('p').text)
        # reg_set = set(登録済みリスト)
        # unr_set = set(未登録リスト)

        # # 未登録者と登録者が被っていない場合は全部許可
        # if reg_set.isdisjoint(unr_set):
        #     cards = __wrapper_find_css_elements('.card')
        #     for card in cards:
        #         if __wrapper_find_css_element('button:nth-child(3)').text == '投票者へ追加する':
        #             __wrapper_find_css_element('button:nth-child(3)').click()
        #             justwait.justWait(window, 1)
        # # 被っている場合荒らしの可能性があるためかぶりを特定してそれ以外許可
        # else:
        #     new_set = (reg_set | unr_set) - reg_set
        #     cards = __wrapper_find_css_elements('.card')
        #     for card in cards:
        #         # 未登録者
        #         if __wrapper_find_css_element('button:nth-child(3)').text == '投票者へ追加する':
        #             # new_setに存在している名前だけ許可していく
        #             if __wrapper_find_tag_element('p').text in new_set:
        #                 __wrapper_find_css_element('button:nth-child(3)').click()
        #                 new_set.remove(__wrapper_find_tag_element('p').text)
        #                 justwait.justWait(window, 1)
        justwait.justWait(window, 1)

    # メンバーリストを閉じる
    try:
        window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/button/span').click()
    except NoSuchElementException:
        pass
    else:
        justwait.justWait(window, 1)
