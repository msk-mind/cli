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

{"patient.patient_id": "SPECTRUM-OV-004", "patient.dmp_patient_id": "P-0039734", "patient.gender": "FEMALE", "patient.race": "WHITE", "patient.vital_status": "1.0", "patient.patient_last_known_alive_age": 26055, "patient.icdo_histology_code": "M8461/3", "patient.icdo_site_code": "C569", "patient.diagnosis_pathology_stage_group": "3C", "patient.diagnosis_clinical_stage_group": "3C", "patient.age_at_diagnosis": 25921, "patient.project_id": "OV"}
{"patient.patient_id": "SPECTRUM-OV-005", "patient.dmp_patient_id": "P-0040521", "patient.gender": "FEMALE", "patient.race": "WHITE", "patient.vital_status": "1.0", "patient.patient_last_known_alive_age": 21413, "patient.icdo_histology_code": "M8461/3", "patient.icdo_site_code": "C569", "patient.diagnosis_pathology_stage_group": "", "patient.diagnosis_clinical_stage_group": "3C", "patient.age_at_diagnosis": 21050, "patient.project_id": "OV"}
...
```

2. Get url to patient data bundle with the optional download flag
```
$ msk-mind get "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --download

http://<vm_ip>:50070/data/tmp/1587488693850.gz
```

3. Get available tables
```
$ msk-mind table

clinical_diagnosis
clinical_patient
patient
test
```

4. Get column details on table patient
```
$ msk-mind table patient

('patient_id', 'string', '')
('patient_dmp_id', 'string', '')
('gender', 'string', '')
('race', 'string', '')
('vital_status', 'string', '')
('patient_last_known_alive_age', 'int', '')
('icdo_histology_code', 'string', '')
('icdo_site_code', 'string', '')
('diagnosis_pathology_stage_group', 'string', '')
('diagnosis_clinical_stage_group', 'string', '')
('age_at_diagnosis', 'int', '')
('project_id', 'string', '')
```