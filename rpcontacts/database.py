# -*- coding: utf-8 -*-
# rpcontacts/database.py

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            gruppo_muscolare VARCHAR(40) NOT NULL,
            esercizio VARCHAR(50),
            materiale VARCHAR(40) NOT NULL,
            carico_dischi VARCHAR(40),
            ripetizioni VARCHAR(40),
            tempo_recupero VARCHAR(40),
        )
        """
    )

def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()

    return True