from utilities import hold_enter, click_word, word_sequence, match_words


def doYouNeedHelp(driver):
    driver.get("https://www.duolingo.com/stories/pt-voce-precisa-de-ajuda")

    hold_enter(driver, 5.5)
    click_word(driver, "Yes")
    hold_enter(driver, 5.5)
    word_sequence(driver, ["Você", "tem", "um", "telefone"])
    hold_enter(driver, 7)
    click_word(driver, "repair")
    hold_enter(driver, 4.5)
    click_word(driver, "eu não sei")
    hold_enter(driver, 2.5)
    click_word(driver, "where")
    hold_enter(driver, 5.5)
    click_word(driver, "works")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
