# first, we need to construct a dataset that has each parameter as a feature. to do this we have to deconstruct
#the 'parameter' column into new columns.
import pandas as pd
import dask.dataframe as dd
from tqdm import tqdm
pd.options.mode.chained_assignment = None

# function to check if parameter is a number.
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
############################################################## data column types
column_types = {
    'fit_intercept':bool,
    'loss':str,
    'C':float,
    'alpha':float,
    'learning_rate':str,
    'penalty':str,
    'l1_ratio':float,
    'eta0':float,
    'power_t':int,
    'min_weight_fraction_leaf':float,
    'criterion':str,
    'n_estimators':int,
    'max_features':str,
    'Unnamed: 19':str,
    'degree':int,
    'kernel':str,
    'gamma':str,
    'coef0':float,
    'dual':bool,
    'weights':str,
    'n_neighbors':int,
    'fit_prior':bool,
    'max_depth':int,
    'binarize':bool,
}


######################################################### get data metafeatures
# metafeatures = pd.read_csv('data_metafeatures.csv',sep=',',index_col=0)
# print('loaded ',
#       metafeatures.shape[1]-1, ' metafeatures for ',
#       metafeatures.shape[0], ' datasets')
################################################################# get ML results
print('loading pmlb results data...')
data = pd.read_csv('sklearn-benchmark5-data.tsv.gz', sep='\t',
                   names=['dataset',
                         'classifier',
                         'parameters',
                         'accuracy',
                         'macrof1',
                         'bal_accuracy']).fillna('')
data.describe()


############################################## make typed columns for parameters
print('converting parameters to features...')

for i,p in tqdm(enumerate(data['parameters'][:1000])):
    d = dict()
    for ps in p.split(','):
        if is_number(ps.split('=')[-1]):
            d[str(ps.split('=')[0])] = float(ps.split('=')[-1])
        else:
            d[str(ps.split('=')[0])] = ps.split('=')[-1]

    # add columns to data
    for key, val in d.items():
        if key is not '':
            if key not in data.columns:
                if column_types[key] == str:
                    data[key] = ' '
                    data[key] = data[key].apply(lambda x: str(x))
                elif column_types[key] == float:
                    data[key] = 0.0
                    data[key] = data[key].apply(lambda x: float(x))
                elif column_types[key] == bool:
                    data[key] = False
                    data[key] = data[key].apply(lambda x: bool(x))
                else:
                    data[key] = 0
                    data[key] = data[key].apply(lambda x: int(x))


data.to_csv('sklearn-benchmark5-data-ml-parameters-nan-small.tsv',
            sep='\t',index=False)
################################################################# fill in values
def write_param(x):
    #x: dataframe partition
    #gNB has no parameters so ignore

    for i,row in x.iterrows():
        p = row['parameters']
        # try:
        if row['classifier'] == 'GaussianNB' or type(row['parameters'])==str:
            continue
        # except KeyError:
        #     print('x[''parameters'']:',x['parameters'])
        #     print('i:',i,'p:',p)

        d = dict()
        try:
            for ps in p.split(','):
                if ps.split('=')[0] != '':
                    if is_number(ps.split('=')[-1]):
                        d[str(ps.split('=')[0])] = float(ps.split('=')[-1])
                    else:
                        d[str(ps.split('=')[0])] = ps.split('=')[-1]

                for key, val in d.items():
                    if key not in x.columns:
                        print('key:',key,' not in ',x.columns)
                        continue
                    if key == 'loss':
                        x[key] = x[key].apply(lambda i: str(i))
                    # try:
                    x.set_value(i,key,val)
                    # except ValueError:
                    #     print('key:',key,'val:',val)
                    #     raise ValueError
                    # assert( x[i][key] == val)
        except Exception:
            print('i:',i,'p:',p)
            # print(repr(e))
            raise ValueError
    return x
import pandas as pd
from dask import delayed
import dask.dataframe as dd
print('reading results data...')
pdf = pd.read_csv('sklearn-benchmark5-data-ml-parameters-nan-small.tsv', sep='\t')
df = dd.from_pandas(pdf,npartitions=20)
print('mapping parameters values to data...')
df2 = df.map_partitions(lambda x: write_param(x))

df2.to_csv('sklearn-benchmark5-data-ml-parameters.tsv',
            sep='\t',index=False)