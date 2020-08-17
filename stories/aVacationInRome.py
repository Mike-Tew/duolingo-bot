from utilities import hold_enter, click_word, word_sequence, tab_selection, match_words


def aVacationInRome(driver):
    driver.get("https://www.duolingo.com/stories/pt-ferias-em-roma")

    hold_enter(driver, 8.5)
    click_word(driver, "Yes")
    hold_enter(driver, 7.5)
    word_sequence(driver, ["Quero", "comer", "pizza", "todo", "dia"])
    hold_enter(driver, 9)
    click_word(driver, "possible")
    hold_enter(driver, 6)
    tab_selection(driver)
    hold_enter(driver, 2)
    click_word(driver, "sure")
    hold_enter(driver, 2.5)
    click_word(driver, "live")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
