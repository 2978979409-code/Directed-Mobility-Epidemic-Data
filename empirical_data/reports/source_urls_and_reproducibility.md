# Empirical data sources and reproducibility

Primary integrated data:
- Kaggle data set: US COVID-19 & Human Mobility (2021)
- Kaggle reference: amroaskar/us-covid-19-and-human-mobility-2021
- Dataset page: https://www.kaggle.com/datasets/amroaskar/us-covid-19-and-human-mobility-2021
- Download endpoint: https://www.kaggle.com/api/v1/datasets/download/amroaskar/us-covid-19-and-human-mobility-2021
- Metadata endpoint: https://www.kaggle.com/api/v1/datasets/view/amroaskar/us-covid-19-and-human-mobility-2021
- License reported by Kaggle metadata: CC0: Public Domain
- Last updated in Kaggle metadata: 2026-01-15T16:24:14.543Z

Independent health-data cross-check:
- NYT official state COVID-19 archive: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

Directed mobility proxy:
- U.S. Census ACS 2021 state-to-state migration table: https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2021/state-to-state-migration/State_to_State_Migrations_Table_2021.xls

Processing choices:
- Duplicate county-date rows in the Kaggle file are collapsed before analysis.
- Health counts use the maximum duplicate value to avoid double-counting cases.
- Google mobility fields are averaged across duplicate rows.
- New Jersey and Pennsylvania are used because their cleaned Kaggle state aggregates agree closely with the NYT state archive.
- The empirical analysis is an illustration of the threshold mechanism, not a full identification of the nonlinear epidemic map.

Reproducibility:
- Main script: generate_submission_figures.py
- Processed data: empirical_data/data
- Figures: figures/empirical_validation_covid_nj_pa.pdf and figures/empirical_data_quality_crosscheck.pdf
- No random sampling is used.
