jdnToGreg_helper(jdn):
    assert False, 'Code is in development.'
    DA_PER_LY = 366
    DA_PER_YR = 365
    LY_PER_CN = 24
    LY_PER_LC = 25
    LD_PER_CN = LY_PER_CN
    LD_PER_LC = LY_PER_LC
    YR_PER_C = 100
    DA_PER_CN = YR_PER_C * DA_PER_YR + LD_PER_CN
    DA_PER_LC = YR_PER_C * DA_PER_YR + LD_PER_LC
    # CUMULATIVE DAYS PER CENTURY WITHIN A PERIOD
    ACCUM_DA_BY_C = [0]
    for _ in range(3):
        ACCUM_DA_BY_C.append(ACCUM_DA_BY_C[-1] + DA_PER_CN)
    ACCUM_DA_BY_C.append(ACCUM_DA_BY_C[-1] + DA_PER_LC)
    DA_PER_PD = ACCUM_DA_BY_C[-1]
    #TODO: REPLACE LAG-VALUE WITH CORRECT VALUE
    LAG = 500
    DA_SINCE_FIRST_PD = jdn + LAG
    DA_OF_PD = DA_SINCE_FIRST_PD % DA_PER_PD
    CN_OF_PD = sum ( map (
        lambda Days : 0 < DA_OF_PD - Days ,
        ACCUM_DA_BY_C ) )
    DA_OF_CN = DA_OF_PD - ACCUM_DA_BY_C[CN_OF_PD] 
    LAST_YEAR_OF_FIRST_PD = -4400
