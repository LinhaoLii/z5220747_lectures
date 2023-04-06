import os
import toolkit_config as cfg
import yf_example2 as yf2


def qan_prc_to_csv(d):
    start = str(d)+'-01-01'  # (3)
    end = str(d)+'-12-31'  # (4)
    tic = "QAN.AX"
    pth = os.path.join(cfg.DATADIR, ('qan_prc_'+str(d)+'.csv'))
    yf2.yf_prc_to_csv(tic, pth, start, end)

if __name__ == "__main__":
    qan_prc_to_csv(2020)