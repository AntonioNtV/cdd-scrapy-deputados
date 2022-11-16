def parse_brl_num_to_float(brl_num):
    return float(brl_num.replace(".", '').replace(",", ".").strip())