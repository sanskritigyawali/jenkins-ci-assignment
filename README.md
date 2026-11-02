# jenkins-ci-assignment
CMSC 426 Jenkins assignment

## Requirements
- Python 3
- Git
- Jenkins with the Git and GitHub plugins for CI setup

The application and tests use Python's standard library and there are no additional Python packages that are required.

## Project files
- app.py: This file contains the add_numbers function and also runs the application.
- tests/test_app.py: This file checks that adding 2 and 3 returns 5.

## Run locally
Clone the repository and open its folder:
```bash
git clone https://github.com/sanskritigyawali/jenkins-ci-assignment.git
cd jenkins-ci-assignment
```

Run the application:
```bash
python3 app.py
```

Run the automated test:
```bash
python3 -m unittest discover -s tests -v
```

The test should pass because add_numbers(2, 3) returns 5.
