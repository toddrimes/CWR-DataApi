# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Publisher Sequence #
publisher_sequence_n = basic.numeric(_config.field_size('publisher', 'sequence_n'), compulsory=True)
publisher_sequence_n = publisher_sequence_n.setName('Publisher Sequence #').setResultsName('publisher_sequence_n')

# Publisher name
name = basic.alphanum(_config.field_size('publisher', 'name'))
name = name.setName('Publisher name').setResultsName('name')

# Publisher Unknown Indicator
unknown = basic.flag()
unknown = unknown.setName('Publisher Unknown Indicator').setResultsName('publisher_unknown')

# Tax ID #
tax_id = basic.numeric(_config.field_size('publisher', 'tax_id'))
tax_id = tax_id.setName('Tax ID #').setResultsName('tax_id')

# Submitter Agreement Number
submitter_agreement_n = basic.alphanum(_config.field_size('publisher', 'submitter_agreement_id'))
submitter_agreement_n = submitter_agreement_n.setName('Submitter Agreement Number').setResultsName(
    'submitter_agreement_id')

# First Recording Refusal Indicator
# TODO: The writer record uses this same field
first_recording_refusal = basic.lookup(('Y', 'N'), columns=1)
first_recording_refusal = first_recording_refusal.setName('First Recording Refusal Indicator').setResultsName(
    'first_recording_refusal')

# International Standard Agreement Code
international_code = basic.alphanum(_config.field_size('publisher', 'international_code'))
international_code = international_code.setName('International Standard Agreement Code').setResultsName(
    'isac')

# Society-assigned Agreement Number
society_assigned_agreement_n = basic.alphanum(_config.field_size('publisher', 'society_agreement_id'))
society_assigned_agreement_n = society_assigned_agreement_n.setName('Society-assigned Agreement Number').setResultsName(
    'society_assigned_agreement_n')
