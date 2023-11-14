# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Tue 14 Nov 2023 15:12:04



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
gZp = Parameter(name = 'gZp',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'g_{\\text{Zp}}',
                lhablock = 'NPINPUTS',
                lhacode = [ 1 ])

Sa = Parameter(name = 'Sa',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\text{Sa}',
               lhablock = 'NPINPUTS',
               lhacode = [ 2 ])

gchi = Parameter(name = 'gchi',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\chi }',
                 lhablock = 'NPINPUTS',
                 lhacode = [ 3 ])

gqV = Parameter(name = 'gqV',
                nature = 'external',
                type = 'real',
                value = 0.5,
                texname = 'g_{\\text{qV}}',
                lhablock = 'NPINPUTS',
                lhacode = [ 4 ])

gqA = Parameter(name = 'gqA',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = 'g_{\\text{qA}}',
                lhablock = 'NPINPUTS',
                lhacode = [ 5 ])

ychi = Parameter(name = 'ychi',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{ychi}',
                 lhablock = 'NPINPUTS',
                 lhacode = [ 6 ])

Se = Parameter(name = 'Se',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{Se}',
               lhablock = 'NPINPUTS',
               lhacode = [ 7 ])

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

Mh = Parameter(name = 'Mh',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{Mh}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MSd = Parameter(name = 'MSd',
                nature = 'external',
                type = 'real',
                value = 450,
                texname = '\\text{MSd}',
                lhablock = 'MASS',
                lhacode = [ 9900026 ])

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

Wh = Parameter(name = 'Wh',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{Wh}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WSd = Parameter(name = 'WSd',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{WSd}',
                lhablock = 'DECAY',
                lhacode = [ 9900026 ])

Wchi = Parameter(name = 'Wchi',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Wchi}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000006 ])

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

gqL = Parameter(name = 'gqL',
                nature = 'internal',
                type = 'real',
                value = 'gqA + gqV',
                texname = 'g_{\\text{qL}}')

gqR = Parameter(name = 'gqR',
                nature = 'internal',
                type = 'real',
                value = '-gqA + gqV',
                texname = 'g_{\\text{qA}}')

gsd = Parameter(name = 'gsd',
                nature = 'internal',
                type = 'real',
                value = '-2*gchi',
                texname = 'g_{\\text{sd}}')

vev2 = Parameter(name = 'vev2',
                 nature = 'internal',
                 type = 'real',
                 value = 'MZp/(2.*gchi)',
                 texname = '\\text{vev2}')

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

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*MSd**2)/(2.*vev2**2) + (Mh**2*Sa**2)/(2.*vev2**2)',
                 texname = '\\text{lam2}')

Mnew = Parameter(name = 'Mnew',
                 nature = 'internal',
                 type = 'real',
                 value = 'Mchi + (vev2*ychi)/(2.*cmath.sqrt(2))',
                 texname = '\\text{Mnew}')

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

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca**2*Mh**2)/(2.*vev**2) + (MSd**2*Sa**2)/(2.*vev**2)',
                 texname = '\\text{lam1}')

lam3 = Parameter(name = 'lam3',
                 nature = 'internal',
                 type = 'real',
                 value = '(Ca*(-Mh**2 + MSd**2)*Sa)/(vev*vev2)',
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

mu2h = Parameter(name = 'mu2h',
                 nature = 'internal',
                 type = 'real',
                 value = 'lam1*vev**2 + (lam3*vev2**2)/2.',
                 texname = '\\mu')

mu2Sd = Parameter(name = 'mu2Sd',
                  nature = 'internal',
                  type = 'real',
                  value = '(lam3*vev**2)/2. + lam2*vev2**2',
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

