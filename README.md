# streaming-03-bonus-ryansmith

Ryan Smith
9/10/2023

Creating a custom send / receive script using rabbitmq to read from a .csv file and send the message, listen to the message and output the message to a new file.

The send/producer will read in the AmazonStock.csv it will get the next row from the file, and transmit that line. 
The listener/consumer will receive the transmitted data, print that line that was recieved into a new .csv file

The data that we will be using is the historical stock data for Amazon which was found on Yahoo. 

https://finance.yahoo.com/quote/AMZN/history?period1=863654400&period2=1693180800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

Below is an image of the two terminals streaming, one sending data from .csv, the other receiving, and then writing to a new.csv

![A look at two terminals sending and receiving messages](./images/Bonus2TerminalsStreaming.png)


