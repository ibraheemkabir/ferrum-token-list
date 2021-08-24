#!/bin/python
import json

js = json.loads(open('./FerrumTokenList.json').read())
print('Valid JSON. Number of tokens:', len(js['tokens']))
