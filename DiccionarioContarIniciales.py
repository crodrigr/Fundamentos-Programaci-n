from collections import Counter 

line = 'El:elef:ante:avanza:hacia:Asia'
#line = 'Varias vacas vuelan sobre Venezuela'
words = line.split(":")
print(words)
letters = [word[0] for word in words]
print(letters)
final = "".join(letters)
mini = str.lower(final)
frase = Counter(mini)
print (frase)