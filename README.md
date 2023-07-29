# AkamaiSensorDataUtility

Just a fun project where i tried to reverse engineer Akamai. However, due to the commencement of my university studies, I was compelled to halt the project. Some noteworthy files involved in the project include:

akamai1.js: This is the original code executed by the browser.
akamai1_rewritten.js: This file contains the deobfuscated version of the original code.
akamaiSensorDataUtility.py: Serving as the main program, it accepts as input the string that the browser sends to Akamai to distinguish between bot and human interactions with the site. The program tries to reverse engineer this string. The string consists of multiple pieces of information, each partitioned by a sequence like "-1,2,-94,-103,". The program segments the string into its discrete components and deciphers them
