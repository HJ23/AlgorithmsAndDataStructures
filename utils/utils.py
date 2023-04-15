
import time
import sys, os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def benchmark(count):
	if(count<=1):
		raise ValueError("[X] Count must be greater than 0 !")
	def decorator(function):
		def run(*args,**kwargs):
			AVERAGE = 0
			blockPrint()
			for _ in range(count):
				START = time.time()
				function(*args,**kwargs)
				AVERAGE += time.time() - START
			enablePrint()
			print(f"FUNCTION RESULT : {function(*args,**kwargs)}")
			print(f"[*] AVERAGE TIME SPENT FOR {function.__name__}  TO EXECUTE : {AVERAGE/count}")
		return run
	return decorator


