import os, os.path
from sys import argv


script, inputFilename = argv

outputFilename = "../lab0/recv/" + inputFilename


txt = open(inputFilename, 'rb')


def mkdir_p(path):
	try:
		os.makedirs(path, exist_ok=True)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise


def safe_open_w(path):
	mkdir_p(os.path.dirname(path))
	return open(path, 'wb')


try:
	with safe_open_w(outputFilename) as f:
		byte = txt.read(1)

		while byte != b"":
			print(byte)
			f.write(byte);
			byte = txt.read(1)
finally:
	txt.close()







