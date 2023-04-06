import yf_example2
import os
'''if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = r'D:\fins5546\toolkit\data'
    pth = f'{datadir}\qan_stk_prc.csv'
    yf_example2.yf_prc_to_csv(tic, pth)'''

if __name__ == "__main__":
    import toolkit_config as cfg
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
    yf_example2.yf_prc_to_csv(tic, pth)
