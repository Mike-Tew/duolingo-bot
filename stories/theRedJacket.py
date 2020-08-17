from utilities import hold_enter, click_word, word_sequence, match_words


def theRedJacket(driver):
    driver.get("https://www.duolingo.com/stories/pt-a-jaqueta-vermelha")

    hold_enter(driver, 11)
    click_word(driver, "No")
    hold_enter(driver, 2.5)
    word_sequence(driver, ["A", "jaqueta", "vermelha", "é", "fantástica"])
    hold_enter(driver, 2)
    click_word(driver, "Olha")
    hold_enter(driver, 5)
    click_word(driver, "hundred")
    hold_enter(driver, 7)
    click_word(driver, "His")
    hold_enter(driver, 6)
    click_word(driver, "cheap")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

