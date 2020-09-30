import numpy as np
import pandas as pd
import gzip, sys

'''
Return single-cell cluster information in the table
---------------------
index | label | count
---------------------
where *index* - is internal cluster index, 
*label* - cluster name,
*count* - number of cells in the cluster
'''
def showClusters(nm):
    cc = pd.read_csv('../data/'+nm+'/cell_groupings.csv', header=None, index_col=0).T
    jj = cc[['Cluster Index', 'Cluster Label']].\
        drop_duplicates().\
        sort_values(by='Cluster Index').\
        reset_index(drop=True)
    jj.columns = ['index', 'label']
    counts = pd.DataFrame(cc['Cluster Index'].value_counts()).reset_index()
    counts.columns = ['index', 'count']
    jj = jj.merge(counts, on='index')
    jj[['index','count']] = jj[['index','count']].astype(np.int64)
    return jj

'''
Extract all gene names into text
and return pandas Series of names
'''
def extractGenes(nm):
    gList = []
    fn = '../data/'+nm+'/expr.csv.gz'
    with gzip.open(fn) as gzo:
        c = 0
        for ln in gzo:
            c += 1
            gene = str(ln)[2:].split(',')[0].split('|')[0].strip()
            gList.append(gene)
    return pd.Series(gList, dtype='string')

'''
Open folder with SPRING data and calculate
counts for every gene in every cluster.
*nm* - folder name (NF stage)
*gene_list* - list with gene names
*cellCount* - print cell count instead of ctRNA summary
Returns well-prepared DataFrame
'''
def drawTable(nm, gene_list, cellCount = False):
    print('Extracting genes..')
    selected = []
    with gzip.open('../data/'+nm+'/expr.csv.gz') as gzo:
        for ln in gzo:
            gene = str(ln)[2:].split(',')[0].split('|')[0].strip()
            if gene in  gene_list:
                selected += [ str(ln)[2:-3].split(',') ]
                print(gene, ' extracted!')
    print('Done!')
    zz = pd.DataFrame(selected)
    # gen correct name column
    clm = list(zz.columns)
    clm[0] = 'name'
    zz.columns = clm
    zz[['name']] = zz[['name']].applymap(lambda x: x.split('|')[0].strip())
    # transpose and prepare for merge
    zzt = zz.T
    zzt.columns = zzt.loc['name']
    zzt = zzt.drop(index='name')
    zzt = zzt.astype(np.float64)
    if cellCount:
        zzt = zzt.apply(np.sign)
        zzt = zzt.astype(np.int64)
    # merge grouping with selected genes
    cgrp = pd.read_csv('../data/'+nm+'/cell_groupings.csv', header=None, index_col=0).T
    cgrp[['Cluster Index']] = cgrp[['Cluster Index']].astype(np.int64)
    cgrp_plus = cgrp.merge(zzt, left_index=True, right_index=True)
    # finalizing counting
    sumTbl = cgrp_plus.groupby('Cluster Index').sum()
    sc = showClusters(nm)
    sc0 = sc[['index', 'label']]
    resTbl = sc0.merge(sumTbl, left_on='index', right_index=True)
    return resTbl