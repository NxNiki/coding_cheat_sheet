# check if dir exists:

import os
from os import path
#trying to make directory if it does not already exist:
if not os.path.exists(result_dir):
    os.mkdir(result_dir)
    
# pandas:
spm_vbm_aal = pd.read_csv(data_dir+"/GMV_AAL_AvgExtract.csv", delimiter = ",", index_col = [0])

spm_vbm_aal.iloc[:,0].replace(to_replace=\
                              r'.nii.gz',
                              value='', regex=True, inplace = True)
                              
# set column name:
aal_label = pd.read_csv(atlas_dir+"/AAL_116_Label.csv", delimiter = ',')
spm_vbm_aal.columns = ['names'] + aal_label['ROIname'].to_list()

# drop column:
label_fa = label_fa.drop(['Unnamed: 0.1'], axis = 1)


# add 'label' to column names to avoid duplication with tract features:
label_fa.columns = [str(col) + '(label)' for col in label_fa.columns]

multimodal_features = pd.concat([vbm, label_fa*-1, tract_fa*-1], axis = 1,)


# change data type in dataframe:
behav_data = behav_data.astype({'SUBJID': 'int64'})
behav_data["Med_Rating"] = behav_data["Med_Rating"].apply(pd.to_numeric, errors='coerce')

# select rows based on value in column:
behav_data = behav_data.loc[behav_data["Med_Rating"]<2,:]

# merge data frame:
behav_feature = behav_data_hc.merge(multimodal_features, how = "inner", right_on = "names", left_on = "SUBJID")


# stats by group:
print(subject_split_info[["Train_index", "Sex"]].groupby(["Train_index", "Sex"]).size())
print(subject_split_info[["Train_index", "age_at_cnb"]].groupby(["Train_index"]).mean())
subject_split_info[["Train_index", "age_at_cnb"]].groupby(["Train_index"]).std()
