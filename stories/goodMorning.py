from utilities import hold_enter, click_word, match_words


def goodMorning(driver):
    driver.get("https://www.duolingo.com/stories/pt-bom-dia")

    hold_enter(driver, 4.5)
    click_word(driver, "true")
    hold_enter(driver, 3)
    click_word(driver, "Where")
    hold_enter(driver, 7)
    click_word(driver, "cansada")
    hold_enter(driver, 1.5)
    click_word(driver, "wants")
    hold_enter(driver, 4)
    click_word(driver, "puts")
    hold_enter(driver, 8)
    click_word(driver, "salt")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
