# README

This is a small Python 3 script and convenience wrapper around some of the functionality in [`notion-py`](https://github.com/jamalex/notion-py).  Its intent is to serialize Notion tables to CSV files.

## Installation
```bash
pip3 install -r requirements.text
```

## Usage

You'll need an API token from Notion.  As of July 2020, Notion's API is not public.  You can grab a _de facto_ token from the cookies loaded in your browser in a logged-in session on `notion.so`.

If you're not sure how to inspect Cookie values, you can use an extension like [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) on Chrome as so:

![Animated GIF of using EditThisCookie to get Notion API token](cookie-grab.gif?raw=true)

Usage syntax is available _via_ `notion2csv.py -h`:
usage: notion2csv.py [-h] TOKEN_V2 URL PATH

```text
Generate a CSV file from a Notion table

positional arguments:
  TOKEN_V2    API token_v2, via logged-in notion.so cookies
  URL         URL of the table to convert
  PATH        Output path for CSV

optional arguments:
  -h, --help  show this help message and exit
```

Currently, this is used as part of the PBLL project to serialize project story artifacts ↔ standard mappings to a CSV file suitable and reflects the structure of that as reflected in [this mock table](https://www.notion.so/powderhousepbll/7f9e7bb5fafe4df2bcd3bbcf2baf7348?v=07e6604a555543d6adffcf48257988ab), _i.e_.

![Project story summary and schema screenshot](story-summary.png?raw=true)

---
…producing CSVs like [this one](https://share.getcloudapp.com/OAuBNBG9)