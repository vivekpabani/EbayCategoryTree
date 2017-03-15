#!/usr/bin/env python

import subprocess
import xml.etree.ElementTree as ET


def fetch_categories_from_ebay():
    """
    Fetch category data from ebay using the shell script.
    """

    proc = subprocess.Popen(['./category.sh'], stdout=subprocess.PIPE)
    data, err = proc.communicate()

    return data
