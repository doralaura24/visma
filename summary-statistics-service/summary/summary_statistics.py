def calculate_frequency(raw_data, target_column):
    raw_data.reset_index(inplace=True)
    raw_data.set_index(["CompanyId", str(target_column)], inplace=True)
    raw_data = raw_data.reset_index(inplace=False)
    raw_data['ColumnName'] = str(target_column)
    raw_data = raw_data.rename(columns={str(target_column): 'ColumnValue'})
    raw_data = raw_data.groupby(['CompanyId', 'ColumnName', 'ColumnValue']).size().reset_index()
    raw_data.rename(columns={raw_data.columns[3]: "Count"}, inplace=True)
    return (raw_data)