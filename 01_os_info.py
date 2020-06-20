# -*- coding: utf-8 -*-

# Нужно собрать информацию о оперционной системе и версии пайтона

# TODO Запустить этот скрипт и закомитить результат его работы (файл os_info.txt)

import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt','w') as ff:
    ff.write(info)
