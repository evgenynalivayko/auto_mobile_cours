#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def wait_for_element_present(driver, locator, error_message, timeout_in_second=5):
    element = WebDriverWait(driver=driver, timeout=timeout_in_second)
    return element.until(expected_conditions.presence_of_element_located(locator), message=error_message)


def wait_for_elements_present(driver, locator, error_message, timeout_in_second=5):
    element = WebDriverWait(driver=driver, timeout=timeout_in_second)
    return element.until(expected_conditions.presence_of_all_elements_located(locator), message=error_message)


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


def assert_element_has_text(element_locator, expected_text, error_message):
    assert element_locator.text == expected_text, error_message


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


def test_text_in_search_input(appium_driver):
    appium_driver.find_element_by_id("org.wikipedia:id/fragment_onboarding_skip_button").click()
    element_locator = wait_for_element_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/voice_search_button']/preceding-sibling::*[1]"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    assert_element_has_text(element_locator, "Search Wikipedia", "Invalid text in search input!")


def test_list_search_results_and_clear_results(appium_driver):
    appium_driver.find_element_by_id(
        "org.wikipedia:id/fragment_onboarding_skip_button").click()
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_send_keys(
        value="QA",
        driver=appium_driver,
        locator=(
        By.XPATH, "//*[@resource-id='org.wikipedia:id/search_src_text']"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    list_search_results = wait_for_elements_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']/child::*"),
        error_message="Cannot find list elements result"
    )
    assert len(list_search_results) > 1, "Fewer than two results found"
    wait_for_element_and_clear(
        driver=appium_driver,
        locator=(By.ID, "org.wikipedia:id/search_src_text"),
        error_message="Cannot find 'Search Wikipedia' input with text or never clear"
    )
    wait_for_element_not_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']"),
        error_message="Search result is still present on the page"
    )


def test_relevant_search_result(appium_driver):
    appium_driver.find_element_by_id(
        "org.wikipedia:id/fragment_onboarding_skip_button").click()
    wait_for_element_and_click(
        driver=appium_driver,
        locator=(By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    wait_for_element_and_send_keys(
        value="JAVA",
        driver=appium_driver,
        locator=(
        By.XPATH, "//*[@resource-id='org.wikipedia:id/search_src_text']"),
        error_message="Cannot find 'Search Wikipedia' input"
    )
    list_search_results = wait_for_elements_present(
        driver=appium_driver,
        locator=(By.XPATH, "//*[@resource-id='org.wikipedia:id/page_list_item_title']"),
        error_message="Cannot find list elements result"
    )
    for element_result in list_search_results:
        assert "JAVA".lower() in element_result.text.lower()
