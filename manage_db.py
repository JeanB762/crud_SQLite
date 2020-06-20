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


def db_update(name, email):
  return """
  UPDATE users SET name = '{}' WHERE email = '{}'
  """.format(name, email)


def db_delete(email):
  return """
  DELETE FROM users WHERE email='{}'
  """.format(email)

def db_select(data, field):
  return """
  SELECT id, name, phone, email
  FROM  users
  WHERE {} = {}""".format(data, field)

# cur.execute(db_insert('Jean','999361184', 'jeanborges946@gmail.com'))

# cur.execute(db_update('Carlos', 'jeanborges941@gmail.com'))

# cur.execute(db_delete('jeanborges941@gmail.com'))

cur.execute(db_select('1', 'id'))
  
data = cur.fetchone()
# con.commit()
con.close()
print(data)