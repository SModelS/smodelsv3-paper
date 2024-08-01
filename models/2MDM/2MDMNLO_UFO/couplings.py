# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Tue 30 Jul 2024 12:00:12


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(Ca*ee**2)/(2.*cw)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-2*Ca*complex(0,1)*lam1*vev',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-6*Ca**3*complex(0,1)*lam1*vev',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(Ca*complex(0,1)*lam3*vev)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(Ca**3*complex(0,1)*lam3*vev)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-2*complex(0,1)*lam1*Sa*vev',
                  order = {'QED':3})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(complex(0,1)*lam3*Sa*vev)',
                  order = {'QED':3})

GC_106 = Coupling(name = 'GC_106',
                  value = '-3*Ca**2*complex(0,1)*lam3*Sa*vev',
                  order = {'QED':3})

GC_107 = Coupling(name = 'GC_107',
                  value = '-3*Ca*complex(0,1)*lam3*Sa**2*vev',
                  order = {'QED':5})

GC_108 = Coupling(name = 'GC_108',
                  value = '-6*complex(0,1)*lam1*Sa**3*vev',
                  order = {'QED':7})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(complex(0,1)*lam3*Sa**3*vev)',
                  order = {'QED':7})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-0.25*(ee**2*vev)/sw**2',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-0.25*(Ca*ee**2*complex(0,1)*vev)/sw**2',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(Ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-0.25*(ee**2*complex(0,1)*Sa*vev)/sw**2',
                  order = {'QED':3})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee**2*complex(0,1)*Sa*vev)/(2.*sw**2)',
                  order = {'QED':3})

GC_116 = Coupling(name = 'GC_116',
                  value = '-0.5*(ee**2*vev)/sw',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-6*Ca**2*complex(0,1)*lam1*Sa*vev + 2*Ca**2*complex(0,1)*lam3*Sa*vev',
                  order = {'QED':3})

GC_119 = Coupling(name = 'GC_119',
                  value = '-6*Ca*complex(0,1)*lam1*Sa**2*vev + 2*Ca*complex(0,1)*lam3*Sa**2*vev',
                  order = {'QED':5})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.5*(Ca*ee**2*complex(0,1)*vev) - (Ca*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (Ca*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = 'Ca*ee**2*complex(0,1)*vev + (Ca*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-0.5*(ee**2*complex(0,1)*Sa*vev) - (cw**2*ee**2*complex(0,1)*Sa*vev)/(4.*sw**2) - (ee**2*complex(0,1)*Sa*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':3})

GC_127 = Coupling(name = 'GC_127',
                  value = 'ee**2*complex(0,1)*Sa*vev + (cw**2*ee**2*complex(0,1)*Sa*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Sa*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':3})

GC_128 = Coupling(name = 'GC_128',
                  value = '8*Ca*complex(0,1)*gchi**2*gZp**2*vev2',
                  order = {'NP':2,'QED':3})

GC_129 = Coupling(name = 'GC_129',
                  value = '-2*Ca*complex(0,1)*lam2*vev2',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'G',
                 order = {'QCD':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-6*Ca**3*complex(0,1)*lam2*vev2',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(Ca*complex(0,1)*lam3*vev2)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(Ca**3*complex(0,1)*lam3*vev2)',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-8*complex(0,1)*gchi**2*gZp**2*Sa*vev2',
                  order = {'NP':2,'QED':5})

GC_134 = Coupling(name = 'GC_134',
                  value = '2*complex(0,1)*lam2*Sa*vev2',
                  order = {'QED':3})

GC_135 = Coupling(name = 'GC_135',
                  value = 'complex(0,1)*lam3*Sa*vev2',
                  order = {'QED':3})

GC_136 = Coupling(name = 'GC_136',
                  value = '3*Ca**2*complex(0,1)*lam3*Sa*vev2',
                  order = {'QED':3})

GC_137 = Coupling(name = 'GC_137',
                  value = '-3*Ca*complex(0,1)*lam3*Sa**2*vev2',
                  order = {'QED':5})

GC_138 = Coupling(name = 'GC_138',
                  value = '6*complex(0,1)*lam2*Sa**3*vev2',
                  order = {'QED':7})

GC_139 = Coupling(name = 'GC_139',
                  value = 'complex(0,1)*lam3*Sa**3*vev2',
                  order = {'QED':7})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '6*Ca**2*complex(0,1)*lam2*Sa*vev2 - 2*Ca**2*complex(0,1)*lam3*Sa*vev2',
                  order = {'QED':3})

GC_141 = Coupling(name = 'GC_141',
                  value = '-6*Ca*complex(0,1)*lam2*Sa**2*vev2 + 2*Ca*complex(0,1)*lam3*Sa**2*vev2',
                  order = {'QED':5})

