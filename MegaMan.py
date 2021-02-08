from selenium import webdriver
from time import sleep

# Define the URL's we will open and a few other variables
main_url = 'https://giangvbng.herokuapp.com/'
tab_url = 'http://www.worldowe.com/stories'
chromedriver = 'C:\GiangNguyen\chromedriverz\chromedriver.exe'


while True:
    browser = webdriver.Chrome(chromedriver)

    # Open Portfolio
    print("opening Portfolio")
    browser.get(main_url)
    # Open a new Window
    browser.execute_script("window.open('');")

    # Switch to the new window and open Worldowe
    browser.switch_to_window(browser.window_handles[1])
    print("opening Worldowe")
    browser.get(tab_url)
    sleep(3600)
    # Close the tab with URL B
    browser.close()
    # Switch back to the first tab with URL A
    browser.switch_to.window(browser.window_handles[0])
    browser.close()
