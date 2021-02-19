import pickle

with open('Jaehi.p','rb') as file:
    name = pickle.load(file)
    address = pickle.load(file)
    age = pickle.load(file)
    score = pickle.load(file)
    print(name,address,age,score,sep = " ")