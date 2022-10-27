# SPDX-FileCopyrightText: 2017-2022 Contributors to the OpenSTEF project <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
"""Specifies the prediction job dataclass."""
from typing import List, Optional, Union

from pydantic import BaseModel

from .model_specifications import ModelSpecificationDataClass
from .split_function import SplitFuncDataClass


class PredictionJobDataClass(BaseModel):
    """Holds all information about the specific forecast that has to be made."""
    id: Union[int, str]
    """The predictions job id (often abreviated as pid)."""
    model: str
    """The model type that should be used.
    
    Options are:
        - ``"xgb"``
        - ``"xgb_quantile"``
        - ``"lgb"``
        - ``"linear"``
        - ``"proloaf"`` (extra dependencies requiered, see README)
    
    If unsure what to pick, choose ``"xgb"``.
    
    """
    forecast_type: str
    """The type of forecasts that should be made.
    
    Options are:
        - ``"demand"``
        - ``"wind"``
        - ``"basecase"``   
        
    If unsure what to pick, choose ``"demand"``.
    
    """
    horizon_minutes: int
    """The horizon of the desired forecast in minutes."""
    resolution_minutes: int
    """The resolution of the desired forecast in minutes."""
    lat: float
    """Latitude of the forecasted location in degrees."""
    lon: float
    """Longitude of the forecasted location in degrees."""
    name: str
    """Name of the forecast, e.g. the location name."""
    train_components: Optional[bool]
    """Whether splitting the forecasts in wind, solar, rest is desired."""
    description: Optional[str]
    """Optional description of the prediction job for human reference."""
    quantiles: Optional[List[float]]
    """Quantiles that have to be forecasted."""
    train_split_func: Optional[SplitFuncDataClass]
    """Optional custom splitting function for operational procces."""
    backtest_split_func: Optional[SplitFuncDataClass]
    """Optional custom splitting function for backtesting."""
    train_horizons_minutes: Optional[List[int]]
    """List of horizons that should be taken into account during training."""
    default_modelspecs: Optional[ModelSpecificationDataClass]
    """Default model specifications"""
    save_train_forecasts: bool = False
    """Indicate wether the forecasts produced during the training process should be saved."""
    completeness_treshold: float = 0.5
    """Minimum fraction of data that should be available for making a regular forecast."""
    minimal_table_length: int = 100
    """Minimum length (in rows) of the forecast input for making a regular forecast."""    
    flatliner_treshold: int = 24
    """Number of consecutive values that have to be constant to detect a flatliner. """
    depends_on: Optional[List[Union[int, str]]]
    """Link to another prediction job on which this prediction job might depend."""    
    sid: Optional[str] 
    """Only required for create_solar_forecast task"""
    turbine_type: Optional[str]  
    """Only required for create_wind_forecast task"""
    n_turbines: Optional[float]  
    """Only required for create_wind_forecast task"""
    hub_height: Optional[float]  
    """Only required for create_wind_forecast task"""
    
    class Config:
        """Pydantic model configuration.

        This following configuration is needed to prevent ids in "depends_on" to be converted from int to str when we
        use integer ids.

        """

        smart_union = True

    def __getitem__(self, item: str) -> any:
        """Allows us to use subscription to get the items from the object."""
        return getattr(self, item)

    def __setitem__(self, key: str, value: any) -> None:
        """Allows us to use subscription to set the items in the object."""
        if hasattr(self, key):
            self.__dict__[key] = value
        else:
            raise AttributeError(f"{key} not an attribute of prediction job.")

    def get(self, key: str, default: any = None) -> any:
        """Allows to use the get functions similar to a python dict."""
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return default
