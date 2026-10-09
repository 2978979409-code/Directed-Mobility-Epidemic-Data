# Directed Mobility Controls Invasion Thresholds

Data release for the manuscript:

> Yang Yang and Xiaoling Han. *Directed Mobility Controls Invasion Thresholds
> in Discrete-Time Patch Epidemic Models*.

This repository follows the transparent data-release pattern used by Tang et al.
for their mechanistic and deep-learning study of susceptible heterogeneity:
source data, processed data, provenance notes, and integrity checks are kept
together in one public repository.

## Contents

| Path | Contents |
|---|---|
| data/ | Synthetic numerical outputs used for threshold, directionality, positivity, time-series, and small-step consistency results |
| empirical_data/raw/ | Frozen third-party source snapshots: Kaggle mobility/health data, the New York Times state COVID-19 archive, and the U.S. Census ACS 2021 migration table |
| empirical_data/data/ | Cleaned and derived empirical tables used in the manuscript |
| empirical_data/reports/ | Source URLs, license metadata, and processing notes supplied with the manuscript archive |
| tools/validate_data.py | Standard-library validation of file hashes, CSV schemas, row counts, and the nested Kaggle ZIP |
| MANIFEST_SHA256.json | SHA-256, byte size, and CSV row/column metadata for every released data file |

The complete release contains 23 data/provenance files. The two largest CSV
files are the frozen integrated Kaggle input and its cleaned derivative. No
individual-level tracking record is included; the files contain county/day,
state/day, and aggregate migration information.

## Validate the release

Python 3.9 or later is sufficient; the validator uses only the standard library.

Run: python tools/validate_data.py

A successful run prints: DATA_VALIDATION_PASS 23 files

GitHub Actions runs the same validation after every push.

## Empirical sources

The frozen empirical inputs come from:

1. **US COVID-19 & Human Mobility (2021)** by Amro Askar on Kaggle. The
   accompanying Kaggle metadata records the dataset license as CC0: Public
   Domain.
2. **The New York Times COVID-19 data in the United States**, used as an
   independent state-level health-data cross-check.
3. **U.S. Census Bureau ACS 2021 State-to-State Migration Flows**, used as a
   directional mobility proxy.

Exact URLs, frozen metadata, and processing choices are recorded in
[the source report](empirical_data/reports/source_urls_and_reproducibility.md).
Source-specific terms are summarized in
[SOURCES_AND_LICENSES.md](SOURCES_AND_LICENSES.md).

## Interpretation

The empirical analysis is a mechanism illustration. Annual migration counts are
used as directional weights; they are not observed daily infectious-movement
rates. The selected New Jersey–Pennsylvania comparison does not identify the
full nonlinear epidemic map or establish a causal mobility effect.

The supplied archive states that duplicate Kaggle county/date rows were
collapsed before analysis: health-count variables use the maximum value and
Google mobility variables use their mean. It also states that New Jersey and
Pennsylvania were selected after comparison with the independent NYT archive.
These statements describe supplied provenance. The generation scripts named in
the draft manuscript were not present in the provided ZIP.

This repository therefore supports access to the exact supplied tables,
integrity and schema verification, and inspection of numerical and empirical
outputs. It does not by itself regenerate the processed empirical tables or
synthetic outputs from model code.

## Related published study

The repository layout was informed by:

> Tang B, Ma K, Liu Y, Wang X, Tang S, Xiao Y, et al. (2024). Managing
> spatio-temporal heterogeneity of susceptibles by embedding it into an
> homogeneous model: A mechanistic and deep learning study. *PLOS Computational
> Biology*, 20(9), e1012497.
> https://doi.org/10.1371/journal.pcbi.1012497

Published data-and-code repository:
https://github.com/yanliu0321/Managing-spatial-temporal-heterogeneity-of-susceptibles

## Citation

Citation metadata is in [CITATION.cff](CITATION.cff). The manuscript is not
assigned a DOI in this repository.

## License and attribution

No single blanket license is applied because the repository mixes
author-generated outputs with third-party snapshots. Consult
[SOURCES_AND_LICENSES.md](SOURCES_AND_LICENSES.md) before redistribution.

