#!/bin/env python
# coding: UTF-8

# log
#
# Copyright(c) 2015 Uptime Technologies, LLC.

import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger('PsqlWrapper')
logger.setLevel(logging.INFO)

INFO = logging.INFO
DEBUG = logging.DEBUG

def setLevel(level):
    logger.setLevel(level)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logger.info(msg, *args)
