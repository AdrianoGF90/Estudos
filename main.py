# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.right = []
        self.wrong = []
    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter.lower()
        if self.letter in self.word:
            self.right.append(self.letter)
        else:
            self.wrong.append(self.letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.wrong) == 6:
            print(board[6])
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if my_try == self.word:
            return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        word_list = [n for n in self.word]
        try_list = []
        for i in word_list:
            if i in self.right:
                try_list.append(i)
            else:
                try_list.append('_')
        global my_try
        my_try = ''.join(map(str, try_list))
        print(my_try)

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.wrong)])

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while True:
    # Verifica o status do jogo
        game.print_game_status()
        print('Palavra: ')
        game.hide_word()
        print('Letras corretas:')
        print(game.right)
        print('Letras erradas:')
        print(game.wrong)
        hint = input('Digite uma letra> ')
        game.guess(hint)

    # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won():
            print('\nParabéns! Você venceu!!')
            print('\nFoi bom jogar com você! Agora vá estudar!\n')
            break
        elif game.hangman_over():
            print('\nGame over! Você perdeu.')
            print('A palavra era ' + game.word)
            print('\nFoi bom jogar com você! Agora vá estudar!\n')
            break
        else:
            continue

# Executa o programa
if __name__ == "__main__":
    main()