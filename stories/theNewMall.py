from utilities import hold_enter, click_word, match_words


def theNewMall(driver):
    driver.get("https://www.duolingo.com/stories/pt-o-novo-shopping")

    hold_enter(driver, 6)
    click_word(driver, "No")
    hold_enter(driver, 14)
    click_word(driver, "quero ver")
    hold_enter(driver, 4)
    click_word(driver, "same")
    hold_enter(driver, 2)
    click_word(driver, "name")
    hold_enter(driver, 5.5)
    click_word(driver, "movies")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
