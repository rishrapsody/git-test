#! /usr/bin/env python


"""
author=Himanshu Dhingra
date=28-May-2020 9:30 PM

1. Login credentials required.
2. Interactive script which performs HTTP and SCP to india and usa testing servers
3. Sends result in an email
4. Displays the result in tabular form
5. SCP provides transfer over Aryaka and MPLS
6. Installs dependencies
7. HTTP does transfer twice cold and warm
"""



import os
import hashlib
import time
import getpass 
import terminal_banner
from tabulate import tabulate
import yagmail
import datetime

#functions defined
#India_File_wget_Transfer()-->perform wget transfer with India server
#USA_File_wget_transfer()-->perform wget transfer with USA server
#India_File_scp_Transfer()-->perform scp transfer with India server
#wget_again()--> perform again wget
#scp_again()--> perform scp again
#USA_File_scp_transfer()-->perform scp transfer with usa server
#wget()--> perform wget
#scp() --> perfomr scp
#type_of_test() --> what test you want to run?
#aryaka() --> banner
#cold_transfer() -->first time transfer over ANAP
#warm_transfer --> second time transfer over ANAP
#write_wget_inputs --> to write wget result into wget file
#scp_mail --> to initiate a scp result mail
#wget_mail -> to initiate a wget result mail
#write_scp_inputs --> to write scp result into scp file


def scp_mail():
	customer_name_input = raw_input("Please enter Customer Name:\n")
        mail_input = raw_input("Please enter your mail address:\n")
        receiver = mail_input
        customer_name = customer_name_input
        body = "Please find attached SCP File transfer for your customer %s" % customer_name
        filename = "inputs_scp.txt"
        yag = yagmail.SMTP("aryakatme@gmail.com","Aryak@123")
        yag.send(
                to = receiver,
		cc = "himanshu.dhingra@aryaka.com",
                subject = "%s Test result" % customer_name,
                contents = body,
                attachments = filename,
                )

def http_mail():
	customer_name_input = raw_input("Please enter Customer Name:\n")
	mail_input = raw_input("Please enter your mail address:\n")
	receiver = mail_input
	customer_name = customer_name_input
	body = "Please find attached HTTP File transfer for your customer %s" % customer_name
	filename = "inputs_http.txt"
	yag = yagmail.SMTP("aryakatme@gmail.com","Aryak@123")
	yag.send(
		to = receiver,
		cc = "himanshu.dhingra@aryaka.com",
		subject = "%s Test result" % customer_name,
		contents = body,
		attachments = filename,
		)

def write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls):
	f = open("inputs_scp.txt","w+")
	f.write("%i MB file \n" % file_size)
	f.write("took %i seconds of time over Aryaka with optimization \n" % scp_time_aryaka)
	f.write("took %i seconds of time over Aryaka without optimization \n" % scp_time_mpls)
	f.close()

def write_http_inputs(file_size,cold_time,warm_time,internet_time):
	f = open("inputs_http.txt","w+")
	f.write("%i MB file \n" % file_size)
	f.write("Cold transfer in %i seconds over Aryaka \n " % cold_time)
	f.write("Warm transfer in %i seconds over Aryaka \n " % warm_time)
	f.write("Internet Transfer took %i seconds \n"% internet_time)
	f.close()

def internet():
	os.system("figlet OVER INTERNET")

