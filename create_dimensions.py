import pandas as pd
pd.set_option('max_rows', 90)
pd.set_option('max_columns', 80)
from data_extraction import combined_df

# creating the dimmesion tables for the data warehouse
dim_branch = combined_df[['unique_bank_branch_id', 'branch_unique_number', 'branch_address',
    'branch_city_name', 'branch_county_name', 'branch_state', 'branch_zipcode', 'branch_service_type',
    'branch_city', 'branch_country_name', 'branch_county_number', 'branch_name', 'branch_state_name',
    'acquisition_date', 'branch_location_established_date', 'holding_company_type', 'bank_office_identifier']]

dim_bank = combined_df[[ 'bank_name', 'unique_bank_id_fed_board', 'bank_hq_name', 'cityhcr', 'bank_hq_state',
    'unique_bank_id_number', 'only_main_office_no_branches', 'address', 'hq_city', 'hq_zipcode', 'bank_class',
    'bank_category', 'bank_asset_classification_category', 'hq_state_name', 'country_hq',
    'primary_industry_classification', 'hq_state']]

dim_area_population = combined_df[['county_2.5_million+_name', 'urban_area_10000_under_50000', 
                                   'urban_area_50000+']]
dim_area_population = dim_area_population.iloc[:, [0,2,4]] # getting rid of duplicate columns

dim_location = combined_df[['branch_longitude', 'branch_latitude', 'in_usa']]

dim_assets = combined_df[['total_assets']]

dim_date = combined_df[['year']] # keeping as a dataframe in order to load to sql_server

dim_charter = combined_df[['charter_type', 'charter_agency_name', 'charter_abbreviation']]

dim_fdic = combined_df[['fdic_regional_office_id', 'fdic_regional_office_name', 'fed_district_id', 
    'fed_district_name']]

dim_currency = combined_df[['currency_district_id', 'currency_district_name', 'regulatory_agency_name']]

# creating a Dataframe instead of a Series to be able to use ignore_index parameter (can't use on a Series)
dim_deposit_code = combined_df[['deposit_code']] 

dim_list = [dim_branch, dim_bank, dim_area_population, dim_location, dim_assets,
            dim_date, dim_charter, dim_fdic, dim_currency, dim_deposit_code]

key_list = ['branch_key', 'bank_key', 'area_population_key', 'location_key', 'assets_key',
            'date_key', 'charter_key', 'fdic_key', 'currency_key', 'deposit_code_key']

# creating the updated dimensions by dropping duplicate values and adding a surogate key to each
# dimension.  See key_list for surogate names. 
df_drop_duplicates_list = []
df_updated_list = []
index = 0
def update_dataframe(*args):
    for arg in args:
        arg = arg.drop_duplicates(ignore_index=True).reset_index()
        df_drop_duplicates_list.append(arg)
    for df in df_drop_duplicates_list:
        global index
        df = df.rename(columns={'index': key_list[index]})
        df_updated_list.append(df)
        index += 1

update_dataframe(*dim_list)

# assigning back to the original dataframes
dim_branch, dim_bank, dim_area_population, dim_location, dim_assets,dim_date, \
dim_charter, dim_fdic, dim_currency, dim_deposit_code = df_updated_list













# index = 0
# for item in df2_list:
#     item = item.rename(columns={'index': key_list[index]})
#     df3_list.append(item)
#     index += 1
# df3_list[3]

# len(df3_list)


# list10 = [5,6,7]
# enumerate(list10)

# for num, ele in enumerate(list10):
#     print(num)

# list_10 = []
# list9 = [5,6,7]

# def n(*args):
#     for arg in args:
#         arg = arg + 10
        
#         print(arg)

# n(5,6,7)

# index = 0
# for item in key_list:
#     print(key[index])
#     index += 1

# # list7 = []
# for i in range(len(key_list)):
#     print(key_list[i])

# for key in key_list:
#     print(key)

# list8 = []
# for key in key_list:
#     list8.append(key)

# list8

# df_list = []
# def update_df(*args):
#     for arg in args:
#         arg = arg.drop_duplicates(ignore_index=True).reset_index()
#         for key in key_list:
#             arg.rename(columns={'index': key}, inplace=True)
#         df_list.append(arg)

# update_df(*dim_list)

# def to_sql_table(df):
#     df.drop_duplicates(ignore_index=True, inplace=True) # this worked but gave copy caveot
# to_sql_table(dim_date)
# print(dim_date)

# THIS ALL WORKED!!!
# def try_2(df):
#     df = df.drop_duplicates(ignore_index=True).reset_index()
#     df = df.rename(columns={'index': 'try_key'})
#     return df
# dim_date = try_2(dim_date)
# print(dim_date)

# THIS ALL WORKED!!
# def update_df(*args):
#     for arg in args:
#        arg = arg.drop_duplicates(ignore_index=True).reset_index()
#     return arg
# dim_date = update_df(dim_date)

# THIS ALL WORKED!!!
# new_dic = []
# def update2(*args):
#     for arg in args:
#         arg = arg.drop_duplicates(ignore_index=True).reset_index()
#         new_dic.append(arg)
# update2(dim_date, dim_deposit_code)
# dim_date, dim_deposit_code = new_dic
# dim_date
# dim_deposit_code

# df_list = []
# def update_df(*args):
#     for arg in args:
#         arg = arg.drop_duplicates(ignore_index=True).reset_index()
#         arg = arg.rename(columns={'index': key_list[0]})
#         df_list.append(arg)

# update_df(dim_branch, dim_bank, dim_area_population, dim_location, dim_assets,
#                     dim_date, dim_charter, dim_fdic, dim_currency, dim_deposit_code)