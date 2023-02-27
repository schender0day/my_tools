import genanki

# read input from file
with open('/Users/xinchen/Documents/questions.txt', 'r') as f:
    input_string = f.read()

# create a model
model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
)

# create or load the deck
deck_id = 2059400110
deck_name = 'CommandLineFun'
try:
    # try to load an existing deck
    deck = genanki.Package('/Users/xinchen/Documents/test2.apkg').col.decks.get(deck_id)
except:
    # create a new deck if it doesn't exist
    deck = genanki.Deck(deck_id, deck_name)

# split the input string into a list of Q:A sets
qa_list = input_string.strip().split('\n\n')

# add each Q:A set to the deck as a separate card
for qa_set in qa_list:
    q, a = qa_set.split('\n')
    note = genanki.Note(
        model=model,
        fields=[q[3:], a[3:]]
    )
    deck.add_note(note)

# create the Anki package and save it to a file
package = genanki.Package(deck)
package.write_to_file('/Users/xinchen/Documents/test2.apkg')
