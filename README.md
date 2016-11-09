# insightDataEng_Challenge
Coding Challenge by Insight Data Engineering Group

This anti-fraud program checks the relation between two users, based on the degree of friendship specified by user. If the relation is outside the degree range, the program will report unverified transaction. 

Note: the query comes in sequentially, every processed query will then be regarded as valid transaction regardless of being either trusted or not, and then added to the knowledge base for future queries. 

To run the program in Linux environment under bash shell:
0. Download the paymo_input files (.csv files) from the website address provided, put them in paymo_input folder
1. Change directory to [path into folder 'digital-wallet-master'] (make sure run.sh is inside current path after cd command)
2. Run the code using: bash run.sh
3. To check the pre-run outputs, download them from the website adress provided in paymo_output folder.

Orgnization of major files:
|- run.sh
|- src
|	|- antifraud.py
|	|- digitalWallet.py
|	|- digitalWallet.pyc
|	|- ReadMe.txt
|- paymo_input
|	|- batch_payment.txt
|	|- stream_payment.txt
|- paymo_output
	|- output1.txt
	|- output2.txt
	|- output3.txt

Contents and format of major files:
1. antifraud.py: 
	main function to drive the fraud detection and result writing
2. digitalWallet.py: 
	modulized functions implementing different parts of the main function
3. batch_payment.txt: 
	transaction history between users, used to construct the original knowledge base
	format: time tag (string), user id 1 (number), user id 2 (number), amount (float, 2 digits), message (string)\n 
4. stream_payment.txt: 
	transactions waiting to be checked, assuming the request comes in sequentially, and processed query will be added to current knowledge base
	format: time tag (string), user id 1 (number), user id 2 (number), amount (float, 2 digits), message (string)\n 
5. output1.txt: 
	output prediction with friendship degree 1, either trusted, or unverified
6. output2.txt: 
	output prediction with friendship degree 2, either trusted, or unverified
7. output3.txt: 
	output prediction with friendship degree 4, either trusted, or unverified

Note: to change the degree of friendship, in this version one can modify parameter "degrees" in antifraud.py
