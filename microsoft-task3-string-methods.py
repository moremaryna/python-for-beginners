
#Microsoft - using strings methods
text = """ Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.
sentences = text.split('. ')
print(sentences)

#You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.
sentences = text.split('. ')
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)