
import numpy as np
import itertools
from scipy.interpolate import  griddata, interp1d
from matplotlib import pyplot as plt
import re
import pandas as pd


columnsDict = {'mass#9000006' : 'mChi', 
               'mass#9900032' : 'mZp', 
               'mass#9900026' : 'mS',
               'mass.9000006' : 'mChi', 
               'mass.9900032' : 'mZp', 
               'mass.9900026' : 'mS',
               'extpar.1' : 'gchi',
               'extpar.2' : 'gq',
               'extpar.3' : 'sina',
               'npinputs.1' : 'gchi',
               'npinputs.2' : 'gq',
               'npinputs.3' : 'sina',

               }


atlasCurve1 = np.array(list(zip([112.70553064275038, 178.77428998505232, 268.16143497757844, 342.0029895366218, 423.61733931240656, 509.118086696562, 563.5276532137518, 617.9372197309417, 680.1195814648729, 726.7563527653214, 788.9387144992526, 847.2346786248131, 1053.2137518684603, 1173.6920777279522, 1282.5112107623318, 1402.9895366218236, 1573.9910313901344, 1752.7653213751867, 1915.9940209267563, 2129.745889387145],[4.267425320056899, 19.203413940256045, 46.941678520625885, 72.54623044096728, 108.81934566145091, 136.55761024182075, 155.7610241820768, 174.96443812233284, 181.3655761024182, 204.83641536273115, 226.17354196301562, 258.17923186344234, 358.4637268847795, 422.47510668563297, 477.95163584637265, 535.5618776671407, 612.375533428165, 695.5903271692745, 772.4039829302986, 872.6884779516357])))
atlasCurve2 = np.array(list(zip([897.7578475336322, 862.780269058296, 823.9162929745889, 804.4843049327354, 788.9387144992526, 785.0523168908819, 804.4843049327354, 855.0074738415545, 913.3034379671151, 963.8266068759342, 1014.3497757847533, 1080.4185351270553, 1134.8281016442452, 1189.2376681614348, 1247.5336322869955, 1321.3751868460388, 1418.5351270553065],[889.7581792318633, 840.6827880512091, 793.7411095305831, 766.0028449502133, 733.9971550497866, 706.2588904694167, 684.9217638691322, 676.3869132290184, 674.25320056899, 687.0554765291606, 701.9914651493598, 725.4623044096728, 748.9331436699857, 770.2702702702702, 798.00853485064, 832.1479374110952, 872.6884779516357])))



fN = 0.3
mh = 125.0
Mn = 0.939
GF = 1.166e-5
v = 0.001 # From 1904.01017v2 -> below Eq.18
GeVm2Tocmm2 = 1/((5.06e13)**2)
pbTocmm2 = 1e-36
@np.vectorize
def sigmaz_gev(mChi,msd,mZp,sina,gB=None,gchi=None,gq=None):
    """
    Analytical expression for sigma_{chiN}(Zp) from 2405.03749 (Eq.14).
    Note that the equation from 2405.03749 assumes the conventions gchi = -(3/2)*gZp and gq = (gZp/3).
    """

    if gchi is None:
        gchi = -(3./2.)*gB # If gB is given, assume 2405.03749 conventions
    if gq is None:
        gq = (gB/3.0)# If gB is given, assume 2405.03749 conventions
    sv = (27/(2*np.pi))*gchi**2*gq**2*(Mn**2/mZp**4)*v**2
    return sv*GeVm2Tocmm2


# ### LZ limits
# LZ_curve = np.genfromtxt('../data/LZ_2207.03764_SI_limits.txt',names=True)
# LZ_limitF = np.vectorize(interp1d(LZ_curve['mass'],LZ_curve['limit']))
# def LZlimit(mChi):
#     """
#     Spin-independent limits from 2207.03764
#     """

#     return LZ_limitF(mChi)

def readMadDMsummary(scanSummary):

    with open(scanSummary,'r') as f:
        headerLines = [l for l in f.readlines() if l.strip() and l.strip()[0] == '#']
    columnLabels = {eval(re.sub(r'\b0', '',h.split(':')[0].replace('[','').replace(']','').replace('#',''))) : 
                        h.split(':')[1].replace('\n','').strip().replace('%','pc') for h in headerLines}
    header = ['']*len(columnLabels)
    for i,label in columnLabels.items():
        header[i-1] = label
    relicData = pd.read_csv(scanSummary,names=header,
                            comment='#',delimiter='\t',index_col=False)
    # Remove unused columns:
    relicData.drop(columns=[c for c in relicData.columns if 'pc_relic' in c]+['Nevents','smearing','xsi','x_f','sigmav(xf)'],inplace=True)
    # Rename columns:
    renameDict = {'Omegah^2' : 'Omegah2', 'mass#9000006' : 'mChi', 'mass#9900032' : 'mZp', 'mass#9900026' : 'mS'}
    relicData.rename(columns=renameDict,inplace=True)
    
    return relicData

