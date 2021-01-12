#!/usr/bin/env bash

export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow db init
# for airflow 2.0
airflow users create  --username admin \
          --firstname test \
          --lastname test \
          --role Admin \
          --email admin@example.org \
          -p admin
# for sample subdag
airflow pools set subdag_pool 124 "Subdag pool"

airflow scheduler & exec airflow webserver
