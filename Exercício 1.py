def Calcular(baseMaior, baseMenor, altura):
    return ((baseMaior + baseMenor)*altura)/2
  
baseMaior = float(input("Insira a base maior do trapézio: "))
baseMenor = float(input("Agora insira a base menor: "))
altura = float(input("Por último, a altura: "))
print (f"{Calcular(baseMaior, baseMenor, altura):.2f}")
