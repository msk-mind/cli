# MSK MIND CLI

Python Command Line Interface to access MSK MIND

## Installation
### Download executable
Simply download `msk-mind` executable.
*Note*: This executable is generated on macOS. It will not work on linux machines.  
To generate an executable, follow the steps for development and run instructions , then run
```
pyinstaller --onefile msk-mind.py
```
The executable will be at `dist/msk-mind`.

### For Development
#### Requirements

- Python 2.7 or 3.4+
- pip

#### Create a virtual environment
```
python -m venv env # or python3
source env/bin/activate
```

#### pip install
```
pip install -r requirements.txt
```

## Usage

### View Help
```
$ msk-mind --help
Usage: msk-mind.py [OPTIONS] COMMAND [ARGS]...

  Welcome to MSK MIND!

Options:
  --host TEXT  [default: http://localhost:8080]
  --help       Show this message and exit.

Commands:
  get    get data that corresponds to the given query.
  table  introspect on available tables and table details.
```

```
$ msk-mind get --help
Usage: msk-mind.py get [OPTIONS] QUERY

  get data that corresponds to the given query.

  QUERY - a SQL select statement.

  DOWNLOAD - an optional flag. If the flat is set, return a URL to the query
  result set.

Options:
  --download  [default: False]
  --help      Show this message and exit.

```

```
$ msk-mind table --help
Usage: msk-mind.py table [OPTIONS] [NAME]

  introspect on available tables and table details.

  NAME - an optional table name. If provided, return column details (name,
  type, comments) for the table.

Options:
  --help  Show this message and exit.
```

### Examples

1. Get patient data where patients have clinical stage '3C'
```
$ msk-mind get "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"

{'description': 'https://msk-mind.github.io/docs/ops.html#happy_day_mate',
 'payload': [{'patient.age_at_diagnosis': 24525,
              'patient.diagnosis_clinical_stage_group': '99',
              'patient.diagnosis_pathology_stage_group': '3C',
              'patient.gender': 'FEMALE',
              'patient.icdo_histology_code': 'M8980/3',
              'patient.icdo_site_code': 'C569',
              'patient.patient_dmp_id': 'P-0039384',
              'patient.patient_id': 'SPECTRUM-OV-001',
              'patient.patient_last_known_alive_age': 25139,
              'patient.project_id': 'OV',
              'patient.race': 'WHITE',
              'patient.vital_status': '1.0'},
  ...
 'status': 'OK',
 'summary': "You are off to great places, today's your day."}
```

2. Get url to patient data bundle with the optional download flag
```
$ msk-mind get "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --download

{'description': 'https://msk-mind.github.io/docs/ops.html#happy_day_mate',
 'payload': 'http://140.163.78.220:50070/data/tmp/1587571607403.gz',
 'status': 'OK',
 'summary': "You are off to great places, today's your day."}
```
