from random import choice

try:
	with open("palavras.txt", "r") as arquivo:
		palavras = list(arquivo.read().split())
		if len(palavras) == 0:
			print("O arquivo está vazio.")
			raise SystemExit

except FileNotFoundError:
	print("O arquivo 'palavras.txt' não foi encontrado.")
	raise SystemExit

palavra = choice(palavras).upper()
PalavraOculta = ["_"] * len(palavra)
LetrasTentadas = []
Tentativas = 6

print(f"""Bem-vindo ao Jogo da Forca!\n\nPalavra: {" ".join(PalavraOculta)}\n\nTentativas restantes: {Tentativas}\nLetras tentadas: Nenhuma""")

while ("_" in PalavraOculta and Tentativas > 0):
	letra = (input("Digite uma letra: ")).upper()
	if(not(len(letra) == 1 and letra.isalpha())):
		print("Entrada inválida. Dígite apenas UMA letra.")
		continue

	LetrasTentadas.append(letra)
	if letra in palavra:
		posicoes = [i for i, c in enumerate(palavra) if c == letra]
		for i in posicoes:
			PalavraOculta[i] = palavra[i]
		print(f"Boa! A letra '{letra}' está na palavra.\n\n")
	else:
		Tentativas -= 1
		print(f"A letra '{letra}' não está na palavra.\n\n")

	print(f"""Palavra: {" ".join(PalavraOculta)}\n\nTentativas restantes: {Tentativas}\nLetras tentadas: {" ".join(LetrasTentadas)}""")

if (Tentativas > 0):
	print(f"Parabéns! Você acertou a palavra: {palavra}")
else:
	print(f"Fim de jogo! A palavra era: {palavra}")