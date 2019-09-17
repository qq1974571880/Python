#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
driver = webdriver.Chrome();
# driver.get("C:\\Web\\Apache24\\htdocs\\document\\book\\货币战争①.txt")
driver.get(url="C:\\Web\\Apache24\\htdocs\\document\\book\\mysql.pdf")
time.sleep(3)
driver.quit()