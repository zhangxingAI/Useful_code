import pandas as pd
'''
通过对股票的各项指标的权重分析选出排位在前20的股票，并写入excel
'''
df = pd.read_csv('个股价格.csv')

avg = df.groupby(df['股票代码']).mean()
weight = avg.eval('权重求和 = 2*日个股交易股数+2*日个股交易金额+2*日个股流通市值+2*日个股总市值 +2*日个股回报率')
weight_sort = weight.sort_values(by='权重求和',ascending=False)

weight_sort_20 = weight_sort[0:19]
weight_sort_20.to_excel('sort_20.xlsx')