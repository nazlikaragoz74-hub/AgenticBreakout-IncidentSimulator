from scipy.stats import f, ncf

def calculate_anova_apriori(alpha: float, power: float, f_effect: float, groups: int = 3) -> dict:
    df_num = groups - 1
    n_per_group = 2
    
    while True:
        n_total = n_per_group * groups
        df_den = n_total - groups
        
        f_crit = f.ppf(1 - alpha, df_num, df_den)
        ncp = (f_effect ** 2) * n_total
        calc_power = 1 - ncf.cdf(f_crit, df_num, df_den, ncp)
        
        # Power hedeflenen değere ulaştığı ilk anda dur
        if calc_power >= power:
            return {
                "n_total": int(n_total),
                "actual_power": round(float(calc_power), 4),
                "critical": round(float(f_crit), 4),
                "df_num": int(df_num),
                "df_den": int(df_den),
                "ncp": round(float(ncp), 4)
            }
        
        n_per_group += 1