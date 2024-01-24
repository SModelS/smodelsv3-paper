# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Thu 14 Sep 2023 17:02:36


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(Ca*ee**2)/(2.*cw)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-0.5*(Ca*ee**2*complex(0,1)*vev) - (Ca*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (Ca*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = 'Ca*ee**2*complex(0,1)*vev + (Ca*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-0.5*(ee**2*complex(0,1)*Sa*vev) - (cw**2*ee**2*complex(0,1)*Sa*vev)/(4.*sw**2) - (ee**2*complex(0,1)*Sa*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'ee**2*complex(0,1)*Sa*vev + (cw**2*ee**2*complex(0,1)*Sa*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Sa*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '8*Ca*complex(0,1)*gchi**2*gZp**2*vev2',
                  order = {'NP':2,'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-8*complex(0,1)*gchi**2*gZp**2*Sa*vev2',
                  order = {'NP':2,'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(complex(0,1)*lam3*Sa*vev) - 2*Ca*complex(0,1)*lam2*vev2',
                  order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-2*complex(0,1)*lam1*Sa*vev - Ca*complex(0,1)*lam3*vev2',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(Ca*complex(0,1)*lam3*vev) + 2*complex(0,1)*lam2*Sa*vev2',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-2*Ca*complex(0,1)*lam1*vev + complex(0,1)*lam3*Sa*vev2',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-6*Ca**2*complex(0,1)*lam1*Sa*vev + 2*Ca**2*complex(0,1)*lam3*Sa*vev - complex(0,1)*lam3*Sa**3*vev - Ca**3*complex(0,1)*lam3*vev2 - 6*Ca*complex(0,1)*lam2*Sa**2*vev2 + 2*Ca*complex(0,1)*lam3*Sa**2*vev2',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-3*Ca**2*complex(0,1)*lam3*Sa*vev - 6*complex(0,1)*lam1*Sa**3*vev - 6*Ca**3*complex(0,1)*lam2*vev2 - 3*Ca*complex(0,1)*lam3*Sa**2*vev2',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-6*Ca**3*complex(0,1)*lam1*vev - 3*Ca*complex(0,1)*lam3*Sa**2*vev + 3*Ca**2*complex(0,1)*lam3*Sa*vev2 + 6*complex(0,1)*lam2*Sa**3*vev2',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(Ca**3*complex(0,1)*lam3*vev) - 6*Ca*complex(0,1)*lam1*Sa**2*vev + 2*Ca*complex(0,1)*lam3*Sa**2*vev + 6*Ca**2*complex(0,1)*lam2*Sa*vev2 - 2*Ca**2*complex(0,1)*lam3*Sa*vev2 + complex(0,1)*lam3*Sa**3*vev2',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-(ychi/cmath.sqrt(2))',
                  order = {'NP':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((Ca*complex(0,1)*ychi)/cmath.sqrt(2))',
                  order = {'NP':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(complex(0,1)*Sa*ychi)/cmath.sqrt(2)',
                  order = {'NP':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-ytau',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = 'ytau',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'G',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*gchi)',
                 order = {'NP':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-2*Ca*gchi*gZp',
                 order = {'NP':1,'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '2*Ca*gchi*gZp',
                 order = {'NP':1,'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*gqL*gZp',
                 order = {'NP':1,'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*gqR*gZp',
                 order = {'NP':1,'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '8*complex(0,1)*gchi**2*gZp**2',
                 order = {'NP':2,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '8*Ca**2*complex(0,1)*gchi**2*gZp**2',
                 order = {'NP':2,'QED':2})

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
                 value = '-6*complex(0,1)*lam2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(complex(0,1)*lam3)',
                 order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-0.5*(ee**2*Sa)/cw',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee**2*Sa)/(2.*cw)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-2*gchi*gZp*Sa',
                 order = {'NP':1,'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '2*gchi*gZp*Sa',
                 order = {'NP':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-8*Ca*complex(0,1)*gchi**2*gZp**2*Sa',
                 order = {'NP':2,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '8*complex(0,1)*gchi**2*gZp**2*Sa**2',
                 order = {'NP':2,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '2*Ca*complex(0,1)*lam2*Sa - Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-2*Ca*complex(0,1)*lam1*Sa + Ca*complex(0,1)*lam3*Sa',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(Ca**2*complex(0,1)*lam3) - 2*complex(0,1)*lam1*Sa**2',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(Ca**2*complex(0,1)*lam3) - 2*complex(0,1)*lam2*Sa**2',
                 order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-2*Ca**2*complex(0,1)*lam1 - complex(0,1)*lam3*Sa**2',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-2*Ca**2*complex(0,1)*lam2 - complex(0,1)*lam3*Sa**2',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa + 6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa - 6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-6*Ca**4*complex(0,1)*lam2 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam1*Sa**4',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-6*Ca**4*complex(0,1)*lam1 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam2*Sa**4',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(Ca**4*complex(0,1)*lam3) - 6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2 - complex(0,1)*lam3*Sa**4',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(Ca*ee)/sw',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(Ca*ee)/(2.*sw)',
                 order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '-2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-0.5*(ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-0.5*(Ca*ee**2)/sw',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(Ca*ee**2)/(2.*sw)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-0.5*(ee*Sa)/sw',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*Sa)/(2.*sw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-0.5*(ee**2*Sa)/sw',
                 order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(ee**2*Sa)/(2.*sw)',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.5*(Ca*cw*ee)/sw - (Ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(Ca*cw*ee)/(2.*sw) + (Ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-0.5*(cw*ee*Sa)/sw - (ee*Sa*sw)/(2.*cw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cw*ee*Sa)/(2.*sw) + (ee*Sa*sw)/(2.*cw)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = 'Ca**2*ee**2*complex(0,1) + (Ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (Ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = 'Ca*ee**2*complex(0,1)*Sa + (Ca*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = 'ee**2*complex(0,1)*Sa**2 + (cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) + (ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-0.5*(ee**2*vev)/cw',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '-0.5*(Ca*ee**2)/cw',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-0.25*(ee**2*vev)/sw**2',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-0.25*(Ca*ee**2*complex(0,1)*vev)/sw**2',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(Ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-0.25*(ee**2*complex(0,1)*Sa*vev)/sw**2',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee**2*complex(0,1)*Sa*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-0.5*(ee**2*vev)/sw',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

