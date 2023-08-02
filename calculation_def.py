from math import sqrt, ceil

import numpy


def calculation_p22(variant):
    l, p, q, d = map(float, variant.split())

    L = l * 100
    P = p * 1000
    Q = q * 10
    D = d * 100

    Z = [0, 0.1 * L, 0.2 * L, 0.3 * L, 0.4 * L, 0.5 * L]

    Ra0 = round((2 * P) - ((P * D) / L), 2)
    Ra1 = (2 * P) - (P * ((0.1 * L - (D / 2))) + P * (0.1 * L + (D / 2))) / L
    Ra2 = (2 * P) - (P * ((0.2 * L - (D / 2))) + P * (0.2 * L + (D / 2))) / L
    Ra3 = (2 * P) - (P * ((0.3 * L - (D / 2))) + P * (0.3 * L + (D / 2))) / L
    Ra4 = (2 * P) - (P * ((0.4 * L - (D / 2))) + P * (0.4 * L + (D / 2))) / L
    Ra5 = (2 * P) - (P * ((0.5 * L - (D / 2))) + P * (0.5 * L + (D / 2))) / L

    Rb1 = (P * ((0.1 * L - (D / 2))) + P * (0.1 * L + (D / 2))) / L
    Rb2 = (P * ((0.2 * L - (D / 2))) + P * (0.2 * L + (D / 2))) / L
    Rb3 = (P * ((0.3 * L - (D / 2))) + P * (0.3 * L + (D / 2))) / L
    Rb4 = (P * ((0.4 * L - (D / 2))) + P * (0.4 * L + (D / 2))) / L
    Rb5 = (P * ((0.5 * L - (D / 2))) + P * (0.5 * L + (D / 2))) / L

    Mq = []
    Qq = []
    Mp = Ra5 * (0.5 * L - D / 2)

    z11 = (0.1 * L - (D / 2)) / 100
    z12 = (0.2 * L - (D / 2)) / 100
    z13 = (0.3 * L - (D / 2)) / 100
    z14 = (0.4 * L - (D / 2)) / 100
    z15 = (0.5 * L - (D / 2)) / 100

    z21 = (0.1 * L + (D / 2)) / 100
    z22 = (0.2 * L + (D / 2)) / 100
    z23 = (0.3 * L + (D / 2)) / 100
    z24 = (0.4 * L + (D / 2)) / 100
    z25 = (0.5 * L + (D / 2)) / 100

    z31 = (0.9 * L - (D / 2)) / 100
    z32 = (0.8 * L - (D / 2)) / 100
    z33 = (0.7 * L - (D / 2)) / 100
    z34 = (0.6 * L - (D / 2)) / 100

    Mp11 = Ra1 * z11
    Mp21 = Ra2 * z12
    Mp31 = Ra3 * z13
    Mp41 = Ra4 * z14
    Mp51 = Ra5 * z15

    Qp12 = Ra1 - P
    Qp22 = Ra2 - P
    Qp32 = Ra3 - P
    Qp42 = Ra4 - P
    Qp52 = Ra5 - P

    Mp12 = (Ra1 * (0.1 * L - (D / 2) + D) - P * D) / 100
    Mp22 = (Ra2 * (0.2 * L - (D / 2) + D) - P * D) / 100
    Mp32 = (Ra3 * (0.3 * L - (D / 2) + D) - P * D) / 100
    Mp42 = (Ra4 * (0.4 * L - (D / 2) + D) - P * D) / 100
    Mp52 = (Ra5 * (0.5 * L - (D / 2) + D) - P * D) / 100

    for z in Z:
        Mq.append(((Q * z) / 2) * (L - z))
        Qq.append(Q * ((L / 2) - z))

    rb1 = (P * d) / l
    ra1 = 2 * P - rb1
    Qp01 = ra1 - P
    Mp01d = ra1 * d - P * d
    l_d = l - d
    f_max = round(L / 500, 1)

    rslt = f'Mq = {max(Mq)}\nQq = {max(Qq)}\nMp = {Mp}'

    Ra_list = dict()
    value = dict()

    value['f_max'] = f_max
    value['Mp11'] = round(Mp11, 2)
    value['Mp21'] = round(Mp21, 2)
    value['Mp31'] = round(Mp31, 2)
    value['Mp41'] = round(Mp41, 2)
    value['Mp51'] = round(Mp51, 2)

    value['Qp12'] = round(Qp12, 2)
    value['Qp22'] = round(Qp22, 2)
    value['Qp32'] = round(Qp32, 2)
    value['Qp42'] = round(Qp42, 2)
    value['Qp52'] = round(Qp52, 2)

    value['Mp12'] = round(Mp12, 2)
    value['Mp22'] = round(Mp22, 2)
    value['Mp32'] = round(Mp32, 2)
    value['Mp42'] = round(Mp42, 2)
    value['Mp52'] = round(Mp52, 2)

    value['z11'] = round(z11, 2)
    value['z12'] = round(z12, 2)
    value['z13'] = round(z13, 2)
    value['z14'] = round(z14, 2)
    value['z15'] = round(z15, 2)
    value['z21'] = round(z21, 2)
    value['z22'] = round(z22, 2)
    value['z23'] = round(z23, 2)
    value['z24'] = round(z24, 2)
    value['z25'] = round(z25, 2)
    value['z31'] = round(z31, 2)
    value['z32'] = round(z32, 2)
    value['z33'] = round(z33, 2)
    value['z34'] = round(z34, 2)

    value['rb1'] = round(rb1, 3)
    value['ra1'] = round(ra1, 3)
    value['Qp01'] = round(Qp01, 3)
    value['Mp01d'] = round(Mp01d, 3)
    value['l_d'] = l_d

    value['Rb1'] = Rb1
    value['Rb2'] = Rb2
    value['Rb3'] = Rb3
    value['Rb4'] = Rb4
    value['Rb5'] = Rb5

    value['l'] = l
    value['p'] = p
    value['q'] = q
    value['d'] = d

    value['Qm'] = q * 1000

    value['L'] = L
    value['P'] = P
    value['Q'] = Q
    value['D'] = D

    value['Z1'] = Z[1] / 100
    value['Z2'] = Z[2] / 100
    value['Z3'] = Z[3] / 100
    value['Z4'] = Z[4] / 100
    value['Z5'] = Z[5] / 100

    value['Mq'] = max(Mq)
    value['Mp'] = Mp
    value['Qq'] = max(Qq)

    value['Mq1'] = int(Mq[1] / 100)
    value['Mq2'] = int(Mq[2] / 100)
    value['Mq3'] = int(Mq[3] / 100)
    value['Mq4'] = int(Mq[4] / 100)
    value['Mq5'] = int(Mq[5] / 100)

    value['Qq1'] = int(Qq[1])
    value['Qq2'] = int(Qq[2])
    value['Qq3'] = int(Qq[3])
    value['Qq4'] = int(Qq[4])
    value['Qq5'] = int(Qq[5])

    Ra_list['Ra0'] = Ra0
    Ra_list['Ra1'] = Ra1
    Ra_list['Ra2'] = Ra2
    Ra_list['Ra3'] = Ra3
    Ra_list['Ra4'] = Ra4
    Ra_list['Ra5'] = Ra5
    # print(value)
    value.update(Ra_list)
    return value, Ra_list


