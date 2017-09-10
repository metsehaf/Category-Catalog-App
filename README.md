# Category Catalog App
An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items. This app/project was part of the Full stack program at [Udacity](https://classroom.udacity.com).
# Documentation
Please refer to [SQLAlchemy](sqlalchemy.org), [flask](http://flask.pocoo.org/docs/0.10/quickstart/#) for more info on how the the server and CRUD functionalities were created. 

# Installation
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.

Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
### Running the Category Catalog App

Once Vagrant is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your VM. change to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.

Type ls to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

Now type python database_setup.py to initialize the database.

Type python lotsofmenus.py to populate the database with categories and catalog items. (Optional)

Type python project.py to run the Flask web server. In your browser visit http://localhost:5000 to view the category catalog app. You should be able to view, add, edit, and delete menu items and categories.
# Author
Girum Hagos
# More information
- [Udacity](https://classroom.udacity.com/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Flask](http://flask.pocoo.org/docs/0.10/quickstart/#)
- [Python](https://www.python.org/) 
