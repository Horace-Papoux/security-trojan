# Security

## API Setup

### 1. Install dependencies

```bash
cd api
pipenv shell
pipenv install
```

### Init the database

```bash
python src/db/init_db.py
```

### 2. Run the server

```bash
python app.py
```

## Web client setup

### 1. Install dependencies

```bash
cd client
npm install
```

### 2. Run the server

```bash
quasar dev
```