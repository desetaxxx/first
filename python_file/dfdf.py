from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///database.db')

# Создание объекта базы данных
Base = declarative_base()

# Определение модели данных
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Создание таблицы в базе данных
Base.metadata.create_all(engine)

# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Пример создания новой записи в таблице
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Запрос данных из таблицы
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# Закрытие сессии
session.close()







