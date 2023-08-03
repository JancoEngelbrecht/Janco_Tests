import sys
import pypyodbc as odbc  # Open Database connection

# records = [
#     ['Janco', 'Fliek', '2020-01-09', 2023],
#     ['Harme', 'Show', None, 2020]
# ]

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-MBKO1DV'
DATABASE_NAME = 'PythonIdea'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    
"""

# try:
#     conn = odbc.connect(connection_string)
# except Exception as e:
#     print('Task is terminated')
#     sys.exit()
# else:
#     cursor = conn.cursor()
#
# insert_statement = """
#     INSERT INTO NetflixMovies
#     VALUES (?,?,?,?)
# """
#
# # try:
#     for record in records:
#         print(record)
#         cursor.execute(insert_statement, record)
# except Exception as e:
#     cursor.rollback()
#     print(e.value)
#     print('transaction rolled back')
# else:
#     print('record inserted successfully')
#     cursor.commit()
#     cursor.close()
#     if conn.connected == 1:
#         print('connection closed')
#         conn.close()

conn = odbc.connect(connection_string)

# get cursor object
cursor = conn.cursor()

# execute your query
cursor.execute("SELECT * FROM NetflixMovies")

# fetch all the matching rows
result = cursor.fetchall()

# loop through the rows
for row in result:
    print(row)