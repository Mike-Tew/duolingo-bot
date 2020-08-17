from utilities import hold_enter, click_word, word_sequence, match_words


def aDate(driver):
    driver.get("https://www.duolingo.com/stories/pt-um-encontro")

    hold_enter(driver, 4)
    click_word(driver, "em um encontro")
    hold_enter(driver, 8)
    click_word(driver, "also")
    hold_enter(driver, 1)
    click_word(driver, "great")
    hold_enter(driver, 5.5)
    word_sequence(driver, ["Meu", "nome", "é", "Júlia"])
    hold_enter(driver, 3)
    click_word(driver, "true")
    hold_enter(driver, 7)
    click_word(driver, "lied")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
