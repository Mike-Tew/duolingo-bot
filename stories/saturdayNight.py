from utilities import hold_enter, click_word, match_words


def saturdayNight(driver):
    driver.get("https://www.duolingo.com/stories/pt-sabado-a-noite")

    hold_enter(driver, 7)
    click_word(driver, "Yes")
    hold_enter(driver, 5.5)
    click_word(driver, "Saturday")
    hold_enter(driver, 6.5)
    click_word(driver, "soccer")
    hold_enter(driver, 6.5)
    click_word(driver, "sábado à noite")
    hold_enter(driver, 3)
    click_word(driver, "player")
    hold_enter(driver, 7)
    click_word(driver, "great")
    hold_enter(driver, 0.1)
    match_words(driver)
    hold_enter(driver, 4)

