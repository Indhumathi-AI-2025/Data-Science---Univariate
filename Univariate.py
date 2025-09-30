class univariate():
#QuanQual Function
    def QuanQual(dataset):
        qual = []
        quan = []
        for ColumnName in dataset.columns:
            if (dataset[ColumnName].dtype == 'O'):
                qual.append(ColumnName)
            else:
                quan.append(ColumnName)
        return quan, qual