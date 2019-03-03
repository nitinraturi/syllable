## Syllable ##
A tool to convert romanian words into syllables with an easy to use web based user interface and database storage facility
Thanks to [silabe.ro](silabe.ro). It is being used as an input and output source.

### Requirements ###
- Python version 3
- beautifulsoup4==4.7.1
- Flask==1.0.2
- Flask-SQLAlchemy==2.3.2


### Installation ###
* Install requirements.txt `pip install -r requirements.txt`
* Create a config.py file at the root directory and put the following credentials for mysql database connectivity.
  * `db_user = your database user`
  * `db_pass = your database password`
  * `db_host = your host`
  * `db_name = your database name`
* Run python db.by to create required table.
* Inside your table structure, change all field collation type to `utf8mb4_unicode_520_ci`
* Run python app.py, server will run by default at port localhost:3007. You can change it inside app.py.

### Usage ###
* Open the browser and go the url where you have started your server.
* On the left hand side, if you just want to analyze the word just hit analyze.
* Or if you want to save it to the database, hit on the Add word button.
* On the righthand side there is a list of saved words.
* If you want to listen to the word pronunciation,click on speak button.  

## Thanks ##
