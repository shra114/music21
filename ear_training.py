from music21_common import *
import random
import time

class EarTrainingGame():
    def __init__(self):
        self.stream1 = ["C","D","E"]
        self.randrange=[]
        self.errornotes=[]
    def add_stream(self, stream1):
        self.stream1 = stream1
    def test(self,number):
        print ("Welcome to the test")
        i = random.randrange(0,number)
        self.randrange.append(i)
        test_stream = [self.stream1[0] , self.stream1[i]]
        for k in range(2):
            play_stream(test_stream)
        if(str(i+1)== input("Enter 1 to "+str(number)+"\n").strip()):
            print ("\n\nGood", test_stream)
            return True
        else:
            print ("\n\nLost", test_stream)
            self.errornotes.append(i)
            return False
    def run_test(self, num_notes=3, runs=2):
        points = 0
        for i in range(runs):
            points += int(self.test(num_notes))
        print ("Score:",str(points)+"/"+str(runs))
        print ("Error notes to practise more", self.errornotes)
        return points

e0  = EarTrainingGame()
e0.stream1 = ["C","D","E","F","G","A","B"]
#e0.stream1 = ["C3","D3","E3","F3","G3","A3","B3"]
e0.run_test(num_notes=3, runs=20)
