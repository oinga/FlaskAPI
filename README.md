# FlaskAPI
Sample FlaskAPI

```
Run with:

flask --app main.py --debug run
or
python main.py
```
```
Dependencies:

config/ folder for db connections
-api key
-username in pat_sched.users
-user users.active must be "1"

library installation: pip install -r requirements.txt
```

```
Current endpoints:

/patients
/patient/<int:pat_id>
/appts
/appts/<int:npi>
/appt/<int:pat_id>
```
