#This program tries to identify possible fraud transactions
#between two users based on their network relation, using Bi-directional BFS search.
#For more details and explanations, check ReadMe.

#Author: Xinjiang Xiang
#Email: xiangxj07@gmail.com
#Last update: 11/8/2016

#Change log:

#Libraries go here
import numpy as np
import copy
import sys
from sets import Set
from digitalWallet import loadTrans, constructNet, fraudDetect, updateNet

#Load file names
batchFile = sys.argv[1]
streamFile = sys.argv[2]
outFile1 = sys.argv[3]
outFile2 = sys.argv[4]
outFile3 = sys.argv[5]

#Load input files
batch = loadTrans(batchFile, usecols=[1, 2], dtype='int')
stream = loadTrans(streamFile, usecols=[1,2], dtype='int')

#Construct network with batch inputs
net = constructNet(batch)

#Process the stream file for fraud detection
degrees = [1,2,4]
fid1 = open(outFile1,'w')
fid2 = open(outFile2,'w')
fid3 = open(outFile3,'w')
print 'Now checking the coming transactions and writing to output...'
count = 0
for pair in stream:
	count += 1
	#evaluate the fraud
	for i in range(0, len(degrees)):
		exec('result = fraudDetect(pair, net, degree=' + str(degrees[i]) + ')')
		result = result+'\n'
		exec('fid' + str(i+1) + '.write(result)')
	#add the current pair to the network if it was not there
	if count % 50000 == 0: print 'Update: ' + str(count) + ' entries processed...'
	net = updateNet(pair, net)
print 'Totaling: ' + str(count) + ' entries processed...'
fid1.close()
fid2.close()
fid3.close()
print 'Examination done.'