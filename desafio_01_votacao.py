# Inicializa a lista de votos e define os candidatos válidos
votos = []
candidatos = ["ana", "bruno", "carlos"]

print("Candidatos:\n1. Ana\n2. Bruno\n3. Carlos")

# Laço de captação de votos
while True:
    voto = input("Digite o nome do candidato (fim para encerrar): ").strip().lower()
    
    if voto == "fim":
        break
    elif voto in candidatos:
        votos.append(voto)
    else:
        print("Voto inválido. Tente novamente.")

print("\n--- Resultado da votação ---")

# Lógica de contagem e verificação de vencedores mais enxuta
resultados = []

# Exibe os votos e guarda as contagens em uma lista
for candidato in candidatos:
    quantidade = votos.count(candidato)
    resultados.append(quantidade)
    print(f"{candidato.capitalize()}: {quantidade} votos")

# Descobre o maior número de votos
maior_voto = max(resultados)

# Cria uma lista apenas com os candidatos que tiveram o maior número de votos
vencedores = []
for candidato in candidatos:
    if votos.count(candidato) == maior_voto:
        vencedores.append(candidato.capitalize())

# Se a lista de vencedores tiver mais de 1 pessoa, é empate
if len(vencedores) > 1:
    print("Houve um empate entre os candidatos.")
else:
    print(f"O vencedor é: {vencedores[0]}")
