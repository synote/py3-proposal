#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class First(object):

    def __init__(self):
        print('--call First __init__')
        self.name = 'first'


class Second(First):

    def __init__(self):
        self.age = 10


class Person(First):

    def __init__(self):
        super(Person, self).__init__()
        self.age = 10


class People(First):
    pass


if __name__ == '__main__':
    print('crate first')
    f = First()
    print('crate second')
    s = Second()
    print('crate person')
    p = Person()
    print('create people')
    people = People()

    # print f.name : first
    print('first name: %s' % f.name)
    print('first attr dict=%s' % f.__dict__)

    try:
        print('second name:%s' % s.name)
    except Exception as e:
        print('second.name attr')
        print('second attr dict=%s' % s.__dict__)

    # print person.name : first, person.age: 10
    print('person name=%s, age=%s' % (p.name, p.age))
    print('person attr dict=%s' % p.__dict__)

    # print people, implicit inherit
    print('people attr dict=%s' % people.__dict__)
