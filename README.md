# flask-tuto
Tutorial for begining with Flask + SQLAlchemy and Flask-RESTful

For use this example run the next step.

1. Clone de repo
   ```
   $git clone git@github.com:isccarrasco/flask-tuto.git
   ```

2. Install the python interpreter as a virtual environment.
   ```
   $python setup.py
   ```

3. Activate the virtualenv
   ```
   $source myenv/bin/activate
   ```

4. Before run the application, ensure that was created the database, if not, create it.
   ```
   $psql -h localhost -U postgres -c "CREATE DATABASE tuto;"
   $psql -h localhost -U postgres -c "CREATE TABLE person ( \
                                        person_id serial primary key unique, \
                                        name varchar, \
                                        address varchar, \
                                        birth_day timestamp);"
   ```

5. Now, you can run the application
   ```
   $python runserver.py
   ```

5. Now yo can navigate to
   ```
   http://localhost:5000/ # To view de Hello Wordl! message
   
   http://localhost:5000/personsList # For see the list of name of persons in the database
   ```