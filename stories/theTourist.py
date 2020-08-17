from utilities import hold_enter, click_word, word_sequence, match_words


def theTourist(driver):
    driver.get("https://www.duolingo.com/stories/pt-o-turista")

    hold_enter(driver, 7)
    click_word(driver, "Yes")
    hold_enter(driver, 2)
    word_sequence(driver, ["De", "onde", "você", "é"])
    hold_enter(driver, 6.5)
    click_word(driver, "study")
    hold_enter(driver, 8)
    click_word(driver, "mais")
    hold_enter(driver, 2)
    click_word(driver, "friends")
    hold_enter(driver, 8)
    click_word(driver, "with")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

