from utilities import hold_enter, click_word, word_sequence, tab_selection, match_words


def aStrangeNoise(driver):
    driver.get("https://www.duolingo.com/stories/pt-um-barulho-estranho")

    hold_enter(driver, 5.5)
    click_word(driver, "Yes")
    hold_enter(driver, 3.5)
    click_word(driver, "vai à janela")
    hold_enter(driver, 4)
    word_sequence(driver, ["E", "tenho", "um", "cachorro", "grande"])
    hold_enter(driver, 4.5)
    click_word(driver, "Vou")
    hold_enter(driver, 5)
    tab_selection(driver)
    hold_enter(driver, 9.5)
    click_word(driver, "dog")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
