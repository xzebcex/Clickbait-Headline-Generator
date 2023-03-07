# Clickbait headline generator.

import random

# Set up the constants.
OBJECTIVE_PRONOUNS = ['Her', 'Him', 'Them']

POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']

PERSONAL_PRONOUNS = ['She', 'He', 'They']

STATES = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
          'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
          'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

NOUNS = ['Actor',	'Gold', 'Painting', 'Advertisement',	'Grass', 'Parrot'
         'Afternoon', 'Greece',	'Pencil', 'Airport', 'Guitar', 'Piano'
         'Ambulance', 'Hair', 'Pillow', 'Animal',	'Hamburger',	'Pizza'
         'Answer', 'Helicopter', 'Planet', 'Apple', 'Helmet', 'Plastic'
         'Army', 'Holiday', 'Portugal', 'Australia', 'Honey', 'Potato'
         'Balloon', 'Horse', 'Queen', 'Banana', 'Hospital', 'Quill'
         'Battery', 'House', 'Rain', 'Beach', 'Hydrogen', 'Rainbow'
         'Beard', 'Ice', 'Raincoat', 'Bed', 'Insect', 'Refrigerator',
         'Belgium', 'Insurance', 'Restaurant']

PLACES = ['Greenhouse', 'Coffeehouse', 'Birthday Party', 'Downtown', 'Barnyard', 'Bungalow',
          'Bazaar', 'Transylvania', 'Aquarium', 'New Brunswick', 'Drugstore', 'Landfill', 'Suburbia',
          'Cathouse', 'Freeway', 'Bathroom', 'Hometown', 'Rose Garden', 'Motel Room', 'Bus Station', 'Government Agency',
          'Massachusetts Institute of Technology', 'Farmhouse', 'Small Boat', 'Moon', 'Underworld',
          'Mountain Range', 'Vacant Lot', 'Dead End']

WHEN = ['Soon', 'This Year', 'Later Today', 'Right Now', 'Next Week']


def main():
    while True:
        response = input(
            'Enter the number of clickbait headlines to generate: ')
        if not response.isdecimal():
            print('Enter a number.')
        else:
            num_of_headlines = int(response)
            break  # Exit the loop.

    for i in range(num_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            headline = generate_are_millennials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()

        print(headline)

    website = random.choice(['Teddies', 'Hesbook', 'blogg', 'pineapple',
                             'woobsite', 'Catgram'])

    when = random.choice(WHEN).lower()
    print('Post these to our', website, when)

# Each of these function return a diffrent type of headline.


def generate_are_millennials_killing_headline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noun)


def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, plural_noun, when)


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECTIVE_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun,
                                                                      pronoun, place)


def generate_dont_want_you_to_know_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun,
                                                                      pronoun, place)


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} WillSurprise You!)'.format(number1, plural_noun, number2)


def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
