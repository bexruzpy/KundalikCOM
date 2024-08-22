import wmi

def get():
	c = wmi.WMI()
	for disk in c.Win32_DiskDrive():
		return disk.SerialNumber
