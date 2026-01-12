#!/usr/bin/env python3

import argparse
import os
import sqlite3

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='filename', 
                        type=str, default='test.db',
                        help='Sqlite3 database file name')
    parser.add_argument('-c', '--clearTables', dest='clearTables',
                        default=False, action='store_true',
                        help='Drop tables before creating')
    return parser.parse_args()

def openDb(fname):
    conn = None
    if os.path.exists(fname):
        print(f'Use existing file {fname} as the database')
        conn = sqlite3.connect(args.filename)
    else:
        print(f'Creating file {fname}')
        conn = sqlite3.connect(args.filename)
    return conn

def createTables(cursor):
    print('Create tables')

    cursor.execute("""CREATE TABLE DocumentType(
    id INTEGER,
    name STRING)""")
    
    cursor.execute("""CREATE TABLE Document(
    id INTEGER,
    name STRING,
    title STRING,
    author STRING,
    documentTypeId INTEGER,
    tags STRING,
    arxivId STRING,
    doi STRING,
    reference STRING)""")
    
    cursor.execute("""CREATE TABLE DocumentCollection(
    id INTEGER,
    name STRING,
    query1_field STRING
    query1_operation STRING
    query1_value STRING
    query2_field STRING
    query2_operation STRING
    query2_value STRING
    query3_field STRING
    query3_operation STRING
    query3_value STRING
    )""")
    
def checkTables(cursor):
    print('Check tables')
    cursor.execute('SELECT name FROM sqlite_master')
    print(cursor.fetchall() )

def deleteTables(conn):
    conn.cursor().execute('DROP TABLE IF EXISTS DocumentType')
    conn.cursor().execute('DROP TABLE IF EXISTS Document')
    conn.cursor().execute('DROP TABLE IF EXISTS DocumentCollection')

def run(args):
    conn = openDb(args.filename)
    if conn is None:
        print(f'Failed to connect to the database file {args.filename}')
        return
    if args.clearTables:
        deleteTables(conn)

    createTables(conn.cursor())
    checkTables(conn.cursor())
    
if __name__ == '__main__':
   args = parseArgs()
   run(args)
   
