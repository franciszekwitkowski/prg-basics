import time
seconds = int(input("Enter the number of seconds to count down: "))


countdown_words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}


while seconds > 0:
    if seconds > 5:
        time.sleep(1)
        seconds -= 1
    else:
      for i in range(seconds):
         time.sleep(1)  
         print(countdown_words[seconds])
         seconds -= 1
         

print("Time's up!")