# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()


# Writer Last Name
last_name = basic.alphanum(_config.field_size('writer', 'last_name'))
last_name = last_name.setName('Writer Last Name').setResultsName('last_name')

# Writer First Name
first_name = basic.alphanum(_config.field_size('writer', 'first_name'))
first_name = first_name.setName('Writer First Name').setResultsName('first_name')

# Writer Unknown Indicator
unknown = basic.flag()
unknown = unknown.setName('Writer Unknown Indicator').setResultsName('writer_unknown')

# Reversionary Indicator
reversionary = basic.flag()
reversionary = reversionary.setName('Reversionary Indicator').setResultsName('reversionary')

# First Recording Refusal Indicator
refusal = basic.flag()
refusal = refusal.setName('First Recording Refusal Indicator').setResultsName('first_record_refusal')

# Work For Hire Indicator
for_hire = basic.flag()
for_hire = for_hire.setName('Work For Hire Indicator').setResultsName('work_for_hire')

# Personal Number
personal_number = basic.numeric(_config.field_size('writer', 'personal_number'))
personal_number = personal_number.setName('Personal Number').setResultsName('personal_number')