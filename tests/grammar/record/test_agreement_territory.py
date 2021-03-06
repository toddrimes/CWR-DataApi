# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.record import agreement_territory


"""
CWR Territory in Agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseAgreementTerritory(unittest.TestCase):
    """
    Tests that the Territory in Agreement grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = agreement_territory.territory_in_agreement

    def test_valid(self):
        """
        Tests that Territory in Agreement grammar decodes correctly formatted record prefixes.
        """
        record = 'TER0000123400000023I0020'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('TER', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(20, result.tis_numeric_code)