# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.parsing.grammar import group

"""
CWR group grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGrammarGroupHeader(unittest.TestCase):
    """
    Tests that GroupHeaderDecoder decodes correctly formatted strings
    """

    def test_valid_full(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.100123456789  '

        result = group.group_header.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(123456789, result.batch_request_id)

    def test_valid_no_batch_request(self):
        """
        Tests that GroupHeaderDecoder decodes a Group Header with no batch id.

        This test contains all the optional fields.
        """
        record = 'GRHACK0123402.10000000000000  '

        result = group.group_header.parseString(record)[0]

        self.assertEqual('GRH', result.record_type)
        self.assertEqual('ACK', result.transaction_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual('02.10', result.version_number)
        self.assertEqual(0, result.batch_request_id)


class TestGrammarGroupTrailer(unittest.TestCase):
    """
    Tests that GroupTrailerDecoder decodes correctly formatted strings
    """

    def test_valid_full(self):
        """
        Tests that GroupHeaderDecoder decodes correctly formatted Group Header.

        This test contains all the optional fields.
        """
        record = 'GRT012340123456701234567             '

        result = group.group_trailer.parseString(record)[0]

        self.assertEqual('GRT', result.record_type)
        self.assertEqual(1234, result.group_id)
        self.assertEqual(1234567, result.transaction_count)
        self.assertEqual(1234567, result.record_count)


class TestGrammarGroupHeaderException(unittest.TestCase):
    """
    Tests that GroupHeaderDecoder throws exceptions with incorrectly formatted strings.
    """

    def test_invalid_wrong_group_id(self):
        """
        Tests that GroupHeaderDecoder throws an exception when the group ID is 0.
        """
        # TODO: Check the exception's info
        record = 'GRHACK0000002.100123456789  '

        self.assertRaises(ParseException, group.group_header.parseString, record)


class TestGrammarGroupTrailerException(unittest.TestCase):
    """
    Tests that GroupTrailerDecoder throws exceptions with incorrectly formatted strings.
    """

    def test_invalid_wrong_group_id(self):
        """
        Tests that GroupTrailerDecoder throws an exception when the group ID is 0.
        """
        record = 'GRHACK0000002.100123456789  '

        self.assertRaises(ParseException, group.group_trailer.parseString, record)