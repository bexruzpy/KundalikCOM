from plyer import uniqueid

device_id = uniqueid.id  # Qurilmaning noyob identifikatori

# Agar qurilma nomi yoki modeli kerak bo'lsa
from plyer import device_info
def get_phone():
	device_model = device_info.get_info('model')  # Qurilma modeli
	device_name = device_info.get_info('manufacturer')  # Qurilma ishlab chiqaruvchisi

	return f"{device_id};{device_model};{device_name}"
print(get_phone())