import re
str="Srinivas is my name. I am always playing free fire now-a-days" \
    "So I am not concentrating on my studies." \
    "One day I will delete Free fire " \
    "So that I cannot play the game"
m1=re.findall("I ",str)
print(m1)
m2=re.search("free fire",str)
print(m2)
m3=re.match(str,"play",flags)
print(m3)