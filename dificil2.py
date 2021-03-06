from random import randint
from typing import List
import copy


def restart_program(z: List[List]):
    sudoku(z)
   
   
def solve(linha, qua1, qua2, qua3, ctt, w, n) -> List:
    ky = True
    l0 = copy.deepcopy(linha)
    q1 = copy.deepcopy(qua1)
    q2 = copy.deepcopy(qua2)
    q3 = copy.deepcopy(qua3)
    ct = copy.deepcopy(ctt)
    b = 0
    while ky:
        a = 0
        for x in l0:
            if x == 0:
                for y in range(0, 100):
                    z = randint(0, 9)
                    if a >= 0 and a <= 2:
                        r = copy.deepcopy(q1)
                    elif a >= 3 and a <= 5:
                        r = copy.deepcopy(q2)
                    else:
                        r = copy.deepcopy(q3)
                    if z not in l0 and z not in ct[a] and z not in r:
                        l0[a] = z
                        break
                a += 1   
                pass
            else: 
                a += 1
                pass
        for x in l0:
            if x == 0:
                l0 = copy.deepcopy(linha)
                break
        if 0 not in l0:
            ky = False
        b += 1
        if b == 50:
            restart_program(w)
        if n == 9 and 0 not in l0:
            break
    return l0


def sudoku(z: List[List]):
    w = copy.deepcopy(z)
    l0 = w[0]
    l1 = w[1]
    l2 = w[2]
    l3 = w[3]
    l4 = w[4]
    l5 = w[5]
    l6 = w[6]
    l7 = w[7]
    l8 = w[8]
    i = l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
    q1 = l0[0:3] + l1[0:3] + l2[0:3]
    q2 = l0[3:6] + l1[3:6] + l2[3:6]
    q3 = l0[6:9] + l1[6:9] + l2[6:9]
    q4 = l3[0:3] + l4[0:3] + l5[0:3]
    q5 = l3[3:6] + l4[3:6] + l5[3:6]
    q6 = l3[6:9] + l4[6:9] + l5[6:9]
    q7 = l6[0:3] + l7[0:3] + l8[0:3]
    q8 = l6[3:6] + l7[3:6] + l8[3:6]
    q9 = l6[6:9] + l7[6:9] + l8[6:9]   
    c1 = l0[0:1] + l1[0:1] + l2[0:1] + l3[0:1] + l4[0:1] + l5[0:1] + l6[0:1] + l7[0:1] + l8[0:1]
    c2 = l0[1:2] + l1[1:2] + l2[1:2] + l3[1:2] + l4[1:2] + l5[1:2] + l6[1:2] + l7[1:2] + l8[1:2]
    c3 = l0[2:3] + l1[2:3] + l2[2:3] + l3[2:3] + l4[2:3] + l5[2:3] + l6[2:3] + l7[2:3] + l8[2:3]
    c4 = l0[3:4] + l1[3:4] + l2[3:4] + l3[3:4] + l4[3:4] + l5[3:4] + l6[3:4] + l7[3:4] + l8[3:4]
    c5 = l0[4:5] + l1[4:5] + l2[4:5] + l3[4:5] + l4[4:5] + l5[4:5] + l6[4:5] + l7[4:5] + l8[4:5]
    c6 = l0[5:6] + l1[5:6] + l2[5:6] + l3[5:6] + l4[5:6] + l5[5:6] + l6[5:6] + l7[5:6] + l8[5:6]
    c7 = l0[6:7] + l1[6:7] + l2[6:7] + l3[6:7] + l4[6:7] + l5[6:7] + l6[6:7] + l7[6:7] + l8[6:7]
    c8 = l0[7:8] + l1[7:8] + l2[7:8] + l3[7:8] + l4[7:8] + l5[7:8] + l6[7:8] + l7[7:8] + l8[7:8]
    c9 = l0[8:9] + l1[8:9] + l2[8:9] + l3[8:9] + l4[8:9] + l5[8:9] + l6[8:9] + l7[8:9] + l8[8:9]
    ct = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

    r1 = solve(l0, q1, q2, q3, ct, z, 1)
    q1[0] = r1[0]
    q1[1] = r1[1]
    q1[2] = r1[2]
    q2[0] = r1[3]
    q2[1] = r1[4]
    q2[2] = r1[5]
    q3[0] = r1[6]
    q3[1] = r1[7]
    q3[2] = r1[8]
    ct[0][0] = r1[0]
    ct[1][0] = r1[1]
    ct[2][0] = r1[2]
    ct[3][0] = r1[3]
    ct[4][0] = r1[4]
    ct[5][0] = r1[5]
    ct[6][0] = r1[6]
    ct[7][0] = r1[7]
    ct[8][0] = r1[8]
    #(f'linha1 - {r1}')
    r2 = solve(l1, q1, q2, q3, ct, z, 2)
    q1[3] = r2[0]
    q1[4] = r2[1]
    q1[5] = r2[2]
    q2[3] = r2[3]
    q2[4] = r2[4]
    q2[5] = r2[5]
    q3[3] = r2[6]
    q3[4] = r2[7]
    q3[5] = r2[8]
    ct[0][1] = r2[0]
    ct[1][1] = r2[1]
    ct[2][1] = r2[2]
    ct[3][1] = r2[3]
    ct[4][1] = r2[4]
    ct[5][1] = r2[5]
    ct[6][1] = r2[6]
    ct[7][1] = r2[7]
    ct[8][1] = r2[8]
    #(f'linha2 - {r2}')
    r3 = solve(l2, q1, q2, q3, ct, z, 3)
    q1[6] = r3[0]
    q1[7] = r3[1]
    q1[8] = r3[2]
    q2[6] = r3[3]
    q2[7] = r3[4]
    q2[8] = r3[5]
    q3[6] = r3[6]
    q3[7] = r3[7]
    q3[8] = r3[8]
    ct[0][2] = r3[0]
    ct[1][2] = r3[1]
    ct[2][2] = r3[2]
    ct[3][2] = r3[3]
    ct[4][2] = r3[4]
    ct[5][2] = r3[5]
    ct[6][2] = r3[6]
    ct[7][2] = r3[7]
    ct[8][2] = r3[8]
    #(f'linha3 - {r3}')
    r4 = solve(l3, q4, q5, q6, ct, z, 4)
    q4[0] = r4[0]
    q4[1] = r4[1]
    q4[2] = r4[2]
    q5[0] = r4[3]
    q5[1] = r4[4]
    q5[2] = r4[5]
    q6[0] = r4[6]
    q6[1] = r4[7]
    q6[2] = r4[8]
    ct[0][3] = r4[0]
    ct[1][3] = r4[1]
    ct[2][3] = r4[2]
    ct[3][3] = r4[3]
    ct[4][3] = r4[4]
    ct[5][3] = r4[5]
    ct[6][3] = r4[6]
    ct[7][3] = r4[7]
    ct[8][3] = r4[8]
