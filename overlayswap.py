import os
import hashlib
import urllib.request
import psutil
import time

procname = 'steam.exe'
renderer = 'GameOverlayRenderer.dll'


renderer_md5 = 'b87c4dd6756e5c53ac44edf8abac5224'

def work():
	for proc in psutil.process_iter():
		if proc.name() == procname:
			proc.kill()
			time.sleep(5)

	with open(renderer, 'rb') as file_to_check:
		data = file_to_check.read()
		md5_returned_renderer = hashlib.md5(data).hexdigest()

		if md5_returned_renderer != renderer_md5:
			print('md5 failed!')

		else:
			print('md5 passed')

			



	if md5_returned_renderer != renderer_md5:
		os.rename('GameOverlayRenderer.dll', 'GameOverlayRenderer.dll.old')
		os.rename('GameOverlayRenderer64.dll', 'GameOverlayRenderer64.dll.old')
		os.rename('GameOverlayUI.exe', 'GameOverlayUI.exe.old')
		os.rename('GameOverlayRenderer.log', 'GameOverlayRenderer.log.old')
		urllib.request.urlretrieve("https://github.com/Junkob101/gs-2023-fix/raw/main/GameOverlayRenderer.dll", "GameOverlayRenderer.dll")
		urllib.request.urlretrieve("https://raw.githubusercontent.com/Junkob101/gs-2023-fix/main/GameOverlayRenderer.log", "GameOverlayRenderer.log")
		urllib.request.urlretrieve("https://github.com/Junkob101/gs-2023-fix/raw/main/GameOverlayRenderer64.dll", "GameOverlayRenderer64.dll")
		urllib.request.urlretrieve("https://github.com/Junkob101/gs-2023-fix/raw/main/GameOverlayUI.exe", "GameOverlayUI.exe")
		urllib.request.urlretrieve("https://raw.githubusercontent.com/Junkob101/gs-2023-fix/main/steam.cfg", "steam.cfg")

	else:
		if os.path.isfile('GameOverlayRenderer.dll.old') == True:
			os.remove('GameOverlayRenderer.dll')
			os.remove('GameOverlayRenderer64.dll')
			os.remove('GameOverlayUI.exe')
			os.remove('GameOverlayRenderer.log')
			os.rename('GameOverlayRenderer.dll.old', 'GameOverlayRenderer.dll')
			os.rename('GameOverlayRenderer64.dll.old', 'GameOverlayRenderer64.dll')
			os.rename('GameOverlayUI.exe.old', 'GameOverlayUI.exe')
			os.rename('GameOverlayRenderer.log.old', 'GameOverlayRenderer.log')
			os.remove('steam.cfg')
		else:
			os.remove('steam.cfg')


#def main():
work()
