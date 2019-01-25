import mysql.connector

def get_sql_from_file(name: str):
    sql_file_input = open(name, 'r')
    sql_text = sql_file_input.read()
    sql_file_input.close()

    #seperate idividual commands
    sql_commands = sql_text.split(';')

    for i in range(0, len(sql_commands)):
        #cannot execute empty strings
        if sql_commands[i].isspace() == True:
            del sql_commands[i]
    return sql_commands

def run_sql_commands_at_cursor(commands, cursor):
    for command in commands:
        cursor.execute(command)

def is_user_admin(cursor):
    #check if the user has rights which technician doesnt have
    is_admin = False
    try:
        cursor.execute('SELECT * FROM mysql.user;')
        is_admin = True
        trash = cursor.fetchall()
    except mysql.connector.errors.ProgrammingError as err:
        is_admin = False
        
    return is_admin

def get_all_machines(cursor):
    cursor.execute('SELECT nazev FROM Pristroj;')
    return cursor.fetchall()

def get_machine_info(cursor, name):
    cursor.execute('SELECT * FROM Pristroj WHERE nazev=\'' + name + '\';')
    return cursor.fetchall()

def remove_machine(cursor, name):
    cursor.execute('DELETE FROM Pristroj WHERE nazev=\'' + name + '\';')

def add_machine(cursor, machine):
    command = "INSERT INTO Pristroj (id_typ,id_oddeleni,id_dodavatel,nazev,inv_cislo,vyr_cislo,umdns,id_stupen,id_status)"
    data = "VALUES (%d, %d, %d, '%s', '%s', '%s', '%s', %d, %d)" % (machine[0], machine[1], machine[2], machine[3], machine[4], machine[5], machine[6], machine[7], machine[8])
    cursor.execute(command + data)
