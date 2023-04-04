# PyMote
#### Video Demo:  https://youtu.be/P7ZzmYzj59A
#### Description:
# My Final Project "PyMote" is a Python Web Application, where you can control smart-gadgets like lamps et cetera. Features of the Programm will be:
Current functions:
--> Create an account with you can log in to PyMote
--> Saving Devices (in a extra csv Profil for the user)
--> Controling devices over the gadget profile

Functions i want to add in the future:
--> Implement functions, like switchng light collor in a specific order or turn the light on/off (over the gadget profile)

Librarrys used: os, csv, flask

PyMote/LogIn
1.: First when you visit PyMote you will be directed to the "login" page. Here the python code checks if the User exist or not. If the User don't exist, there will be an error message
that the login data is invalid or there was no account for the user created. If the account is already created and the login input is valid, the user will be redirected to the homepage
of there account (This is the start page that i explain later).

PyMote/register
2.: Becouse there won't be valid data, u have first clivk the link in the login page to get redirected to the "register" page. Here the user is able to create a account with his own
defined username and password. Here the Python code will check if the user already exist. If that's the case there will come an errror message that the user already exist. Else, the
userdata will be saved in a csv file named "user.csv" for the login, and an extra "{USER}.csv" file will be created with the headers "gadgets" and "Status" that i will explain later.

PyMote/start
3.: After login into your Account over the loginpage you will be faced with the strat page of PyMote. Here you can navigate over the drop down menu to all the other sections, like
gadgets, account and you can logout. Here you can see your current devices that you have addet and togle them on or off. Also you can see with wich account you are currently loged in.

PyMote/gadgets
4.: Over the drop-down menu, you can navigate to gadgets. On the gadget site you can add gadgets or delet them. Here the users are able to name theyre gadgets how they want. After a
gadget is addet, the data will be saved in the uniqu {USER}.csv file. Added gadgets will be "off" by default. After going back to the start page the device will be shown with it's
current status.

/delet-gadget
5.: If the User click the delet button the delet-gadget functions comes in handy. This function will delet the specific defice selected. In the {USER}.csv file the complet row of the
gadget will be removed.

/toggle-gadget
6.: This function is simular to the "delet-gadgte" function. After clicking on the "toggle" button, on the start page, the Python code will check the current status of the Gadget inside
the {USER}.csv file. Deppending on the current status of the gadget, it will be turned off or on. This also changes the Status inside the {USER}.csv file.

PyMote/account
7.: Finally, after selecting the Account page ofer the drop-down menu, the user is here able to delet there account. After clicking on the delet button the user will be redirected to the
"login" page. While this happens the Python code will first delet the {USER}.csv file afterwards inside the user.csv file, the comnplet row with "Username" and "Password" will be
removed. If now the user try's again logging in with there old data it wount be posible, becouse there data aren't anymore inside the user.csv file. Obviously the user have to create a
new account over the register page in this case.

#Future Functions that i will implement woun't be in Python but i will describe them:
Using a Node MCU v3 i want to use the Arduino IDE to code a json server with c++. The Node MCU v3 module should then be able to communicate with the Flask server. In this way gadgets
that will be connectet to the Node MCU V3 module will then able to be managed over the Python Flask sever. For example when you Register a Lamp you can toggle it on and of over the Flask
server. The technical part will manage the Node MCU module.
