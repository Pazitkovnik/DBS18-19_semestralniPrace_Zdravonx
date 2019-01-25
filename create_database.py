import mysql.connector
import sql_functions

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="koloslav12,KOLO",
)
cursor = my_database.cursor()
cursor.execute("DROP database Zdravonx_database")
cursor.execute("CREATE DATABASE Zdravonx_database")

##my_database = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    passwd="koloslav12,KOLO",
##    database="Zdravonx_database"
##)
my_database = mysql.connector.connect(
    host="localhost",
    user="jaroslav",
    passwd="password",
    database="Zdravonx_database"
)

cursor = my_database.cursor()

#insert tables etc.
sql_commands = sql_functions.get_sql_from_file('soubory/createScript.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)

sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_typ.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_stupen.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_oddeleni.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_dodavatel.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_authority.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)

sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_user.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_servisFirma.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_status.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_interval.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_pristroj.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)

sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_dokument.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_pristrojDokument.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_nakup.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_servisZP.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)
sql_commands = sql_functions.get_sql_from_file('soubory/insertScript_kontrolaZP.sql')
sql_functions.run_sql_commands_at_cursor(sql_commands, cursor)

cursor.execute('SELECT * FROM Authority;')
my_result = cursor.fetchall()
for x in my_result:
  print(x)
