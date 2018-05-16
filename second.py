# -*- coding: utf-8 -*-

import pinyin


def initialStr(val):
    if isinstance(val,str):
        if val == None:
            return ''

    else:
        return "类型不对"
