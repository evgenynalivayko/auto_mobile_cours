#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MainClass:
    z = 14
    x = 45
    __class_number = 20
    __class_string = "Hello, world"

    def get_local_number(self):
        return self.z

    def get_class_number(self):
        return self.__class_number

    def get_class_string(self):
        return self.__class_string