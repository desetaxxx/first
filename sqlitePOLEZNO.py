import sqlite3
from spisok import x

base = sqlite3.connect('new.db')
cur = base.cursor()


'''base.execute('CREATE TABLE IF NOT EXISTS athletes(name, gender, age, country, sport)')
base.commit()

cur.execute('INSERT INTO athletes VALUES(?, ?, ?, ?, ?)',('Nik', 'male', '23', 'Canada','hockey'))
base.commit()

cur.execute('INSERT INTO athletes VALUES(?, ?, ?, ?, ?)',('Egor', 'male', '25', 'Russia','hockey'))
base.commit()

cur.executemany('INSERT INTO athletes VALUES(?, ?, ?, ?, ?)',(x))
base.commit()'''

'''r = cur.execute('SELECT * FROM athletes').fetchall()   
print(r)   ''' # получаем всю базу данных

'''r = cur.execute('SELECT name FROM athletes  WHERE country ==?',('Russia',)).fetchone()    
print(r)'''   # получаем имя !!!ОДНО!!! по стране

'''cur.execute('UPDATE athletes SET country == ? WHERE name == ?',('USA', 'Egor'))    
base.commit()   ''' # меняем в таблице страну у Егора

'''cur.execute('UPDATE athletes SET country == ? WHERE country == ?',('China', 'Russia'))    
base.commit()''' # массого заменяем!!!! поменяли страну Россия у всех на Китай

#cur.execute('DELETE FROM назание таблицы')  удалить все данные из таблицы

'''cur.execute('DELETE FROM athletes WHERE name == ?',('Egor',))
base.commit()''' #удалили Егора из таблицы

# base.execute('DROP TABLE IF EXESTS athletes')  полногстью удаляем базу данных
# base.commit()

base.close()