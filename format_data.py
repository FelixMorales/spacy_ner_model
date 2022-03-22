import spacy
from tqdm import tqdm
from spacy.tokens import DocBin
from spacy.language import Language
import json

def create_training(json_file: str, nlp: Language):
    db = DocBin()
    f = open(json_file)
    TRAIN_DATA = json.load(f)

    for text, annot in tqdm(TRAIN_DATA): 
        doc = nlp.make_doc(text) 
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents 
        db.add(doc)
    return db



nlp = spacy.blank('en')

training_data = create_training('data/training_data.json', nlp)
training_data.to_disk("./spacy_format_data/training_data.spacy")

validation_data = create_training('data/validation_data.json', nlp)
validation_data.to_disk("./spacy_format_data/validation_data.spacy")