def get_Gmax(value, metal):
    E = 2e6

    R = metal['R']
    L = value['L']
    D = value['D']
    Mq = value['Mq']
    Mp = value['Mp']
    f_max = value['f_max']

    m1 = 0.9
    n1 = 1.1
    n2 = 1.3

    hj = (1 / 4) * ((R * m1) / E) * L * (L / f_max) * (
            (5 / (6 * n1)) + (1 / n2) * (
            1 - ((L - D) ** 2) / (3 * L ** 2)))
    ha = sqrt((3 * ((Mq * n1) + (Mp * n2))) / (2 * R * m1 * 1))

    h_dict = dict()
    val = dict()
    cnt = 0

    for H in range(50, 150):
        Sv = round(0.08 * sqrt(H), 1)
        for i in [1.0, 1.1, 1.2]:
            Sg = round(i * Sv, 1)  # Sg = (1.0...1.2)Sv
            Bg = 20 * Sg
            Hv = H - 2 * Sg

            Jf = ceil(((Sv * Hv ** 3) / 12) + 2 * (((Bg * Sg ** 3) / 12) +
                                                   (Bg * Sg) * ((
                                                                        H - Sg) / 2) ** 2))

            Gmax = ceil((Mq * n1 + Mp * n2) / (Jf * m1) * H / 2)


            if (R - ((R / 100) * 5)) <= Gmax <= R:
                cnt += 1

                d_gmax = ceil(((R - Gmax) / R) * 100)

                val[cnt] = {'Sv': Sv, 'Sg': Sg, 'Bg': Bg, 'Hv': Hv,
                            'Jf': Jf, 'Gmax': Gmax, 'H': H, 'a_i': i,
                            'd_gmax': d_gmax}

    h_dict['hj'] = round(hj, 2)
    h_dict['ha'] = round(ha, 2)

    return val, h_dict


