n=int(input("Informe a quantidade numeros do conjunto "))
somavalores=0
conjunto= []
for i in range(n):
  num=int(input(f"Informe o {i+1}º número do conjunto: "))
  somavalores+=num
  conjunto.append(num)
maior=max(conjunto)
menor=min(conjunto)
print(f"O maior valor do conjunto : {maior}")
print(f"O menor valor do conjunto: {menor} ")  
print(f"A soma dos valores do conjunto é: {somavalores}")  
