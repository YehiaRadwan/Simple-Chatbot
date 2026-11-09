import time

#variable to store time info
now = time.ctime()


#ChatBot intro
print("Hi i'm chatbot how can I help you")

#Q & A dictionary for chat
conversation={
  "hi":"Hello how can i help you",
  "how are you":"I'm fine how are you",
  "what is this website for":"It is just a chatbot website",
  "how were you made":"I was coded on replit.com",
  "who created you":"I was made by Yehia",
  "what do you like to be called":"You can call me chatter",
  "what is your purpose":"To talk to users like you",
  "do you know siri":"They were my rival in chatbot school",
  "are you a human":"No but I can still talk to you",
  "what is the time":"The time is: " + now,
}
#create function for chatbot
def chatbot():

  a = input()
  a = a.lower()
  x = a.split()
  if "table" in a or "multiple" in a:
    for y in range(len(x)):
     num = int(input("Enter the number: ")) 
     print("Multiplication Table of", num) 
     for i in range(1, 11):
      print(num,"X",i,"=",num * i)
    chatbot()

  elif "sum" in a or "addition" in a:
    for y in range(len(x)):
     num1 = int(input("Enter the value of n: "))
     hold = num1
     sum = 0

     if num1 <= 0: 
      print("Enter a whole positive number!") 
     else: 
      while num1 > 0:
        sum = sum + num1
        num1 = num1 - 1;
    # displaying output
      print("Sum of first", hold, "natural numbers is: ", sum)

  elif a in conversation:
    result = conversation[a]
    print ("\n\t\t"+ result)
  elif a =="stop":
   print("\n\t\t Is there anything that I can help?")
   b = input()
   b = b.lower()
   if b == "yes":
     print("\n\t\t Go on")
     chatbot()
   elif b =="no":
    print("\n\t\t Thank you for your time have a nice day")
    exit()
   else:
    print ("\n\t\t Sorry I didn't get it")

while True:
  chatbot()