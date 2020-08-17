from utilities import hold_enter, click_word, match_words


def inTheMuseum(driver):
    driver.get("https://www.duolingo.com/stories/pt-no-museu")

    hold_enter(driver, 4)
    click_word(driver, "avô")
    hold_enter(driver, 3)
    click_word(driver, "Yes")
    hold_enter(driver, 12)
    click_word(driver, "female")
    hold_enter(driver, 5)
    click_word(driver, "looks")
    hold_enter(driver, 2.5)
    click_word(driver, "beautiful")
    hold_enter(driver, 6)
    click_word(driver, "grandmother")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
