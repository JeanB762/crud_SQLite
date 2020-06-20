from manage_db import db_insert, db_select, db_update, db_delete
from pprint import pprint

# db_insert('Jean', '99999999', 'Jean@gmail.com')
# db_insert('Carlos', '99999999', 'Carlos@gmail.com')
# db_insert('Borges', '99999999', 'Borges@gmail.com')
# db_insert('Oliveira', '99999999', 'Oliveira@gmail.com')
# db_insert('Silva', '99999999', 'Silva@gmail.com')
# db_insert('Mingau', '99999999', 'Mingau@gmail.com')

pprint(db_select('99999999', 'phone'))