def India_File_http_Transfer():
	http_file_size_banner =  "Which file do you want to transfer from India \n 1. 10 MB (Aryaka and Internet) \n 2. 50 MB (Aryaka and Internet) \n 3. 100 MB (Aryaka and Internet) \n 4. 500 MB (Aryaka and Internet) \n 5. 1000 MB (Aryaka and Internet)"
	India_http_banner = terminal_banner.Banner(http_file_size_banner)
	print(India_http_banner)
	print "\n \n \nPlease type your input below(number)"
	file_size_input = input()

	if file_size_input == 1:
		cold_transfer()
		start = int(time.time())
		Result=os.system("wget http://10.0.20.13/10MB_INDIA_Aryaka")
		end = int(time.time())
		http_india_time_cold = end - start
		warm_transfer()
		start = int(time.time())
                Result=os.system("wget http://10.0.20.13/10MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_warm = end - start
		file_size = 10
		internet()
		start = int(time.time())
		result = os.system("wget http://147.75.230.104/10MB_INDIA_Internet")
		end = int(time.time())
		internet_time = end - start
		os.system('clear')
		cold_time = http_india_time_cold
		warm_time = http_india_time_warm
		write_http_inputs(file_size,cold_time,warm_time,internet_time)
		print (tabulate({"10 MB File": ["Cold 10 MB File Transfer\n over Aryaka (in seconds)",http_india_time_cold]}, tablefmt="grid"))
		print (tabulate({"10 MB Warm File": ["Warm 10 MB File Transfer\nover Aryaka (in seconds)",http_india_time_warm]}, tablefmt="grid"))
		print (tabulate({"10 MB Internet File": ["10 MB Internet File Transfer\n (in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	elif file_size_input == 2:
		cold_transfer()
		start = int(time.time())
                Result=os.system("wget http://10.0.20.13/50MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_cold = end - start
		warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/50MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_warm = end - start
		internet()
		start = int(time.time())
		result = os.system("wget http://147.75.230.104/50MB_INDIA_Internet")
		end = int(time.time())
		internet_time = end - start
		os.system('clear')
		file_size = 50
		cold_time = http_india_time_cold
                warm_time = http_india_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"50 MB File": ["Cold 50 MB File Transfer \nover Aryaka (in seconds)",http_india_time_cold]}, tablefmt="grid"))
		print (tabulate({"50 MB Warm File": ["Warm 50 MB File Transfer \nover Aryaka (in seconds)",http_india_time_warm]}, tablefmt="grid"))
		print (tabulate({"50 MB Internet File": ["50 MB Internet File transfer\n (in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	elif file_size_input == 3:
                cold_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/100MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_cold = end - start
                warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/100MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_warm = end - start
                internet()
                start = int(time.time())
                result = os.system("wget http://147.75.230.104/100MB_INDIA_Internet")
                end = int(time.time())
                internet_time = end - start
                os.system('clear')
                file_size = 100
                cold_time = http_india_time_cold
                warm_time = http_india_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"100 MB File": ["Cold 100 MB File Transfer \nover Aryaka (in seconds)",http_india_time_cold]}, tablefmt="grid"))
                print (tabulate({"100 MB Warm File": ["Warm 100 MB File Transfer \nover Aryaka (in seconds)",http_india_time_warm]}, tablefmt="grid"))
                print (tabulate({"100 MB Internet File": ["100 MB Internet File transfer\n (in seconds)",internet_time]}, tablefmt="grid"))
                http_again()
	elif file_size_input == 4:
                cold_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/500MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_cold = end - start
                warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/500MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_warm = end - start
                internet()
                start = int(time.time())
                result = os.system("wget http://147.75.230.104/500MB_INDIA_Internet")
                end = int(time.time())
                internet_time = end - start
                os.system('clear')
                file_size = 500
                cold_time = http_india_time_cold
                warm_time = http_india_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"500 MB File": ["Cold 50 MB File Transfer \nover Aryaka (in seconds)",http_india_time_cold]}, tablefmt="grid"))
                print (tabulate({"500 MB Warm File": ["Warm 50 MB File Transfer \nover Aryaka (in seconds)",http_india_time_warm]}, tablefmt="grid"))
                print (tabulate({"500 MB Internet File": ["50 MB Internet File transfer\n (in seconds)",internet_time]}, tablefmt="grid"))
                http_again()
	elif file_size_input == 5:
		cold_transfer()
		start = int(time.time())
                Result=os.system("wget http://10.0.20.13/1000MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_cold = end - start
		warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://10.0.20.13/1000MB_INDIA_Aryaka")
                end = int(time.time())
                http_india_time_warm = end - start
		internet()
		start = int(time.time())
                result = os.system("wget http://147.75.230.104/1000MB_INDIA_Internet")
                end = int(time.time())
                internet_time = end - start
		os.system('clear')
		file_size = 1000
                cold_time = http_india_time_cold
                warm_time = http_india_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"1000 MB File": ["Cold 1000 MB File Transfer \nover Aryaka (in seconds)",http_india_time_cold]}, tablefmt="grid"))
		print (tabulate({"1000 MB Warm File": ["Warm 1000 MB File Transfer \nover Aryaka (in seconds)",http_india_time_warm]}, tablefmt="grid"))
		print (tabulate({"1000 MB Internet File": ["1000 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	else:
        	print "Wrong input! Please try again"
        	India_File_http_Transfer()
        
    
def USA_File_http_transfer():
    	http_file_size_banner =  "Which file do you want to transfer from USA \n 1. 10 MB (Aryaka and Internet) \n 2. 50 MB (Aryaka and Internet) \n 3. 100 MB (Aryaka and Internet) \n 4. 500 MB (Aryaka and Internet) \n 5. 1000 MB (Aryaka and Internet)"
	USA_http_banner = terminal_banner.Banner(http_file_size_banner)
	print(USA_http_banner)
	print "\n \n \nPlease type your input below(number)"
	file_size_input = input()

	if file_size_input == 1:
		cold_transfer()
		start = int(time.time())
                Result=os.system("wget http://192.168.18.1/10MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_cold = end - start
		warm_transfer()
		start = int(time.time())
                Result=os.system("wget http://192.168.18.1/10MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_warm = end - start
		internet()
		start = int(time.time())
                result = os.system("wget http://167.179.35.124/10MB_US_Internet")
                end = int(time.time())
                internet_time = end - start
		os.system('clear')
		file_size = 10
                cold_time = http_usa_time_cold
                warm_time = http_usa_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
		print (tabulate({"10 MB File": ["Cold 10 MB File Transfer\nover Aryaka (in seconds)",http_usa_time_cold]}, tablefmt="grid"))
		print (tabulate({"10 MB Warm File": ["Warm 10 MB File Transfer\n over Aryaka (in seconds)",http_usa_time_warm]}, tablefmt="grid"))
		print (tabulate({"10 MB Internet File": ["10 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	elif file_size_input == 2:
                cold_transfer()
                start = int(time.time())
                Result=os.system("wget http://192.168.18.1/50MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_cold = end - start
                warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://192.168.18.1/50MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_warm = end - start
                internet()
                start = int(time.time())
                result = os.system("wget http://167.179.35.124/50MB_US_Internet")
                end = int(time.time())
                internet_time = end - start
                os.system('clear')
                file_size = 50
                cold_time = http_usa_time_cold
                warm_time = http_usa_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"50 MB File": ["Cold 100 MB File Transfer\n over Aryaka (in seconds)",http_usa_time_cold]},tablefmt = "grid"))
                print (tabulate({"50 MB Warm File": ["Warm 100 MB File Transfer\nover Aryaka (in seconds)",http_usa_time_warm]}, tablefmt="grid"))
                print (tabulate({"50 MB Internet File": ["100 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
                http_again()
	elif file_size_input == 3:
		cold_transfer()
		start = int(time.time())
                Result=os.system("wget http://192.168.18.1/100MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_cold = end - start
		warm_transfer()
		start = int(time.time())
                Result=os.system("wget http://192.168.18.1/100MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_warm = end - start
		internet()
		start = int(time.time())
                result = os.system("wget http://167.179.35.124/100MB_US_Internet")
                end = int(time.time())
                internet_time = end - start
		os.system('clear')
		file_size = 100
                cold_time = http_usa_time_cold
                warm_time = http_usa_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"100 MB File": ["Cold 100 MB File Transfer\n over Aryaka (in seconds)",http_usa_time_cold]},tablefmt = "grid"))
		print (tabulate({"100 MB Warm File": ["Warm 100 MB File Transfer\nover Aryaka (in seconds)",http_usa_time_warm]}, tablefmt="grid"))
		print (tabulate({"100 MB Internet File": ["100 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	elif file_size_input == 4:
                cold_transfer()
                start = int(time.time())
                Result=os.system("wget http://192.168.18.1/500MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_cold = end - start
                warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://192.168.18.1/500MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_warm = end - start
                internet()
                start = int(time.time())
                result = os.system("wget http://167.179.35.124/500MB_US_Internet")
                end = int(time.time())
                internet_time = end - start
                os.system('clear')
                file_size = 500
                cold_time = http_usa_time_cold
                warm_time = http_usa_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"500 MB File": ["Cold 100 MB File Transfer\n over Aryaka (in seconds)",http_usa_time_cold]},tablefmt = "grid"))
                print (tabulate({"500 MB Warm File": ["Warm 100 MB File Transfer\nover Aryaka (in seconds)",http_usa_time_warm]}, tablefmt="grid"))
                print (tabulate({"500 MB Internet File": ["100 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
                http_again()
	elif file_size_input == 5:
		cold_transfer()
		start = int(time.time())
                Result=os.system("wget http://192.168.18.1/1000MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_cold = end - start
		warm_transfer()
                start = int(time.time())
                Result=os.system("wget http://192.168.18.1/1000MB_US_Aryaka")
                end = int(time.time())
                http_usa_time_warm = end - start
		internet()
		start = int(time.time())
                result = os.system("wget http://167.179.35.124/1000MB_US_Internet")
                end = int(time.time())
                internet_time = end - start
		os.system('clear')
		file_size = 1000
                cold_time = http_usa_time_cold
                warm_time = http_usa_time_warm
                write_http_inputs(file_size,cold_time,warm_time,internet_time)
                print (tabulate({"1000 MB File": ["Cold 1000 MB File Transfer\nover Aryaka (in seconds)",http_usa_time_cold]},tablefmt = "grid"))
		print (tabulate({"1000 MB Warm File": ["Warm 1000 MB File Transfer\n over Aryaka (in seconds)",http_usa_time_warm]}, tablefmt="grid"))
		print (tabulate({"1000 MB Internet File": ["1000 MB Internet File Transfer\n(in seconds)",internet_time]}, tablefmt="grid"))
		http_again()
	else:
        	print "Wrong input! Please try again"
        	USA_File_http_Transfer()

def India_File_scp_Transfer():
	scp_file_size_banner = "Which file do you want to transfer from India \n 1. 10 MB (Aryaka- with and without optimzation) \n 2. 100 MB (Aryaka- with and without optimzation) \n 3. 1000 MB (Aryaka- with and without Optimization)"
	India_scp_banner = terminal_banner.Banner(scp_file_size_banner)
	print(India_scp_banner)
	print "\n \n \nPlease type your input below(number)"
	file_size_input = input()

	if file_size_input == 1:
		os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
		start = int(time.time())
		os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@10.0.20.13:/tme/type_of_files/10MB .")
		end = int(time.time())
		scp_india_time_aryaka = end - start
		os.system('clear')
		print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_india_time_aryaka)
		os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
		time.sleep(2)
		start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@10.0.20.13:/tme/type_of_files/10MB .")
                end = int(time.time())
                scp_india_time_mpls = end - start
		os.system('clear')
		print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_india_time_mpls)
		time.sleep(2)
		os.system('clear')
		file_size = 10
		scp_time_aryaka = scp_india_time_aryaka
		scp_time_mpls = scp_india_time_mpls
		write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
		print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_india_time_aryaka],"20":["SCP File Transfer over Aryaka \n without optimization (in seconds)",scp_india_time_mpls]}, tablefmt="grid"))
		scp_again()
	elif file_size_input == 2:
		os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
        	start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@10.0.20.13:/tme/type_of_files/100MB .")
                end = int(time.time())
                scp_india_time_aryaka = end - start
		os.system('clear')
		print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_india_time_aryaka)
                os.system('figlet OVER MPLS WITHOUT OPTIMIZATION')
		time.sleep(2)
		start = int(time.time())
		os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@10.0.20.13:/tme/type_of_files/100MB .")
                end = int(time.time())
                scp_india_time_mpls = end - start
		os.system('clear')
                print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_india_time_mpls)
                time.sleep(2)
                os.system('clear')
		file_size = 100
                scp_time_aryaka = scp_india_time_aryaka
		scp_time_mpls = scp_india_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_india_time_aryaka],"20":["SCP File Transfer over Aryaka \n without optimization (in seconds)",scp_india_time_mpls]}, tablefmt="grid"))
		scp_again()
	elif file_size_input == 3:
		os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
        	start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@10.0.20.13:/tme/type_of_files/1000MB .")
                end = int(time.time())
                scp_india_time_aryaka = end - start
		os.system('clear')
		print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_india_time_aryaka)
		os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
		os.system('clear')
		start = int(time.time())
		os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@10.0.20.13:/tme/type_of_files/1000MB .")
                end = int(time.time())
                scp_india_time_mpls = end - start
		os.system('clear')
                print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_india_time_mpls)
		time.sleep(2)
                os.system('clear')
		file_size = 1000
                scp_time_aryaka = scp_india_time_aryaka
		scp_time_mpls = scp_india_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_india_time_aryaka],"20":["SCP File Transfer over over Aryaka \n without optimziation (in seconds)",scp_india_time_mpls]}, tablefmt="grid"))
		scp_again()
	else:
        	os.system('clear')
        	print "Wrong Input! Please try again"
		India_File_scp_Transfer()



