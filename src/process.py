import os

def read_var(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_result(result, file_path):
    with open(file_path, 'w') as file:
        file.write(result)

def compare_vars(var1, var2):
    if var1 == var2:
        return "Les variables sont égales."
    else:
        return "Les variables sont différentes."

# Chemins vers les fichiers contenant les variables
variable1_path = .github/workflows/variable1.py
variable2_path = .github/workflows/variable2.py
result_path = .github/workflows/resultcheck.py

# Lire les variables
var1 = read_var(variable1_path)
var2 = read_var(variable2_path)

# Comparer les variables
result = compare_vars(var1, var2)

# Écrire le résultat
write_result(result, result_path)

print("La comparaison est terminée. Vérifiez le fichier result.txt pour les résultats.")
