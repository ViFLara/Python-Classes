from class3_television import Television
from class5_counter_letters import counter_letters, test

television = Television()
print(television.on)
television.power()
print(television.on)

list = ['dog', 'elephant', 'bird']
amount_letters = counter_letters(list)
print('Total letters per word: {}'.format(amount_letters))

print(test())