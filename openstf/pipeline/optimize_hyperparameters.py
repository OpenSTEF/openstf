# SPDX-FileCopyrightText: 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
import pandas as pd
import optuna
import structlog

from openstf.model.objective_creator import ObjectiveCreator
from openstf.feature_engineering.feature_applicator import TrainFeatureApplicator
from openstf.validation import validation

# This is required to disable the default optuna logger and pass the logs to our own
# structlog logger
optuna.logging.enable_propagation()  # Propagate logs to the root logger.
optuna.logging.disable_default_handler()  # Stop showing logs in sys.stderr.

logger = structlog.get_logger(__name__)

# See https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize
N_TRIALS: int = 8  # The number of trials.
TIMEOUT: int = 200  # Stop study after the given number of second(s).
TRAIN_HORIZONS: list[float] = [0.25, 24.0]


def optimize_hyperparameters_pipeline(
    pj: dict,
    input_data: pd.DataFrame,
    horizons: list[float] = TRAIN_HORIZONS,
    n_trials: int = N_TRIALS,
    timeout: int = TIMEOUT,
) -> dict:
    """Optimize hyperparameters pipeline.

    Args:
        pj (dict): Prediction job
        input_data (pd.DataFrame): Raw training input data
        horizons (list[float]): horizons for feature engineering.
        n_trials (int, optional): The number of trials. Defaults to N_TRIALS.
        timeout (int, optional): Stop study after the given number of second(s).
            Defaults to TIMEOUT.

    Raises:
        ValueError: If the input_date is insufficient.

    Returns:
        dict: Optimized hyperparameters.
    """
    # Validate and clean data
    validated_data = validation.clean(validation.validate(input_data))

    # Check if sufficient data is left after cleaning
    if not validation.is_data_sufficient(validated_data):
        raise ValueError(
            f"Input data is insufficient for {pj['name']} "
            f"after validation and cleaning"
        )

    input_data_with_features = TrainFeatureApplicator(horizons=horizons).add_features(
        input_data
    )

    # Create objective (NOTE: this is a callable class)
    objective = ObjectiveCreator.create_objective(model_type=pj["model"])

    study = optuna.create_study(
        pruner=optuna.pruners.MedianPruner(n_warmup_steps=5), direction="minimize"
    )

    study.optimize(
        objective(input_data_with_features),
        n_trials=n_trials,
        timeout=timeout,
        callbacks=[_log_study_progress],
        show_progress_bar=False,
    )

    optimized_hyperparams = study.best_params
    optimized_error = study.best_value

    logger.info(
        f"Finished hyperparameter optimization, error objective {optimized_error} "
        f"and params {optimized_hyperparams}"
    )

    return optimized_hyperparams


def _log_study_progress(
    study: optuna.study.Study, trial: optuna.trial.FrozenTrial
) -> None:
    # Collect study and trial data
    trial_index = study.trials.index(trial)
    best_trial_index = study.trials.index(study.best_trial)
    value = trial.value
    params = trial.params
    duration = (trial.datetime_complete - trial.datetime_start).total_seconds()
    # Log information about this trial
    logger.debug(
        f"Trial {trial_index} finished with value: {value} and parameters: {params}."
        f"Best trial is {best_trial_index}. Iteration took {duration} s"
    )
