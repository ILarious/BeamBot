metals = {
        'C38/23': {'R': 2100, 'Rsr': 1300, 'Rsm': 3200, 'm_name': 'C38/23',
                   'R_2': 205, 'Rsr_2': 125, 'Rsm_2': 315},
        'C44/29': {'R': 2600, 'Rsr': 1500, 'Rsm': 3900, 'm_name': 'C44/29',
                   'R_2': 255, 'Rsr_2': 145, 'Rsm_2': 380},
        'C46/33': {'R': 2900, 'Rsr': 1700, 'Rsm': 4300, 'm_name': 'C46/33',
                   'R_2': 285, 'Rsr_2': 165, 'Rsm_2': 420},
        'C52/40': {'R': 3400, 'Rsr': 2000, 'Rsm': 5100, 'm_name': 'C52/40',
                   'R_2': 335, 'Rsr_2': 195, 'Rsm_2': 500},
        'C60/45': {'R': 3800, 'Rsr': 2300, 'Rsm': 5700, 'm_name': 'C60/45',
                   'R_2': 375, 'Rsr_2': 225, 'Rsm_2': 560},
        'C70/60': {'R': 4400, 'Rsr': 2600, 'Rsm': 6500, 'm_name': 'C70/60',
                   'R_2': 430, 'Rsr_2': 225, 'Rsm_2': 640},
        'C85/75': {'R': 5300, 'Rsr': 3100, 'Rsm': 8000, 'm_name': 'C85/75',
                   'R_2': 520, 'Rsr_2': 305, 'Rsm_2': 785}
    }

def isfloat(element):
    try:
        if list((map(float, element.split()))):
            return True
    except ValueError:
        return False


def is_num(element):
    try:
        if int(element):
            return True
    except ValueError:
        return False

def is_metal(element):
    try:
        if element in metals:
            return True
    except:
        return False