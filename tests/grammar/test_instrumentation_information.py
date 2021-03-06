# -*- coding: utf-8 -*-
import unittest

from cwr.grammar import work_detail

"""
CWR Instrumentation Information grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentationInformationValid(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.instrumentation_information

    def test_valid_full(self):
        summary = 'INS0000123400000023012BBADESCRIPTION                                       '
        detail_1 = 'IND0000123400000023ALT123'
        detail_2 = 'IND0000123400000023ALT123'

        record = summary + '\n' + detail_1 + '\n' + detail_2

        result = self.grammar.parseString(record)

        self.assertEqual(3, len(result))

        self.assertEqual('INS', result[0].record_type)
        self.assertEqual('IND', result[1].record_type)
        self.assertEqual('IND', result[2].record_type)