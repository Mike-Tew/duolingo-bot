from utilities import hold_enter, click_word, match_words


def theTest(driver):
    driver.get("https://www.duolingo.com/stories/pt-o-teste")

    hold_enter(driver, 7)
    click_word(driver, "Yes")
    hold_enter(driver, 2.5)
    click_word(driver, "think")
    hold_enter(driver, 5)
    click_word(driver, "nunca")
    hold_enter(driver, 5)
    click_word(driver, "two")
    hold_enter(driver, 6)
    click_word(driver, "Tomorrow")
    hold_enter(driver, 9)
    click_word(driver, "help")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

