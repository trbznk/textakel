import pickle
import textakel
import time

with open("random_text_1000000.pickle", "rb") as f:
    text = pickle.load(f)

functions = textakel.get_functions()
text = text*100
data = []

for function in functions:
    print(f"{function}...")
    start = time.time()
    textakel.takel(function, text)
    end = time.time()
    seconds = end-start
    data.append((function, seconds))


print(data)
