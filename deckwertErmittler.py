from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import time


def deckwert_ermittlung(textfile_location):
    # Create the webdriver object
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': ''}  # enter your download directory here
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # get website link
    driver.get('https://deckstats.net')

    # open textfile and save as string
    with open(textfile_location, 'r') as file:
        decklist = file.read().replace('\t',' ')
    print(decklist)

    # read deck name
    deckname = re.search("[ \w-]+?(?=\.)", textfile_location).group()

    # Obtain buttons by class name and click all of them
    driver.find_element(By.NAME, 'user').send_keys('MagicNerdism')
    driver.find_element(By.NAME, 'passwrd').send_keys('MN4d616769634e65726469736d')
    driver.find_element(By.ID, 'user_login_segment').click()
    time.sleep(1) #schauen ob man auf richtige Webseite warten kann
    driver.find_element(By.LINK_TEXT,'Okay!').click()
    driver.find_element(By.XPATH, "(//i[@class='fa fa-plus'])[1]").click()
    driver.find_element(By.ID, 'deckbuilder_new_deck_dialog_name').send_keys(deckname)
    format_selecter = Select(driver.find_element(By.ID, 'deckbuilder_new_deck_dialog_format'))
    format_selecter.select_by_value('3')
    driver.find_element(By.ID, 'deckbuilder_new_deck_dialog_is_public').click()
    driver.find_element(By.XPATH, "(//span[text()='OK'])[1]").click()
    time.sleep(1) #schauen ob man auf richtige Webseite warten kann
    driver.find_element(By.XPATH, "//span[text()[normalize-space()='Paste/upload list']]").click()
    time.sleep(1) #schauen ob man auf richtige Webseite warten kann
    driver.find_element(By.ID, 'deckbuilder_upload_list_dialog_textarea').send_keys(decklist)
    time.sleep(1)
    driver.find_element(By.XPATH, "(//span[text()='OK'])[5]").click()
    driver.find_element(By.XPATH, "//span[text()[normalize-space()='Speichern']]").click()
    driver.find_element(By.XPATH, "(//span[text()='OK'])[2]").click()
    driver.find_element(By.ID, 'ui-id-14').click()
    mainboardPrice = driver.find_element(By.XPATH, "(//td[@title='Total price on Cardmarket for the card versions listed'])[1]").getText()
    sideboardPrice = driver.find_element(By.XPATH, "(//td[@title='Total price on Cardmarket for the card versions listed'])[2]").getText()
    driver.quit()
    return mainboardPrice, sideboardPrice


print(deckwert_ermittlung('C:/Users/Fabian/Desktop/SampleDeckliste.txt'))
