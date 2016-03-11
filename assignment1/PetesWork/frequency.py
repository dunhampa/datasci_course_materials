import sys
import json
from json import JSONDecoder
import pprint
import fileinput

class word_to_rate:

    def __init__(self):
       self.pos_sents=0
       self.neg_sents=0
       self.count=0

    def add_pos(self):
        self.pos_sents=self.pos_sents+1
    def add_neg(self):
        self.neg_sents=self.neg_sents+1
    def incr_cnt(self):
        self.count=self.count+1


def main():
    
    #file for arguments
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])#2

    affin_dict=return_AFFIN_dict()  
    #print affin_dict.keys()
    new_dict={}
    #for each tweet
    #print affin_dict.keys()   
    
   # if 'fuck' in affin_dict:
       #print "HERE"
    
    #break 
    for each_line in fileinput.input(sys.argv[1]):
     
      myobj=(json.loads(each_line))
      
      #the line is a tweet, so lets score it
      if 'text' in myobj:
         tweet=(myobj['text'])
         words=tweet.split()
         sent_score=0
       
        #looking at each word 
         for each_word in words: 
           
            if each_word in affin_dict:
               dummy=0 #if word is in AFFIN we don't do anythin
              # print "here:" + each_word
           
            else:
               if not each_word in new_dict:
                 #we need to add it to the dictionary
                 new_word=word_to_rate()
                 new_dict[each_word]=new_word
                 new_dict[each_word].incr_cnt()#count is one
               else:
                 #lets increment its occurence
                 new_dict[each_word].incr_cnt()
               for word in words:                  
                  if get_sent_score(word,affin_dict)>0:
                     new_dict[each_word].add_pos()
                  if get_sent_score(word,affin_dict)<0:
                     new_dict[each_word].add_neg()
                    
    for item in new_dict.keys():          
        if new_dict[item].pos_sents!=0 and new_dict[item].neg_sents!=0:
           floatrate=float(new_dict[item].pos_sents)/(new_dict[item].neg_sents)
           if floatrate < 0.25:
              rating=-4
           elif floatrate < 0.33:
              rate=-3
           elif floatrate < 0.5: 
              rate = -2
           elif floatrate <0.75:
              rate = -1
           elif floatrate <0.99:
              rate = 0
           elif floatrate  < 1.25:
              rate =1 
           elif floatrate < 1.33:
              rate =2
           elif floatrate < 1.5:
              rate =3 
           elif floatrate < 1.75:
              rate =4
           else:
             rate =5 
        else:
             rate=0 

        #This was for problem 3
        #print item + " "+ str(rate)
        
        print item + " " + str(float(new_dict[item].count)/(len(new_dict.keys())))
     
def return_AFFIN_dict():

  # afinnfile=open(sys.argv[1])
   scores = {} # initialize an empty dictionary

   #for line in afinnfile:
    # term, score  = line.split("\t")
     # The file is tab-delimited. "\t" means "tab character"
     #scores[term] = int(score)  # Convert the score to an integer.
   
   return scores #returning dictionary so we only get it once


def get_sent_score(word, scores):
  
   if word in scores:
      score=scores[word]
   else:
     score=0

   return float(score)


def check_if_AFFIN(word, scores):

   if word in scores:
      indict=True 
   else:
      indict=False

   return indict

















def comeonnow(filepass):
    s = open(filepass,'r').readline()
    # s=unicode_string.encode(s)
    myobj=(json.loads(s))
    print len(myobj)
   # print len(myobj(['user:'])
   # pprint.pprint(myobj['user'])
    pprint.pprint(myobj)
    

    s = open(filepass,'r').readline()
    # s=unicode_string.encode(s)
    myobj=(json.loads(s))
    print len(myobj)
    print len(myobj['user'])
   # pprint.pprint(myobj['user'])
    pprint.pprint(myobj)






def loads_invalid_obj_list(filepass):

    s = open(filepass, 'r').readline()
    #s=filepass.readline()
    # s=unicode_string.encode(s)
    decoder = JSONDecoder()
    s_len = len(s)
    print(len(s))
    objs = []
    end = 0
    while end != s_len:
        obj, end = decoder.raw_decode(s, idx=end)
        objs.append(obj)
        #print (decoder.raw_decode(s,indx=end))
    return objs
   
  











if __name__ == '__main__':
    main()
