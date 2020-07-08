#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Generate a CSV file from a Notion table')
parser.add_argument('token_v2', metavar='toven_v2', type=str,
                   help='API token_v2, pulled from inspecting cookies in a logged-in Notion.so session')
parser.add_argument('url', metavar='URL', type=str,
                   help='URL of the table to convert')

args = parser.parse_args()
print(args)