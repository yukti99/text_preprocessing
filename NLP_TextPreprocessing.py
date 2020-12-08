# -*- coding: utf-8 -*-
"""
@author: yukti
"""

import nltk
import re
import string 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Uncomment these lines if nltk not installed already 
# nltk.download()
# nltk.download('punkt')


# TEXT PREPROCESSING 

class NLP_Preprocess_Text:
    def __init__(self):
        pass
    
    def convert_lower(self,text):
         return text.lower()
    
    def remove_numbers(self,text):
        return "".join(ch for ch in text if not ch.isdigit())
    
    def spell_corrector(self,text):
        for i in range(len(text)):
            sp = TextBlob(text[i])
            text[i] = str(sp.correct())
        return text
            
            
    def remove_punctuations(self,text):
        return "".join([ch for ch in text if ch not in string.punctuation])
    
    def remove_tags(self,text):
        text = re.sub('<[^<]+?>', '', text)
        return text
            
    
    def remove_extra_spaces(self,text):
        text = re.sub(' +|\\n+', ' ', text)
        return text
    
    def Tokenize_text(self,text):
        tokenized_text = nltk.word_tokenize(text)
        return tokenized_text
    
    def get_vocab_size(self,text):    
        v = []
        for i in text:
            if i not in v:
                v.append(i)
        # v has all unique words now
        return str(len(v))
    
    def highest_freq_words(self,freq_file,text):       
        df = {}
        for i in text:
            if i not in df:
                df[i] = 1
            else:
                df[i] = df[i]+1
                
        sorted_freq = sorted(df.items(), key = lambda x:(x[1]),reverse = True)
        num = min(50, len(sorted_freq))
        for i in range(num):
            s = " ("+str(i+1)+") "+str(sorted_freq[i][0])+": "+str(sorted_freq[i][1])+"\n"
            freq_file.write(s)
        freq_file.write("\n")
        
    def remove_stop_words(self,text):
        StopWords = stopwords.words('english')
        l=[]
        for i in text:
            if i not in StopWords:
                l.append(i)
        return l
    
    def Stem_words(self,words):
        stemmer = PorterStemmer()
        Stemmed_words = [stemmer.stem(w) for w in words]
        return " ".join(Stemmed_words)
    
    def Lemmatize_words(self,words):
        lemmatizer = WordNetLemmatizer()
        l_words = [lemmatizer.lemmatize(w) for w in words]
        return " ".join(l_words)
        
    def Preprocess_Text(self,text):
        print("Processing data...")
        output_file = open("Output_TextProcessing.txt","w+") 
        
        # Normalization of Text
        text = self.convert_lower(text)
        text = self.remove_numbers(text)
        text = self.remove_punctuations(text)   
        text = self.remove_tags(text)
        text = self.remove_extra_spaces(text) 
        # now we have cleaned our text
        output_file.write("\nAfter Text Cleaning, noise removal and spell correction : \n"+text) 
        
        # Tokenization    
        text = self.Tokenize_text(text)
        
        # Correcting misspelled words
        text = self.spell_corrector(text)
    
        output_file.write("\n\nAfter Tokenization and Normalization : \n"+str(text))
        print("Data Normalization and Tokenization done...")
        # Calculating total and Unique words in text
        output_file.write("\n\nTotal words in text = "+str(len(text)))    
        output_file.write("\n\nVocabulary Size (Unique words) = "+ self.get_vocab_size(text))
        output_file.write("\n\nThe most frequent 50 words with their frequency are - \n")
        
        # Finding the Highest Frequency words
        self.highest_freq_words(output_file,text)
        
        # Removing stop words
        text = self.remove_stop_words(text)    
        output_file.write("\n\nAfter removing Stop Words : \n"+str(text))
        
        # Finding the Highest Frequency words after removing stop words
        output_file.write("\n\nFrequency After Removing Stop words: \n")
        self.highest_freq_words(output_file,text)
        
        # Stemming 
        output_file.write("\n\nAfter Stemming: \n")
        stemmed_text = self.Stem_words(text)
        output_file.write(stemmed_text)
        print("Text stemming done...")
        
        # Lemmatization
        output_file.write("\n\nAfter Lemmatization: \n")
        lem_text = self.Lemmatize_words(text)
        output_file.write(lem_text)
        print("Text Lemmatization done...")
        
        # Output message for user!
        print("Please check \"Output_TextProcessing.txt\" file for Results!!")
       
      
   





