# AkamaiSensorDataUtility

Just a fun project where i tried to reverse engineer Akamai. With the start of the university I had to stop the project.
Notable Files:
- akamai1.js the code that the browser executes
- akamai1_rewritten.js the same code deobfuscated
- akamaiSensorDataUtility.py the main program, takes in input the string that the browser send to akamai to check if the site is used by a bot or a human. the program attempts to reverse engineer that string. The string is composed of multiple informations each seperated by a string like "-1,2,-94,-103,". The program splits the string in it's individual information and decodes it.
