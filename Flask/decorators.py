# -*- coding: utf-8 -*-

def do_twice(func):
    def wrapper_do_twice():
        print('before')
        func()
        func()
        print('after')
    return wrapper_do_twice