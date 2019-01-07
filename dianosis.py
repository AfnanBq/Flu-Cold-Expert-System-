from pyknow import *# import pyknow library from python

#Expert System part (ES)
class FluorCold(Fact): #fact class craetion
    """ Info about the Flu and cold symptoms"""
    pass
#create knowldge engine class, this class works as a workplace for ES
#includes all the rules, facts, and methods the basic components of ES
class Diagnosis(KnowledgeEngine):
     
    #@Rule contian the fact of fever inside it (LHS), so once the input is
    # one of these facts, the actions will be performed
    
    
    #First rule to check the fever symptoms for flu
    @Rule(FluorCold (symptom= L('moderate fever') | L('high fever') | L('high temperature') | L('high hyperthermia')
                     | L('moderate temperature')| L('moderate hyperthermia')| L('hyperthermia') | L('dry cough')
                     | L('runny nose') | L('moderate tiredness')| L('severe tiredness ') | L('moderate fatigue') | L('severe fatigue') | L('sneezing')
                     | L('moderate headache') | L('severe headache') | L('migraine') | L('moderate migraine')| L('severe migraine')
                     |L('fainting') | L('lightheadedness')| L('syncope')
                     | L('vomiting') | L('stomach upset')| L(' sickness') | L('low appetite')
                     | L('pain throat') | L('throat sore')))#LHS the facts
    def flu_symp(self):#RHS the actions 
        global fluCount# declare the counter as global to allow use it with this function 
        fluCount +=1 #increse the counter
          #Second rule to check the cold symptoms for cold
    @Rule(FluorCold (symptom= L('no fever') | L('mild fever') | L('mild pyrexia') | L('mucus producing cough ')|L('stuffy nose') | L('runny nose')
                     |L('mild tiredness') | L('mild exhaustion') | L('exhaustion')| L('sneezing') |L('mild headache') | L('mild head pain') 
                     |L('head pain')|L('pain throat') | L('throat sore')|L('no fainting') | L('no lightheadedness')| L('no syncope')
                     |L('no vomiting') | L('no stomach upset')| L('no sickness') | L('no low appetite')))
    def cold_symp(self):
        global coldCount
        coldCount +=1
   
        #the beginning of the main part
        #This part of program is like interactive part between the user and the program,
#
print("Dear friend,")
print("This is Dr.Fnn system to diagnosis  respiratory illnesses, hope this is help you")
print("We hope you follow the instructions to get accurate diagnosis")
print("1- You have to enter at leas 3 symptoms.")
print("2- Once you finish, you have to enter exit to see your result.")
print("****************************************************************")
fluCount = 0 # declare and assign the counter for flu
coldCount = 0# declare and assign the counter for cold
engine = Diagnosis()
count = 0 #counter to check the number of the entered symptoms
while(1):
    count +=1
    symptom = input()# get it input from the user
    if symptom == "exit":# once the user enter exit the program will close, and show the result
        break
    engine.reset() # Prepare the engine for the execution.
    engine.declare(FluorCold(symptom = symptom.strip().lower()))# 
    engine.run() # Run the engin
    
# check for the conditions to give the results 
if ((fluCount >= 3) and (fluCount > coldCount)):
  print("You have flu!")
  print("I hope you feel better soon,I wish you a speedy recovery.")
  print("May hope Allah blesses you, quickly")
  
elif ((coldCount >= 3) and (coldCount > fluCount)):
    print("You have cold!")
    print("I hope you feel better soon,I wish you a speedy recovery.")
    print("May Allah blesses you, quickly")
    
elif ((fluCount >= 3) and (coldCount >= 3) and (coldCount == fluCount)):
    print("Either flu or cold, if you want more accurate result enter another symptom!")
    
elif ((fluCount < 3) or (coldCount < 3)):
    print("You have to enter another symptom to get accurate result")
  

print("This program made with love, very warm regards xoxo <3")
    


