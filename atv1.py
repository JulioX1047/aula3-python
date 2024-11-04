idade=int(input("Informe sua idade :"))
if idade>=18 and idade<60:
  print("Adulto")
elif idade>=60:
  print("IDOSO")
elif idade<12 :
  print("CRIANÇA")
elif idade >12 and idade<=18:
  print("Adolescente")  