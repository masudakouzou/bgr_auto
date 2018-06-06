from src.bgrsrc import phase
from src.bgrsrc import justwait
from src.bgrsrc import leave
from src.bgrsrc import createroom
from src.bgrsrc import options
from src.bgrsrc import enter
from src.bgrsrc import waitphase
from src.bgrsrc import deleteroom


def isExistCSSElement(window, css):
    try:
        window.find_element_by_css_selector(css)
    except:
        return False
    else:
        return True


def isExistClassElement(window, class_name):
    try:
        window.find_element_by_class_name(class_name)
    except:
        return False
    else:
        return True


# 部屋が止まってしまった場合の処理

def create__cannot_questioning(window):
    justwait.justWait(window, 2)
    if '結果フェーズ' == phase.getPhaseName(window):
        if isExistClassElement(window, '.modal'):
            window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/button/span').click()
        leave.leave(window)
        justwait.justWait(window, 3)
        deleteroom.delete(window)
        justwait.justWait(window, 3)
        createroom.create(window)
        justwait.justWait(window, 1)
        options.setting(window)
        justwait.justWait(window, 1)
        enter.enter(window)
        justwait.justWait(window, 1)
        waitphase.waiting(window)


# サーバー側の都合で投票モードに移行できなかった場合のメソッド
def create__cannot_voting(window):
    """
    こちらの場合、いつまで経っても回答フェーズであるため
    フェーズ名を監視します
    """
    justwait.justWait(window, 2)
    if '回答フェーズ' == phase.getPhaseName(window):
        leave.leave(window)
        justwait.justWait(window, 3)
        deleteroom.delete(window)
        justwait.justWait(window, 3)
        createroom.create(window)
        justwait.justWait(window, 1)
        options.setting(window)
        justwait.justWait(window, 1)
        enter.enter(window)
        justwait.justWait(window, 1)
        waitphase.waiting(window)
