# Results

This directory contains **verified canonical result artifacts** only. Historical MSc results and current research-extension results are kept clearly separated.

## Currently committed

- `msc_original_results.csv` — historical MSc model-comparison accuracies recovered from the dissertation.
- `canonical_research_metrics.csv` — compact machine-readable record of the currently audited research-extension average-precision values and the chronological positive-event count.

## Research-extension artifacts still to be committed

The authoritative analysis record indicates the following outputs should eventually be added after their provenance, code version and dataset hash are confirmed:

- `MASTER_RANDOM_VS_TEMPORAL_RESULTS.csv`
- `TEMPORAL_MODEL_RESULTS.csv`
- `UNSEEN_DEVICE_RESULTS.csv`
- `FEATURE_ABLATION_RESULTS.csv`
- `THRESHOLD_SENSITIVITY_RESULTS.csv`
- `TEMPORAL_GAP_SENSITIVITY.csv`
- `TEMPORAL_RECALL_UNCERTAINTY.csv`
- `TEMPORAL_PR_CURVES.csv`
- `TEMPORAL_CALIBRATION.csv`
- `TEMPORAL_THRESHOLD_SNAPSHOTS.csv`
- `MASTER_EXPERIMENT_INDEX.csv`

These names are an output inventory, not a claim that those files are currently present.

## Canonical-result rule

Only results generated under the documented protocol should be treated as canonical. Later reruns with changed model configurations must be stored separately and must not silently replace audited results.

The research audit specifically excludes `FINAL_TEMPORAL_AUDIT_RESULTS.csv` from the canonical record because a later Random Forest configuration conflicted with the approved temporal result.

## Reproducibility

Each research result should eventually be traceable to an experiment ID, dataset hash, code version/commit, model configuration, split protocol and environment metadata. See `../docs/reproducibility.md` for the complete reproducibility checklist.
