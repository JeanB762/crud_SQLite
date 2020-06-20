import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor() 
 
# HardCode insertion
# sql = """
#   INSERT INTO users(name, phone, email)
#   VALUES('Jean', '3595333961184', 'jeanborges946@gmail.com' ) """

# cur.execute(sql)
# con.commit()
# con.close()

# With a function

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