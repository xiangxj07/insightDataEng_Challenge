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
from digitalWallet import loadTrans, constructNet, fraudDetect, updateNet, processQuery

#Load file names
batchFile = sys.argv[1]
streamFile = sys.argv[2]
outFiles = sys.argv[3:]

#Load input files
batch = loadTrans(batchFile, usecols=[1, 2], dtype='int')
stream = loadTrans(streamFile, usecols=[1,2], dtype='int')

#Construct network with batch inputs
net = constructNet(batch)

#Process the stream file for fraud detection
degrees = [1,2,4]
net = processQuery(stream, net, degrees, outFiles)