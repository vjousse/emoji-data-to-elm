#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import collections
import emoji_data_python
import logging

logger = logging.getLogger(__name__)


def create_list(
        emojione,
        google,
        apple,
        facebook,
        twitter,
        messenger):

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

        if (emojione and dict_values['has_img_emojione']) or \
                (google and dict_values['has_img_google']) or \
                (apple and dict_values['has_img_apple']) or \
                (facebook and dict_values['has_img_facebook']) or \
                (twitter and dict_values['has_img_twitter']) or \
                (messenger and dict_values['has_img_messenger']):

            if not first:
                elm_list = elm_list + '\n, '
            else:
                first = False

            elm_list = \
                elm_list + '( "{}", [ "{}" ] )'.format(
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

    parser.add_argument(
            "--emojione",
            help="Add emojione icons",
            action="store_true")

    parser.add_argument(
            "--google",
            help="Add google icons",
            action="store_true")

    parser.add_argument(
            "--apple",
            help="Add apple icons",
            action="store_true")

    parser.add_argument(
            "--facebook",
            help="Add facebook icons",
            action="store_true")

    parser.add_argument(
            "--twitter",
            help="Add twitter icons",
            action="store_true")

    parser.add_argument(
            "--messenger",
            help="Add messenger icons",
            action="store_true")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    print(create_list(
        args.emojione,
        args.google,
        args.apple,
        args.facebook,
        args.twitter,
        args.messenger
        ))
