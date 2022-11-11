def pd_replace_value(df, col, old, new):
    df.loc[df[col] == old, col] = new
    return df
def sns_hist_and_bar(df, col, bins=10, figsize=(10, 5)):
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    sns.histplot(df[col], bins=bins, ax=ax[0])
    sns.barplot(x=df[col].value_counts().index, y=df[col].value_counts(), ax=ax[1])
    plt.show()
    def arrays_to_dict(arrays):
        return {k: v for k, v in zip(arrays[0], arrays[1])}
    
    country ={
        'tw': 'Taiwan',
        'jp'
    }
   # sorted  list based on date
   
   
   cpus=['AMD A10-Series 9600P 2.4GHz', 'AMD A10-Series 9620P 2.5GHz',
       'AMD A10-Series A10-9620P 2.5GHz', 'AMD A12-Series 9700P 2.5GHz',
       'AMD A12-Series 9720P 2.7GHz', 'AMD A12-Series 9720P 3.6GHz',
       'AMD A4-Series 7210 2.2GHz', 'AMD A6-Series 7310 2GHz',
       'AMD A6-Series 9220 2.5GHz', 'AMD A6-Series 9220 2.9GHz',
       'AMD A6-Series A6-9220 2.5GHz', 'AMD A8-Series 7410 2.2GHz',
       'AMD A9-Series 9410 2.9GHz', 'AMD A9-Series 9420 2.9GHz',
       'AMD A9-Series 9420 3GHz', 'AMD A9-Series A9-9420 3GHz',
       'AMD E-Series 6110 1.5GHz', 'AMD E-Series 7110 1.8GHz',
       'AMD E-Series 9000 2.2GHz', 'AMD E-Series 9000e 1.5GHz',
       'AMD E-Series E2-6110 1.5GHz', 'AMD E-Series E2-9000 2.2GHz',
       'AMD E-Series E2-9000e 1.5GHz', 'AMD FX 8800P 2.1GHz',
       'AMD FX 9830P 3GHz', 'AMD Ryzen 1600 3.2GHz',
       'AMD Ryzen 1700 3GHz', 'Intel Atom X5-Z8350 1.44GHz',
       'Intel Atom Z8350 1.92GHz', 'Intel Atom x5-Z8300 1.44GHz',
       'Intel Atom x5-Z8350 1.44GHz', 'Intel Atom x5-Z8550 1.44GHz',
       'Intel Celeron Dual Core 3205U 1.5GHz',
       'Intel Celeron Dual Core 3855U 1.6GHz',
       'Intel Celeron Dual Core N3050 1.6GHz',
       'Intel Celeron Dual Core N3060 1.60GHz',
       'Intel Celeron Dual Core N3060 1.6GHz',
       'Intel Celeron Dual Core N3350 1.1GHz',
       'Intel Celeron Dual Core N3350 2.0GHz',
       'Intel Celeron Dual Core N3350 2GHz',
       'Intel Celeron Quad Core N3160 1.6GHz',
       'Intel Celeron Quad Core N3450 1.1GHz',
       'Intel Celeron Quad Core N3710 1.6GHz', 'Intel Core M 1.1GHz',
       'Intel Core M 1.2GHz', 'Intel Core M 6Y30 0.9GHz',
       'Intel Core M 6Y54 1.1GHz', 'Intel Core M 6Y75 1.2GHz',
       'Intel Core M 7Y30 1.0GHz', 'Intel Core M M3-6Y30 0.9GHz',
       'Intel Core M M7-6Y75 1.2GHz', 'Intel Core M m3 1.2GHz',
       'Intel Core M m3-7Y30 2.2GHz', 'Intel Core M m7-6Y75 1.2GHz',
       'Intel Core i3 6006U 2.0GHz', 'Intel Core i3 6006U 2.2GHz',
       'Intel Core i3 6006U 2GHz', 'Intel Core i3 6100U 2.1GHz',
       'Intel Core i3 6100U 2.3GHz', 'Intel Core i3 7100U 2.4GHz',
       'Intel Core i3 7130U 2.7GHz', 'Intel Core i5 1.3GHz',
       'Intel Core i5 1.6GHz', 'Intel Core i5 1.8GHz',
       'Intel Core i5 2.0GHz', 'Intel Core i5 2.3GHz',
       'Intel Core i5 2.9GHz', 'Intel Core i5 3.1GHz',
       'Intel Core i5 6200U 2.3GHz', 'Intel Core i5 6260U 1.8GHz',
       'Intel Core i5 6300HQ 2.3GHz', 'Intel Core i5 6300U 2.4GHz',
       'Intel Core i5 6440HQ 2.6GHz', 'Intel Core i5 7200U 2.50GHz',
       'Intel Core i5 7200U 2.5GHz', 'Intel Core i5 7200U 2.70GHz',
       'Intel Core i5 7200U 2.7GHz', 'Intel Core i5 7300HQ 2.5GHz',
       'Intel Core i5 7300U 2.6GHz', 'Intel Core i5 7440HQ 2.8GHz',
       'Intel Core i5 7500U 2.7GHz', 'Intel Core i5 7Y54 1.2GHz',
       'Intel Core i5 7Y57 1.2GHz', 'Intel Core i5 8250U 1.6GHz',
       'Intel Core i7 2.2GHz', 'Intel Core i7 2.7GHz',
       'Intel Core i7 2.8GHz', 'Intel Core i7 2.9GHz',
       'Intel Core i7 6500U 2.50GHz', 'Intel Core i7 6500U 2.5GHz',
       'Intel Core i7 6560U 2.2GHz', 'Intel Core i7 6600U 2.6GHz',
       'Intel Core i7 6700HQ 2.6GHz', 'Intel Core i7 6820HK 2.7GHz',
       'Intel Core i7 6820HQ 2.7GHz', 'Intel Core i7 6920HQ 2.9GHz',
       'Intel Core i7 7500U 2.5GHz', 'Intel Core i7 7500U 2.7GHz',
       'Intel Core i7 7560U 2.4GHz', 'Intel Core i7 7600U 2.8GHz',
       'Intel Core i7 7660U 2.5GHz', 'Intel Core i7 7700HQ 2.7GHz',
       'Intel Core i7 7700HQ 2.8GHz', 'Intel Core i7 7820HK 2.9GHz',
       'Intel Core i7 7820HQ 2.9GHz', 'Intel Core i7 7Y75 1.3GHz',
       'Intel Core i7 8550U 1.8GHz', 'Intel Core i7 8650U 1.9GHz',
       'Intel Pentium Dual Core 4405U 2.1GHz',
       'Intel Pentium Dual Core 4405Y 1.5GHz',
       'Intel Pentium Dual Core N4200 1.1GHz',
       'Intel Pentium Quad Core N3700 1.6GHz',
       'Intel Pentium Quad Core N3710 1.6GHz',
       'Intel Pentium Quad Core N4200 1.1GHz',
       'Intel Xeon E3-1505M V6 3GHz', 'Intel Xeon E3-1535M v5 2.9GHz',
       'Intel Xeon E3-1535M v6 3.1GHz', 'Samsung Cortex A72&A53 2.0GHz']
   # valid velocity from cpus
   pattern= re.compile(r'(\d+\.?\d*)\s?(GHz|MHz)')
   #valid company from cpus
   pattern2= re.compile(r'(\w+)')
   
   
    
    