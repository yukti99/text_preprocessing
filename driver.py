# -*- coding: utf-8 -*-
"""
@author: yukti
"""
from NLP_TextPreprocessing import NLP_Preprocess_Text

doc1 = open("doc1.txt","r",encoding="utf8")
doc2 = open("doc2.txt","r",encoding="utf8")
doc3 = open("doc3.txt","r",encoding="utf8")
doc4 = open("doc4.txt","r",encoding="utf8")


data = doc1.read()+doc2.read()+doc3.read()+doc4.read()
text_processor = NLP_Preprocess_Text()
text_processor.Preprocess_Text(data)




