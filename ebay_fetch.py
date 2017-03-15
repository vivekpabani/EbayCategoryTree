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


def extract_category_data(xml):
    """
    Extract xml data to get the category data as list.
    """

    category_data = list()
    root = ET.fromstring(xml)
    category_array = root.find('{urn:ebay:apis:eBLBaseComponents}CategoryArray')

    for category in category_array.findall('{urn:ebay:apis:eBLBaseComponents}Category'):
        cid = int(category.find('{urn:ebay:apis:eBLBaseComponents}CategoryID').text)
        clevel = int(category.find('{urn:ebay:apis:eBLBaseComponents}CategoryLevel').text)
        cname = category.find('{urn:ebay:apis:eBLBaseComponents}CategoryName').text
        cname.encode("utf8")
        offer = category.find('{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled')
        if offer:
            print(offer)
        if offer and offer == 'true':
            offer = 1
        else:
            offer = 0
        parent_id = int(category.find('{urn:ebay:apis:eBLBaseComponents}CategoryParentID').text)
        category_data.append([cid, clevel, cname, offer, parent_id])

    return category_data
