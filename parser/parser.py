from rabbitmq_utils import *
from consts import *


def send_messages():
    connection = get_rabbitmq_connection()
    channel = get_channel(connection)
    create_and_bind_queue(channel)
    phrases = read_input()

    for phrase in phrases:
        parsed_phrase = parse_phrase(phrase)
        publish_message(channel, parsed_phrase)

    connection.close()


def read_input():
    with open('input.txt', 'r') as file:
        return file.read().split('\n')


def parse_phrase(phrase):
    print(phrase)

    for word, number in WORDS_TO_DIGITS.items():
        phrase = phrase.replace(word, number)

    return phrase.replace(' ', '')


send_messages()
