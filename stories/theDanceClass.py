from utilities import hold_enter, click_word, tab_selection, try_all_span, match_words


def theDanceClass(driver):
    driver.get("https://www.duolingo.com/stories/pt-a-aula-de-danca")

    hold_enter(driver, 7)
    click_word(driver, "No")
    hold_enter(driver, 3)
    tab_selection(driver)
    hold_enter(driver, 5)
    click_word(driver, "difficult")
    hold_enter(driver, 3)
    tab_selection(driver)
    hold_enter(driver, 7)
    try_all_span(driver, 5)
    hold_enter(driver, 6)
    click_word(driver, "accidentally")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)
