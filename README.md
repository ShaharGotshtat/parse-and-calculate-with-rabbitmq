# Parse and Calculate with Rabbitmq

This is a dockerized Python and Rabbitmq application.
One Python docker (the "Parser") reads verbal arithmetical operations from input file and publishes messages to the Rabbitmq queue.
Another Python docker reads the messages from the Rabbitmq queue, calculates the arithmetic value and print it to an output file.

### Run:
1. Clone the project.
2. Update the input.txt file with your input (the file contains examples).
3. From the project's root directory, in the terminal, run ```docker-compose up```.

### Verify that it worked:
Rabbitmq:

1. On your browser, go to ```http://localhost:15672/#/```.
2. Find ```parse_and_calculate_queue``` under 'Queues'.
3. See activity in the graphs.

Actual results:

1. Without stopping the docker compose, open another tab in the terminal.
2. Connect to the Calculator docker: ```docker exec -it parse-and-calculate-with-rabbitmq_calculator_1 /bin/bash```
3. While in the docker, type ```cat output.txt``` to see the parsed phrases with their results. 
