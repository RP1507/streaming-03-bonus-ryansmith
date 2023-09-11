import pika
import csv
import signal
import sys

def process_message(message):
    """
    Processes a received message and writes it to an output CSV file.

    Parameters:
        message (str): The received message to be processed and written to the CSV file.

    """
    with open('AmazonOut.csv', 'a') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(message.split(','))  # Split message by comma and write as CSV row

def callback(ch, method, properties, body):
    """
    Callback function to handle received messages.

  Listens for messages on the queue.
This process runs continuously. 

Approach
---------
Simple - one producer / one consumer.


Since this process runs continuously, 
if we want to emit more messages, 
we'll need to open a new terminal window.


Terminal Reminders
------------------

- Use Control c to close a terminal and end a process.

- Use the up arrow to get the last command executed.

    """
    message = body.decode()
    print(f"Received message: {message}")
    process_message(message)

def main_consumer(queue_name):
    """

    To exit the message, press CTRL+C.

    Parameters:
        queue_name (str): The name of the queue to consume messages from.

    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    # Set up the Ctrl+C handler
    def keyboard_interrupt(signal, frame):
        """
        Handle interrupt signal (Ctrl+C)

        This function is invoked when an interrupt signal Ctrl+C is received.

        Parameters:
        signal: The interrupt signal received (not used in the function).
        frame: The current stack frame (not used in the function).

        """
        print('\n Receiving has ended...')
        channel.stop_consuming()
        connection.close()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, keyboard_interrupt)
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        keyboard_interrupt(None, None)

if __name__ == '__main__':
    queue_name = 'stock_data'  
    main_consumer(queue_name)