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