def http_again():
		http_again_banner =  "\n \n \n \n \nDo you want to perform the file transfer test again\n1. ARR and Compression \n2. SCP \n3. NO"
                http_again_banner_display = terminal_banner.Banner(http_again_banner)
		print(http_again_banner_display)
		again = input()
                if again==1:
			http_mail()
                        http()
                elif again==2:
			http_mail()
                        scp()
                else:
			http_mail()
                        os.system("figlet HAVE A NICE DAY")
			os.system("figlet SEE YOU SOON")
                        exit

		


def scp_again():
		scp_again_banner = "\n \n \n \n \nDo you want to perform the use case tests again\n1. ARR and Compression \n2. SCP \n3. NO"
		scp_again_banner_display = terminal_banner.Banner(scp_again_banner)
		print(scp_again_banner_display)
                again = input()
                if again==1:
			scp_mail()
                        http()
                elif again==2:
			scp_mail()
                        scp()
		else:
			scp_mail()
			os.system('figlet HAVE A NICE DAY')
			os.system('figlet SEE YOU SOON')
			exit



def USA_File_scp_transfer():
        scp_file_size_banner =  "Which file do you want to transfer from USA \n 1. 10MB(Aryaka- with and without Optimization) \n 2. 50MB(Aryaka- with and without Optimization) \n 3. 100MB(Aryaka- with and without Optimization) \n 4. 500MB(Aryaka- with and without optimization)\n 5. 1000MB(Aryaka- with and without Optimization)"
	USA_scp_banner = terminal_banner.Banner(scp_file_size_banner)
	print(USA_scp_banner)
	print "\n \n \nPlease type your input below(number)"
        file_size_input = input()

        if file_size_input == 1:
		os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@192.168.18.1:/root/tme/type_of_files/10MB .")
                end = int(time.time())
                scp_usa_time_aryaka = end - start
		os.system('clear')
		print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_aryaka)
		os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
		time.sleep(2)
		start = int(time.time())
		os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@192.168.18.1:/root/tme/type_of_files/10MB .")
		end = int(time.time())
		scp_usa_time_mpls = end - start
		os.system('clear')
		print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_mpls)
		time.sleep(2)
                os.system('clear')
		file_size = 10
                scp_time_aryaka = scp_usa_time_aryaka
		scp_time_mpls = scp_usa_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_usa_time_aryaka],"20": ["SCP File transfer over Aryaka \n without optimization (in seconds)",scp_usa_time_mpls]}, tablefmt="grid"))
		scp_again()
	elif file_size_input == 2:
                os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
                time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@192.168.18.1:/root/tme/type_of_files/50MB .")
                end = int(time.time())
                scp_usa_time_aryaka = end - start
                os.system('clear')
                print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_aryaka)
                os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
                time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@192.168.18.1:/root/tme/type_of_files/50MB .")
                end = int(time.time())
                scp_usa_time_mpls = end - start
                os.system('clear')
                print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_mpls)
                time.sleep(2)
                os.system('clear')
                file_size = 50
                scp_time_aryaka = scp_usa_time_aryaka
                scp_time_mpls = scp_usa_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_usa_time_aryaka],"20": ["SCP File transfer over Aryaka \n without optimization (in seconds)",scp_usa_time_mpls]}, tablefmt="grid"))
                scp_again()
        elif file_size_input == 3:
		os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@192.168.18.1:/root/tme/type_of_files/100MB .")
                end = int(time.time())
                scp_usa_time_aryaka = end - start
		os.system('clear')
                print("Over Aryaka with optimziationFILE TRANSFER took %i seconds \n" % scp_usa_time_aryaka)
                os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
		time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@192.168.18.1:/root/tme/type_of_files/100MB .")
                end = int(time.time())
                scp_usa_time_mpls = end - start
		os.system('clear')
                print("Over Aryaka without OptimizationFILE TRANSFER took %i seconds \n" % scp_usa_time_mpls)
                time.sleep(2)
		os.system('clear')
		file_size = 100
                scp_time_aryaka = scp_usa_time_aryaka
		scp_time_mpls = scp_usa_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_usa_time_aryaka],"20": ["SCP File transfer over Aryaka \n without optimization (in seconds)",scp_usa_time_mpls]}, tablefmt="grid"))
		scp_again()
	elif file_size_input == 4:
                os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
                time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@192.168.18.1:/root/tme/type_of_files/500MB .")
                end = int(time.time())
                scp_usa_time_aryaka = end - start
                os.system('clear')
                print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_aryaka)
                os.system('figlet OVER ARYAKA WITHOUT OPTIMIZATION')
                time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@192.168.18.1:/root/tme/type_of_files/500MB .")
                end = int(time.time())
                scp_usa_time_mpls = end - start
                os.system('clear')
                print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_mpls)
                time.sleep(2)
                os.system('clear')
                file_size = 500
                scp_time_aryaka = scp_usa_time_aryaka
                scp_time_mpls = scp_usa_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_usa_time_aryaka],"20": ["SCP File transfer over Aryaka \n without optimization (in seconds)",scp_usa_time_mpls]}, tablefmt="grid"))
                scp_again()
	elif file_size_input == 5:
                os.system('figlet OVER ARYAKA WITH OPTIMIZATION')
		time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -vvv -r SE@192.168.18.1:/root/tme/type_of_files/1000MB .")
                end = int(time.time())
                scp_usa_time_aryaka = end - start
		os.system('clear')
                print("Over Aryaka with optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_aryaka)
                os.system('figlet Over ARYAKA WITHOUT OPTIMIZATION')
		time.sleep(2)
                start = int(time.time())
                os.system("sshpass -p 'Aryak@123' scp -P 50000 -vvv -r SE@192.168.18.1:/root/tme/type_of_files/1000MB .")
                end = int(time.time())
                scp_usa_time_mpls = end - start
		os.system('clear')
                print("Over Aryaka without optimization FILE TRANSFER took %i seconds \n" % scp_usa_time_mpls)
                time.sleep(2)
                os.system('clear')
                file_size = 1000
                scp_time_aryaka = scp_usa_time_aryaka
                scp_time_mpls = scp_usa_time_mpls
                write_scp_inputs(file_size,scp_time_aryaka,scp_time_mpls)
                print (tabulate({"10": ["SCP File transfer over Aryaka \n with optimization (in seconds)",scp_usa_time_aryaka],"20":["SCP File transfer over Aryaka \n without optimization (in seconds)",scp_usa_time_mpls]}, tablefmt="grid"))
                scp_again()      
	else:
                os.system('clear')
                print "Wrong Input! Please try again"
                USA_File_scp_transfer()




def http():
	os.system('clear')
	aryaka()
	http_intro = "Hello! Welcome to the ARR and Compression Use Case \nWhere would you like to test the ARR and Compression Use Case \n1. India \n2. USA \n\033[1m ARR and Compression use case can be used to compare between Aryaka and Internet\033[0m"
	http_intro_banner = terminal_banner.Banner(http_intro)
	print(http_intro_banner)
	print "\n \n \nPlease type your input below(number)"		
	site_http_input = input()

	if site_http_input == 1:
		India_response = os.system('ping 10.0.20.13 -c 3')
		if India_response == 0:
            		os.system('clear')
	    		aryaka()
            		print "India Servers are up! You can start the ARR and Compression use case"
            		India_File_http_Transfer() #perform the wget Transfer
		else:
			os.system('clear')
			aryaka()
			print "India Servers are down! Please try with USA server"
			wget() # go back to the wget function
	elif site_http_input == 2:
		USA_response = os.system('ping 192.168.18.1 -c 3')
		if USA_response == 0:
			os.system('clear')
			aryaka()
			print "USA Server is up! You can start the ARR and Compression use case"
			USA_File_http_transfer()
		else:
			os.system('clear')
			aryaka()
			print "USA server is down! Please try with India Server"
			http()
	else:
		os.system('clear')
		aryaka()
		print "Wrong Input! Please try again"
		http()

def scp():
	os.system('clear')
	aryaka()
	scp_intro =  "Hello! Welcome to the SCP File transfer test \nWhere would you like to have the SCP File Transfer test \n1. India \n2. USA \n\033[1m SCP File transfer test can be used to compare between Aryaka- with and without optimization\033[0m"
	scp_intro_banner = terminal_banner.Banner(scp_intro)
	print(scp_intro_banner)
	print "\n \n \nPlease type your input below(number)"
	site_scp_input = input()

	if site_scp_input == 1:
		India_response = os.system('ping 10.0.20.13 -c 3')
		if India_response == 0:
			os.system('clear')
			aryaka()
			print "India Server is up! You can start the SCP file transfer test"
			India_File_scp_Transfer() #perform the wget Transfer
		else:
			os.system('clear')
			aryaka()
			print "India Server is down! Please try with USA server"
			scp() # go back to the wget function
	elif site_scp_input == 2:
		USA_response = os.system('ping 192.168.18.1 -c 3')
		if USA_response == 0:
			os.system('clear')
			aryaka()
			print "USA Server is up! You can start the SCP file transfer test"
			USA_File_scp_transfer()
		else:
			os.system('clear')
			aryaka()
			print "USA server is down! Please try with the India Server"
			scp()
	else:
		os.system('clear')
		aryaka()
		print "Wrong Input! Please try again"
		scp()


def type_of_test():
	os.system('clear')
	os.system("figlet -w 150 Welcome to")
	aryaka()
	intro = "What type of test do you want to do? \n1: ARR and Compression:This use case uses HTTP(WGET), is a computer program that retrieves content from a web server over the port 80 \n                       Since it is not secure protocol, ANAP will be able to optimize the traffic by performing ARR \n2: SCP: SCP is a Secure Gateway Protocol is a means of securely transferrring file over the port 22 \n        Since it is a secure protocol, ANAP will not be able to optimize the traffic and no ARR\n\033[1m SCP File transfer test can be used to compare between Aryaka- with and without optimization\033[0m\n\033[1m HTTP File transfer test can be used to compare between Aryaka and Internet\033[0m"
	intro_banner = terminal_banner.Banner(intro)
	print(intro_banner)
	print "\n \n \nPlease type your input below(number)"
	type_of_test_input = input ()

	if type_of_test_input == 1:
		http()
	elif type_of_test_input ==2:
		scp()
	else:
		print "Wrong input"
		type_of_test()

def aryaka():
	os.system('figlet -w 150 ARYAKA NETWORKS')

def cold_transfer():
	os.system('figlet COLD TRANSFER')
	cold_transfer_def = "Cold transfer is the first time transfer of a file from one device to another. First time when a file gets transferred over the ANAP, ANAP builds the required signatures in its memory. \n \n \n \n \n"
	cold_transfer_def_banner = terminal_banner.Banner(cold_transfer_def)
	print(cold_transfer_def_banner)


def warm_transfer():
	os.system('figlet WARM TRANSFER')
	warm_transfer_def = "Warm transfer is the second /consecutive time transfer of the file from one device to another. Now the file would be served from the local ANAP rather than fetching from the remote site. \n \n \n \n"
	warm_transfer_def_banner = terminal_banner.Banner(warm_transfer_def)
	print(warm_transfer_def_banner)


#main function
if __name__ == "__main__":
	type_of_test()

