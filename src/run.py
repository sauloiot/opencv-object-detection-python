from examples import exemplo4, exemplo1, exemplo2, exemplo3

print('1: detecção facil por imagem v1')
print('2: detecção facil por imagem v2')
print('3: detecção facil por camera v2')
print('4: detecção facil por camera v2')

input1 = input("Escolha o exemplo a ser executado: ")

print('opção escolhida: ' + input1)

if input1 == "1":
    exemplo1.run()
if input1 == "2":
    exemplo2.run()
if input1 == "3":
    exemplo3.run()
if input1 == "4":
    exemplo4.run()
else:
   print("end")
