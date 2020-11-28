#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def appium_driver():
    appium_url = "http://127.0.0.1:4723/wd/hub"
    # Create a desired capabilities object as a starting point.
    capabilities = DesiredCapabilities.ANDROID.copy()
    capabilities['platform'] = "ANDROID"
    capabilities['deviceName'] = "and80"
    capabilities['version'] = "8.0.0"
    capabilities['automationName'] = "Appium"
    capabilities['appPackage'] = "org.wikipedia"
    capabilities['appActivity'] = ".main.MainActivity"
    capabilities['app'] = \
        "/Users/evgenynalivayko/Documents/git/auto_mobile_cours/" \
        "apks/org.wikipedia_50334_apps.evozi.com.apk"
    # Instantiate an instance of Remote WebDriver with the desired capabilities
    __driver = webdriver.Remote(desired_capabilities=capabilities,
                                command_executor=appium_url)
    yield __driver  # provide the fixture value
    __driver.quit()
