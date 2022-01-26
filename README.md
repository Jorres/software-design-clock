# Clock pattern demonstration

## How to launch

Make sure you have python and `virtualenv` module. 
The whole program has been tested using python 3.8, however should
also work with python 2.x.

Create and enter the virtual environment (optional):
```
python -m venv env
source env/bin/activate
```

Install pytest (the only dependency) and launch it:
```
python install -r requirements.txt
pytest
```

## Repository structure

1. `mocked_clock.py` and `realtime_clock.py` contain different implementations
   of an interface with a method `now`.
2. `event_statistics.py` contains RPM calculation logic
3. `event_statistics_test.py` contains tests
