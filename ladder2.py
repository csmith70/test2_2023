import LHD

data_in = LHD.load_comma_data('Tanom.csv', 4)
years = data_in[:,0]
print(years)
