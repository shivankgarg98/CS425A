#paint
## Dependencies

## Running the application
1. Run the server by `python3 server.py IP-ADDR PORT`
2. Run the paint application by `python3 paint.py IP-ADDR PORT`

## Tasks pending
0. [ ]We need to we need to map the coordinate system for various collaborating devices. ( different laptops has different screen size ). So publish the coordinates after converting them to the ratio of MAX_WIDTH, MAX_HEIGHT.
1. [ ]Send messages in more elegant way i.e. using json. We can convert JSON to string by `json.dumps(json_data)` and send this string. After receiving we can again get the data in JSON format by `json.loads(json_dump_string)`. This will prevent error that occur due to inapt message due to out-of boundary co-ordinates.
2. [ ]Implement persistent drawing. i.e. when a user connects after some part of drawing is done then he must be able to fetch the current state of canvas.
3. [x] Implement different brushes, colours, brush-size changing option, eraser ( a white brush :-p ).
4. [ ]Implement Voice chat while drawing
5. [ ]Implement user identifier (Add a name above cursor of people drawing in my canvas).
6. [ ]Implement Log-in/signup and databases stuffs.
7. [ ]Ajustment with screen resizement?
