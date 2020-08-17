from utilities import hold_enter, click_word, word_sequence, match_words


def whosSpeaking(driver):
    driver.get("https://www.duolingo.com/stories/pt-quem-fala")

    hold_enter(driver, 4.5)
    click_word(driver, "Yes")
    hold_enter(driver, 4)
    click_word(driver, "telefone do")
    hold_enter(driver, 6)
    word_sequence(driver, ["Eu", "preciso", "de", "um", "favor", "Luís"])
    hold_enter(driver, 10)
    click_word(driver, "police")
    hold_enter(driver, 3)
    click_word(driver, "boss")
    hold_enter(driver, 6)
    click_word(driver, "instead")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
