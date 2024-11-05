tradutor1 = {}
tradutor1 = {"Pineapple":"abacaxi", "apple":"maça","orange":"laranja"}
print (tradutor1)
del (tradutor1["apple"])
print(tradutor1)
print(tradutor1.pop('apple','Fruta não encontrado'))
tradutor1.clear()
print(tradutor1)