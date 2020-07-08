#!/usr/bin/env python3

# For parsing command lines
import argparse
import re

# For interacting with the Notion API, via https://github.com/jamalex/notion-py
from notion.client import NotionClient

# For serializing table to CSV
import csv
from renderer import BaseHTMLRenderer
import base64

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
except TypeError:
    print(args.url, "does not appear to be a valid Notion collection URL…")
    exit()


# Helper function for serializing a block to HTML and then base64
def block2b64HTML(block_id):
    block = client.get_block("d015d1d97c6142a29f80126eb8c81746")
    html = BaseHTMLRenderer(block).render()
    return base64.b64encode(str.encode(html))


# Access the collection view from the URL and construct our dictionary
collection_view = client.get_collection_view(args.url)
collection_dicts = [
    {
        'artifact_id': row.id,
        'artifact_title': row.title,
        'artifact_content': block2b64HTML(row.id.replace('-', '')),
        'activity_ids': ",".join([a.id for a in row.activity]),
        'activity_titles': ",".join([a.title for a in row.activity]),
        # Notion API doesn't mirror rollups, so we query the standards directly
        'standard_ids': ",".join([
                ",".join([
                    s.id for s in client.get_block(a.id).standards_engaged])
                for a in row.activity]),
        'standard_titles': ",".join([
                ",".join([
                    s.title for s in client.get_block(a.id).standards_engaged])
                for a in row.activity])
    }
    for row in collection_view.collection.get_rows()
]
