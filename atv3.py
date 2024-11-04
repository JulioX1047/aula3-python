cont=0
qtp=0
qti=0

while cont<10:
  n=float(input("Informe  um número: "))
  if n%2==0:
    qtp+=1;
    print(f" Esse numero é par : {n}")
  else:
    qti+=1;
    print(f" Esse numero é impar : {n}")
  
  cont+=1
  print(f"Quantidade de números pares: {qtp}")
  print(f"Quantidade de números impares: {qti}")
  