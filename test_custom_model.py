import spacy

# Load trained custom model
nlp_ner = spacy.load('./model-best') 

f = open("test_data/test_text.txt", "r")
test_text = f.read()

print('\nTESTING TEXT =====>')
print(test_text)
print('<=====\n')

doc = nlp_ner(test_text)

print('Entities found =====>')
for word in doc.ents:
    print(f'text: {word.text} - tag: {word.label_}')
print('<=====\n')