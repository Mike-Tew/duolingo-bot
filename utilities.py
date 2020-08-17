import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def use_chrome():
    # Set Chrome webdriver options and profile
    options = Options()
    options.add_argument(
        "user-data-dir=C:\\Users\\Michael\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    return webdriver.Chrome(r"C:\chromedriver.exe", options=options)


def hold_enter(driver, seconds):
    # Simulate holding down the enter key
    start = time.time()
    while time.time() < start + seconds:
        driver.find_element_by_tag_name("body").send_keys(Keys.ENTER)
        time.sleep(0.1)


def click_word(driver, word):
    # Click on the word of the provided text
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{word}')]").click()
    except:
        pass


def word_sequence(driver, word_list):
    # Click on a list of words in sequence
    try:
        choices = driver.find_element_by_class_name("_2-hAU")
        for word in word_list:
            choices.find_element_by_xpath(f".//*[contains(text(), '{word}')]").click()
    except:
        pass


def tab_selection(driver):
    # Tab and click through selection
    actions = ActionChains(driver)
    for _ in range(3):
        try:
            actions = actions.send_keys(Keys.TAB)
            actions = actions.send_keys(Keys.SPACE)
        except:
            pass
    actions.perform()


def try_all_span(driver, num):
    # Click on all words with a span tag
    try:
        input_choices = driver.find_element_by_class_name("_2-hAU")
        for _ in range(num):
            for choice in input_choices.find_elements_by_tag_name("span"):
                choice.click()
    except:
        pass


def match_words(driver):
    words = ["words"]
    while len(words) > 0:
        words = driver.find_elements_by_css_selector("button._1bXp6:not(._1CGKV)")
        for _ in range(0, len(words) - 1):
            words[0].click()
            words[_ + 1].click()


def validate_num(num):
    try:
        num = int(num)
        if num > 0:
            return num
        return 0

    except:
        return 0
