from rabbitmq_utils import read_messages


def solve_arithmetic_phrase(channel, method, properties, body):
    with open('output.txt', 'a') as file:
        body_str = eval(body)
        result = eval(body_str)
        file.write(f'{body_str} = {result}\n')

    return result


read_messages(solve_arithmetic_phrase)
