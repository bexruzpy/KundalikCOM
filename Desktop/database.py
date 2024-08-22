import pickle
class DatabaseConnect(object):
	"""docstring for DatabaseConnect"""
	def __init__(self):
		super(DatabaseConnect, self).__init__()
		self.database_file_name = "database.db"
		try:
			with open(self.database_file_name, "rb") as f:
				self.dict_data = pickle.load(f)
		except:
			self.dict_data = {
				"logined": False,
				"profile": dict(),
				"all_data_logins": dict()
			}
			with open(self.database_file_name, "wb") as f:
				pickle.dump(self.dict_data, f)
	# database fileni yangilash funksiyasi
	def refresh(self) -> None:
		with open(self.database_file_name, "wb") as f:
			pickle.dump(self.dict_data, f)

	# login malumotlarini taxrirlash
	def login(self, user_id: int, token: str, username: str, fullname: str, sex: int) -> None:
		self.dict_data["profile"]["username"] = username
		self.dict_data["profile"]["fullname"] = fullname
		self.dict_data["profile"]["token"] = token
		self.dict_data["profile"]["user_id"] = user_id
		self.dict_data["profile"]["sex"] = sex
		self.dict_data["logined"] = True
		self.refresh()
	# logout qilish ->login ma'lumotlarini o'chirib tashlaydi
	def logout(self) -> None:
		self.dict_data["profile"] = dict()
		self.dict_data["logined"] = False
		self.refresh()
	# login qilingan yoki yo'qligi haqida aytuvchi funksiya
	def isLogined(self) -> bool:
		return self.dict_data["logined"]


