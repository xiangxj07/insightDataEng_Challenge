#This is the function library for antifraud.py

#Author: Xinjiang Xiang
#Email: xiangxj07@gmail.com
#Last update: 11/8/2016

#Change log:

#Libraries go here
import numpy as np
import copy
import warnings
from sets import Set
from collections import deque

def loadTrans(fname, usecols=None, dtype=None):
	"""
	Load the transaction files, the format is fixed
	-------------
	Parameters:
	fname: string, indicating the path to the file, 
		note the first line is always skiped.
	usecols: number tuple or list, the columns of data to be used
	out: a matrix containing history of every transaction, each entry is a string
	"""
	if usecols is not None:
		usecols = list(usecols)
	#read lines in fname
	fid = open(fname, 'r')
	row = 0
	out = []
	print 'Loading data files...'
	for line in fid:
		row += 1
		if row != 1:
			line = line.split(', ', 4)
			#use specified columns
			if usecols:
				col = []
				for i in usecols:
					col.append(line[i])
				line = col
			#convert to int if needed
			if dtype == 'int':
				line = map(int, line)
			out.append(line)
	print 'File loading done...'
	fid.close()
	return out

def constructNet(M):
	"""
	Construct the network based on current batch file, using hash table
	---------------
	Parameter:
	M: the matrix containing all transaction pairs that has happened
	dict: a hash table recording all users, and everyone who has direct transaction with 
		a pecific person, like a tree nodes and connections
	"""
	if M == []:
		warnings.warn('The input matrix is empty !')
	dict = {}
	print 'Constructing the network...'
	for pair in M:
		dict = updateNet(pair, dict)
	print 'Network construction done...'
	return dict

def fraudDetect(pair, dict, degree=1):
	"""
	Search the network using Bi-Directional BFS to check whether 
	two users are within the specified friend network.
	---------------
	Parameter:
	pair: the pair of user IDs to be queried for transaction
	dict: current hash table with the transaction record between two users
	degree: the degree of friend network, by defaul is 1
	out: either "trusted" or "unverified"
	"""
	root1 = [pair[0]]
	root2 = [pair[1]]
	visited1 = Set([pair[0]])
	visited2 = Set([pair[1]])
	#transaction between the same person is trusted
	if root1 == root2:
		return 'trusted'
	#if a person is new, return untrusted
	if (not dict.has_key(pair[0])) or (not dict.has_key(pair[1])):
		return 'unverified'
	#check the net for two different persons using Bi-Directional BFS
	while degree >= 1:
		#Check the descendent of root1
		newRoot1 = []
		for root in root1:
			queue = deque(dict[root])
			while queue:
				node = queue.pop()
				#if the node is in the desendent of the other root, return yes
				if node in visited2:
					return 'trusted'
				else:
					if node not in visited1:
						#add new node to set
						visited1.add(node)
						#also add it to the root list to be checked in next step
						newRoot1.append(node)
		degree -= 1
		if degree <= 0: 
			return 'unverified'
		root1 = newRoot1
		
		#Check the descendent of root2
		newRoot2 = []
		for root in root2:
			queue = deque(dict[root])
			while queue:
				node = queue.pop()
				#if the node is in the desendent of the other root, return yes
				if node in visited1:
					return 'trusted'
				else:
					if node not in visited2:
						#add new node to set
						visited2.add(node)
						#also add it to the root list to be checked in next step
						newRoot2.append(node)
		degree -= 1
		if degree <= 0: 
			return 'unverified'
		root2 = newRoot2	

def updateNet(pair, dict):
	'''
	Add the current pair to the network, if they don't exist
	---------------
	Parameter:
	pair: the pair of user IDs that did the transaction
	dict: current hash table with the transaction record between two users
	out: the updated netw
	'''
	user1 = pair[0]
	user2 = pair[1]
	#add user2 to user1's connection
	if not dict.has_key(user1):
		dict[user1] = [user2]
	else:
		if user2 not in dict[user1]:
			dict[user1].append(user2)
	#add user1 to user2's connection
	if not dict.has_key(user2):
		dict[user2] = [user1]
	else:
		if user1 not in dict[user2]:
			dict[user2].append(user1)
	return dict