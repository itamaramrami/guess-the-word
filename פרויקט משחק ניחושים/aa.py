import random
with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()
my_dict = {}# מילון של רשימת השחקנים עם הניקוד
my_name=[]# רשימת המילים שכבר נוחשו
the_guessing_word=""# מחרוזת להוספת ניחוש האות  
num=int(input("Enter The number of participants:"))
while num!=0:
   key =input("Enter your name:")
   my_name.append(key)
   my_dict[key]=0
   num=num-1
the_number_of_games=int(input("Enter the number of games"))
for i in range(the_number_of_games):
   A_word_we_will_play=random.choice(words)
   if A_word_we_will_play in my_name:
        A_word_we_will_play=random.choice(words)
   else:
      my_name.append(A_word_we_will_play)
   The_hidden_word=("*"*len(A_word_we_will_play))
   The_hidden_word=list(The_hidden_word)
   print(The_hidden_word)
   while "*" in The_hidden_word:
      for key in my_dict:
         guess=input(f"{key}, Enter your guess:")
         while guess in the_guessing_word or len(guess)>1:
               guess=input("Enter your guess")
         the_guessing_word+=guess
         for i in range(len(A_word_we_will_play)):
               if A_word_we_will_play[i]==guess:
                     The_hidden_word[i]=guess
                     my_dict[key]+=1
                     print(my_dict)
         if  "*" not in The_hidden_word:
             print(A_word_we_will_play) 
             break          
         print(The_hidden_word) 
   the_guessing_word=""      
max_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_key]
print(f"The player who won is {max_key} With {max_value} points")

    