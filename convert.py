#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import collections
import emoji_data_python
import logging

logger = logging.getLogger(__name__)


def create_list():

    sorted_short_names = collections.OrderedDict(
        sorted(emoji_data_python.emoji_short_names.items()))

    logger.debug("{} shortnames available".format(len(sorted_short_names)))

    first = True
    elm_list = "[ "
    for short_name, values in sorted_short_names.items():
        dict_values = values.__dict__
        logger.debug("{} {}".format(
            dict_values['short_name'],
            dict_values['unified']))

        if first:
            elm_list = \
                elm_list + '( "{}", [ "{}" ] )'.format(
                    dict_values['short_name'],
                    dict_values['unified'].lower())

            first = False
        else:
            elm_list = \
                elm_list + '\n, ( "{}", [ "{}" ] )'.format(
                    dict_values['short_name'],
                    dict_values['unified'].lower())

    elm_list = elm_list + "\n]"
    return elm_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a List ( String, List String ) to the Elm format'
                    ' with emoji data')

    parser.add_argument(
            "-v", "--verbose",
            help="Increase output verbosity",
            action="store_true")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    print(create_list())