def interpolateData(x,y,z,nx=200,ny=200,method='linear',fill_value=np.nan,xnew=None,ynew=None):

    if x.min() == x.max() or y.min() == y.max(): # Can not interpolate
        return None,None,None
    elif xnew is None or ynew is None:
        xnew = np.linspace(x.min(),x.max(),nx)
        ynew = np.linspace(y.min(),y.max(),ny)

    xi = np.array([list(v) for v in itertools.product(xnew,ynew)])
    znew = griddata(list(zip(x,y)),z,xi=xi, 
                    method=method,fill_value=fill_value)
    znew = np.reshape(znew,(len(xnew),len(ynew)))
    xnew,ynew  = np.meshgrid(xnew,ynew,indexing='ij')

    return xnew,ynew,znew

def getContours(x,y,z,contourValues):
    

    contours = plt.contour(x, y, z, contourValues)
    plt.close()

    contoursDict = {}

    for i,item in enumerate(contours.collections):
        cV = contourValues[i]
        xData = []
        yData = []
        for p in item.get_paths():
            v = p.vertices
            xData += list(v[:, 0])
            yData += list(v[:, 1])
        if len(xData) == 0:
            continue
        contoursDict[cV] = np.array(list(zip(xData,yData)))
    
    return contoursDict

def saveContours(contoursDict,fname,header):

    with open(fname,'w') as f:
        for cV,data in contoursDict.items():
            np.savetxt(f,data,fmt='%.4e',delimiter=',',header=header,comments='\n\n# Contour value=%1.2f \n' %cV)
    print('Contours saved to %s' %fname)

def readContours(fname):

    contoursDict = {}
    with open(fname,'r') as f:
        dataBlocks = f.read().split('#')[1:]
        for data in dataBlocks: 
            data = data.splitlines()
            cV = eval(data[0].split('=')[1])
            dataPts = np.genfromtxt(data,delimiter=',',names=True,skip_header=1)
            contoursDict[cV] = dataPts

    return contoursDict

def label_line(fig,line, label_text, 
               near_i=None, near_x=None, near_y=None, 
               rotation_offset=0, offset=(0,0),fontsize=13,
               xmin=None,rotation=None,boxalpha=1.0):
    """call 
        l, = plt.loglog(x, y)
        label_line(l, "text", near_x=0.32)
    """
    def put_label(i):
        """put label at given index"""
        i = min(i, len(x)-2)
        dx = sx[i+1] - sx[i]
        dy = sy[i+1] - sy[i]
        if rotation is None:
            rot = np.rad2deg(np.arctan2(dy, dx)) + rotation_offset
        else:
            rot = rotation
        pos = [(x[i] + x[i+1])/2. + offset[0], (y[i] + y[i+1])/2 + offset[1]]
        if pos[0] > xmin:
            plt.text(pos[0], pos[1], label_text, size=fontsize, 
                     rotation=rot, color = line.get_color(),
                     ha="center", va="center", bbox = dict(ec='1',fc='1',alpha=boxalpha))

    x = line.get_xdata()
    y = line.get_ydata()
    ax = fig.get_axes()[0]
    if ax.get_xscale() == 'log':
        sx = np.log10(x)    # screen space
    else:
        sx = x
    if ax.get_yscale() == 'log':
        sy = np.log10(y)
    else:
        sy = y

    # find index
    if near_i is not None:
        i = near_i
        if i < 0: # sanitize negative i
            i = len(x) + i
        put_label(i)
    elif near_x is not None:
        for i in range(len(x)-2):
            if (x[i] < near_x and x[i+1] >= near_x) or (x[i+1] < near_x and x[i] >= near_x):
                put_label(i)
    elif near_y is not None:
        for i in range(len(y)-2):
            if (y[i] < near_y and y[i+1] >= near_y) or (y[i+1] < near_y and y[i] >= near_y):
                put_label(i)
    else:
        raise ValueError("Need one of near_i, near_x, near_y")
