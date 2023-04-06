import yfinance                           # (1)
start = '2020-01-01'                      # (3)
end = None                                # (4)
tic = "WES.AX"                            # (W1)
df = yfinance.download(tic, start, end)   # (W2)
print(df)                                 # (W3)
df.to_csv('wes_stk_prc.csv')              # (W4)

APIKEY = 'abcdcf'