#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.main_class import MainClass


class TestMainClass:
    def test_get_local_number(self):
        get_local_number_result = MainClass().get_local_number()
        assert get_local_number_result == 14, f'метод get_local_number вернул {get_local_number_result} вместо 14'

    def test_get_class_number(self):
        get_class_number_result = MainClass().get_class_number()
        assert get_class_number_result > 45, f'get_class_number_result вернул {get_class_number_result}, что меньше 45'

    def test_get_class_string(self):
        get_class_string_result = MainClass().get_class_string()
        n = 0
        sub_word = ["hello", "Hello"]
        for word in sub_word:
            if word in get_class_string_result:
                n = n + 1
        assert n > 0, f'Строка "{get_class_string_result}" не содержит подстрок {sub_word}'
