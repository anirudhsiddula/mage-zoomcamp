if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    color = data[1]
    data = data[0]
    zero_passengers_df = data[data['passenger_count'].isin([0])]
    zero_passengers_count = zero_passengers_df['passenger_count'].count()
    non_zero_passengers_df = data[data['passenger_count'] > 0]
    non_zero_passengers_count = non_zero_passengers_df['passenger_count'].count()
    print(f'Preprocessing: records with zero passengers: {zero_passengers_count}')
    print(f'Preprocessing: records with 1 passenger or more: {non_zero_passengers_count}')
    return [non_zero_passengers_df,color]