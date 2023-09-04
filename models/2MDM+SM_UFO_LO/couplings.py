# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Sat 26 Aug 2023 18:11:30


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(complex(0,1)*gchi*gZp)/2.',
                order = {'NP':1,'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*gq*gZp',
                 order = {'NP':1,'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '2*Ca**2*complex(0,1)*gsd**2*gZp**2',
                 order = {'NP':2,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-6*Ca**4*complex(0,1)*lam1',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-6*Ca**4*complex(0,1)*lam2',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(Ca**4*complex(0,1)*lam3)',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-2*Ca*complex(0,1)*gsd**2*gZp**2*Sa',
                 order = {'NP':3,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '2*complex(0,1)*gsd**2*gZp**2*Sa**2',
                 order = {'NP':4,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-6*Ca**2*complex(0,1)*lam3*Sa**2',
                 order = {'NP':2,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-6*complex(0,1)*lam1*Sa**4',
                 order = {'NP':4,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-6*complex(0,1)*lam2*Sa**4',
                 order = {'NP':4,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(complex(0,1)*lam3*Sa**4)',
                 order = {'NP':4,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa',
                 order = {'NP':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa',
                 order = {'NP':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2',
                 order = {'NP':2,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'NP':3,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'NP':3,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'NP':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'NP':2,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '-0.16666666666666666*(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'Ca**2*ee**2*complex(0,1) + (Ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (Ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = 'Ca*ee**2*complex(0,1)*Sa + (Ca*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'NP':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ee**2*complex(0,1)*Sa**2 + (cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) + (ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'NP':2,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-6*Ca**3*complex(0,1)*lam1*vev',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(Ca**3*complex(0,1)*lam3*vev)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-3*Ca**2*complex(0,1)*lam3*Sa*vev',
                 order = {'NP':1,'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-3*Ca*complex(0,1)*lam3*Sa**2*vev',
                 order = {'NP':2,'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-6*complex(0,1)*lam1*Sa**3*vev',
                 order = {'NP':3,'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(complex(0,1)*lam3*Sa**3*vev)',
                 order = {'NP':3,'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(Ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee**2*complex(0,1)*Sa*vev)/(2.*sw**2)',
                 order = {'NP':1,'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-6*Ca**2*complex(0,1)*lam1*Sa*vev + 2*Ca**2*complex(0,1)*lam3*Sa*vev',
                 order = {'NP':1,'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-6*Ca*complex(0,1)*lam1*Sa**2*vev + 2*Ca*complex(0,1)*lam3*Sa**2*vev',
                 order = {'NP':2,'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = 'Ca*ee**2*complex(0,1)*vev + (Ca*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (Ca*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'ee**2*complex(0,1)*Sa*vev + (cw**2*ee**2*complex(0,1)*Sa*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Sa*sw**2*vev)/(2.*cw**2)',
                 order = {'NP':1,'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-0.5*Mchi/xev',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(Ca*complex(0,1)*Mchi)/xev',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(complex(0,1)*Mchi*Sa)/(2.*xev)',
                 order = {'NP':1,'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '2*Ca*complex(0,1)*gsd**2*gZp**2*xev',
                 order = {'NP':2,'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-6*Ca**3*complex(0,1)*lam2*xev',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(Ca**3*complex(0,1)*lam3*xev)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-2*complex(0,1)*gsd**2*gZp**2*Sa*xev',
                 order = {'NP':3,'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '3*Ca**2*complex(0,1)*lam3*Sa*xev',
                 order = {'NP':1,'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-3*Ca*complex(0,1)*lam3*Sa**2*xev',
                 order = {'NP':2,'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '6*complex(0,1)*lam2*Sa**3*xev',
                 order = {'NP':3,'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'complex(0,1)*lam3*Sa**3*xev',
                 order = {'NP':3,'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '6*Ca**2*complex(0,1)*lam2*Sa*xev - 2*Ca**2*complex(0,1)*lam3*Sa*xev',
                 order = {'NP':1,'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-6*Ca*complex(0,1)*lam2*Sa**2*xev + 2*Ca*complex(0,1)*lam3*Sa**2*xev',
                 order = {'NP':2,'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((Ca*complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*Sa*yc)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((Ca*complex(0,1)*yd1x1)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((complex(0,1)*Sa*yd1x1)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((Ca*complex(0,1)*yd2x2)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((complex(0,1)*Sa*yd2x2)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((Ca*complex(0,1)*yd3x3)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((complex(0,1)*Sa*yd3x3)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((Ca*complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((complex(0,1)*Sa*ye)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((Ca*complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*Sa*ym)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((Ca*complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((complex(0,1)*Sa*yup)/cmath.sqrt(2))',
                 order = {'NP':1,'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

