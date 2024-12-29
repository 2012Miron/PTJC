import pickle
import os

CoolText = "Eat more this softer files."
Path = 'Test.pkl'

with open(Path, 'wb') as file:
    pickle.dump(CoolText, file)
print("Text dumped.")
