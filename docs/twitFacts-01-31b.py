#imports the p5 stuff
from p5 import *

#imports tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#imports for cgi requests and time management
import requests
import re
from time import sleep
import random

#this is for clearing the terminal window. 
import os
#this checks the operating system, to determine correct clear command.
os.system('cls' if os.name == 'nt' else 'clear')

#import twitter_credentials
#variables that contain twitter user credentials
ACCESS_TOKEN = "1197684969411403782-AiYbaHtpx4u6bq1lzWaRPUtAeTcd1e"
ACCESS_TOKEN_SECRET = "UO1J7bdmVdvdu1aWWBEFxg1S0s1CzpwcT9ZuOJ4GujPEq" 
CONSUMER_KEY = "SoHbJoMHWFIJLDwETFEnZ19oG"
CONSUMER_SECRET = "ZQOJSEtFmXrYQSWvqdo8w7bHHchZMN84pCybo8UAtA9ahN6Ngg" 
    
print("1" + '\n\n')    
    
class StdOutListener(StreamListener):
    
    print("2" + '\n\n') 
#    def on_data(self, data):
#        print(data)
#        return True
    
    def on_status(self, status):
        
#        if status.retweeted_status:
#            return

        #search for retweets and skip them with this:
        #if hasattr (status, 'retweeted_status'):
            #print("retweet skipped")
            #return
        
        #print(status.text)
        
#        if "capitalism" in status.text:
#            print("capitalism")
#            return
        print("3" + '\n\n') 
        #----------test sequences----------
        if "qazwsx" in status.text:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n' + "qazwsx:")
            print(status.text + '\n\n')
            #moveCamera(5)
            return
        
        if "In fact, " in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "qazedc:")
            print(status.text + '\n\n')
            #moveCamera(6)
            return
        #--------------------------------
        
        if "The fact is" in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "unrest:")
            print(status.text + '\n\n')
            #moveCamera(1)
            return
        
#        if "in fact" in status.text:
#            os.system('cls' if os.name == 'nt' else 'clear')
#            #print('\n' + "late capitalism:")
#            print(status.text + '\n\n')
#            #moveCamera(2)
#            return
        
        if "The fact of " in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "Ross and Rachel:")
            print(status.text + '\n\n')
            #moveCamera(4)
            return
        
        if "Fact: " in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "another planet:")
            print(status.text + '\n\n')
            
            return
        
        if "In fact," in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "Princess Diana:")
            print(status.text + '\n\n')
            #moveCamera(7)
            return

        if "A fact:" in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "economic anxiety:")
            print(status.text + '\n')
            #moveCamera(8)
            return
        
        if "it's a fact that" in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "security camera:")
            print(status.text + '\n')
            #moveCamera(9)
            return
        
        if "It's a fact" in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "billion dollars:")
            print(status.text + '\n\n')
            #moveCamera(10)
            return
        
        if "Its a fact" in status.text:
            #os.system('cls' if os.name == 'nt' else 'clear')
            #print('\n' + "internet of things:")
            print(status.text + '\n\n')
            #moveCamera(11)
            return        
        
        print("3b" + '\n\n') 
#    def on_error(self, status):
#        print(status)

    def on_error(self, status_code):
        print >> stderr, "Encountered an error with status code:"             
        sys.stderr.flush()
        # if the error for bad credentials, end stream
        if status_code == 401:
            return False
        # rate limit, close
        if status_code == 420:
            return False

    # When timed out
    def on_timeout(self):
        # Print timeout message
        print >> stderr, "Timeout..."
        # Wait 10 seconds
        time.sleep(60)    
        # Return nothing
        return
    print("4" + '\n\n') 
    
if __name__ == "__main__":
    print("5" + '\n\n') 
    listener = StdOutListener()
    #auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    #auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    print("5b" + '\n\n')
    stream = Stream(auth, listener)
    print("5c" + '\n\n')
    stream.filter(track=['qazwsx', 'In fact, ', 'The fact is', 'in fact', 'the fact of', 'fact:', 'Fact:', 'the fact is', "It's a fact", "it's a fact", 'Its a fact', 'its a fact'])
    
    print("5d" + '\n\n')
    

    
    