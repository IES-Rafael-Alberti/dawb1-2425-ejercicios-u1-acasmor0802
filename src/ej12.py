peso = float(input("Introduce tu peso (en kg): "))
estatura = float(input("Introduce tu estatura (en metros): "))
indice = (peso / ((estatura*10)**2))*100
print(f"Tu indice de masa corporal es de: {round(indice,2)}")