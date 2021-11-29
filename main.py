def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
   summa = summa + int(simbols) 
  return summa
teksts=input("ivadi skaitli")
res= countNumbers(teksts)
print (res)