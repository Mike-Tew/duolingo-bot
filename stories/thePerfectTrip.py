from utilities import hold_enter, click_word, match_words


def thePerfectTrip(driver):
    driver.get("https://www.duolingo.com/stories/pt-a-viagem-perfeita")

    hold_enter(driver, 7)
    click_word(driver, "national")
    hold_enter(driver, 4.5)
    click_word(driver, "No")
    hold_enter(driver, 2.5)
    click_word(driver, "fazer")
    hold_enter(driver, 8.5)
    click_word(driver, "tomorrow")
    hold_enter(driver, 5)
    click_word(driver, "Boa ideia")
    hold_enter(driver, 11)
    click_word(driver, "evening")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
