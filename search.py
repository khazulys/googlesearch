try:
	from googlesearch import search
	import os
	from time import sleep
	os.system('cls' if os.name=='nt' else 'clear')
	print ("\033[1;36m  ╔═╗┌─┐┌─┐┌─┐┬  ┌─┐  ╔═╗┌─┐┌─┐┬─┐┌─┐┬ ┬	")
	print ("\033[1;35m  ║ ╦│ ││ ││ ┬│  ├┤   ╚═╗├┤ ├─┤├┬┘│  ├─┤ ")
	print ("\033[1;31m  ╚═╝└─┘└─┘└─┘┴─┘└─┘  ╚═╝└─┘┴ ┴┴└─└─┘┴ ┴	")
	print ("\033[1;33m     Search In Termux Coded By Khazul ")
except ImportError:
    print("No module named 'google' found")
# to search
query = input("\n\033[1;30m[√]\033[1;32m Whats you mean?\n\033[1;31m=>\033[1;36m ")
print ("\033[1;32m[?]\033[1;33m Opening Google Chrome..")
sleep(2.5)
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
	print ("\033[1;34m[!]\033[1;35m Result Link:\033[1;39m " +j)
	print ("\033[1;32m[+]\033[1;33m Copy Link and Paste in Your Browser..")
	print ("\033[1;32m[!]\033[1;33m Thanks for use my tool..")
