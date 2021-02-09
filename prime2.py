#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {1: 'One', 2: 'Two', 3: 'Three'}

    new_school = {}
    for key, value in school.items():
        new_school[value] = key
    print(new_school)
