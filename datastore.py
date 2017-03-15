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

    def create_table(self):

        self.connect()

        self.cursor.execute('''CREATE TABLE categories
                               (cid integer, clevel integer, cname text, offer integer, parent_id integer)''')

        self.conn.commit()

    def insert_all(self, rows):

        self.connect()

        self.cursor.executemany("INSERT INTO categories VALUES (?, ?, ?, ?, ?)", rows)

        self.conn.commit()

    def retrieve_by_cid(self, cid):

        self.connect()

        exists = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='categories'")

        if not exists.fetchone():
            print("Table does not exist.")
            return -1

        rows = self.cursor.execute("SELECT * FROM categories WHERE cid = {}".format(cid))

        return rows.fetchall()

    def retrieve_by_parent_id(self, parent_id):

        self.connect()

        exists = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='categories'")

        if not exists.fetchone():
            print("Table does not exist.")
            return -1

        rows = self.cursor.execute("SELECT * FROM categories WHERE parent_id = {} and cid != {}".format(parent_id, parent_id))

        return rows.fetchall()
