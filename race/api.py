from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
import swat
import socket

app = Flask(__name__)


@app.route("/simulate")
def home():

	sim_filname = 'sample_transactions.xlsx'
	final_path = os.path.join(curr_dir,sim_filname)
	print(final_path)

	results = conn.table.tableExists(caslib='PUBLIC',name=orig_tablename)

	if results.exists:
		print('True\n')
		conn.table.dropTable(caslib='PUBLIC',name=orig_tablename)
		print('Table ' + orig_tablename + 'already exists. Dropping ...\n')

	conn.upload(final_path,casout=dict(name = orig_tablename,promote=True,caslib='PUBLIC'))
	print("Successfully uploaded " + sim_filname)

	os.system("mv /home/sasdemo/Nikhil/new_user_transactions_original.csv /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv.tmp")
	os.system("mv /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv /home/sasdemo/Nikhil/new_user_transactions_original.csv")
	os.system("mv /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv.tmp /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv")

	print('\n-------File Moved--------\n')

	return "Transaction Simulation Complete"


@app.route("/original")
def original():

	orig_filname = 'original_custid.xlsx'
	final_path = os.path.join(curr_dir,orig_filname)
	print(final_path)

	results = conn.table.tableExists(caslib='PUBLIC',name=orig_tablename)

	if results.exists:
		print('True\n')
		conn.table.dropTable(caslib='PUBLIC',name=orig_tablename)
		print('Table ' + orig_tablename + 'already exists. Dropping ...\n')

	conn.upload(final_path,casout=dict(name = orig_tablename,promote=True,caslib='PUBLIC'))
	print("Successfully uploaded " + orig_filname)

	os.system("mv /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv /home/sasdemo/Nikhil/new_user_transactions_original.csv.tmp")
	os.system("mv /home/sasdemo/Nikhil/new_user_transactions_original.csv /home/sasdemo/Nikhil/simulation/new_user_transactions_original.csv")
	os.system("mv /home/sasdemo/Nikhil/new_user_transactions_original.csv.tmp /home/sasdemo/Nikhil/new_user_transactions_original.csv")


	print('\n-------File Moved Back to Original State--------\n')

	return "Back to Original State"


if __name__ == '__main__':
    #conn = swat.CAS('localhost', 5570, 'sasdemo', 'Orion123')
    #conn.session.timeout(time=9999999999)

	ip_addr = socket.gethostbyname(socket.gethostname())

	conn = swat.CAS(ip_addr,5570,'sasdemo','Orion123')
	print(conn)
	curr_dir = os.getcwd()
	print(curr_dir)

	# sim_filname = 'sample_transactions.xlsx'
	# final_path = os.path.join(curr_dir,sim_filname)
	# print(final_path)
	orig_tablename = 'TRANSACTIONS_CUSTID'

	app.run(debug=True, host=ip_addr, port='5001',ssl_context='adhoc')