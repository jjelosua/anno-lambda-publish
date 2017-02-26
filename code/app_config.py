#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import logging

# env vars
SRC_BUCKET = os.environ.get('SRC_BUCKET')
DST_BUCKET = os.environ.get('DST_BUCKET')

# Global vars
DEFAULT_MAX_AGE = 20

LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'
LOG_LEVEL = logging.INFO

PREVIEW_FACTCHECK = os.environ.get('PREVIEW_FACTCHECK')
CURRENT_FACTCHECK = os.environ.get('CURRENT_FACTCHECK')
FACTCHECKS_DIRECTORY_PREFIX = 'factchecks/'
DEPLOYMENT_TARGET = 'production'
AUTOINIT_LOADER = False
