#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.main_class import MainClass


class TestMainClass:
    def test_get_local_number(self):
        get_local_number_result = MainClass().get_local_number()
        assert get_local_number_result == MainClass.z, f'метод get_local_number вернул {get_local_number_result} вместо {MainClass.z}'

    def test_get_class_number(self):
        get_class_number_result = MainClass().get_class_number()
        assert get_class_number_result > MainClass.x, f'get_class_number_result вернул {get_class_number_result}, что меньше {MainClass.x}'

    def test_get_class_string(self):
        get_class_string_result = MainClass().get_class_string()
        has_substring = False
        sub_word = ["hello", "Hello"]
        for word in sub_word:
            if word in get_class_string_result:
                has_substring = True
                break
        assert has_substring, f'Строка "{get_class_string_result}" не содержит подстрок {sub_word}'
