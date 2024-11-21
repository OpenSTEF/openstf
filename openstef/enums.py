# SPDX-FileCopyrightText: 2017-2023 Contributors to the OpenSTEF project <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
from enum import Enum

class BiddingZone(Enum):
    DE_50HZ = 'DE_50HZ'
    AL = 'AL'
    DE_AMPRION = 'DE_AMPRION'
    AT = 'AT'
    BY = 'BY'
    BE = 'BE'
    BA = 'BA'
    BG = 'BG'
    CZ_DE_SK = 'CZ_DE_SK'
    HR = 'HR'
    CWE = 'CWE'
    CY = 'CY'
    CZ = 'CZ'
    DE_AT_LU = 'DE_AT_LU'
    DE_LU = 'DE_LU'
    DK = 'DK'
    DK_1 = 'DK_1'
    DK_1_NO_1 = 'DK_1_NO_1'
    DK_2 = 'DK_2'
    DK_CA = 'DK_CA'
    EE = 'EE'
    FI = 'FI'
    MK = 'MK'
    FR = 'FR'
    DE = 'DE'
    GR = 'GR'
    HU = 'HU'
    IS = 'IS'
    IE_SEM = 'IE_SEM'
    IE = 'IE'
    IT = 'IT'
    IT_SACO_AC = 'IT_SACO_AC'
    IT_CALA = 'IT_CALA'
    IT_SACO_DC = 'IT_SACO_DC'
    IT_BRNN = 'IT_BRNN'
    IT_CNOR = 'IT_CNOR'
    IT_CSUD = 'IT_CSUD'
    IT_FOGN = 'IT_FOGN'
    IT_GR = 'IT_GR'
    IT_MACRO_NORTH = 'IT_MACRO_NORTH'
    IT_MACRO_SOUTH = 'IT_MACRO_SOUTH'
    IT_MALTA = 'IT_MALTA'
    IT_NORD = 'IT_NORD'
    IT_NORD_AT = 'IT_NORD_AT'
    IT_NORD_CH = 'IT_NORD_CH'
    IT_NORD_FR = 'IT_NORD_FR'
    IT_NORD_SI = 'IT_NORD_SI'
    IT_PRGP = 'IT_PRGP'
    IT_ROSN = 'IT_ROSN'
    IT_SARD = 'IT_SARD'
    IT_SICI = 'IT_SICI'
    IT_SUD = 'IT_SUD'
    RU_KGD = 'RU_KGD'
    LV = 'LV'
    LT = 'LT'
    LU = 'LU'
    LU_BZN = 'LU_BZN'
    MT = 'MT'
    ME = 'ME'
    GB = 'GB'
    GE = 'GE'
    GB_IFA = 'GB_IFA'
    GB_IFA2 = 'GB_IFA2'
    GB_ELECLINK = 'GB_ELECLINK'
    UK = 'UK'
    NL = 'NL'
    NO_1 = 'NO_1'
    NO_1A = 'NO_1A'
    NO_2 = 'NO_2'
    NO_2_NSL = 'NO_2_NSL'
    NO_2A = 'NO_2A'
    NO_3 = 'NO_3'
    NO_4 = 'NO_4'
    NO_5 = 'NO_5'
    NO = 'NO'
    PL_CZ = 'PL_CZ'
    PL = 'PL'
    PT = 'PT'
    MD = 'MD'
    RO = 'RO'
    RU = 'RU'
    SE_1 = 'SE_1'
    SE_2 = 'SE_2'
    SE_3 = 'SE_3'
    SE_4 = 'SE_4'
    RS = 'RS'
    SK = 'SK'
    SI = 'SI'
    GB_NIR = 'GB_NIR'
    ES = 'ES'
    SE = 'SE'
    CH = 'CH'
    DE_TENNET = 'DE_TENNET'
    DE_TRANSNET = 'DE_TRANSNET'
    TR = 'TR'
    UA = 'UA'
    UA_DOBTPP = 'UA_DOBTPP'
    UA_BEI = 'UA_BEI'
    UA_IPS = 'UA_IPS'
    XK = 'XK'
    DE_AMP_LU = 'DE_AMP_LU'
    
    
class ModelType(Enum):
    XGB = "xgb"
    XGB_QUANTILE = "xgb_quantile"
    XGB_MULTIOUTPUT_QUANTILE = "xgb_multioutput_quantile"
    LGB = "lgb"
    LINEAR = "linear"
    LINEAR_QUANTILE = "linear_quantile"
    ARIMA = "arima"
    FLATLINER = "flatliner"


class ForecastType(Enum):
    DEMAND = "demand"
    WIND = "wind"
    SOLAR = "solar"
    BASECASE = "basecase"


class PipelineType(Enum):
    FORECAST = "forecast"
    TRAIN = "train"
    HYPER_PARMATERS = "hyper_parameters"
