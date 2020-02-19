# Spambot
A spambot created in order to send multiple messages to a target in a few seconds. Done automatically. This uses Python.
What the spambot does is logs into messenger for you after requesting your username and password. **THIS DOES NOT SAVE YOUR LOGIN INFORMATION NOR DOES IT SHARE THE INFORMATION**. 

This allows you to choose a target, what message to send, and how many messages to send them that message.

# Prequisites
Your resolution must be 1920x1080 and must have [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/browsers/). This does not currently work with other  You also need the latest version of [Python 3.7](https://www.python.org/downloads/release/python-374/) and you need [Git BASH](https://gitforwindows.org/) which is a command-line interface (CLI). You also need the packages:
- Selenium
- Pyautogui

# Installation of prerequisites
So install python and git bash as normal by following through the installation process. In order to install the packages, you need a virtual environment.

You create a virtual environment by opening git bash. No need to change the directory. The command for creating a virtual environment is:
  *py -3.6 -m venv name* where for "name" you can input the name of your choosing. Such as *py 3.6 -m venv virtualenv*
  
You will then have to activate the virtual environment. You need to do this each time you close git bash and want to use the spambot. You do this by source name/scripts/activate* where you substitute "name" with the name of your virtual environment. 

After in the virtual environment, you must install the packages. This only needs to be done once. To do this, enter into git bash:
- *pip install Selenium*
- *pip install pyautogui*

Both these packages will take a short amount of time to install. 

# Navigating to the spambot
Next, you need to go into the folder that the spambot  is in. For example, lets say my spambot is on my desktop in a folder called spambot. I will have to do the following commands.
- *cd Desktop*
- *cd spambot*
"*cd*" is used to change directories.When typing, you can press "tab" in order to fill in words if available so that you do not have to type the whole word. 

# Using the spambot
Firstly, you should know that once you activate the spambot, you must NOT move your mouse cursor. If you suspect it is not working properly or if a mistake is made, drag your mouse cursor into the bottom left corner. You can do this even if the cursor is moving. You must do this quickly in order to regain control and activate the failsafe.

In order to activate the spambot, while in the folder do the command:
- *python spambot.py*

This will then run and will load the messenger site. You will then be prompted to enter the information requested. If you wish to back out of it, do "crtl + c" then press enter in order to exit out.

When entering prompts, DO NOT use any other characters other than letters and numbers. This includes not using symbols such as &,",',%,$

I hope you enjoy the spambot. Made by Viraj Kulkarni.
