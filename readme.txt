There are 3 receivers, i.e., receive_database.py, receive_frontend.py, and receive_webscript.py. 
They receive massages that are send to database, front end, and web script respectively.
There are 3 senders, i.e., send_database.py, send_frontend.py, and send_webscript.py. 
They send messages to database, front end, and web script respectively.
There is also one public sender, which sends messages to a given receiver. 

First, type the following commands to start the 3 receivers:
python receive_database.py
python receive_frontend.py
python receive_webscript.py

If we want to send a message to a specific receiver, e.g., database, then type the following command:
python send_database.py 'message content'
or type:
python send.py database 'message_content'