0x14. JavaScript - Web scraping
Scripting
API
JavaScript
 By: Guillaume, CTO at Holberton School
 Weight: 1
 Project will start Apr 25, 2023 6:00 AM, must end by Apr 26, 2023 6:00 AM
 Checker was released at Apr 25, 2023 12:00 PM
 An auto review will be launched at the deadline
Resources
Read or watch:

Working with JSON data
The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco
request module
Modern JS
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JavaScript programming is amazing
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/node
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
All your files must be executable
The length of your files will be tested using wc
You are not allowed to use var
More Info
Install Node 10
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semi-standard
Documentation

$ sudo npm install semistandard --global
Install request module and use it
Documentation

$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Tasks
0. Readme
mandatory
Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x14-javascript-web_scraping
File: 0-readme.js
   
1. Write me
mandatory
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x14-javascript-web_scraping
File: 1-writeme.js
   
2. Status code
mandatory
Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x14-javascript-web_scraping
File: 2-statuscode.js
   
3. Star wars movie title
