uma_lista = [35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
uma_lista.sort()
print(uma_lista)

uma_lista.sort(reverse=True)
print(uma_lista)

outra_lista = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
outra_lista.sort()
print(outra_lista)

outra_lista.sort(reverse=True)
print(uma_lista)

mean = sum(uma_lista) / len(outra_lista)
uma_lista.sort()
print(f'media{mean : .2f}')