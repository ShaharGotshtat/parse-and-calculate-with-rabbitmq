from rabbitmq_utils import *
from consts import *


def send_messages():
    connection = get_rabbitmq_connection(HOST)
    channel = get_channel(connection)
    create_and_bind_queue(channel)
    phrases = read_input()

    for phrase in phrases:

        if contains_digits(phrase):
            print(f'Phrase {phrase} is invalid! it contains digits.')
            continue

        parsed_phrase = parse_phrase(phrase)
        publish_message(channel, parsed_phrase)

    connection.close()


def read_input():
    with open('input.txt', 'r') as file:
        return file.read().split('\n')


def contains_digits(phrase):
    return any(char.isdigit() for char in phrase)


def parse_phrase(phrase):
    for word, number in WORDS_TO_DIGITS.items():
        phrase = phrase.replace(word, number)

    return phrase.replace(' ', '')


send_messages()
