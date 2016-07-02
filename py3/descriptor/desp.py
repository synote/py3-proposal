#!/usr/bin/env python
# -*- coding: utf-8 -*-

'descriptor'

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

class API(object):
    """introspection descriptor
    """
    def _print_values(self, obj):

        def _print_value(key):
            if key.startswith('_'):
                return ''

            value = getattr(obj, key)
            if not hasattr(value, 'im_func'):
                doc = type(value).__name__
            else:
                if value.__doc__ is None:
                    doc = 'no docstring'
                else:
                    doc = value.__doc__

            return ' %s : %s' %(key, doc)

        res = [_print_value(item) for item in dir(obj) ]
        return '\n'.join([item for item in res
                      if item != ''])

    def __get__(self, obj, cls):
        if obj is not None:
            return self._print_values(obj)
        else:
            return self._print_values(cls)


class MyClass(object):
    """
    show descriptor
    """
    __doc__ = API()

    x = RevealAccess(10, 'var "x"')
    y = 5

    def __init__(self):
        self.a = 2

    def meth(self):
        """
        My method
        """
        return 0


