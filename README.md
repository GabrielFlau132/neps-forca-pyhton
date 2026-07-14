# 🎯 Jogo da Forca em Python

Um jogo da forca desenvolvido em Python que seleciona aleatoriamente uma palavra de um arquivo de texto e desafia o jogador a descobri-la antes que suas tentativas acabem.

## 📋 Funcionalidades

* ✅ Seleção aleatória de palavras.
* ✅ Leitura das palavras a partir de um arquivo externo (`palavras.txt`).
* ✅ Validação de entrada do usuário.
* ✅ Controle de letras já tentadas.
* ✅ Atualização da palavra a cada acerto.
* ✅ Sistema de tentativas restantes.
* ✅ Tratamento de erros para:

  * arquivo inexistente;
  * arquivo vazio.

---

## 📂 Estrutura do projeto

```text
.
├── forca.py
├── palavras.txt
└── README.md
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/jogo-da-forca.git
```

### 2. Entre na pasta

```bash
cd jogo-da-forca
```

### 3. Execute o programa

```bash
python forca.py
```

---

## 📝 Arquivo `palavras.txt`

O jogo utiliza um arquivo chamado `palavras.txt`.

Cada palavra pode estar em uma linha diferente ou separada por espaços.

Exemplo:

```text
python
computador
algoritmo
programacao
desenvolvimento
```

ou

```text
python computador algoritmo programacao desenvolvimento
```

---

## 🎮 Como jogar

Ao iniciar o programa será exibida uma palavra oculta:

```text
_ _ _ _ _ _
```

Digite apenas **uma letra** por vez.

Se a letra existir na palavra:

* ela será revelada nas posições corretas.

Caso contrário:

* você perderá uma tentativa.

O jogo termina quando:

* todas as letras forem descobertas; ou
* as tentativas chegarem a zero.

---

## 💻 Exemplo

```text
Bem-vindo ao Jogo da Forca!

Palavra:
_ _ _ _ _ _

Tentativas restantes: 6
Letras tentadas: Nenhuma

Digite uma letra: A

Boa! A letra 'A' está na palavra.

Palavra:
_ A _ A _ _

Tentativas restantes: 6
Letras tentadas: A
```

---

## ⚠️ Tratamento de erros

O programa verifica automaticamente situações como:

### Arquivo inexistente

```text
O arquivo 'palavras.txt' não foi encontrado.
```

### Arquivo vazio

```text
O arquivo está vazio.
```

Nesses casos, o programa é encerrado de forma controlada.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca padrão (`random`)

Não é necessário instalar dependências externas.

---

## 📚 Conceitos praticados

Este projeto utiliza diversos conceitos fundamentais de Python:

* Manipulação de arquivos
* Tratamento de exceções (`try` / `except`)
* Listas
* Laços de repetição (`while`)
* Estruturas condicionais (`if`)
* List Comprehension
* Manipulação de strings
* Validação de entrada
* Seleção aleatória (`random.choice`)

---

## 🚀 Possíveis melhorias

* Desenho da forca em ASCII.
* Sistema de níveis de dificuldade.
* Categorias de palavras.
* Ranking de jogadores.
* Interface gráfica com Tkinter ou Pygame.
* Sistema de pontuação.
* Evitar letras repetidas.
* Menu principal.
* Jogar novamente sem reiniciar o programa.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e de aprendizado.

---

Desenvolvido em **Python** como prática de lógica de programação, manipulação de arquivos e estruturas de controle.
