#paint
## Dependencies

## Running the application
1. Run the server by `python3 server.py IP-ADDR PORT`
2. Run the paint application by `python3 paint.py IP-ADDR PORT`

## Tasks pending
1. Send messages in more elegant way i.e. using json. We can convert JSON to string by `json.dumps(json_data)` and send this string. After receiving we can again get the data in JSON format by `json.loads(json_dump_string)`. This will prevent error that occur due to inapt message due to out-of boundary co-ordinates.
2. Implement different brushes, colours, brush-size changing option, eraser ( a white brush :-p ).
3. Implement Voice chat while drawing
4. Implement user identifier (Add a name above cursor of people drawing in my canvas).
5. Implement Log-in/signup and databases stuffs.
