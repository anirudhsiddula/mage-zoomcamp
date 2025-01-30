if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from mage_ai.data_preparation.variable_manager import set_global_variable, get_global_variable



@transformer
def transform(*args, **kwargs):
    colors = kwargs['taxis']
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
    
    url_list = [[{color: f"{base_url}{color}/{color}_tripdata_2021-01.csv.gz"} for color in colors]]
    
    return url_list