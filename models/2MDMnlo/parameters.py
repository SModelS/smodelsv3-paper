# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Thu 24 Aug 2023 14:37:31



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
g1p = Parameter(name = 'g1p',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_p',
                lhablock = 'BLINPUTS',
                lhacode = [ 1 ])

MH2 = Parameter(name = 'MH2',
                nature = 'external',
                type = 'real',
                value = 450.,
                texname = '\\text{MH2}',
                lhablock = 'BLINPUTS',
                lhacode = [ 2 ])

Sa = Parameter(name = 'Sa',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{Sa}',
               lhablock = 'BLINPUTS',
               lhacode = [ 3 ])

Se = Parameter(name = 'Se',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{Se}',
               lhablock = 'BLINPUTS',
               lhacode = [ 4 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

gchi = Parameter(name = 'gchi',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\chi }',
                 lhablock = 'ZPRIME',
                 lhacode = [ 1 ])

gq = Parameter(name = 'gq',
               nature = 'external',
               type = 'real',
               value = 0.5,
               texname = 'g_q',
               lhablock = 'ZPRIME',
               lhacode = [ 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MZp = Parameter(name = 'MZp',
                nature = 'external',
                type = 'real',
                value = 1500,
                texname = '\\text{MZp}',
                lhablock = 'MASS',
                lhacode = [ 9900032 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH1 = Parameter(name = 'MH1',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{MH1}',
                lhablock = 'MASS',
                lhacode = [ 9900025 ])

Mchi = Parameter(name = 'Mchi',
                 nature = 'external',
                 type = 'real',
                 value = 50,
                 texname = '\\text{Mchi}',
                 lhablock = 'MASS',
                 lhacode = [ 9000006 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WZp = Parameter(name = 'WZp',
                nature = 'external',
                type = 'real',
                value = 80.,
                texname = '\\text{WZp}',
                lhablock = 'DECAY',
                lhacode = [ 9900032 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH1 = Parameter(name = 'WH1',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{WH1}',
                lhablock = 'DECAY',
                lhacode = [ 9900025 ])

Wchi = Parameter(name = 'Wchi',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Wchi}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

WH2 = Parameter(name = 'WH2',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{WH2}',
                lhablock = 'DECAY',
                lhacode = [ 9900026 ])

Ca = Parameter(name = 'Ca',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - Sa**2)',
               texname = '\\text{Ca}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

gsd = Parameter(name = 'gsd',
                nature = 'internal',
                type = 'real',
                value = '-2*gchi',
                texname = 'g_{\\text{sd}}')

xev = Parameter(name = 'xev',
                nature = 'internal',
                type = 'real',
                value = 'MZp/(2.*g1p*gchi)',
                texname = '\\text{xev}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(MH1**2 + MH2**2 + (MH1**2 - MH2**2)*(Ca**2 - Sa**2))/MZp**2',
                 texname = '\\text{lam1}')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(gchi**2*(MH1**2 + MH2**2 + (-MH1**2 + MH2**2)*(Ca**2 - Sa**2)))/MZp**2',
                 texname = '\\text{lam2}')

ychi = Parameter(name = 'ychi',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mchi*cmath.sqrt(2))/xev',
                 texname = '\\text{ychi}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*Ca*gchi*(MH1**2 - MH2**2)*Sa)/(MZp*vev)',
                 texname = '\\text{lam3}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

mu2H1 = Parameter(name = 'mu2H1',
                  nature = 'internal',
                  type = 'real',
                  value = '-(lam1*vev**2) - (lam3*xev**2)/2.',
                  texname = '\\mu')

mu2H2 = Parameter(name = 'mu2H2',
                  nature = 'internal',
                  type = 'real',
                  value = '(lam3*vev**2)/2. + lam2*xev**2',
                  texname = '\\text{$\\mu $prime}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

