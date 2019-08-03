import math
import json 
import pandas as pd
import numpy as np
import unicodedata 
from flashtext import KeywordProcessor
import re

#loai bo json khong co entities
#get length of setence
#convert to list of index to seperate chunks
def getLstIdx(data):
	""" Return list of index to seperate chunking
	Agrs: data: [{json} {json} {json} {json}]
	Return: Lists of seperating index for each json
	Ex: [["so 15 pho Nui Truc Quan Ba Dinh thanh pho Ha Noi"]] -> [[0 1 4 8]]
	"""
	idx_lst = []

	for json_item in data:
		idx_item_set = {0}
		for item in json_item['entities']:
			idx_item_set.add(item['start'])
			idx_item_set.add(item['end'])
		idx_item_set.add(len(json_item['text']))
		
		_idx_lst= list(idx_item_set)

		idx_lst.append(sorted(_idx_lst))
		idx_item_set.clear()
		break
	return idx_lst


def normalizeText(sent):
	d = ",.!?/&-:;@'..."
	cleanString= re.sub("["+"\\".join(d)+"]", ' ' ,sent)

	return cleanString

def getSentence(data):
	sent_lst = []

	for json_item in data:
		sent_lst.append(json_item['text'])

	return sent_lst

def getChunkingWord(data):
	""" Return chunking of normalized sentence
	Agrs: Normalized sentence
	Ex: ["so 15 pho Nui Truc Quan Ba Dinh thanh pho Ha Noi" -> [[So] [15] [pho] [Nui Truc] [Quan] [Ba Dinh] [Thanh Pho] [Ha Noi]]
	Return: Lists of chunking word
	"""
	idx_lst = getChunkingWord(data)
	sent_lst = getSentence(data)
	# for sent_lst

def getChunkingTag(list_tag):
	""" Return tag of each chunking of sentence
	Agrs: Chunking list, index of start-end 
	pass
	Ex: [[So] [15] [pho] [Nui Truc] [Quan] [Ba Dinh] [Thanh Pho] [Ha Noi]] ->  [[B_so_nha][I_so_nha][B_duong_pho][I_duong_pho][I_phuong_xa][B_phuong_xa][I_quan_huyen][B_quan_huyen][B_tinh_tp][I_tinh_tp]]
	Return: Lists of chunking word
	"""
	pass

def convertJson2Csv(filename):
	data = []
	with open(filename) as f:
		for line in f:
			json_item= json.loads(line)
			#if json_item['entities'] is not null 
			if json_item['entities']:
				data.append(json_item)
	return data


data = convertJson2Csv('address_tagger_1.0.0.json')
# lst_norm = normalizeText('40/31/30B Quang Trung -')
# print(lst_norm)
# data_idx= getLstIdx(data)
# print(data_idx)
sent_lst = getSentence(data)
print(sent_lst)