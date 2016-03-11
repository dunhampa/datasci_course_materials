import sys
import json
from json import JSONDecoder
import pprint
import fileinput

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #print(loads_invalid_obj_list(sys.argv[2]))
   
    #comeonnow(sys.argv[2])
   
    sent_score=0    

    for each_line in fileinput.input(sys.argv[2]):
      myobj=(json.loads(each_line))
      
      #if 'text' in myobj:
        #tweet=(myobj['text'])
       # words=tweet.split()
      #  sent_score=0
       
        #for each_word in words: 
        #  sent_score= get_sent_score(each_word)+sent_scoren
       # print sent_score 

      
      if 'user' in myobj:
         if 'location' in myobj['user']:
            foundlocation= myobj['user']['location']
            if foundlocation is not None:
               print foundlocation
                  #if 'location' in what:
                  #toprint=what['location']
                  #print(toprint)
                  #print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            #print((myobj['coordinates'])['coordinates'])
      #   else:
            #print ("user but no job")
      #else:
       # print("no user")

  
    #  else:
       # sent_score=0
     # print sent_score
      

     

def locationtokeep():

      myobj=(json.loads(each_line))
      if 'user' in myobj:
       # print("true")
       print(myobj['user']['location'])
      else:
        print("false")



def get_sent_score(word):
  # afinnfile = open("AFINN-111.txt")
   afinnfile=open(sys.argv[1])
   scores = {} # initialize an empty dictionary

   for line in afinnfile:
     term, score  = line.split("\t")
     # The file is tab-delimited. "\t" means "tab character"
     scores[term] = int(score)  # Convert the score to an integer.
  
   if word in scores:
      score=scores[word]
   else:
      score=0

   return score



















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
