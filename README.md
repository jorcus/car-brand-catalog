###Project 3: Item Catalog
The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system with API endpoint JSON and ATOM. In this sample project, the homepage displays all current categories along with the latest added items. This project also had the add functionality of be able to store store images for an item. Post request are also protect against prevent cross-site request forgeries.

###Requirements
* Virtual Box - [download](https://www.virtualbox.org/wiki/Downloads)
* Vagrant - [download](https://www.vagrantup.com/downloads)

####Installation Steps:
1. Download project(.zip) and extract it:
2. Move to project folder:
  - Linux: Type `cd car_catalog`
3. Turn on the virtual machine:
  - Linux: Type `vagrant up`
  - Linux: Followed by `vagrant ssh`
  - You are now in your Virtual Machine.
4. Move to the folder:
  - Vagrant terminal: Type `cd /vagrant`
5. To create the database:
  - Vagrant terminal: Type `python database_setup.py`
6. To populate database:
  - Vagrant terminal: Type `python brand_data.py`
  - When complete console will display `Added items!`
7. Start server:
  - Vagrant terminal: Type `python project.py`
  - When running console will display
  ```
  * Running on http://0.0.0.0:5000/
  * Restarting with reloader
  ```
8   . Go to browser and enter `http://localhost:5000/`

###Verisons

1. Python 2.7.6
2. Vagrant 1.7.2
3. Virtual Box 4.3.10