#(f'linha4 - {r4}')
    r5 = solve(l4, q4, q5, q6, ct, z, 5)
    q4[3] = r5[0]
    q4[4] = r5[1]
    q4[5] = r5[2]
    q5[3] = r5[3]
    q5[4] = r5[4]
    q5[5] = r5[5]
    q6[3] = r5[6]
    q6[4] = r5[7]
    q6[5] = r5[8]
    ct[0][4] = r5[0]
    ct[1][4] = r5[1]
    ct[2][4] = r5[2]
    ct[3][4] = r5[3]
    ct[4][4] = r5[4]
    ct[5][4] = r5[5]
    ct[6][4] = r5[6]
    ct[7][4] = r5[7]
    ct[8][4] = r5[8]
    #(f'linha5 - {r5}')
    r6 = solve(l5, q4, q5, q6, ct, z, 6)
    q4[6] = r6[0]
    q4[7] = r6[1]
    q4[8] = r6[2]
    q5[6] = r6[3]
    q5[7] = r6[4]
    q5[8] = r6[5]
    q6[6] = r6[6]
    q6[7] = r6[7]
    q6[8] = r6[8]
    ct[0][5] = r6[0]
    ct[1][5] = r6[1]
    ct[2][5] = r6[2]
    ct[3][5] = r6[3]
    ct[4][5] = r6[4]
    ct[5][5] = r6[5]
    ct[6][5] = r6[6]
    ct[7][5] = r6[7]
    ct[8][5] = r6[8]
    #(f'linha6 - {r6}')
    r7 = solve(l6, q7, q8, q9, ct, z, 7)
    q7[0] = r7[0]
    q7[1] = r7[1]
    q7[2] = r7[2]
    q8[0] = r7[3]
    q8[1] = r7[4]
    q8[2] = r7[5]
    q9[0] = r7[6]
    q9[1] = r7[7]
    q9[2] = r7[8]
    ct[0][6] = r7[0]
    ct[1][6] = r7[1]
    ct[2][6] = r7[2]
    ct[3][6] = r7[3]
    ct[4][6] = r7[4]
    ct[5][6] = r7[5]
    ct[6][6] = r7[6]
    ct[7][6] = r7[7]
    ct[8][6] = r7[8]
    #(f'linha7 - {r7}')
    r8 = solve(l7, q7, q8, q9, ct, z, 8)
    q7[3] = r8[0]
    q7[4] = r8[1]
    q7[5] = r8[2]
    q8[3] = r8[3]
    q8[4] = r8[4]
    q8[5] = r8[5]
    q9[3] = r8[6]
    q9[4] = r8[7]
    q9[5] = r8[8]
    ct[0][7] = r8[0]
    ct[1][7] = r8[1]
    ct[2][7] = r8[2]
    ct[3][7] = r8[3]
    ct[4][7] = r8[4]
    ct[5][7] = r8[5]
    ct[6][7] = r8[6]
    ct[7][7] = r8[7]
    ct[8][7] = r8[8]
    #(f'linha8 - {r8}')
    r9 = solve(l8, q7, q8, q9, ct, z, 9)
    q7[6] = r9[0]
    q7[7] = r9[1]
    q7[8] = r9[2]
    q8[6] = r9[3]
    q8[7] = r9[4]
    q8[8] = r9[5]
    q9[6] = r9[6]
    q9[7] = r9[7]
    q9[8] = r9[8]
    ct[0][8] = r9[0]
    ct[1][8] = r9[1]
    ct[2][8] = r9[2]
    ct[3][8] = r9[3]
    ct[4][8] = r9[4]
    ct[5][8] = r9[5]
    ct[6][8] = r9[6]
    ct[7][8] = r9[7]
    ct[8][8] = r9[8]
    #(f'linha9 - {r9}')
    rf = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9
    resposta = r1, r2, r3, r4, r5, r6, r7, r8, r9
    
    x = f"""
        -------------------------
       | {i[0]} {i[1]} {i[2]} | {i[3]} {i[4]} {i[5]} | {i[6]} {i[7]} {i[8]} |
       | {i[9]} {i[10]} {i[11]} | {i[12]} {i[13]} {i[14]} | {i[15]} {i[16]} {i[17]} |
       | {i[18]} {i[19]} {i[20]} | {i[21]} {i[22]} {i[23]} | {i[24]} {i[25]} {i[26]} |
       |-------.-------.-------|
       | {i[27]} {i[28]} {i[29]} | {i[30]} {i[31]} {i[32]} | {i[33]} {i[34]} {i[35]} |
       | {i[36]} {i[37]} {i[38]} | {i[39]} {i[40]} {i[41]} | {i[42]} {i[43]} {i[44]} |
       | {i[45]} {i[46]} {i[47]} | {i[48]} {i[49]} {i[50]} | {i[51]} {i[52]} {i[53]} |
       |-------.-------.-------|'
       | {i[54]} {i[55]} {i[56]} | {i[57]} {i[58]} {i[59]} | {i[60]} {i[61]} {i[62]} |
       | {i[63]} {i[64]} {i[65]} | {i[66]} {i[67]} {i[68]} | {i[69]} {i[70]} {i[71]} |
       | {i[72]} {i[73]} {i[74]} | {i[75]} {i[76]} {i[77]} | {i[78]} {i[79]} {i[80]} |
       '-------------------------'"""

    y = f"""     
    -------------------------
    | {rf[0]} {rf[1]} {rf[2]} | {rf[3]} {rf[4]} {rf[5]} | {rf[6]} {rf[7]} {rf[8]} |
    | {rf[9]} {rf[10]} {rf[11]} | {rf[12]} {rf[13]} {rf[14]} | {rf[15]} {rf[16]} {rf[17]} |
    | {rf[18]} {rf[19]} {rf[20]} | {rf[21]} {rf[22]} {rf[23]} | {rf[24]} {rf[25]} {rf[26]} |
    |-------.-------.-------|
    | {rf[27]} {rf[28]} {rf[29]} | {rf[30]} {rf[31]} {rf[32]} | {rf[33]} {rf[34]} {rf[35]} |
    | {rf[36]} {rf[37]} {rf[38]} | {rf[39]} {rf[40]} {rf[41]} | {rf[42]} {rf[43]} {rf[44]} |
    | {rf[45]} {rf[46]} {rf[47]} | {rf[48]} {rf[49]} {rf[50]} | {rf[51]} {rf[52]} {rf[53]} |
    |-------.-------.-------|
    | {rf[54]} {rf[55]} {rf[56]} | {rf[57]} {rf[58]} {rf[59]} | {rf[60]} {rf[61]} {rf[62]} |
    | {rf[63]} {rf[64]} {rf[65]} | {rf[66]} {rf[67]} {rf[68]} | {rf[69]} {rf[70]} {rf[71]} |
    | {rf[72]} {rf[73]} {rf[74]} | {rf[75]} {rf[76]} {rf[77]} | {rf[78]} {rf[79]} {rf[80]} |
    -------------------------"""
    print()
    print('Sudoko a ser resolvido:')
    print(x)
    print()
    print('Possivel solu??ao para o sudoko:')
    print(y)
    print()
    print('Saida esperada:')
    print(resposta)
    exit()   
    
    
    
if __name__ == '__main__':
    l1 = [[0,0,1,0,0,2,0,0,5],
    [0,7,0,0,3,0,0,4,0],
    [5,0,0,9,0,0,7,0,0],
    [3,0,0,1,0,0,5,0,9],
    [0,5,0,0,9,0,0,1,0],
    [6,0,9,0,0,3,0,0,7],
    [4,0,3,0,0,8,0,0,1],
    [0,8,0,0,1,0,0,5,0],
    [1,0,0,3,0,0,8,0,0]
    ]
    sudoku(l1)
    