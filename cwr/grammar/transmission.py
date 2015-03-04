# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from data.accessor import CWRTables, CWRConfiguration
from cwr.grammar.field import table, special, record, basic
from cwr.transmission import TransmissionHeader, TransmissionTrailer


"""
CWR Transmission grammar.

This stores grammar for parsing the CWR Transmission Header and Transmission Trailer.

The Transmission Header contains the following fields:
- Record Type.
- Sender Type.
- Sender ID.
- Sender Name
- EDI Version.
- Creation Date.
- Creation Time.
- Transmission Date.
- Character Set.

The Transmission Trailer contains the following fields:
- Record Type.
- Group Count.
- Transaction Count.
- Record Count.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Transmission fields.

These fields are:
- Record Type. One for the header and another for the trailer, both a pre-defined string.
- Sender Type. Alphanumeric.
- Sender ID. Alphanumeric.
- Sender Name. Alphanumeric.
- EDI Version. Must be a predefined string.
- Creation Date. Date.
- Creation Time. Time.
- Transmission Date. Date.
- Character Set. Alphanumeric.
"""

# Sender ID
sender_id = basic.numeric(_config.field_size('transmission_header', 'sender_id'), compulsory=True)
sender_id = sender_id.setName('Sender ID').setResultsName('sender_id')

# Sender Name
sender_name = basic.alphanum(_config.field_size('transmission_header', 'sender_name'), compulsory=True)
sender_name = sender_name.setName('Sender Name').setResultsName('sender_name')

# EDI Version
edi_version = pp.Literal(_config.field_value('transmission_header', 'edi_version'))
edi_version = edi_version.setName('EDI Version').setResultsName('edi_version')

# Creation Date
creation_date = basic.date(compulsory=True)
creation_date = creation_date.setName('Creation Date').setResultsName('creation_date')

# Creation Time
creation_time = basic.time()
creation_time = creation_time.setName('Creation Time').setResultsName('creation_time')

# Transmission Date
transmission_date = basic.date(compulsory=True)
transmission_date = transmission_date.setName('Transmission Date').setResultsName('transmission_date')

# Character Set
character_set = table.char_code(_config.field_size('transmission_header', 'character_set'))
character_set = character_set.setName('Character Set').setResultsName('character_set')

"""
Transmission patterns.

These are the grammatical structures for the Transmission Header and Transmission Trailer.
"""

# Creation date and time pattern
creation_date_time = pp.Group(creation_date + creation_time)
creation_date_time = creation_date_time.setName('Creation Date and Time').setResultsName('creation_date_time')

# Transmission Header pattern
transmission_header = special.lineStart + record.record_type(_config.record_type('transmission_header')) + \
                      table.sender_type(True) + sender_id + sender_name + edi_version + \
                      creation_date_time + transmission_date + character_set + special.lineEnd

# Transmission Header pattern
transmission_trailer = special.lineStart + record.record_type(_config.record_type('transmission_trailer')) + \
                       record.group_count + record.transaction_count + \
                       record.record_count + special.lineEnd

transmission_trailer.leaveWhitespace()
"""
Parsing actions for the patterns.

The header will be parsed into a TransmissionHeader and the trailer into a TransmissionTrailer.
"""

transmission_header.setParseAction(lambda h: _to_transmissionheader(h))
transmission_trailer.setParseAction(lambda t: _to_transmissiontrailer(t))

creation_date_time.setParseAction(lambda d: _combine_date_time(d[0].creation_date, d[0].creation_time))


def _combine_date_time(date, time):
    """
    Combines the received date and time.

    :param date: date to combine
    :param time: time to combine
    :return: the date and time combined
    """
    return datetime.datetime.combine(date, time)


def _to_transmissionheader(parsed):
    """
    Transforms the final parsing result into a TransmissionHeader instance.

    :param parsed: result of parsing a Transmission Header
    :return: a TransmissionHeader created from the parsed record
    """
    return TransmissionHeader(parsed.record_type, parsed.sender_id, parsed.sender_name, parsed.sender_type,
                              parsed.creation_date_time,
                              parsed.transmission_date, parsed.edi_version, parsed.character_set)


def _to_transmissiontrailer(parsed):
    """
    Transforms the final parsing result into a TransmissionTrailer instance.

    :param parsed: result of parsing a Transmission Trailer
    :return: a TransmissionTrailer created from the parsed record
    """
    return TransmissionTrailer(parsed.record_type, parsed.group_count, parsed.transaction_count, parsed.record_count)