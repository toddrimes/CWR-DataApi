# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import work_detail


"""
CWR Entire Work Title grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestEntireWorkTitleGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.entire_title

    def test_valid_full(self):
        record = 'EWT0000123400000023THE TITLE                                                   T0123456789ESLAST NAME 1                                  FIRST NAME 1                  THE SOURCE                                                  00014107338I-000000229-7LAST NAME 2                                  FIRST NAME 2                  00014107339I-000000230-7ABCD0123456789'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('EWT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('THE TITLE', result.title)
        self.assertEqual(12345678, result.iswc.id_code)
        self.assertEqual(9, result.iswc.check_digit)
        self.assertEqual('ES', result.language_code)
        self.assertEqual('LAST NAME 1', result.writer_1_last_name)
        self.assertEqual('FIRST NAME 1', result.writer_1_first_name)
        self.assertEqual('THE SOURCE', result.source)
        self.assertEqual(14107338, result.writer_1_ipi_name)
        self.assertEqual('I', result.writer_1_ipi_base.header)
        self.assertEqual(229, result.writer_1_ipi_base.id_code)
        self.assertEqual(7, result.writer_1_ipi_base.check_digit)
        self.assertEqual('LAST NAME 2', result.writer_2_last_name)
        self.assertEqual('FIRST NAME 2', result.writer_2_first_name)
        self.assertEqual(14107339, result.writer_2_ipi_name)
        self.assertEqual('I', result.writer_2_ipi_base.header)
        self.assertEqual(230, result.writer_2_ipi_base.id_code)
        self.assertEqual(7, result.writer_2_ipi_base.check_digit)
        self.assertEqual('ABCD0123456789', result.submitter_work_n)
