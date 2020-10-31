#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MainClass:
    __class_number = 20
    __class_string = "Hello, world"

    def get_local_number(self):
        return 14

    def get_class_number(self):
        return self.__class_number

    def get_class_string(self):
        return self.__class_string