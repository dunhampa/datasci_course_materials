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
         if 'coordinates' in myobj:
            what = myobj['coordinates']
            #print(what)
            if what is not None:
               if 'coordinates' in what:
                  toprint=what['coordinates']
                  print(toprint)
                  print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            #print((myobj['coordinates'])['coordinates'])
      #   else:
            #print ("user but no job")
      #else:
       # print("no user")

  
    #  else:
       # sent_score=0
     # print sent_score
      n = json.dumps(coord)  
      states = json.loads(n)     
      #states=(json.loads(o))

     # print states
      if 'state' in states:
         print(states['Alabama'])
     

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




coord={
    "states": {
        "state": {
            "point": [
                {
                    "_lat": "35.0041",
                    "_lng": "-88.1955"
                },
                {
                    "_lat": "34.9918",
                    "_lng": "-85.6068"
                },
                {
                    "_lat": "32.8404",
                    "_lng": "-85.1756"
                },
                {
                    "_lat": "32.2593",
                    "_lng": "-84.8927"
                },
                {
                    "_lat": "32.1535",
                    "_lng": "-85.0342"
                },
                {
                    "_lat": "31.7947",
                    "_lng": "-85.1358"
                },
                {
                    "_lat": "31.5200",
                    "_lng": "-85.0438"
                },
                {
                    "_lat": "31.3384",
                    "_lng": "-85.0836"
                },
                {
                    "_lat": "31.2093",
                    "_lng": "-85.1070"
                },
                {
                    "_lat": "31.0023",
                    "_lng": "-84.9944"
                },
                {
                    "_lat": "30.9953",
                    "_lng": "-87.6009"
                },
                {
                    "_lat": "30.9423",
                    "_lng": "-87.5926"
                },
                {
                    "_lat": "30.8539",
                    "_lng": "-87.6256"
                },
                {
                    "_lat": "30.6745",
                    "_lng": "-87.4072"
                },
                {
                    "_lat": "30.4404",
                    "_lng": "-87.3688"
                },
                {
                    "_lat": "30.1463",
                    "_lng": "-87.5240"
                },
                {
                    "_lat": "30.1546",
                    "_lng": "-88.3864"
                },
                {
                    "_lat": "31.8939",
                    "_lng": "-88.4743"
                },
                {
                    "_lat": "34.8938",
                    "_lng": "-88.1021"
                },
                {
                    "_lat": "34.9479",
                    "_lng": "-88.1721"
                },
                {
                    "_lat": "34.9107",
                    "_lng": "-88.1461"
                }
            ],
            "_name": "Alabama",
            "_colour": "#ff0000"
        }
    }
}
   
  

if __name__ == '__main__':
    main()