def get_table(value):
    L = value['L']
    P = value['P']
    Q = value['Q']
    D = value['D']
    Mp = value['Mp']
    Sv = value['Sv']
    Hv = value['Hv']
    Bg = value['Bg']
    Sg = value['Sg']
    Jf = value['Jf']
    Qq = value['Qq']

    m1 = 0.9
    n1 = 1.1
    n2 = 1.3

    Ra0 = value['Ra0']
    Ra1 = value['Ra1']
    Ra2 = value['Ra2']
    Ra3 = value['Ra3']
    Ra4 = value['Ra4']
    Ra5 = value['Ra5']

    Ra = [Ra0, Ra1, Ra2, Ra3, Ra4, Ra5]

    s1 = round(Bg * Sg * ((Hv / 2) + (Sg / 2)), 1)
    s2 = round(Sv * (Hv / 2) * (Hv / 4), 1)
    s = s1 + s2
    Tmax = abs(ceil((((Qq * n1) + (Ra0 * n2)) / (Sv * Jf * m1)) * s))

    value['s1'] = s1
    value['s2'] = s2
    value['s'] = s
    value['Tmax'] = Tmax

    L_lst = [1, 0.1 * L, 0.2 * L, 0.3 * L, 0.4 * L, 0.5 * L]
    x = [D, D / 2 + 0.1 * L, D / 2 + 0.2 * L, D / 2 + 0.3 * L, D / 2 + 0.4 * L,
         0.5 * L]

    for i in range(len(x)):
        Mqq = ((Q * x[i]) / 2 * (L - x[i]))
        Qqq = Q * ((L / 2) - x[i])

        if x[i] == D:
            Mpp = (-P * x[i] + Ra[i] * x[i])
        elif x[i] > D:
            Mpp = (Ra[i] * (L_lst[i] - (D / 2) + D) - P * D)

        Qpp = Ra[i] - P

        Gj = ceil(((((Mqq * n1) + (Mpp * n2)) / (Jf * m1)) * (Hv / 2)))
        Tj = abs(ceil(((Qqq * n1) + (Qpp * n2)) / (Sv * Hv * m1)))
        Ga = ceil(sqrt((Gj ** 2) + (3 * Tj ** 2)))

        lst_t = ['Gj', 'Tj', 'Ga', 'Mqq', 'Qqq', 'Qpp', 'Mpp']
        lst_i = [Gj, Tj, Ga, Mqq, Qqq, Qpp, Mpp]

        for val_s, val_i in zip(lst_t, lst_i):
            value[f'{val_s}{i}'] = round(val_i, 2)

    a = 4
    x = Sg * Bg
    y = (Sg + a) / 2

    f22 = x
    bg_16 = Bg / 16
    y_bg_16 = 1 + bg_16

    l_side = numpy.array(
        [[16, -x], [1, 1]])  # Матрица (левая часть системы)
    r_side = numpy.array([[0], [y]])  # Вектор (правая часть системы)

    y1, y2 = map(lambda Yi: round(float(Yi), 2),
                 numpy.array(numpy.linalg.solve(l_side, r_side)))

    Jr = ((a ** 4) / 12) + ((a ** 2) * (y1 ** 2))
    Jgp = ((Bg * (Sg ** 3)) / 12) + (Bg * Sg * (y2 ** 2))

    Jj = round(Jr + Jgp, 1)

    z = round(3.25 * (Jj / Sv) ** (1 / 3), 2)
    Gu = round((P * n2) / (z * Sv * m1), 2)

    lst_t = ['f22', 'bg_16', 'y_bg_16', 'y', 'y1', 'y2', 'Jj', 'z', 'Gu']
    lst_i = [f22, bg_16, y_bg_16, y, y1, y2, Jj, z, Gu]

    for val_s, val_i in zip(lst_t, lst_i):
        value[f'{val_s}'] = round(val_i, 2)

    return value


