# Example conditional statement inside a comprehension
nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [word.title() for word in words if len(word) == 3]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript

# Example set
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

no_nickelback = [song for song in songs if song[0] != 'Nickelback']
print("no nickelback", no_nickelback)
