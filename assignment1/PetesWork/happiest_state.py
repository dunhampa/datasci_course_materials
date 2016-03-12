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

#Using a static dict so no external resources are needed    
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


def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    state_dict={}
   
    sent_score=0 
    
    scores=init_sent_dict(sent_file)   

    for each_line in tweet_file:#fileinput.input(sys.argv[2]):
      
      myobj=(json.loads(each_line))
      
      scorefound=0 #this is a conditional within loop, to iterate through each state
      
      #Nested if statements first determine if tweet has the data neededed
      if 'user' in myobj and 'text' in myobj:
         if 'location' in myobj['user']:
            foundlocation= myobj['user']['location']
            if foundlocation is not None:
                
               #For each state pull the value and add boundaries for regex
               for STabr, state in abbrev.iteritems():#"STabr" is the key, state is the value
                    STabrB="\\b"+STabr+"\\b" #adding \b on each side, for regex this is a boundary (whole words only)
                    state="\\b"+state+"\\b"
                    
                    #Checks if state abbreviation or state full word is in the location of tweets
                    if re.search(STabrB,foundlocation) or re.search(state,foundlocation):
                       
                       if scorefound==0: #this bypasses loop, to exit once state if found (score calculated once if more than one state location)
                          tweet=(myobj['text'])
                          words=tweet.split()
                          sent_score=0
       
                          for each_word in words: 
                             sent_score= get_sent_score(each_word,scores)+sent_score
                          scorefound=1 
                       update_state(STabr, state_dict, sent_score)       
    
    
    maximum=0.0001
    maxAbr=""                                          
    for key,state in state_dict.iteritems():  
       state.ave()
       
       #debug print only
       state_print_debug(key,state)
       
       aveHaps=float(state.sum)/float(state.count)
       
       if aveHaps>maximum:
           maximum=aveHaps
           maxAbr=key
                                                   
    print maxAbr#Print the happiest state abbreviation
    


# Updates state dictionary
# If state does not exist as a key, key is created
# Then score is added key and count is incremented

def update_state(stateAbbrev, state_dict, score):
                           
   if not stateAbbrev in state_dict:
      #we need to add it to the dictionary
      state_obj=stateRate()
      state_dict[stateAbbrev]=state_obj
  
   state_dict[stateAbbrev].incre()
   state_dict[stateAbbrev].add(score)

               

# Returns sentiment score for word

def get_sent_score(word,scores):
  
   if word in scores:
      score=scores[word]
   else:
      score=0

   return score

#Returns a dictionary from the sentiment file

def init_sent_dict(sent_file):
   
   #afinnfile=open(sys.argv[1])
   scores = {} # initialize an empty dictionary

   for line in sent_file:#afinnfile:
     term, score  = line.split("\t")
     scores[term] = int(score)  

   return scores

#print statement used for debugging
def state_print_debug(key, state):
    print "AVERAGES:"
    print "----"
    print key
    print state.count
    print state.sum
    print state.aveHap
    print "----"













   
  











if __name__ == '__main__':
    main()
