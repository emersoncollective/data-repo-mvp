#!/usr/bin/env python3

import hashlib
import re
import pandas as pd


def are_files_identical(filename1, filename2):

    # Use hashlib to store the hash of a file
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(filename1, "rb") as file:

        # Use file.read() to read the size of file
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h1.update(chunk)

    with open(filename2, "rb") as file:

        # Use file.read() to read the size of file a
        # and read the file in small chunks
        # because we cannot read the large files.
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h2.update(chunk)

        # hexdigest() is of 160 bits
        if h1.hexdigest() == h2.hexdigest():
            return True
        else:
            return False


def get_date_from_filename(file):
    date_re = r"(january|february|march|april|may|june|july|august|september|october|november|december)_(\d{1,2})_(\d{4})"
    re_find = re.findall(date_re, file)
    if re_find:
        return pd.to_datetime("_".join(re_find[0]), format="%B_%d_%Y")
    return None
