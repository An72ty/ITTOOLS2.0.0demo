# -*- coding: utf-8 -*-
import sqlite3
import os.path
import os
import json
import shutil


def isPluginCorrect(path):
    if os.path.isdir(path):
        return True


def initTable(dbPath: str = 'data/pluginsInfoDB.db') -> None:
    # Connect
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        # Init sqlite table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS plugins (
            name TEXT,
            version TEXT,
            icon TEXT
        )
        """)
        con.commit()


def remove(name: str, dbPath: str = 'data/pluginsInfoDB.db') -> None:
    # Connect
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM plugins WHERE name=:name", {"name": name})
        # Close
        con.commit()


def insert(name: str, version: str, icon: str, dbPath: str = 'data/pluginsInfoDB.db') -> None:
    # Connect
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO plugins VALUES (:name, :version, :icon)", {
                    "name": name, "version": version, "icon": icon})
        con.commit()


def getPluginsList(dbPath: str = 'data/pluginsInfoDB.db') -> list:
    # updateDB()
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM plugins")
        response = cur.fetchall()
        con.commit()
        return response


def getVersion(name: str, dbPath: str = 'data/pluginsInfoDB.db') -> str:
    # Connect
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        cur.execute('SELECT (version) FROM plugins WHERE name=:name',
                    {"name": name})
        response = cur.fetchall()
        if response != []:
            response = response[0][0]
        return response


def updateDB(dbPath: str = 'data/pluginsInfoDB.db') -> None:
    global isPluginCorrect
    # Connect
    with sqlite3.connect(dbPath) as con:
        cur = con.cursor()
        # Drop table
        cur.execute("DROP TABLE plugins")
        # Reinit it
        cur.execute("""
        CREATE TABLE IF NOT EXISTS plugins (
            name TEXT,
            version TEXT,
            icon TEXT
        )
        """)
        folders = os.listdir('plugins/')
        for folderName in folders:
            folderPath = 'plugins/'+folderName
            if isPluginCorrect(folderPath):
                d = json.loads(open(folderPath+'/info.json').read())
                cur.execute(
                    "INSERT INTO plugins VALUES (:name, :version, :icon)", d)
        con.commit()
