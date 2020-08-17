from utilities import hold_enter, click_word, tab_selection, match_words


def suprise(driver):
    driver.get("https://www.duolingo.com/stories/pt-surpresa")

    hold_enter(driver, 7.5)
    click_word(driver, "No")
    hold_enter(driver, 4)
    click_word(driver, "friend")
    hold_enter(driver, 4.5)
    click_word(driver, "também")
    hold_enter(driver, 9)
    click_word(driver, "perfect")
    hold_enter(driver, 3.5)
    click_word(driver, "love")
    hold_enter(driver, 8)
    tab_selection(driver)
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
