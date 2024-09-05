import requests
import pickle
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import kundalikcom_func


class DatabaseConnect(object):
    """docstring for DatabaseConnect"""
    def __init__(self):
        super(DatabaseConnect, self).__init__()
        self.database_file_name = "database.db"
        self.browser = requests.session()
        try:
            with open(self.database_file_name, "rb") as f:
                self.dict_data = pickle.load(f)
                self.browser = pickle.load(f)
        except:
            self.dict_data = {
                "logined": False,
                "profile": dict(),
                "all_data_logins": dict(),
                "profile_kundalikcom": dict()
            }
            self.browser = requests.session()
            with open(self.database_file_name, "wb") as f:
                pickle.dump(self.dict_data, f)
                pickle.dump(self.browser, f)
        self.dict_data["profile_kundalikcom"]["mal"] = {
        "day_1": {"date": "2024.8.30", "foiz": 100},
        "day_2": {"date": "2024.8.29", "foiz": 50},
        "day_3": {"date": "2024.8.28", "foiz": 30},
        "day_4": {"date": "2024.8.27", "foiz": 10},
        }
        self.day_1 = self.dict_data["profile_kundalikcom"]["mal"]["day_1"]
        self.day_2 = self.dict_data["profile_kundalikcom"]["mal"]["day_2"]
        self.day_3 = self.dict_data["profile_kundalikcom"]["mal"]["day_3"]
        self.day_4 = self.dict_data["profile_kundalikcom"]["mal"]["day_4"]
    def login_kundalik(self, login, password):
        try:
            res = self.browser.get("https://emaktab.uz")
            soup = BeautifulSoup(res.content, "html.parser")
            how = True
            if "Chiqish" not in soup.get_text():
                self.browser = requests.session()
                how, data = kundalikcom_func.login_user(self.browser, login, password)
                self.browser = data["browser"]
            if how:
                res = self.browser.get("https://schools.emaktab.uz/v2/school")
                maktab_id = int(res.url.split("school=")[-1])
                res = self.browser.get(f"https://schools.emaktab.uz/v2/school?school={maktab_id}&view=profile")
                soup = BeautifulSoup(res.content, "html.parser")
                content = soup.find(id="ContentPartInfo")
                maktab_nomi = soup.find(id="subheader").get_text().strip()
                res = content.find_all("td")
                joylashuv = res[11].get_text().strip()[:-1].split("(")
                tuman, viloyat = joylashuv[0].strip(), joylashuv[1].strip()
                return True, {
                "maktab_nomi": maktab_nomi,
                "maktab_id": maktab_id,
                "tuman": tuman,
                "viloyat": viloyat,
                "token": self.dict_data["profile"]["token"]
                }
            else:
                text = soup.find_all(class_="message")[0].get_text().strip()
                return False, True
        except requests.exceptions.ConnectionError:
            return False, None
        except:
            return False, False
    # database fileni yangilash funksiyasi
    def refresh(self) -> None:
        with open(self.database_file_name, "wb") as f:
            pickle.dump(self.dict_data, f)
            pickle.dump(self.browser, f)
    # login malumotlarini taxrirlash
    def login(self, token: str, data: dict) -> None:
        self.dict_data["profile"] = data
        self.dict_data["profile"]["token"] = token
        self.dict_data["logined"] = True
        self.refresh()
    # logout qilish ->login ma'lumotlarini o'chirib tashlaydi
    def logout(self) -> None:
        self.dict_data["profile"] = dict()
        self.dict_data["logined"] = False
        self.refresh()
    # login qilingan yoki yo'qligi haqida aytuvchi funksiya
    def isLoginedKundalik(self) -> bool:
        return "login" in self.dict_data["profile_kundalikcom"]
    def isLogined(self) -> bool:
        return self.dict_data["logined"]
    def get_profile(self):
        return self.dict_data["profile"]
    def get_kundalik_profile(self):
        return self.dict_data["profile_kundalikcom"]
    def set_today(self, foiz):
        now = datetime.now()
        if str(now).split()[0] == self.dict_data["profile_kundalikcom"]["mal"]["day_1"]["date"]:
            self.dict_data["profile_kundalikcom"]["mal"]["day_1"]["foiz"] = foiz
        else:
            self.dict_data["profile_kundalikcom"]["mal"]["day_4"] = self.dict_data["profile_kundalikcom"]["mal"]["day_3"]
            self.dict_data["profile_kundalikcom"]["mal"]["day_3"] = self.dict_data["profile_kundalikcom"]["mal"]["day_2"]
            self.dict_data["profile_kundalikcom"]["mal"]["day_2"] = self.dict_data["profile_kundalikcom"]["mal"]["day_1"]
            self.dict_data["profile_kundalikcom"]["mal"]["day_1"] = {
                "date": str(now).split()[0],
                "foiz": foiz
            }
        self.refresh()
    def get_4_day(self):
        try:
            mals = self.dict_data["profile_kundalikcom"]["mal"]

            now = datetime.now()
            if str(now).split()[0] == self.dict_data["profile_kundalikcom"]["mal"]["day_1"]["date"]:
                return mals
            else:
                self.dict_data["profile_kundalikcom"]["mal"]["day_4"] = self.dict_data["profile_kundalikcom"]["mal"]["day_3"]
                self.dict_data["profile_kundalikcom"]["mal"]["day_3"] = self.dict_data["profile_kundalikcom"]["mal"]["day_2"]
                self.dict_data["profile_kundalikcom"]["mal"]["day_2"] = self.dict_data["profile_kundalikcom"]["mal"]["day_1"]
                self.dict_data["profile_kundalikcom"]["mal"]["day_1"] = {
                    "date": str(now).split()[0],
                    "foiz": -1
                }
                database.refresh()
                return self.dict_data["profile_kundalikcom"]["mal"]
        except:
            day_1 = datetime.now()
            day_2 = day_1 - timedelta(days=1)
            day_3 = day_1 - timedelta(days=2)
            day_4 = day_1 - timedelta(days=3)
            self.dict_data["profile_kundalikcom"]["mal"] = {
                "day_1": {"date": str(day_1).split()[0], "foiz": 0},
                "day_2": {"date": str(day_2).split()[0], "foiz": 0},
                "day_3": {"date": str(day_3).split()[0], "foiz": 0},
                "day_4": {"date": str(day_4).split()[0], "foiz": 0},
            }
            return self.dict_data["profile_kundalikcom"]["mal"]
    def get_len_logins(self):
        return len(self.dict_data["all_data_logins"])
    def get_classes(self):
        return kundalikcom_func.get_all_group(self.browser, self.dict_data["profile_kundalikcom"]["maktab_id"])
    def get_logins(self):
        return self.dict_data["all_data_logins"]
    def get_user(self, user_id):
        return self.dict_data["all_data_logins"][user_id]
    def set_user(self, user_id, login=False, parol=False):
        if login:
            self.dict_data["all_data_logins"][user_id]["login"] = login
        if parol:
            self.dict_data["all_data_logins"][user_id]["parol"] = parol
        self.refresh()
    def login_user(self, user_id):
        try:
            user = self.get_user(user_id)
            print(user)
            res = user["browser"].get("https://emaktab.uz")
            soup = BeautifulSoup(res.content, "html.parser")
            if "Chiqish" in soup.get_text():
                print("1 ta")
                return True
            else:
                how, data = kundalikcom_func.login_user(user["browser"], user["login"], user["parol"])
                if how:
                    self.dict_data["all_data_logins"][user_id]["browser"] = data["browser"]
                    self.refresh()
                return how

        except:
            return False
# database = DatabaseConnect()
# prof = database.get_kundalik_profile().copy()
# import time
# for i in range(1000):
#     print(f"{i+1})",kundalikcom_func.login_user(prof["login"], prof["parol"]))
