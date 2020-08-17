from utilities import hold_enter, click_word, match_words


def theHoneymoon(driver):
    driver.get("https://www.duolingo.com/stories/pt-a-lua-de-mel")

    hold_enter(driver, 7.5)
    click_word(driver, "o aeroporto")
    hold_enter(driver, 2.5)
    click_word(driver, "Yes")
    hold_enter(driver, 6)
    click_word(driver, "honeymoon")
    hold_enter(driver, 5.5)
    click_word(driver, "want")
    hold_enter(driver, 5.5)
    click_word(driver, "love")
    hold_enter(driver, 4)
    click_word(driver, "already")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

