import signal
import time
import os

def slowprint(words):
	for char in words:
	    time.sleep(0.01)
	    print(char, end='', flush=True)

def fastprint(words):
	for char in words:
	    time.sleep(0.001)
	    print(char, end='', flush=True)


def printer():
	i=0
	while 1>0:	
		fastprint('ThIs CoMpUtEr iS hAcKeD. LOL. PrAy tO the LoRd for HeLp')
		i=i+1
		j=0
		if (i+20)%50==0:
			fastprint('\u001b[32;1m'+'PRESS CTRL+C TO STOP'+'\033[0m')
		if (i+10)%50==0:
			fastprint('\u001b[32;1m'+'PRESS CTRL+C TO STOP'+'\033[0m')
		if (i+5)%50==0:
			slowprint('\t\u001b[31;1m'+'SELL ME YOUR SOUL'+'\033[0m'+'\t')
		if (i+35)%50==0:		
			print('\x1b[1;33;41m\t\t' + 'DO NOT TRY TO EXIT, ELSE PREPARE FOR WRATH' + '\t\t\x1b[0m')
		if i%10000==0:
			time.sleep(1000)


def printshit():
	slowprint('\u001b[36;1m'+'\n\n\nCONGRATS IISERB USER!. You succeeded in stopping the program.'+'\033[0m')
	slowprint('\n\n' + '\u001b[32;1m' + 'noob_of_iiserb '+'\033[0m' + 'sends his regards.')
	time.sleep(2.5)
	slowprint('\u001b[31;1m'+'\n\nWAIT! Did you really think there would be no consequences?'+'\033[0m\n')
	time.sleep(2)
	slowprint('\u001b[31;1m'+'PROCEEDING TO WIPE THIS COMPUTER'+'\033[0m\n')
	slowprint('\u001b[36;1m'+'DELETING USER DATA IN 3...')
	time.sleep(1)
	slowprint('2...')
	time.sleep(1)
	slowprint('1...')
	time.sleep(1)
	os.system('clear')
	print('\x1b[0;37;47m' + 'NOOB'*10000 + '\x1b[0m')
	time.sleep(10)
	slowprint('\u001b[36;1m'+'Just kidding, HA!'+'\033[0m')
	time.sleep(1)
	os.system('clear')

def handler(signum, frame):
	pass

signal.signal(signal.SIGTSTP, handler)

while 1>0:
	try:
		printer()
	except:
		try:
			printshit()
			continue
		except:
			continue


while True:
   pass


