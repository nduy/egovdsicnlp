# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 07:42:14 2023

@author: duynd
"""
import nltk;
import re;
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

stop_words = stop_words.union(set(stopwords.words('spanish')));
#stop_words = stop_words.union(set(stopwords.words('french')));
#stop_words = stop_words.union(set(stopwords.words('portuguese')));
stop_words = stop_words.union(set(stopwords.words('italian')));
#stop_words = stop_words.union(set(stopwords.words('swedish')));
#stop_words = stop_words.union(set(stopwords.words('slovene')));
#stop_words = stop_words.union(set(stopwords.words('greek')));
#stop_words = stop_words.union(set(stopwords.words('danish')));
stop_words = stop_words.union(set(stopwords.words('dutch')));
#stop_words = stop_words.union(set(stopwords.words('finnish')));
#stop_words = stop_words.union(set(stopwords.words('german')));

def demoiseText(txt):
    """
    

    Parameters
    ----------
    txt : String
        Text string to denoise.
    Method:
        1.remove all special characters
        2. Remove escape characters
    Returns
    -------
    the denoised version of txt.

    """
    cleaned_txt=txt
    cleaned_txt= re.sub('[^a-zA-Z0-9 \n\.]', '', txt);
    
    return cleaned_txt;

    pass

def strictDemoiseText(txt):
    """
    

    Parameters
    ----------
    txt : String
        Text string to denoise.
    Method:
        1.remove all special characters
        2. Remove escape characters
    Returns
    -------
    the denoised version of txt.

    """
    cleaned_txt= txt
    cleaned_txt= re.sub('[^a-zA-Z0-9 \n\.]', ' ', txt);
    cleaned_txt= cleaned_txt.replace('.',' ',100)
    cleaned_txt= cleaned_txt.replace(',',' ',100)
    cleaned_txt= cleaned_txt.replace(';',' ',100)
    cleaned_txt= cleaned_txt.replace(';',' ',100)
    
    return cleaned_txt;
    pass

def Stricttext2lemmaList (txt):
    """
    Convert a text into a list of lemmas.

    Parameters
    ----------
    txt : String
        DESCRIPTION.

    Returns
    -------
    List of token (string type).

    """
    s= strictDemoiseText(txt);
    tokens= word_tokenize(s);
    lemmatizer = WordNetLemmatizer()
    rs=[];
    for t in tokens:
        if (len(t)>=1 and (not t.lower() in stop_words)):
            rs.append(lemmatizer.lemmatize(t));
    return rs
     