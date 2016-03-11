import sys 

def main():
   afinnfile = open("AFINN-111.txt")
   scores = {} # initialize an empty dictionary

   for line in afinnfile:
     term, score  = line.split("\t")  
     # The file is tab-delimited. "\t" means "tab character"
     scores[term] = int(score)  # Convert the score to an integer.

    # print scores.keys()#.items() # Print every (term, score) pair in the dictionary
  
#     print scores['reckless']

   
#print scores.keys()

   print scores[sys.argv[1]]

if __name__ == '__main__':
    main()
            
