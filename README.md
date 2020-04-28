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

  QUERY - a SQL select statement.

Options:
  --help  Show this message and exit.
```

```
$ msk-mind files --help
Usage: msk-mind.py files [OPTIONS] QUERY

  query operational metadata.

  QUERY - Atlas DSL query.

Options:
  --help  Show this message and exit.
```

```
$ msk-mind download-files --help
Usage: msk-mind.py download-files [OPTIONS] QUERY

  download operational metadata.

  QUERY - Atlas DSL query.

Options:
  --help  Show this message and exit.
```

### Examples

1. Get patient data where patients have clinical stage '3C'
```
$ msk-mind metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"

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

2. Get url to patient data bundle
```
$ msk-mind download-metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --download

{'description': 'https://msk-mind.github.io/docs/ops.html#happy_day_mate',
 'payload': 'http://<vm_ip>:50070/data/tmp/1587571607403.gz',
 'status': 'OK',
 'summary': "You are off to great places, today's your day."}
```

3. Get operational metadata for genomic files
```
$ msk-mind files "hive_table where name like '*genomic*' and createTime >= '2020-04-20'"

{'description': 'https://msk-mind.github.io/docs/ops.html#happy_day_mate',
 'payload': [{'attributes': {'aliases': None,
                             'columns': [{'guid': 'c3a7a2c0-8ce1-4495-85ee-986fe0314009',
                                          'typeName': 'hive_column'},
                                         {'guid': '1c531a05-e64c-4168-9cfb-41c667f0c2df',
                                          'typeName': 'hive_column'},
                                         {'guid': '3505a8e2-515c-4ca9-8229-0ec2ce6d06b3',
                                          'typeName': 'hive_column'},
                                         {'guid': '6872a6ed-f68a-41c1-b9b0-a6f0d5b020fe',
                                          'typeName': 'hive_column'},
                                         {'guid': 'd0c05a06-ca3d-42f7-9c47-27a8ff4aa902',
                                          'typeName': 'hive_column'},
                                         {'guid': 'd3e4aa5d-4b5f-4875-b07f-d7aaadcc0af2',
                                          'typeName': 'hive_column'},
                                         {'guid': 'bcb30b2f-20e6-41b1-ad1e-56479b9c609c',
                                          'typeName': 'hive_column'},
                                         {'guid': 'f89e825d-97b4-4abe-942f-638b233cb416',
                                          'typeName': 'hive_column'}],
                             'comment': None,
                             'createTime': 1587498187000,
                             'db': {'guid': 'c61cceb3-fdda-4f15-be8d-b19ef2295559',
                                    'typeName': 'hive_db'},
                             'description': None,
                             'lastAccessTime': 1587498187000,
                             'name': 'genomic_bam',
                             'owner': 'maria_dev',
                             'parameters': {'EXTERNAL': 'TRUE',
                                            'skip.header.line.count': '1',
                                            'transient_lastDdlTime': '1587498187'},
                             'partitionKeys': None,
                             'qualifiedName': 'default.genomic_bam@Sandbox',
                             'retention': 0,
                             'sd': {'guid': '68df2335-24a9-48a0-b08e-b171b86a6e51',
                                    'typeName': 'hive_storagedesc'},
                             'tableType': 'EXTERNAL_TABLE',
                             'temporary': False,
                             'viewExpandedText': None,
                             'viewOriginalText': None},
              'classifications': [],
              'create_time': datetime.datetime(2020, 4, 21, 19, 43, 7, 812000, tzinfo=tzutc()),
              'created_by': 'maria_dev',
              'guid': '6cabc390-f2d3-4faf-9498-89c2fa2f1950',
              'home_id': None,
              'is_proxy': None,
              'meanings': None,
              'provenance_type': 0,
              'proxy': False,
              'relationship_attributes': None,
              'status': 'ACTIVE',
              'type_name': 'hive_table',
              'update_time': datetime.datetime(2020, 4, 21, 19, 43, 7, 812000, tzinfo=tzutc()),
              'updated_by': 'maria_dev',
              'version': 0},
              ...]
 'status': 'OK',
 'summary': "You are off to great places, today's your day."}
```

4. Get url to the data bundle
```
$ msk-mind download-files "hive_table where name like '*genomic*' and createTime >= '2020-04-20'"

{'description': 'https://msk-mind.github.io/docs/ops.html#happy_day_mate',
 'payload': 'http://<vm_ip>:50070/data/tmp/1588078078927.gz',
 'status': 'OK',
 'summary': "You are off to great places, today's your day."}
```
