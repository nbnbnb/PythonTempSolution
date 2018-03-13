#!/usr/bin/python
print('-------------- start-------------')
print()

import gettext

t = gettext.translation('example', './locale', fallback=True)
_ = t.gettext
print(_('This message is in the script.'))

with open('abc.txt') as f:
    print(f.read())


if __name__ == '__main__':
    print()
    print('--------------- end -------------')