def stability_check(value):
    Bg = value['Bg']
    Sg = value['Sg']
    Hv = value['Hv']
    Sv = value['Sv']
    H = value['H']

    m1 = 0.9
    n1 = 1.1
    n2 = 1.3

    Mq = value['Mq']
    Mp = value['Mp']
    Jf = value['Jf']
    R = value['R']

    for Li in range(10, 21):
        l0 = Li * Bg
        a = round(8 * (((l0 * Sg) / (Bg * H)) ** 2) * (
                    1 + ((Hv * Sv ** 3) / (2 * Bg * Sg ** 3))), 2)

        if a <= 4:
            FI = 1.85
        elif 4 < a <= 12:
            FI = 2.63
        elif 12 < a <= 20:
            FI = 3.37
        elif 20 < a <= 28:
            FI = 4.03
        elif 28 < a <= 40:
            FI = 4.59
        elif 40 < a <= 56:
            FI = 5.60
        elif 56 < a <= 72:
            FI = 6.50
        elif 72 < a <= 80:
            FI = 7.31

        Jx = ceil(((Sv * (Hv ** 3)) / 12) + 2 * (
                (((Bg * (Sg ** 3))) / 12) + (Bg * Sg) * (
                (Hv + Sg) / 2) ** 2))

        Jy = round(((Hv * Sv ** 3) / 12) + (2 * ((Sg * Bg ** 3) / 12)), 2)

        fi = round((10 ** 3) * FI * (Jy / Jx) * (H / l0) ** 2, 2)

        fi_p = fi

        if 1 > fi > 0.85:
            fi = 0.85
            fi_if1 = '1 >'
            fi_if2 = '> 0.85'
        elif 1.25 > fi >= 1:
            fi = 0.90
            fi_if1 = '1.25 >'
            fi_if2 = '> 1.00'
        elif 1.55 > fi >= 1.25:
            fi = 0.96
            fi_if1 = '1.55 >'
            fi_if2 = '> 1.25'
        elif fi >= 1.55:
            fi = 1.00
            fi_if2 = '>= 1.55'
            fi_if1 = ''

        GGMAX = ceil(((Mq * n1 + Mp * n2) / (Jf * m1)) * (H / 2))

        if GGMAX <= fi * R:
            rslt = {
                'l0': l0,
                'Li': Li,
                'aaa': a,
                'FI': FI,
                'Jx': Jx,
                'Jy': Jy,
                'fi': fi,
                'fi_p': fi_p,
                'fi_if1': fi_if1,
                'fi_if2': fi_if2,
                'GGMAX': GGMAX
            }
            value.update(rslt)

            return value


def IF28(a, val, K, G):

    Hv = val['Hv']
    Sv = val['Sv']
    Ga5 = val['Ga5']
    Gu = val['Gu']
    Tj0 = val['Tj0']

    a_r = a
    K_y = K
    G0_0 = G

    if a_r >= Hv:
        v = 1.5
        ddd = Hv
        k1 = 9
    else:
        v = round(Hv/a_r, 1)
        ddd = a_r
        k_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i_lst = [0.2, 0.5, 0.7, 0.9, 1, 1.2, 1.3, 1.4, 1.5, 1.6]
        k1 = [k for k, i in zip(k_lst, i_lst) if i == v]

    t0_0 = round((1250 + (950/(v**2))) * ((100*Sv)/ddd)**2, 2)
    Gu0_0 = round(10**7 * k1 * ((Sv / a_r) ** 2), 2)
    if28 = round(sqrt(
        (((Ga5 / G0_0) + (Gu / Gu0_0)) ** 2) + ((Tj0 / t0_0) ** 2)), 2)

    if if28 < 0.9:
        rslt = {
            'K_y': K_y,
            'k1': k1,
            'G0_0': G0_0,
            'Gu0_0': Gu0_0,
            't0_0': t0_0,
            'v': v,
            'ddd': ddd,
            'a_r': a_r,
            'if28': if28
        }

        return rslt

    else:
        a = a_r - 0.1
        IF28(a, val, K, G)

