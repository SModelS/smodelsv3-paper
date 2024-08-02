# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Fri 2 Aug 2024 15:07:54


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(cosa*ee**2)/(2.*cw)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-6*cosa**3*complex(0,1)*lam1*vev',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cosa*complex(0,1)*lam3*vev)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(cosa**3*complex(0,1)*lam3*vev)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-2*complex(0,1)*lam1*sina*vev',
                  order = {'NP':1,'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(complex(0,1)*lam3*sina*vev)',
                  order = {'NP':1,'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-3*cosa**2*complex(0,1)*lam3*sina*vev',
                  order = {'NP':1,'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-3*cosa*complex(0,1)*lam3*sina**2*vev',
                  order = {'NP':2,'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-6*complex(0,1)*lam1*sina**3*vev',
                  order = {'NP':3,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(complex(0,1)*lam3*sina**3*vev)',
                  order = {'NP':3,'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-0.25*(ee**2*vev)/sw**2',
                  order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-0.25*(cosa*ee**2*complex(0,1)*vev)/sw**2',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cosa*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-0.25*(ee**2*complex(0,1)*sina*vev)/sw**2',
                  order = {'NP':1,'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee**2*complex(0,1)*sina*vev)/(2.*sw**2)',
                  order = {'NP':1,'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-0.5*(ee**2*vev)/sw',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-6*cosa**2*complex(0,1)*lam1*sina*vev + 2*cosa**2*complex(0,1)*lam3*sina*vev',
                  order = {'NP':1,'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-6*cosa*complex(0,1)*lam1*sina**2*vev + 2*cosa*complex(0,1)*lam3*sina**2*vev',
                  order = {'NP':2,'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-0.5*(cosa*ee**2*complex(0,1)*vev) - (cosa*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (cosa*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = 'cosa*ee**2*complex(0,1)*vev + (cosa*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (cosa*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-0.5*(ee**2*complex(0,1)*sina*vev) - (cw**2*ee**2*complex(0,1)*sina*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sina*sw**2*vev)/(4.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = 'ee**2*complex(0,1)*sina*vev + (cw**2*ee**2*complex(0,1)*sina*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sina*sw**2*vev)/(2.*cw**2)',
                  order = {'NP':1,'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-2*cosa*complex(0,1)*lam2*vev2',
                  order = {'NP':-1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-6*cosa**3*complex(0,1)*lam2*vev2',
                  order = {'NP':-1,'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(cosa*complex(0,1)*lam3*vev2)',
                  order = {'NP':-1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = 'G',
                 order = {'QCD':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cosa**3*complex(0,1)*lam3*vev2)',
                  order = {'NP':-1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '2*cosa*complex(0,1)*gZp**2*QBphi**2*vev2',
                  order = {'NP':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '2*complex(0,1)*lam2*sina*vev2',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = 'complex(0,1)*lam3*sina*vev2',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '3*cosa**2*complex(0,1)*lam3*sina*vev2',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-2*complex(0,1)*gZp**2*QBphi**2*sina*vev2',
                  order = {'NP':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-3*cosa*complex(0,1)*lam3*sina**2*vev2',
                  order = {'NP':1,'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '6*complex(0,1)*lam2*sina**3*vev2',
                  order = {'NP':2,'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = 'complex(0,1)*lam3*sina**3*vev2',
                  order = {'NP':2,'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '6*cosa**2*complex(0,1)*lam2*sina*vev2 - 2*cosa**2*complex(0,1)*lam3*sina*vev2',
                  order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-6*cosa*complex(0,1)*lam2*sina**2*vev2 + 2*cosa*complex(0,1)*lam3*sina**2*vev2',
                  order = {'NP':1,'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(ychi/cmath.sqrt(2))',
                  order = {'NP':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((cosa*complex(0,1)*ychi)/cmath.sqrt(2))',
                  order = {'NP':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(complex(0,1)*sina*ychi)/cmath.sqrt(2)',
                  order = {'NP':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cosa*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*sina*yt)/cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-ytau',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = 'ytau',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cosa*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*sina*ytau)/cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*gchi)',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-I2a33',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'I3a33',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-2*complex(0,1)*lam1',
                 order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-6*complex(0,1)*lam1',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-2*cosa**2*complex(0,1)*lam1',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-6*cosa**4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-6*complex(0,1)*lam2',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-2*cosa**2*complex(0,1)*lam2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-6*cosa**4*complex(0,1)*lam2',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(complex(0,1)*lam3)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cosa**2*complex(0,1)*lam3)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(cosa**4*complex(0,1)*lam3)',
                 order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(cosa*gZp*QBphi)',
                 order = {'NP':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'cosa*gZp*QBphi',
                 order = {'NP':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '2*complex(0,1)*gZp**2*QBphi**2',
                 order = {'NP':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '2*cosa**2*complex(0,1)*gZp**2*QBphi**2',
                 order = {'NP':2})

GC_34 = Coupling(name = 'GC_34',
                 value = 'complex(0,1)*gZp*QBq',
                 order = {'NP':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-0.5*(ee**2*sina)/cw',
                 order = {'NP':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee**2*sina)/(2.*cw)',
                 order = {'NP':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(gZp*QBphi*sina)',
                 order = {'NP':2})

GC_38 = Coupling(name = 'GC_38',
                 value = 'gZp*QBphi*sina',
                 order = {'NP':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-2*cosa*complex(0,1)*gZp**2*QBphi**2*sina',
                 order = {'NP':3})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-2*complex(0,1)*lam1*sina**2',
                 order = {'NP':2,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-2*complex(0,1)*lam2*sina**2',
                 order = {'NP':2,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(complex(0,1)*lam3*sina**2)',
                 order = {'NP':2,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-6*cosa**2*complex(0,1)*lam3*sina**2',
                 order = {'NP':2,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '2*complex(0,1)*gZp**2*QBphi**2*sina**2',
                 order = {'NP':4})

GC_45 = Coupling(name = 'GC_45',
                 value = '-6*complex(0,1)*lam1*sina**4',
                 order = {'NP':4,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-6*complex(0,1)*lam2*sina**4',
                 order = {'NP':4,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(complex(0,1)*lam3*sina**4)',
                 order = {'NP':4,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '2*cosa*complex(0,1)*lam2*sina - cosa*complex(0,1)*lam3*sina',
                 order = {'NP':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-2*cosa*complex(0,1)*lam1*sina + cosa*complex(0,1)*lam3*sina',
                 order = {'NP':1,'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '6*cosa**3*complex(0,1)*lam2*sina - 3*cosa**3*complex(0,1)*lam3*sina',
                 order = {'NP':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-6*cosa**3*complex(0,1)*lam1*sina + 3*cosa**3*complex(0,1)*lam3*sina',
                 order = {'NP':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-6*cosa**2*complex(0,1)*lam1*sina**2 - 6*cosa**2*complex(0,1)*lam2*sina**2 + 4*cosa**2*complex(0,1)*lam3*sina**2',
                 order = {'NP':2,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '6*cosa*complex(0,1)*lam2*sina**3 - 3*cosa*complex(0,1)*lam3*sina**3',
                 order = {'NP':3,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-6*cosa*complex(0,1)*lam1*sina**3 + 3*cosa*complex(0,1)*lam3*sina**3',
                 order = {'NP':3,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cosa**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cosa*ee**2*complex(0,1)*sina)/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee**2*complex(0,1)*sina**2)/(2.*sw**2)',
                 order = {'NP':2,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-0.5*(cosa*ee)/sw',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cosa*ee)/(2.*sw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.5*(cosa*ee**2)/sw',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cosa*ee**2)/(2.*sw)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-0.5*(ee*sina)/sw',
                 order = {'NP':1,'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee*sina)/(2.*sw)',
                 order = {'NP':1,'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-0.5*(ee**2*sina)/sw',
                 order = {'NP':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee**2*sina)/(2.*sw)',
                 order = {'NP':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-0.5*(cosa*cw*ee)/sw - (cosa*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cosa*cw*ee)/(2.*sw) + (cosa*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-0.5*(cosa*ee**2)/cw',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '-0.5*(cw*ee*sina)/sw - (ee*sina*sw)/(2.*cw)',
                 order = {'NP':1,'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cw*ee*sina)/(2.*sw) + (ee*sina*sw)/(2.*cw)',
                 order = {'NP':1,'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = 'cosa**2*ee**2*complex(0,1) + (cosa**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cosa**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = 'cosa*ee**2*complex(0,1)*sina + (cosa*cw**2*ee**2*complex(0,1)*sina)/(2.*sw**2) + (cosa*ee**2*complex(0,1)*sina*sw**2)/(2.*cw**2)',
                 order = {'NP':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = 'ee**2*complex(0,1)*sina**2 + (cw**2*ee**2*complex(0,1)*sina**2)/(2.*sw**2) + (ee**2*complex(0,1)*sina**2*sw**2)/(2.*cw**2)',
                 order = {'NP':2,'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-0.5*(ee**2*vev)/cw',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-2*cosa*complex(0,1)*lam1*vev',
                 order = {'QED':1})

