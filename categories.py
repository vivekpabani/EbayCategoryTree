#!/usr/bin/env python3

import sys
import getopt
from datastore import DataStore
from create_html import create_html_page
from ebay_fetch import fetch_categories_from_ebay, extract_category_data


def rebuild():
    """
    Build the datastore/database by fetching the category data from ebay
    """

    # fetch data and extract from xml
    category_data_xml = fetch_categories_from_ebay()
    category_data = extract_category_data(category_data_xml)

    # connect to database
    datastore = DataStore()
    datastore.connect()

    # create a new table. drop first if exists
    datastore.drop_table()
    datastore.create_table()

    # insert data into datastore
    datastore.insert_all(category_data)

    # close connection
    datastore.disconnect()


def main():
    """
    Get argumentsm and call rebuild or render accordingly.
    """

    arguments = sys.argv[1:]

    if not arguments:
        print("Please run with correct arguments.")
        sys.exit(1)

    try:
        opts, args = getopt.getopt(arguments,"",["rebuild", "render="])
    except getopt.GetoptError:
        print("Please run with correct arguments.")
        sys.exit(1)

    for opt, arg in opts:
        if opt == '--rebuild':
            rebuild()
        elif opt == "--render":
            try:
                cid = int(arg)
            except:
                print("Invalid ID")
                return
            render(cid)


if __name__ == "__main__":

    main()