def stability_check_elements(value):

    Hv = value['Hv']
    P = value['P']
    d = value['d']
    Qm = value['Qm']
    H = value['H']
    Sv = value['Sv']
    L = value['L']
    l = value['l']
    Rsm = value['Rsm']

    Ga5 = value['Ga5']
    Gu = value['Gu']
    Tj0 = value['Tj0']


    K_y = round(Hv/Sv, 1)


    G0_0 = round(75*(10**4)*(Sv/Hv), 2)
    a_rr = round((1.5 * Hv))

    rslt = IF28(a_rr, value, K_y, G0_0)

    value.update(rslt)

    a_r = value['a_r']

    L15 = 15 * Sv
    L15_2 = 2 * L15

    Lzz = L - L15_2

    Npr_r = ceil(Lzz / a_r)
    Azz = round(Lzz / (Npr_r + 1), 1)

    Bpr_r = ceil(round((H / 30) + 4, 1))

    Spr_r = round(((Bpr_r / 15)+0.1), 1)

    rbb = round(((P * d + ((Qm * l**2) / 2)) / l), 2)
    raa = round(((2*P) + (Qm*l) - rbb), 2)

    for x in [0.8, 0.9, 1]:
        Sop_r = x * Sv

        if_pro = (raa * 1.3)/(2 * 0.9 * 2 * (Bpr_r - 1.5) * Sop_r)
        print(if_pro)

        if if_pro < Rsm:

            rslt2 = {
                'L15': round(L15, 2),
                'L15_2': round(L15_2, 2),
                'Lzz': round(Lzz, 2),
                'Npr_r': round(Npr_r, 2),
                'Azz': round(Azz, 2),
                'Bpr_r': round(Bpr_r, 2),
                'Spr_r': round(Spr_r, 2),
                'rbb': round(rbb, 2),
                'raa': round(raa, 2),
                'Sop_r': round(Sop_r, 2),
                'if_pro': round(if_pro, 2)
            }

            value.update(rslt2)

            return value

def calculation_of_welded(value):

    Bg = value['Bg']
    Sg = value['Sg']
    Sv = value['Sv']
    H = value['H']
    P = value['P']
    Qq = value['Qq']
    Ra0 = value['Ra0']
    Jf = value['Jf']
    Gu = value['Gu']
    Spr_r = value['Spr_r']
    Bpr_r = value['Bpr_r']
    raa = value['raa']

    SSV = round(((Bg * Sg) * ((H-Sg)/2)), 2)
    TQQ = round((((Qq*1.1 + Ra0*1.3)/(Jf*Sv*0.9))*SSV), 2)
    GKV = round((sqrt((Gu**2)+(3*(TQQ**2)))), 2)
    KKK = (Spr_r * 10)
    TPR = round(((0.4*P*1.3)/((2*2*2*0.85*Spr_r)*(Bpr_r-1.5)*0.9)), 2)
    TPR2 = round(((0.4*raa*1.3)/((2*2*2*0.85*Spr_r)*(Bpr_r-1.5)*0.9)), 2)


    res = {
        'SSV': SSV,
        'TQQ': TQQ,
        'GKV': GKV,
        'KKK': KKK,
        'TPR': TPR,
        'TPR2': TPR2
    }

    value.update(res)

    return value


def base_plate_calculation(value):
    Bg = value['Bg']
    raa = value['raa']
    R = value['R']

    bpl = 1.1 * Bg
    apl = 1.5 * bpl
    dotv = 2

    Spl = round(sqrt((6 * raa * 1.3 * apl)/(8 * R * 0.9*(bpl - (2*dotv)))), 2)

    res = {
        'bpl': round(bpl, 2),
        'apl': round(apl, 2),
        'dotv': round(dotv, 2),
        'Spl': round(Spl, 2)
    }

    value.update(res)

    return value

def update_value(value, element):
    value.update(element)
    return value
