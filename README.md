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
Usage: msk-mind [OPTIONS] COMMAND [ARGS]...

  Welcome to MSK MIND!

Options:
  --host TEXT  [default: http://localhost:8080]
  --help       Show this message and exit.

Commands:
  download-files     download operational metadata.
  download-metadata  download domain metadata.
  files              query operational metadata.
  list-columns       show available columns given a table.
  list-databases     show available databases.
  list-tables        show available tables given a database.
  metadata           query domain metadata.
```

```
$ msk-mind metadata --help
Usage: msk-mind metadata [OPTIONS] QUERY

  query domain metadata.

  QUERY - a SQL select statement.

Options:
  --help  Show this message and exit.
```

```
$ msk-mind download-metadata --help
Usage: msk-mind download-metadata [OPTIONS] QUERY

  download domain metadata.

  QUERY - SQL select statement.

  :returns: link to download the data bundle.

Options:
  --help  Show this message and exit.
```

```
$ msk-mind files --help
Usage: msk-mind.py files [OPTIONS] QUERY

  query operational metadata.

  QUERY - Atlas DSL query.

  :returns: operational metadata.

Options:
  --help  Show this message and exit.
```

```
$ msk-mind download-files --help
Usage: msk-mind.py download-files [OPTIONS] QUERY

  download operational metadata.

  QUERY - Atlas DSL query.

  :returns: link to download the data bundle.

Options:
  --help  Show this message and exit.
```

```
msk-mind list-databases --help
Usage: msk-mind.py list-databases [OPTIONS]

  show available databases.

  :returns: list of available databases.

Options:
  --help  Show this message and exit.
```

```
msk-mind list-tables --help
Usage: msk-mind.py list-tables [OPTIONS] DB

  show available tables given a database.

  DB - database name.

  :returns: list of table names and comments

Options:
  --help  Show this message and exit.
```

```
msk-mind list-columns --help
Usage: msk-mind.py list-columns [OPTIONS] DB TABLE

  show available columns given database and table.

  DB - database name.

  TABLE - table name in the database.

  :returns: list of column names and comments

Options:
  --help  Show this message and exit.
```

### Examples

1. Get patient data where patients have clinical stage '3C'
```
$ msk-mind metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"

{'payload': [{'patient.age_at_diagnosis': 24525,
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
 'status': 'OK'}
```

2. Get url to patient data bundle
```
$ msk-mind download-metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --download

{'payload': 'http://<vm_ip>:50070/data/tmp/1587571607403.gz',
 'status': 'OK'}
```

3. Get operational metadata for files
```
$ msk-mind files "from hive_table where name like '*clinical*' select name, owner"

{'payload': [{'name': 'clinical_patient', 'owner': 'raj_ops'},
             {'name': 'clinical_diagnosis', 'owner': 'raj_ops'}],
 'status': 'OK'}
```

```
$ msk-mind files "from hdfs_path where name like '*genomic*' select name, qualifiedName, path"

{'payload': [{'name': '/user/hive/genomic_cna',
              'path': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_cna',
              'qualifiedName': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_cna@Sandbox'},
             {'name': '/user/hive/genomic_maf',
              'path': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_maf',
              'qualifiedName': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_maf@Sandbox'},
             {'name': '/user/hive/genomic_bam',
              'path': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_bam',
              'qualifiedName': 'hdfs://sandbox-hdp.hortonworks.com:8020/user/hive/genomic_bam@Sandbox'}],
 'status': 'OK'}
```

4. Get url to the data bundle
```
$ msk-mind download-files "hive_table where name like '*genomic*' and createTime >= '2020-04-20'"

{'payload': 'http://<vm_ip>:50070/data/tmp/1588078078927.gz',
 'status': 'OK'}
```

5. List available databases.
```
$ msk-mind list-databases

clinical
genomic
```

6. List available tables.
```
$ msk-mind list-tables clinical

| name       | description                                                                       |
|------------+-------------------------------------------------------------------------------|
| medication | None                                                                          |
| patient    | (Patient level) de-identified patient IDs, demographics info, survival status |
| diagnosis  | None                                                                          |
```

7. List available columns.
```
$ msk-mind list-columns clinical patient

| name                         | type   | description   |
|------------------------------+--------+---------------|
| dmp_patient_id               | string | None          |
| patient_last_known_alive_age | int    | None          |
| project_id                   | string | None          |
| gender                       | string | None          |
| race                         | string | None          |
| patient_id                   | string | None          |
| vital_status                 | string | None          |
```
