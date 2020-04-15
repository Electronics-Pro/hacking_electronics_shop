# hacking_electronics_shop
Not much. The repository for IP project code... adding details later.

Files:
1. crt_db.py : use this to create the database and tables.
2. start_here.py : client side gui.
3. start_here_admin.py : admin side gui.

Also do not forget to add admin userid, password, email, email password, mysql password as environment variables as:

1. adminus: username used by admin in start_here_admin.py login.
2. adminpa: password used by admin in start_here_admin.py login.
3. mailus: email id from where confirmation messages are sent in start_here.py and start_here_admin.py (gmail, can be changed).
4. mailpa: password of above address(make sure to change to less secure: https://myaccount.google.com/lesssecureapps
           or add python as a trusted user: https://myaccount.google.com/apppasswords).
5. mysqlpa: add in your mysql password(considering user is "root").

Finally add the images folder where your python files are located.
