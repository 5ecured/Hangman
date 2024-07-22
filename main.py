import random

word_list = ['tekken', 'pecel', 'rawon', 'bolu', 'kukus']
chosen_word = random.choice(word_list)
print('+++++GAME START+++++')
# print(chosen_word)

display = []

for i in chosen_word:
    display += '_'

print(display)

while '_' in display:
    player_guess = input('Guess a letter\n').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == player_guess:
            display[i] = player_guess

    print(display)

print('You win!')