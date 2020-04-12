# coding: UTF-8
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.action_chains import ActionChains

# base_url = "https://soil-inventory.dc.affrc.go.jp/figure.html?lat=35.681841&lng=138.764019&zoom=12"
base_url = "https://soil-inventory.dc.affrc.go.jp/figure.html"


def main():
    lat = 35.016817
    lng = 134.993005
    url = f"{base_url}?lat={lat}&lng={lng}&zoom=12"

    # ヘッドレスモードの設定。
    # True => ブラウザを描写しない。
    # False => ブラウザを描写する。
    options = Options()
    options.set_headless(True)

    # Chromeを起動
    driver = webdriver.Firefox()
    driver.get(url=url)
    x, y = driver.find_element_by_class_name("leaflet-interactive").location.values()
    actions = ActionChains(driver)
    actions.move_by_offset(x, y)
    actions.click()
    actions.perform()

    soil_info = driver.find_element_by_class_name(name="leaflet-popup-content").text.split('\n')

    return soil_info