from utilities import hold_enter, click_word, tab_selection, match_words


def aLittleBitOfMoney(driver):
    driver.get("https://www.duolingo.com/stories/pt-um-pouco-de-dinheiro")

    hold_enter(driver, 5)
    click_word(driver, "Yes")
    hold_enter(driver, 5)
    click_word(driver, "buy")
    hold_enter(driver, 4.5)
    click_word(driver, "right")
    hold_enter(driver, 5)
    tab_selection(driver)
    hold_enter(driver, 5.5)
    click_word(driver, "pedir uma pizza")
    hold_enter(driver, 6.5)
    click_word(driver, "theater")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

