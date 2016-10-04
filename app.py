from twython import Twython
import markov
import regex

#the twitter stuff

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# read the list of cities and generate city names

with open("ut-cities.txt") as f:
	text_cities = f.read()

line_cities = text_cities.strip()
model = markov.build_model(line_cities, 2)
markov_ut = markov.generate(model, 2)

full_list_cities = ''.join(markov_ut)
list_ut = full_list_cities.split()

def count_letters(word):
    return len(word) - word.count(' ')

final_list = []
for line in list_ut:
    if (15 > count_letters(line) > 4) and (line.istitle() is True):
        final_list.append(line)

ut_cities0 = final_list[0] + ', UT' + "\n"
ut_cities1 = final_list[1] + ', UT' + "\n"
ut_cities2 = final_list[2] + ', UT' + "\n"
ut_cities3 = final_list[3] + ', UT' + "\n"

ut_sentence = ut_cities0 + ut_cities1 + ut_cities2 + ut_cities3

if len(ut_sentence) < 140:
	result=ut_sentence
	twitter.update_status(status=result)
