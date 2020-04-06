# MSK MIND CLI

Python Command Line Interface to access MSK MIND

## Installation
### Download executable
Simply download `msk-mind` executable.
*Note*: This executable is generated on macOS. It will not work on linux machines.  
To generate an executable, follow the steps for development, then run
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
msk-mind --help
msk-mind business --help
msk-mind operation --help
```

### Examples

1. Get patients with clinical stage '3C'
```
msk-mind business get_metadata "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"
```
Output:
```
{"patient.patient_id": "SPECTRUM-OV-004", "patient.dmp_patient_id": "P-0039734", "patient.gender": "FEMALE", "patient.race": "WHITE", "patient.vital_status": "1.0", "patient.patient_last_known_alive_age": 26055, "patient.icdo_histology_code": "M8461/3", "patient.icdo_site_code": "C569", "patient.diagnosis_pathology_stage_group": "3C", "patient.diagnosis_clinical_stage_group": "3C", "patient.age_at_diagnosis": 25921, "patient.project_id": "OV"}
{"patient.patient_id": "SPECTRUM-OV-005", "patient.dmp_patient_id": "P-0040521", "patient.gender": "FEMALE", "patient.race": "WHITE", "patient.vital_status": "1.0", "patient.patient_last_known_alive_age": 21413, "patient.icdo_histology_code": "M8461/3", "patient.icdo_site_code": "C569", "patient.diagnosis_pathology_stage_group": "", "patient.diagnosis_clinical_stage_group": "3C", "patient.age_at_diagnosis": 21050, "patient.project_id": "OV"}
...
```

2. Get file information
```
msk-mind operation get_files '{
  "dmpIds": ["P-0039384"],
  "createTime": "2020-03-01",
  "fileType":"IMAGE_HNE"
}'
```
Output:
```
{'create_time': datetime.date(2020, 3, 2),  'id': 'P-0039384',  'path': '/data/P-0039384/1500649.svs',  'type': 'IMAGE_HNE'}
{'create_time': datetime.date(2020, 3, 2),  'id': 'P-0039384',  'path': '/data/P-0039384/1500784.svs',  'type': 'IMAGE_HNE'}
...
```

