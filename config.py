#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pepkobot Copyright © 2018 Il'ya Marshal Semyonov
# License: https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import pymysql.cursors
telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN', '1908335294:AAGJDtPL5SyTMQRQonybbB3MlFXyIgkAXbg')

DB = pymysql.connect(host='localhost',
                             user='root',
                             port='',
                             password='')
