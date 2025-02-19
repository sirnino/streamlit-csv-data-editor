def get_row_count(df):
    return df.shape[0]

def get_types_dict(df, column_name='type'):
    output_dict = {}
    if column_name in df.columns:
        types = df[column_name].unique()
        for t in types:
            amount_for_type = df[df[column_name]==t].shape[0]
            perc = round(100*amount_for_type/df.shape[0], 1)
            output_dict[t] = perc
    
    return output_dict