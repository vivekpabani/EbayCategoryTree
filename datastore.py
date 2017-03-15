#!/usr/bin/env python

import sqlite3 as lite

class DataStore:
    """
    Datastore is a class to create database for category data.
    It provides create database, create and drop tables and insert/retrieve data functions.
    """

    def __init__(self):

        self.db = "ebay.db"
        self.conn = None
        self.cursor = None
