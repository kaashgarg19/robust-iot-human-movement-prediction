# Flagship Repository Audit

**Audit scope:** `research/iot-human-movement-prediction/` on the `main` branch.

## Overall assessment

The repository is a clean research portfolio foundation. The dataset source and licence are documented, the MSc work is separated from the later research extension, and the main research workflow is documented. A few technical reproducibility items can be added as the project develops.

## File-by-file status

| Area | Status | Audit finding |
|---|---|---|
| `README.md` | PASS | Clear project overview and MSc connection. |
| `docs/research_questions.md` | PASS | Research questions are clearly stated. |
| `docs/msc_foundation.md` | PASS | Separates the MSc foundation from the later extension. |
| `docs/msc_original_implementation.md` | PASS | Documents the recovered historical implementation. |
| `docs/msc_results.md` | PASS | Historical accuracy results are clearly labelled. |
| `docs/dissertation.md` | PASS | Records the dissertation without publishing private academic material. |
| `docs/codebook.md` | PASS | Dataset fields and key data-quality decisions are documented. |
| `docs/dataset_documentation.md` | PASS | Dataset source, structure and licence are documented. |
| `docs/methodology.md` | PASS | Describes the main data and modelling workflow. |
| `docs/experimental_protocol.md` | PASS | Records the current experiment sequence and evaluation rules. |
| `docs/reproducibility.md` | PASS | Provides setup instructions, dataset checks and evaluation order. |
| `notebooks/01_data_validation.ipynb` | PASS | First-step dataset validation notebook. |
| `notebooks/02_msc_original_analysis.ipynb` | PASS | Historical MSc reconstruction is clearly labelled. |
| `notebooks/03_baseline_models.ipynb` | PASS | Implements the documented random evaluation. |
| `notebooks/04_temporal_evaluation.ipynb` | PASS | Implements chronological evaluation. |
| `notebooks/05_robustness_analysis.ipynb` | PASS | Documents the robustness analysis and result references. |
| `src/data.py` | PASS | Data loading and validation utilities. |
| `src/splits.py` | PASS | Random and chronological split helpers. |
| `src/models.py` | PASS | Model configurations are defined explicitly. |
| `src/evaluation.py` | PASS | Evaluation functions are centralised. |
| `src/msc_original.py` | PASS | Historical reconstruction is kept separate from the current workflow. |
| `results/msc_original_results.csv` | PASS | Historical results are preserved in machine-readable form. |
| `results/canonical_research_metrics.csv` | PASS | Current compact research metrics are preserved. |
| `figures/msc_model_accuracy.svg` | PASS | Clearly presented as a reconstruction of the historical results. |
| `figures/msc_research_bridge.svg` | PASS | Shows the connection between the MSc work and current research. |
| `data/raw/` | PASS | Raw third-party data is not redistributed in the repository. |
| `requirements.txt` | PASS | Main project dependencies are listed. |

## Technical improvements for later

These are project-development items rather than unfinished documentation:

1. Record the SHA-256 hash of the exact local dataset used for each canonical run.
2. Record exact Python and package versions for reproducible reruns.
3. Add detailed result files for individual robustness experiments when they are ready for publication.
4. Keep figures and result files linked to the relevant experiment and code version.

## Current repository position

The basic documentation phase is complete. The repository now gives a reader a clear path through:

**MSc project → dataset → methodology → original results → research extension**

Further technical analysis can be added later without changing the basic structure.
