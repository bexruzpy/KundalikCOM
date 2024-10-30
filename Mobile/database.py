import sqlite3
import uuid
class DatabaseConnection:
	def __init__(self):
		self.db = sqlite3.connect('KundalikMobile.db')
		self.c = self.db.cursor()
		self.create_tables()

		self.device_id = self.get_data("device_id")
		print(self.get_data("device_id"))
		if self.device_id is None:
			self.device_id = str(uuid.uuid4())
			self.set_data("device_id", self.device_id)
		self.db.commit()

	def create_tables(self):
		try:
			self.c.execute('''CREATE TABLE IF NOT EXISTS datas (
				key TEXT NOT NULL,
				data TEXT NOT NULL
			)''')
		except sqlite3.Error as e:
			print(f"Error creating datas table: {e}")

		try:
			self.c.execute('''CREATE TABLE IF NOT EXISTS logins (
				id INTEGER PRIMARY KEY,
				name TEXT NOT NULL,
				login TEXT NOT NULL UNIQUE,
				password TEXT NOT NULL
			)''')
		except sqlite3.Error as e:
			print(f"Error creating logins table: {e}")

	def get_data(self, key):
		try:
			self.c.execute('''SELECT * FROM datas WHERE key = ?''', (key,))
			result = self.c.fetchone()
			if result is not None:
				return result[1]
			return None
		except sqlite3.Error as e:
			print(f"Database error: {e}")
			return None

	def set_data(self, key, data):
		self.c.execute('''SELECT * FROM datas WHERE key = ?''', (key,))
		fetched_data = self.c.fetchone()
		
		if fetched_data:
			self.c.execute('''UPDATE datas SET data = ? WHERE key = ?''', (data, key))
		else:
			self.c.execute('''INSERT INTO datas (key, data) VALUES (?, ?)''', (key, data))
		
		self.db.commit()
	
	def logout(self):
		try:
			self.c.execute('''DELETE FROM datas WHERE key = ?''', ("token",))
		except:
			pass
	
	# Login ma'lumotlarini olish
	def get_login(self, _id):
		pass
	
	# Login ma'lumotlarini yaratish
	def add_login(self, name, login, password):
		pass

	# Login ma'lumotlarini o'chirish
	def delete_login(self, _id):
		pass

	# Login ma'lumotlarini taxrirlash
	def set_login(self, _id, login, password, name):
		pass

	# Database ni yopish dasturdan chiqilganda
	def close(self):
		self.db.close()