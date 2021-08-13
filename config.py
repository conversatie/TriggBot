#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pepkobot Copyright © 2018 Il'ya Marshal Semyonov
# License: https://www.gnu.org/licenses/gpl-3.0.en.html
import os


telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN', '1908335294:AAGJDtPL5SyTMQRQonybbB3MlFXyIgkAXbg')

DB = {
    'host': os.environ.get('DB_HOST'),
    'port': int(os.environ.get('DB_PORT'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'db': os.environ.get('DB_NAME'),
    'charset': 'utf8mb4'
}
