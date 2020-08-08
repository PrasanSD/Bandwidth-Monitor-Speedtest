import speedtest
import sys

def speedTest(): 
	s = speedtest.Speedtest()
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	
	result = s.results.dict()

	return result["download"], result["upload"], result["ping"]

def main():
	while True:
		download, upload, ping = speedTest()

		# convert to Mbps
		download = download * 1e-6
		upload = upload * 1e-6

		print("Download Speed: " + str(download) + " Mbps \n")
		print("Upload Speed: " + str(upload) + " Mbps \n")
		print(quit)
		print('\n')	
	
	# Write to a csv
	""" with open('log.csv', 'w') as file:
		file.write('Download \t Upload \t Ping\n')
		file.write('%.3f'%download);
		file.write(' Mbps\t ')
		file.write(str('%.3f'%upload))
		file.write(' Mbps\t ')
		file.write(str(ping))
		file.write(' ms\n')

		file.close() """

if __name__ == '__main__':
	try:
		main()
	except Exception as ex:
		print(ex)
		sys.exit(1)
	