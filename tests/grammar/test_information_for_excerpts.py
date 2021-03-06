# -*- coding: utf-8 -*-
import unittest

from cwr.grammar import work_detail

"""
CWR Information for Versions grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInformationForExcerptsValid(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.information_for_excerpts

    def test_valid_full(self):
        title = 'EWT0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'
        nra = 'NCT0000123400000023THE TITLE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ES'
        now_1 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'
        now_2 = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        record = title + '\n' + nra + '\n' + now_1 + '\n' + now_2

        result = self.grammar.parseString(record)

        self.assertEqual(4, len(result))

        self.assertEqual('EWT', result[0].record_type)
        self.assertEqual('NCT', result[1].record_type)
        self.assertEqual('NOW', result[2].record_type)
        self.assertEqual('NOW', result[3].record_type)

    def test_valid_min(self):
        title = 'EWT0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        record = title

        result = self.grammar.parseString(record)

        self.assertEqual(1, len(result))

        self.assertEqual('EWT', result[0].record_type)
