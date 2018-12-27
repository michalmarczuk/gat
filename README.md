# gat tests

Go to gat directory:

`cd GAT`

---

## To run locally:

Install libraries:

`pip3 install -r requirements.txt`


Set environment variables:

`export DRIVER=chrome`

`TESTS_CONFIG_ENV_FILENAME=test`


Run all tests:

`python3 -m pytest --reruns 3`

Run single test:

`python3 -m pytest tests/login/positive --reruns 3`

---

## To run on docker:

Go to docker directory:

`cd docker`

Build image:

`./build.sh`

Run all tests:

`./run.sh`

Run single test:

`./run.sh login/negative`
