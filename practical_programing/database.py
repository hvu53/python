import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 343333)')
cur.execute('INSERT INTO PopByRegion VALUES("Japn", 343333)')
cur.execute('INSERT INTO PopByRegion VALUES (?,?)', ("Japan", 100452))

# saving changes
con.commit()

# Retrieving Data
cur.execute('SELECT Region, Population from PopByRegion')
cur.fetchone() # return a tuple, if there re no more method, return None
cur.fetall()

cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region DESC')
cur.fetchall()

cur.execute('SELECT Region, Population FROM PopByRegion WHERE Population > 10000')
cur.fetchall()

# Updating & Deleting
cur.execute('UPDATE PopByRegion SET Population = 100600 WHERE Region="Japan"')
cur.fetchone()

cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')

# To remove the entire table
cur.execute('DROP TABLE PopByRegion');

# NOT NULL
cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, Population INTEGER)')
countries = [(),(),() ...]
for c in countries:
	cur.execute('INSERT INTO PopByCountry VALUES (?,?,?)', (c[0], c[1], c[2]))
con.commit()

