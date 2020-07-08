#!/usr/bin/env python3

# For parsing command lines
import argparse
import re

# For interacting with the Notion API, via https://github.com/jamalex/notion-py
from notion.client import NotionClient

# Parse command line arguments to extract API token and URL
parser = argparse.ArgumentParser(
    description='Generate a CSV file from a Notion table')
parser.add_argument('token_v2', metavar='toven_v2', type=str,
                    help='API token_v2, via logged-in notion.so cookies')
parser.add_argument('url', metavar='URL', type=str,
                    help='URL of the table to convert')
args = parser.parse_args()

# Initialize client with `token_v2`
client = NotionClient(token_v2=args.token_v2)

# Access a database using the URL of the database page
try:
    url_regex = re.compile('https?\:\/\/www.notion.so/.+?/(.+?)(\?|\n)')
    collection_id = url_regex.match(args.url)[1]
    print(collection_id)
except TypeError:
    print(args.url, "does not appear to be a valid Notion collection URL…")
    exit()

collection_view = client.get_collection_view(args.url)

print(collection_view.collection.get_rows())
