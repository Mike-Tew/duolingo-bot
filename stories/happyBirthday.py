from utilities import hold_enter, click_word, tab_selection, match_words


def happyBirthday(driver):
    driver.get("https://www.duolingo.com/stories/pt-feliz-anivers%C3%A1rio")

    hold_enter(driver, 4)
    click_word(driver, "Não é meu")
    hold_enter(driver, 5)
    click_word(driver, "turn")
    hold_enter(driver, 4)
    click_word(driver, "presente")
    hold_enter(driver, 3)
    click_word(driver, "computer")
    hold_enter(driver, 6)
    tab_selection(driver)
    hold_enter(driver, 8)
    click_word(driver, "29")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
