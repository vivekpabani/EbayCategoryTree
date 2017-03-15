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


def render(cid):
    """
    Fetch the data for given category id from datastore.
    If available, render an html script with the data tree.
    If unavailable, print an error message.
    """

    # connect to database
    datastore = DataStore()
    datastore.connect()

    # fetch record from database with given id
    record = datastore.retrieve_by_cid(cid)

    # check if table doesn't exist
    if record == -1:
        return

    # if record doesn't exist in table, return
    if not record:
        print("No category with ID: {}".format(cid))
        return

    # if exists, fetch all children

    records = fetch_all_children(datastore, record)

    # connection close
    datastore.disconnect()

    # create an html file with name as cid
    create_html_page(cid, records)


def fetch_all_children(datastore, records):
    """
    Fetch all children of given records recursively to form a tree
    """

    answer = list()

    # for each record in records, first insert it into answer.
    # then fetch its children using its id as parentid
    # if children found, extend answer by calling this function recursively on children

    for record in records:
        answer.append(record)
        parent_id = record[0]
        children = datastore.retrieve_by_parent_id(parent_id)
        if children:
            answer.append(fetch_all_children(datastore, children))

    return answer


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
