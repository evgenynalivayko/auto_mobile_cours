#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def wait_for_element_present(driver, locator, error_message, timeout_in_second=5):
    element = WebDriverWait(driver=driver, timeout=timeout_in_second)
    return element.until(expected_conditions.presence_of_element_located(locator), message=error_message)


def wait_for_element_and_click(driver, locator, error_message, timeout_in_second=5):
    element = wait_for_element_present(driver=driver, locator=locator, error_message=error_message, timeout_in_second=timeout_in_second)
    element.click()
    return element


def wait_for_element_and_send_keys(value, driver, locator, error_message, timeout_in_second=5):
    element = wait_for_element_present(driver=driver, locator=locator, error_message=error_message, timeout_in_second=timeout_in_second)
    element.send_keys(value)
    return element


def wait_for_element_not_present(driver, locator, error_message, timeout_in_second=5):
    element = WebDriverWait(driver=driver, timeout=timeout_in_second)
    element.until(expected_conditions.invisibility_of_element_located(locator), message=error_message)
    return element


def wait_for_element_and_clear(driver, locator, error_message, timeout_in_second=5):
    element = wait_for_element_present(driver=driver, locator=locator,
                                       error_message=error_message,
                                       timeout_in_second=timeout_in_second)
    element.clear()
    return element


def test_first(appium_driver):
    appium_driver.find_element_by_id("org.wikipedia:id/fragment_onboarding_skip_button").click()
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_send_keys(
        value="Java",
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_src_text']"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@text='Object-oriented programming language']"),
        error_message="Cannot find 'Object-oriented programming language' topic searching by 'Java'",
        timeout_in_second=15
    )


def test_cancel_search(appium_driver):
    appium_driver.find_element_by_id("org.wikipedia:id/fragment_onboarding_skip_button").click()
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.ID, "org.wikipedia:id/search_container"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_send_keys(
        value="Java",
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_src_text']"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_clear(
        driver=appium_driver,
        locator=(By.ID, "org.wikipedia:id/search_src_text"),
        error_message="Cannot find 'Search Wikipedia' input with text or never clear"
    )
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.CLASS_NAME, "android.widget.ImageButton"),
        error_message="Cannot find icon to cancel search"
    )
    wait_for_element_not_present(
        driver=appium_driver,
        locator=(By.CLASS_NAME, "android.widget.ImageButton"),
        error_message="Icon to cancel search is still present on the page"
    )


def test_compare_article_title(appium_driver):
    appium_driver.find_element_by_id("org.wikipedia:id/fragment_onboarding_skip_button").click()
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_send_keys(
        value="Java",
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_src_text']"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@text='Object-oriented programming language']"),
        error_message="Cannot find 'Java' article"
    )
    title_element = wait_for_element_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='pcs-edit-section-title-description']/preceding-sibling::*[1]"),
        error_message="Cannot find 'Search Wikipedia' input",
        timeout_in_second=20
    )
    assert title_element.text == "Java (programming language)", "We see unexpected title!"
