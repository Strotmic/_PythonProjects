import sqlite3
import re
from typing import final

def change(naam,  id):
    try:
        string = '''UPDATE test SET name ='{0}' Where id = {1}'''
        final = string.format(naam,id)
        print(final)
        cur.execute(final)
    except:
        print(' Error')

def find(naam):
    naam ='.....'+naam
    cur.execute("select * from test")
    string = re.findall(naam,str(cur.fetchall()),1)
    print(string)

con = sqlite3.connect('test.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE if not exists test(id integer primary key, name text not null)''')

# Insert a row of data
#cur.execute("insert into test(id, name) values(4,'Bob2')")

#cur.execute('''insert into test(id, name) values(13,"Mary")''')

cur.execute('''select * from test''')

#for i in con:
    #print(i)
for row in cur.execute('SELECT * FROM test ORDER BY id'):
        print(row)

find('Tim')
change('Tim',11)


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
