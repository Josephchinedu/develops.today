# develops.today

## run this project
Clone this project

#### Build everything:
```sh
docker-compose up --build
```

#### Setup the initial database:

```sh
./run manage migrate 
```

#### Formatting the code base:

```sh
python -m black develops.today
```