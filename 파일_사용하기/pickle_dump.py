import pickle
name = "Jaehi"
age = 20
address = "사랑시 고백구 행복동"
score = {'korean':70,'math':5,'English':60,'science':70}

with open('Jaehi.p','wb') as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(score,file)
