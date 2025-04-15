question=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

question=question.lower().strip() #per rendere tutto minuscolo e senza spazi prima e dopo la parola

if(question == "42"):
    print("Yes")
elif(question =="forty-two"):
    print("Yes")
elif(question =="forty two"):
    print("Yes")
else: print("No")



