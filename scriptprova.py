# SCRIPT STEP 4

from rpcontacts.database import createConnection
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery

# Create a connection
createConnection("contacts.sqlite")

# Confirm that contacts table exists

db = QSqlDatabase.database()
db.tables()
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        gruppo_muscolare,
        esercizio,
        materiale,
        carico_dischi,
        ripetizioni,
        tempo_recupero
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """
)

data = []

#Sample data
for name, job, email in data:
    insertDataQuery.addBindValue(gruppo_muscolare)
    insertDataQuery.addBindValue(esercizio)
    insertDataQuery.addBindValue(materiale)
    insertDataQuery.addBindValue(carico_dischi)
    insertDataQuery.addBindValue(ripetizioni)
    insertDataQuery.addBindValue(tempo_recupero)
    insertDataQuery.exec()

query = QSqlQuery()
query.exec("SELECT gruppo_muscolare, esercizio, materiale, carico_dischi, ripetizioni, tempo_recupero FROM contacts")
i=0
#query.exec("TRUNCATE TABLE contacts")

while query.next():
    print(query.value(0), query.value(1), query.value(2), query.value(3), query.value(4), query.value(5))
    i+=1
    print(i)

