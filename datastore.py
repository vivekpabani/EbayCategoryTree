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

    def connect(self):
        if not (self.conn and self.cursor):
            try:
                self.conn = lite.connect(self.db)
                self.cursor = self.conn.cursor()
            except:
                print("Connection Error.")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
