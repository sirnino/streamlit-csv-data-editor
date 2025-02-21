import pandas as pd

import utils.render as R
import utils.data as D


title = "CSV Data Editor"

R.init(title=title)
R.render_sidebar()

uploaded_file, separator, submitted = R.render_header(title=title)

if submitted and uploaded_file:
    df = pd.read_csv(uploaded_file, sep=separator)
    row_count = D.get_row_count(df)
    categories = D.get_types_dict(df)
    
    R.render_metrics(uploaded_file.name, row_count, categories)
    
    #R.render_data(df, f"edited_{uploaded_file.name}")
    R.render_chart_area(df)
    