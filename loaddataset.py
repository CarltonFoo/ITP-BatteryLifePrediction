import h5py
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Enter Dataset
matFilename = './datasets/2018-08-28_batchdata_updated_struct_errorcorrect.mat'
f = h5py.File(matFilename)

batch = f['batch']

num_cells = batch['summary'].shape[0]  # find size (number of summary data)

bat_dict = {}
for i in range(num_cells):
    cl = f[batch['cycle_life'][i, 0]][::2]
    # policy = f[batch['policy_readable'][i,0]].value.tobytes()[::2].decode() <-- deprecated, need some other way to dissect code
    policy = f[batch['policy_readable'][i, 0]]
    summary_IR = np.hstack(f[batch['summary'][i, 0]]['IR'][0, :].tolist())
    summary_QC = np.hstack(f[batch['summary'][i, 0]]['QCharge'][0, :].tolist())
    summary_QD = np.hstack(f[batch['summary'][i, 0]]
                           ['QDischarge'][0, :].tolist())
    summary_TA = np.hstack(f[batch['summary'][i, 0]]['Tavg'][0, :].tolist())
    summary_TM = np.hstack(f[batch['summary'][i, 0]]['Tmin'][0, :].tolist())
    summary_TX = np.hstack(f[batch['summary'][i, 0]]['Tmax'][0, :].tolist())
    summary_CT = np.hstack(f[batch['summary'][i, 0]]
                           ['chargetime'][0, :].tolist())
    summary_CY = np.hstack(f[batch['summary'][i, 0]]['cycle'][0, :].tolist())
    summary = {'IR': summary_IR, 'QC': summary_QC, 'QD': summary_QD, 'Tavg':
               summary_TA, 'Tmin': summary_TM, 'Tmax': summary_TX, 'chargetime': summary_CT,
               'cycle': summary_CY}

    cycles = f[batch['cycles'][i, 0]]
    cycle_dict = {}
    for j in range(cycles['I'].shape[0]):
        I = np.hstack((f[cycles['I'][j, 0]]))
        Qc = np.hstack((f[cycles['Qc'][j, 0]]))
        Qd = np.hstack((f[cycles['Qd'][j, 0]]))
        Qdlin = np.hstack((f[cycles['Qdlin'][j, 0]]))
        T = np.hstack((f[cycles['T'][j, 0]]))
        Tdlin = np.hstack((f[cycles['Tdlin'][j, 0]]))
        V = np.hstack((f[cycles['V'][j, 0]]))
        dQdV = np.hstack((f[cycles['discharge_dQdV'][j, 0]]))
        t = np.hstack((f[cycles['t'][j, 0]]))
        cd = {'I': I, 'Qc': Qc, 'Qd': Qd, 'Qdlin': Qdlin,
              'T': T, 'Tdlin': Tdlin, 'V': V, 'dQdV': dQdV, 't': t}
        cycle_dict[str(j)] = cd

    cell_dict = {'cycle_life': cl, 'charge_policy': policy,
                 'summary': summary, 'cycles': cycle_dict}
    key = 'b1c' + str(i)
    bat_dict[key] = cell_dict

# Test for charge policy
# strlist = ""
# for c in bat_dict['b1c0']['charge_policy']:
#     strlist = strlist + chr(c[0])
# print(strlist)


# Summary data

# Available sizes (summary)
summ_batch_size = "Batch size: " + str(num_cells)
summ_cell_size = "Cell size: " + \
    str(len(bat_dict["b1c" + str(num_cells-1)]['summary']['cycle']))
# print(summ_batch_size + "\n" + summ_cell_size)

# Individual cells


def summ_all(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1

    cycle = bat_dict[batch_num]['summary']['cycle'][cell_num]
    QD = bat_dict[batch_num]['summary']['QD'][cell_num]
    QC = bat_dict[batch_num]['summary']['QC'][cell_num]
    IR = bat_dict[batch_num]['summary']['IR'][cell_num]
    Tmax = bat_dict[batch_num]['summary']['Tmax'][cell_num]
    Tmin = bat_dict[batch_num]['summary']['Tmin'][cell_num]
    Tavg = bat_dict[batch_num]['summary']['Tavg'][cell_num]
    chargetime = bat_dict[batch_num]['summary']['chargetime'][cell_num]

    print("Cycle: {} \nQDischarge: {} \nQCharge: {} \nIR: {} \nTmax: {} \nTmin: {} \nTavg: {} \nCharge Time: {}".format(
          cycle, QD, QC, IR, Tmax, Tmin, Tavg, chargetime))


def summ_cycle(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['cycle'][cell_num])


def summ_Qd(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['QD'][cell_num])


def summ_Qc(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['QC'][cell_num])


def summ_IR(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['IR'][cell_num])


def summ_Tmax(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['Tmax'][cell_num])


def summ_Tmin(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['Tmin'][cell_num])


def summ_Tavg(batch, cell):
    batch_num = 'b1c' + str(batch)
    cell_num = cell-1
    print(bat_dict[batch_num]['summary']['Tavg'][cell_num])


def summ_chargetime(batch, cell):
    batch_num = 'b1c' + str(batch-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['summary']['chargetime'][cell_num])


# Cycles

# Available sizes (cycles) --> The cell size differs here because some data has 752/762/751/1001, might need to trim dataset
cycles_batch_size = "Batch size: " + str(num_cells)
cycles_cycle_size = "Cycle size: " + \
    str(len(bat_dict["b1c" + str(num_cells-1)]['cycles']))
cycles_cell_size = ("Cell size: " +
                    str(len(bat_dict["b1c" + str(num_cells-1)]['cycles']['0']['t'])))
# print(cycles_batch_size + "\n" + cycles_cycle_size + "\n" + cycles_cell_size)


# Individual cells


def cycles_all(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    t = bat_dict[batch_num]['cycles'][cycle_num]['t'][cell_num]
    QD = bat_dict[batch_num]['cycles'][cycle_num]['Qd'][cell_num]
    QC = bat_dict[batch_num]['cycles'][cycle_num]['Qc'][cell_num]
    I = bat_dict[batch_num]['cycles'][cycle_num]['I'][cell_num]
    V = bat_dict[batch_num]['cycles'][cycle_num]['V'][cell_num]
    T = bat_dict[batch_num]['cycles'][cycle_num]['T'][cell_num]
    Tdlin = bat_dict[batch_num]['cycles'][cycle_num]['Tdlin'][cell_num]
    Qdlin = bat_dict[batch_num]['cycles'][cycle_num]['Qdlin'][cell_num]
    dQdV = bat_dict[batch_num]['cycles'][cycle_num]['dQdV'][cell_num]

    print("Time: {} \nQDischarge: {} \nQCharge: {} \nCurrent: {} \nVoltage: {} \nTemperature: {} \nTdlin: {} \nQdlin: {} \ndQdV: {}".format(
          t, QD, QC, I, V, T, Tdlin, Qdlin, dQdV))


def cycles_t(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['t'][cell_num])


def cycles_Qd(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['Qd'][cell_num])


def cycles_Qc(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['Qc'][cell_num])


def cycles_I(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['I'][cell_num])


def cycles_V(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['V'][cell_num])


def cycles_T(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['T'][cell_num])


def cycles_Tdlin(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['Tdlin'][cell_num])


def cycles_Qdlin(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['Qdlin'][cell_num])


def cycles_dQdV(batch, cycle, cell):
    batch_num = 'b1c' + str(batch-1)
    cycle_num = str(cycle-1)
    cell_num = cell-1

    print(bat_dict[batch_num]['cycles'][cycle_num]['dQdV'][cell_num])


cycles_all(46, 120, 740)
