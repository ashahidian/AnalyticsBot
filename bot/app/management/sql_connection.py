# cheat sheet
# https://gist.github.com/hofmannsven/9164408

# to connect microsoft sql
# https://django-mssql.readthedocs.io/en/latest/
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html

# run sql
# mysql -u root -p
# password p4ssw0rd

# show databases;
# use db;
# show tables;

import mysql.connector

# needs to receive user, password and database too, as variables

# function to get categorie elements
# not called in project as is.
# categories have been filled for test purposes
def sql_call(sql_request):
    connection = mysql.connector.connect(user='root', password='p4ssw0rd', database='simple_test')
    cursor = connection.cursor()

    # query_names = ("SELECT client_name FROM example_table")

    # cursor.execute(query_names)
    cursor.execute(sql_request)

    for (client_name) in cursor:
        value = "client names {}".format(client_name)
    cursor.close()
    connection.close()

    return value
