#!/usr/bin/env python3.5
#coding=UTF-8

import requests
import time
import json

expired = 110
token = 'xoxp-9212542417-9212304530-50314118053-38e86be512'


ts_to = int(time.time()) - expired * 24 * 60 * 60

def files_list():
	params = {
		'token': token,
		'ts_to': ts_to,
		'count': 1000
		}
	uri = 'https://slack.com/api/files.list'
	response = requests.get(uri, params=params)
	return json.loads(response.text)['files']

def files_del(ids):
	count = 0
	num_files = len(ids)
	for file_id in ids:
		count = count + 1
		params = {
			'token': token,
			'file': file_id
			}
		uri = 'https://slack.com/api/files.delete'
		response = requests.get(uri, params=params)
		print (count, "of", num_files, "-", file_id, json.loads(response.text)['ok'])

files = files_list()
ids = [f['id'] for f in files]
files_del(ids)