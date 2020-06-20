import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor() 

def db_insert(name, phone, email):
  return """
  INSERT INTO users(name, phone, email)
    VALUES('{}', '{}', '{}') 
    """.format(name, phone, email)

cur.execute(db_insert('Jota Borges', 
                      '3598987676', 
                      'jeanborges941@gmail.com'))
con.commit()
con.close()