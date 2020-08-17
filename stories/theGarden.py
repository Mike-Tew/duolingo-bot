from utilities import hold_enter, click_word, word_sequence, match_words


def theGarden(driver):
    driver.get("https://www.duolingo.com/stories/pt-o-jardim")

    hold_enter(driver, 4)
    click_word(driver, "grandma")
    hold_enter(driver, 3)
    click_word(driver, "beautiful")
    hold_enter(driver, 2.5)
    click_word(driver, "respect")
    hold_enter(driver, 12)
    word_sequence(driver, ["Espera", "um", "minuto"])
    hold_enter(driver, 7)
    click_word(driver, "flores")
    hold_enter(driver, 6.5)
    click_word(driver, "flowers")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
