Usage
=====

Commands
--------
.. click:: mind:cli
   :prog: mind
   :show-nested:

Examples
--------

A set of Zeppelin notebooks with CLI examples are provided.
The notebooks can be found on the hdp sandbox at http://<staging_ip>:9995/#/

- Get patient data where patients have clinical stage '3C'

.. code-block:: bash

    $ mind query "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'"

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


- Get url to patient data bundle

.. code-block:: bash

    $ mind download "SELECT * FROM patient WHERE diagnosis_clinical_stage_group = '3C'" --download

    {'payload': 'http://<vm_ip>:50070/data/tmp/1587571607403.gz',
     'status': 'OK'}


- Get operational metadata for files

.. code-block:: bash

    $ mind query "from hive_table where name like '*clinical*' select name, owner"

    {'payload': [{'name': 'clinical_patient', 'owner': 'raj_ops'},
                 {'name': 'clinical_diagnosis', 'owner': 'raj_ops'}],
    'status': 'OK'}


    $ mind query "from hdfs_path where name like '*genomic*' select name, qualifiedName, path"

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

- Get url to the data bundle

.. code-block:: bash

    $ mind download "hive_table where name like '*genomic*' and createTime >= '2020-04-20'"

    {'payload': 'http://<vm_ip>:50070/data/tmp/1588078078927.gz',
    'status': 'OK'}

- List available databases.

.. code-block:: bash

    $ mind list-databases

    clinical
    genomic

- List available tables.

.. code-block:: bash

    $ mind list-tables clinical

    | name       | description                                                                   |
    |------------+-------------------------------------------------------------------------------|
    | medication | None                                                                          |
    | patient    | (Patient level) de-identified patient IDs, demographics info, survival status |
    | diagnosis  | None                                                                          |

- List available columns.

.. code-block:: bash

    $ mind list-columns clinical patient

    | name                         | type   | description   |
    |------------------------------+--------+---------------|
    | dmp_patient_id               | string | None          |
    | patient_last_known_alive_age | int    | None          |
    | project_id                   | string | None          |
    | gender                       | string | None          |
    | race                         | string | None          |
    | patient_id                   | string | None          |
    | vital_status                 | string | None          |
