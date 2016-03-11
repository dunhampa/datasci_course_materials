import sys
import json
from json import JSONDecoder
import pprint
import fileinput
import re

class stateRate:

    def __init__(self):
       self.aveHap=0.00
       self.sum=0
       self.count=0

    def add(self,score):
        self.sum=self.sum+score
    def incre(self):
        self.count=self.count+1
    def ave(self):
        self.aveHap=float(self.sum)/float(self.count)






def hw():
    print 'Hello, world!'
    
abbrev = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])#open("/Volumes/SDCX/Dropbox/102_COURSERA MOOC/05_Data Science At Scale/Assign1Mac/AFINN-111.txt")#
    tweet_file = open(sys.argv[2])#("/Volumes/SDCX/Dropbox/102_COURSERA MOOC/05_Data Science At Scale/Assign1Mac/output.txt")#open
    
    state_dict={}
   
    sent_score=0    

    for each_line in fileinput.input(sys.argv[2]):#"/Volumes/SDCX/Dropbox/102_COURSERA MOOC/05_Data Science At Scale/Assign1Mac/output.txt"):
      myobj=(json.loads(each_line))
      
      scorefound=0
      if 'user' in myobj and 'text' in myobj:
         if 'location' in myobj['user']:
            foundlocation= myobj['user']['location']
            if foundlocation is not None:
               for STabr, state in abbrev.iteritems():
                    STabrB="\\b"+STabr+"\\b"
                    state="\\b"+state+"\\b"
                    if re.search(STabrB,foundlocation) or re.search(state,foundlocation):
                       #print STabr
                       if scorefound==0:
                          tweet=(myobj['text'])
                          words=tweet.split()
                          sent_score=0
       
                          for each_word in words: 
                             sent_score= get_sent_score(each_word)+sent_score
                          scorefound=1 
                       update_state(STabr, state_dict, sent_score)       
    maximum=0.0001
    maxAbr=""                                          
    for key,state in state_dict.iteritems():  
       state.ave()
       #print "AVERAGES:"
       #print "----"
       #print key
       #print state.count
       #print state.sum
       #print state.aveHap
       #print "----"
       aveHaps=float(state.sum)/float(state.count)
       if aveHaps>maximum:
           #print key
           #print aveHaps
           maximum=aveHaps
           maxAbr=key
    #print "MAX:"                                                
    print maxAbr
    #print maximum

def update_state(stateAbbrev, state_dict, score):
                           
   if not stateAbbrev in state_dict:
      #we need to add it to the dictionary
      state_obj=stateRate()
      state_dict[stateAbbrev]=state_obj
  
   state_dict[stateAbbrev].incre()#count is one
   state_dict[stateAbbrev].add(score)
   #print stateAbbrev 
   #print state_dict[stateAbbrev].sum
               
     





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
