"""
DML - Manipulação de dados
"""

import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor() 

def db_insert(name, phone, email):
  return """
    INSERT INTO users(name, phone, email)
    VALUES('{}', '{}', '{}') 
    """.format(name, phone, email)


# cur.execute(db_insert('Jean','999361184', 'jeanborges946@gmail.com'))

# con.commit()
# con.close()

def db_update(name, email):
  return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

# cur.execute(db_update('Carlos', 'jeanborges941@gmail.com'))

# con.commit()
# con.close()

def db_delete(email):
  return """
    DELETE FROM users WHERE email='{}'
    """.format(email)


cur.execute(db_delete('jeanborges941@gmail.com'))

con.commit()
con.close()