GC_142 = Coupling(name = 'GC_142',
                  value = '-(ychi/cmath.sqrt(2))',
                  order = {'NP':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((Ca*complex(0,1)*ychi)/cmath.sqrt(2))',
                  order = {'NP':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(complex(0,1)*Sa*ychi)/cmath.sqrt(2)',
                  order = {'NP':1,'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                  order = {'QED':3})

GC_149 = Coupling(name = 'GC_149',
                  value = '-ytau',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_150 = Coupling(name = 'GC_150',
                  value = 'ytau',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                  order = {'QED':3})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*gchi)',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-2*Ca*gchi*gZp',
                 order = {'NP':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '2*Ca*gchi*gZp',
                 order = {'NP':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*gqL*gZp',
                 order = {'NP':1,'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*gqR*gZp',
                 order = {'NP':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '8*complex(0,1)*gchi**2*gZp**2',
                 order = {'NP':2,'QED':4})

GC_22 = Coupling(name = 'GC_22',
                 value = '8*Ca**2*complex(0,1)*gchi**2*gZp**2',
                 order = {'NP':2,'QED':4})

GC_23 = Coupling(name = 'GC_23',
                 value = '-I2a33',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = 'I3a33',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-2*complex(0,1)*lam1',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-6*complex(0,1)*lam1',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-2*Ca**2*complex(0,1)*lam1',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-6*Ca**4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-6*complex(0,1)*lam2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-2*Ca**2*complex(0,1)*lam2',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-6*Ca**4*complex(0,1)*lam2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(complex(0,1)*lam3)',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(Ca**2*complex(0,1)*lam3)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(Ca**4*complex(0,1)*lam3)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(ee**2*Sa)/cw',
                 order = {'QED':4})

GC_37 = Coupling(name = 'GC_37',
                 value = '(ee**2*Sa)/(2.*cw)',
                 order = {'QED':4})

GC_38 = Coupling(name = 'GC_38',
                 value = '-2*gchi*gZp*Sa',
                 order = {'NP':1,'QED':4})

GC_39 = Coupling(name = 'GC_39',
                 value = '2*gchi*gZp*Sa',
                 order = {'NP':1,'QED':4})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-8*Ca*complex(0,1)*gchi**2*gZp**2*Sa',
                 order = {'NP':2,'QED':6})

GC_41 = Coupling(name = 'GC_41',
                 value = '8*complex(0,1)*gchi**2*gZp**2*Sa**2',
                 order = {'NP':2,'QED':8})

GC_42 = Coupling(name = 'GC_42',
                 value = '-2*complex(0,1)*lam1*Sa**2',
                 order = {'QED':6})

GC_43 = Coupling(name = 'GC_43',
                 value = '-2*complex(0,1)*lam2*Sa**2',
                 order = {'QED':6})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(complex(0,1)*lam3*Sa**2)',
                 order = {'QED':6})

GC_45 = Coupling(name = 'GC_45',
                 value = '-6*Ca**2*complex(0,1)*lam3*Sa**2',
                 order = {'QED':6})

GC_46 = Coupling(name = 'GC_46',
                 value = '-6*complex(0,1)*lam1*Sa**4',
                 order = {'QED':10})

GC_47 = Coupling(name = 'GC_47',
                 value = '-6*complex(0,1)*lam2*Sa**4',
                 order = {'QED':10})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(complex(0,1)*lam3*Sa**4)',
                 order = {'QED':10})

GC_49 = Coupling(name = 'GC_49',
                 value = '2*Ca*complex(0,1)*lam2*Sa - Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':4})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-2*Ca*complex(0,1)*lam1*Sa + Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':4})

GC_51 = Coupling(name = 'GC_51',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa',
                 order = {'QED':4})

GC_52 = Coupling(name = 'GC_52',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa',
                 order = {'QED':4})

GC_53 = Coupling(name = 'GC_53',
                 value = '-6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2',
                 order = {'QED':6})

GC_54 = Coupling(name = 'GC_54',
                 value = '6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':8})

GC_55 = Coupling(name = 'GC_55',
                 value = '-6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':8})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'QED':4})

GC_63 = Coupling(name = 'GC_63',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'QED':6})

GC_64 = Coupling(name = 'GC_64',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-0.5*(Ca*ee)/sw',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(Ca*ee)/(2.*sw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '-0.5*(Ca*ee**2)/sw',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(Ca*ee**2)/(2.*sw)',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '-0.5*(ee*Sa)/sw',
                 order = {'QED':3})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee*Sa)/(2.*sw)',
                 order = {'QED':3})

GC_78 = Coupling(name = 'GC_78',
                 value = '-0.5*(ee**2*Sa)/sw',
                 order = {'QED':4})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee**2*Sa)/(2.*sw)',
                 order = {'QED':4})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-0.5*(Ca*cw*ee)/sw - (Ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(Ca*cw*ee)/(2.*sw) + (Ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '-0.5*(Ca*ee**2)/cw',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '-0.5*(cw*ee*Sa)/sw - (ee*Sa*sw)/(2.*cw)',
                 order = {'QED':3})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cw*ee*Sa)/(2.*sw) + (ee*Sa*sw)/(2.*cw)',
                 order = {'QED':3})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = 'Ca**2*ee**2*complex(0,1) + (Ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (Ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = 'Ca*ee**2*complex(0,1)*Sa + (Ca*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'QED':4})

GC_97 = Coupling(name = 'GC_97',
                 value = 'ee**2*complex(0,1)*Sa**2 + (cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) + (ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':6})

GC_98 = Coupling(name = 'GC_98',
                 value = '-0.5*(ee**2*vev)/cw',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

