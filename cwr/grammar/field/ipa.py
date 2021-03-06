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

# Interested Party Last Name
ip_last_name = basic.alphanum(_config.field_size('ipa', 'ip_last_name'), compulsory=True)
ip_last_name = ip_last_name.setName('Interested Party Last Name').setResultsName('ip_last_name')

# Interested Party Writer First Name
ip_writer_first_name = basic.alphanum(_config.field_size('ipa', 'ip_name'))
ip_writer_first_name = ip_writer_first_name.setName('Interested Party Writer First Name').setResultsName(
    'ip_writer_first_name')
