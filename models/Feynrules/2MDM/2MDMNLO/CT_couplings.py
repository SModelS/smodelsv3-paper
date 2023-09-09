# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Sat 9 Sep 2023 05:02:22


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_130_1 = Coupling(name = 'R2GC_130_1',
                      value = '-0.125*(complex(0,1)*G**2*MT**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_131_2 = Coupling(name = 'R2GC_131_2',
                      value = '-0.125*(Ca*complex(0,1)*G**2*MT*yt)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'QCD':2,'QED':1})

R2GC_132_3 = Coupling(name = 'R2GC_132_3',
                      value = '-0.125*(complex(0,1)*G**2*MT*Sa*yt)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'QCD':2,'QED':1})

R2GC_133_4 = Coupling(name = 'R2GC_133_4',
                      value = '-0.0625*(complex(0,1)*G**2*yt**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':2})

R2GC_134_5 = Coupling(name = 'R2GC_134_5',
                      value = '-0.0625*(Ca**2*complex(0,1)*G**2*yt**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':2})

R2GC_135_6 = Coupling(name = 'R2GC_135_6',
                      value = '-0.0625*(Ca*complex(0,1)*G**2*Sa*yt**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':2})

R2GC_136_7 = Coupling(name = 'R2GC_136_7',
                      value = '-0.0625*(complex(0,1)*G**2*Sa**2*yt**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':2})

R2GC_137_8 = Coupling(name = 'R2GC_137_8',
                      value = '-0.16666666666666666*(complex(0,1)*G**2*gqL*gZp)/cmath.pi**2',
                      order = {'NP':1,'QCD':2,'QED':1})

R2GC_138_9 = Coupling(name = 'R2GC_138_9',
                      value = '-0.16666666666666666*(complex(0,1)*G**2*gqR*gZp)/cmath.pi**2',
                      order = {'NP':1,'QCD':2,'QED':1})

R2GC_139_10 = Coupling(name = 'R2GC_139_10',
                       value = '-0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_142_11 = Coupling(name = 'R2GC_142_11',
                       value = '(ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_153_12 = Coupling(name = 'R2GC_153_12',
                       value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_153_13 = Coupling(name = 'R2GC_153_13',
                       value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_154_14 = Coupling(name = 'R2GC_154_14',
                       value = '-0.006944444444444444*(ee*complex(0,1)*G**3)/cmath.pi**2',
                       order = {'QCD':3,'QED':1})

R2GC_154_15 = Coupling(name = 'R2GC_154_15',
                       value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_155_16 = Coupling(name = 'R2GC_155_16',
                       value = '-0.006944444444444444*(ee*complex(0,1)*G**2*gqL*gZp)/cmath.pi**2 - (ee*complex(0,1)*G**2*gqR*gZp)/(144.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':2})

R2GC_155_17 = Coupling(name = 'R2GC_155_17',
                       value = '(ee*complex(0,1)*G**2*gqL*gZp)/(72.*cmath.pi**2) + (ee*complex(0,1)*G**2*gqR*gZp)/(72.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':2})

R2GC_156_18 = Coupling(name = 'R2GC_156_18',
                       value = '(complex(0,1)*G**3*gqL*gZp)/(96.*cmath.pi**2) + (complex(0,1)*G**3*gqR*gZp)/(96.*cmath.pi**2)',
                       order = {'NP':1,'QCD':3,'QED':1})

R2GC_157_19 = Coupling(name = 'R2GC_157_19',
                       value = '-0.03125*(complex(0,1)*G**3*gqL*gZp)/cmath.pi**2 + (complex(0,1)*G**3*gqR*gZp)/(32.*cmath.pi**2)',
                       order = {'NP':1,'QCD':3,'QED':1})

R2GC_158_20 = Coupling(name = 'R2GC_158_20',
                       value = '(complex(0,1)*G**2*gqL**2*gZp**2)/(48.*cmath.pi**2) + (complex(0,1)*G**2*gqR**2*gZp**2)/(48.*cmath.pi**2)',
                       order = {'NP':2,'QCD':2,'QED':2})

R2GC_159_21 = Coupling(name = 'R2GC_159_21',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_159_22 = Coupling(name = 'R2GC_159_22',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_160_23 = Coupling(name = 'R2GC_160_23',
                       value = '-0.005208333333333333*(cw*ee*complex(0,1)*G**3)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_160_24 = Coupling(name = 'R2GC_160_24',
                       value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_161_25 = Coupling(name = 'R2GC_161_25',
                       value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_161_26 = Coupling(name = 'R2GC_161_26',
                       value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_162_27 = Coupling(name = 'R2GC_162_27',
                       value = '-0.010416666666666666*(cw*ee*complex(0,1)*G**2*gqL*gZp)/(cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gqL*gZp*sw)/(288.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gqR*gZp*sw)/(144.*cw*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':2})

R2GC_162_28 = Coupling(name = 'R2GC_162_28',
                       value = '(cw*ee*complex(0,1)*G**2*gqL*gZp)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gqL*gZp*sw)/(288.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*gqR*gZp*sw)/(72.*cw*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':2})

R2GC_163_29 = Coupling(name = 'R2GC_163_29',
                       value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_163_30 = Coupling(name = 'R2GC_163_30',
                       value = '-0.003472222222222222*(ee**2*complex(0,1)*G**2)/cmath.pi**2 + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_164_31 = Coupling(name = 'R2GC_164_31',
                       value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_165_32 = Coupling(name = 'R2GC_165_32',
                       value = '-0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_168_33 = Coupling(name = 'R2GC_168_33',
                       value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_181_34 = Coupling(name = 'R2GC_181_34',
                       value = '-0.015625*G**3/cmath.pi**2',
                       order = {'QCD':3})

R2GC_182_35 = Coupling(name = 'R2GC_182_35',
                       value = 'G**3/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_183_36 = Coupling(name = 'R2GC_183_36',
                       value = '-0.005208333333333333*G**4/cmath.pi**2',
                       order = {'QCD':4})

R2GC_183_37 = Coupling(name = 'R2GC_183_37',
                       value = 'G**4/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_184_38 = Coupling(name = 'R2GC_184_38',
                       value = '-0.005208333333333333*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_184_39 = Coupling(name = 'R2GC_184_39',
                       value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_185_40 = Coupling(name = 'R2GC_185_40',
                       value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_185_41 = Coupling(name = 'R2GC_185_41',
                       value = '-0.015625*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_186_42 = Coupling(name = 'R2GC_186_42',
                       value = '-0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_187_43 = Coupling(name = 'R2GC_187_43',
                       value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_187_44 = Coupling(name = 'R2GC_187_44',
                       value = '-0.03125*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_188_45 = Coupling(name = 'R2GC_188_45',
                       value = '-0.0625*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_189_46 = Coupling(name = 'R2GC_189_46',
                       value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_190_47 = Coupling(name = 'R2GC_190_47',
                       value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_191_48 = Coupling(name = 'R2GC_191_48',
                       value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_193_49 = Coupling(name = 'R2GC_193_49',
                       value = '-0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2',
                       order = {'QCD':3})

R2GC_195_50 = Coupling(name = 'R2GC_195_50',
                       value = '-0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':1})

R2GC_212_51 = Coupling(name = 'R2GC_212_51',
                       value = '-0.16666666666666666*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_214_52 = Coupling(name = 'R2GC_214_52',
                       value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_214_53 = Coupling(name = 'R2GC_214_53',
                       value = '(3*complex(0,1)*G**2)/(32.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_215_54 = Coupling(name = 'R2GC_215_54',
                       value = '-0.0625*(complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_216_55 = Coupling(name = 'R2GC_216_55',
                       value = 'G**3/(24.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_216_56 = Coupling(name = 'R2GC_216_56',
                       value = '(11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_217_57 = Coupling(name = 'R2GC_217_57',
                       value = '(5*G**3)/(32.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_218_58 = Coupling(name = 'R2GC_218_58',
                       value = '(3*G**3)/(16.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_219_59 = Coupling(name = 'R2GC_219_59',
                       value = '-0.041666666666666664*G**3/cmath.pi**2',
                       order = {'QCD':3})

R2GC_219_60 = Coupling(name = 'R2GC_219_60',
                       value = '(-5*G**3)/(32.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_220_61 = Coupling(name = 'R2GC_220_61',
                       value = '(-11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_221_62 = Coupling(name = 'R2GC_221_62',
                       value = '(-3*G**3)/(16.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_222_63 = Coupling(name = 'R2GC_222_63',
                       value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_222_64 = Coupling(name = 'R2GC_222_64',
                       value = '(7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_223_65 = Coupling(name = 'R2GC_223_65',
                       value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_223_66 = Coupling(name = 'R2GC_223_66',
                       value = '(15*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_225_67 = Coupling(name = 'R2GC_225_67',
                       value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_226_68 = Coupling(name = 'R2GC_226_68',
                       value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_233_69 = Coupling(name = 'R2GC_233_69',
                       value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_237_70 = Coupling(name = 'R2GC_237_70',
                       value = '(G**2*yt)/(3.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_238_71 = Coupling(name = 'R2GC_238_71',
                       value = '-0.3333333333333333*(G**2*yt)/cmath.pi**2',
                       order = {'QCD':2,'QED':1})

R2GC_239_72 = Coupling(name = 'R2GC_239_72',
                       value = '(G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_240_73 = Coupling(name = 'R2GC_240_73',
                       value = '(Ca*complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_241_74 = Coupling(name = 'R2GC_241_74',
                       value = '(complex(0,1)*G**2*Sa*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

UVGC_170_1 = Coupling(name = 'UVGC_170_1',
                      value = {-1:'(-3*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_171_2 = Coupling(name = 'UVGC_171_2',
                      value = {-1:'-0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2})

UVGC_172_3 = Coupling(name = 'UVGC_172_3',
                      value = {-1:'-0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_174_4 = Coupling(name = 'UVGC_174_4',
                      value = {-1:'(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_181_5 = Coupling(name = 'UVGC_181_5',
                      value = {-1:'(-11*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_181_6 = Coupling(name = 'UVGC_181_6',
                      value = {-1:'G**3/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_182_7 = Coupling(name = 'UVGC_182_7',
                      value = {-1:'(11*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_182_8 = Coupling(name = 'UVGC_182_8',
                      value = {-1:'G**3/(64.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_183_9 = Coupling(name = 'UVGC_183_9',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_183_10 = Coupling(name = 'UVGC_183_10',
                       value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_184_11 = Coupling(name = 'UVGC_184_11',
                       value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_184_12 = Coupling(name = 'UVGC_184_12',
                       value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_186_13 = Coupling(name = 'UVGC_186_13',
                       value = {-1:'-0.0078125*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_186_14 = Coupling(name = 'UVGC_186_14',
                       value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_187_15 = Coupling(name = 'UVGC_187_15',
                       value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_187_16 = Coupling(name = 'UVGC_187_16',
                       value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_188_17 = Coupling(name = 'UVGC_188_17',
                       value = {-1:'-0.041666666666666664*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_189_18 = Coupling(name = 'UVGC_189_18',
                       value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_190_19 = Coupling(name = 'UVGC_190_19',
                       value = {-1:'(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_191_20 = Coupling(name = 'UVGC_191_20',
                       value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_192_21 = Coupling(name = 'UVGC_192_21',
                       value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_192_22 = Coupling(name = 'UVGC_192_22',
                       value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_192_23 = Coupling(name = 'UVGC_192_23',
                       value = {-1:'-0.0078125*(complex(0,1)*G**3)/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_192_24 = Coupling(name = 'UVGC_192_24',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_192_25 = Coupling(name = 'UVGC_192_25',
                       value = {-1:'(complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_193_26 = Coupling(name = 'UVGC_193_26',
                       value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_195_27 = Coupling(name = 'UVGC_195_27',
                       value = {-1:'-0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                       order = {'QCD':2,'QED':1})

UVGC_212_28 = Coupling(name = 'UVGC_212_28',
                       value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_212_29 = Coupling(name = 'UVGC_212_29',
                       value = {-1:'-0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_214_30 = Coupling(name = 'UVGC_214_30',
                       value = {-1:'( 0 if MT else -0.041666666666666664*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**2*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':2})

UVGC_215_31 = Coupling(name = 'UVGC_215_31',
                       value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_215_32 = Coupling(name = 'UVGC_215_32',
                       value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_215_33 = Coupling(name = 'UVGC_215_33',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':2})

UVGC_216_34 = Coupling(name = 'UVGC_216_34',
                       value = {-1:'-0.020833333333333332*G**3/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_216_35 = Coupling(name = 'UVGC_216_35',
                       value = {-1:'(39*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_216_36 = Coupling(name = 'UVGC_216_36',
                       value = {-1:'( 0 if MT else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':3})

UVGC_217_37 = Coupling(name = 'UVGC_217_37',
                       value = {-1:'(31*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_217_38 = Coupling(name = 'UVGC_217_38',
                       value = {-1:'(3*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_218_39 = Coupling(name = 'UVGC_218_39',
                       value = {-1:'(53*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_218_40 = Coupling(name = 'UVGC_218_40',
                       value = {-1:'G**3/(32.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_219_41 = Coupling(name = 'UVGC_219_41',
                       value = {-1:'G**3/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_219_42 = Coupling(name = 'UVGC_219_42',
                       value = {-1:'(-31*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_219_43 = Coupling(name = 'UVGC_219_43',
                       value = {-1:'( 0 if MT else G**3/(16.*cmath.pi**2) ) - G**3/(24.*cmath.pi**2)',0:'( (G**3*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':3})

UVGC_220_44 = Coupling(name = 'UVGC_220_44',
                       value = {-1:'(-45*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_220_45 = Coupling(name = 'UVGC_220_45',
                       value = {-1:'-0.015625*G**3/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_221_46 = Coupling(name = 'UVGC_221_46',
                       value = {-1:'(-53*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_221_47 = Coupling(name = 'UVGC_221_47',
                       value = {-1:'-0.0078125*G**3/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_222_48 = Coupling(name = 'UVGC_222_48',
                       value = {-1:'(83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_222_49 = Coupling(name = 'UVGC_222_49',
                       value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_222_50 = Coupling(name = 'UVGC_222_50',
                       value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':4})

UVGC_223_51 = Coupling(name = 'UVGC_223_51',
                       value = {-1:'(335*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_223_52 = Coupling(name = 'UVGC_223_52',
                       value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_224_53 = Coupling(name = 'UVGC_224_53',
                       value = {-1:'-0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_224_54 = Coupling(name = 'UVGC_224_54',
                       value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_224_55 = Coupling(name = 'UVGC_224_55',
                       value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':4})

UVGC_225_56 = Coupling(name = 'UVGC_225_56',
                       value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_225_57 = Coupling(name = 'UVGC_225_57',
                       value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_225_58 = Coupling(name = 'UVGC_225_58',
                       value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_225_59 = Coupling(name = 'UVGC_225_59',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_226_60 = Coupling(name = 'UVGC_226_60',
                       value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_226_61 = Coupling(name = 'UVGC_226_61',
                       value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_227_62 = Coupling(name = 'UVGC_227_62',
                       value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_227_63 = Coupling(name = 'UVGC_227_63',
                       value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_227_64 = Coupling(name = 'UVGC_227_64',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_228_65 = Coupling(name = 'UVGC_228_65',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_229_66 = Coupling(name = 'UVGC_229_66',
                       value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MT else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(3.*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_230_67 = Coupling(name = 'UVGC_230_67',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MT else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_231_68 = Coupling(name = 'UVGC_231_68',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*gqL*gZp)/cmath.pi**2 if MT else (complex(0,1)*G**2*gqL*gZp)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gqL*gZp)/(12.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*gqL*gZp)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gqL*gZp*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*gqL*gZp)/cmath.pi**2 ) + (complex(0,1)*G**2*gqL*gZp)/(12.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2,'QED':1})

UVGC_232_69 = Coupling(name = 'UVGC_232_69',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*gqR*gZp)/cmath.pi**2 if MT else (complex(0,1)*G**2*gqR*gZp)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gqR*gZp)/(12.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*gqR*gZp)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gqR*gZp*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*gqR*gZp)/cmath.pi**2 ) + (complex(0,1)*G**2*gqR*gZp)/(12.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2,'QED':1})

UVGC_233_70 = Coupling(name = 'UVGC_233_70',
                       value = {-1:'( (complex(0,1)*G**2*MT)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*MT)/cmath.pi**2 ) + (complex(0,1)*G**2*MT)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MT)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT/MU_R))/cmath.pi**2 if MT else (complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MT)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_234_71 = Coupling(name = 'UVGC_234_71',
                       value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MT else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_235_72 = Coupling(name = 'UVGC_235_72',
                       value = {-1:'( -0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MT else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (-5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) + (cw*ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(12.*cw*cmath.pi**2) if MT else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_236_73 = Coupling(name = 'UVGC_236_73',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(3.*cw*cmath.pi**2) if MT else (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_237_74 = Coupling(name = 'UVGC_237_74',
                       value = {-1:'-0.041666666666666664*(G**2*yt)/cmath.pi**2'},
                       order = {'QCD':2,'QED':1})

UVGC_237_75 = Coupling(name = 'UVGC_237_75',
                       value = {-1:'( (G**2*yt)/(12.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yt)/cmath.pi**2 )',0:'( (13*G**2*yt)/(24.*cmath.pi**2) - (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_237_76 = Coupling(name = 'UVGC_237_76',
                       value = {-1:'(G**2*yt)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_238_77 = Coupling(name = 'UVGC_238_77',
                       value = {-1:'(G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_238_78 = Coupling(name = 'UVGC_238_78',
                       value = {-1:'( -0.08333333333333333*(G**2*yt)/cmath.pi**2 if MT else (G**2*yt)/(24.*cmath.pi**2) )',0:'( (-13*G**2*yt)/(24.*cmath.pi**2) + (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yt)/cmath.pi**2 ) + (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_238_79 = Coupling(name = 'UVGC_238_79',
                       value = {-1:'-0.3333333333333333*(G**2*yt)/cmath.pi**2'},
                       order = {'QCD':2,'QED':1})

UVGC_239_80 = Coupling(name = 'UVGC_239_80',
                       value = {-1:'( (G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(G**2*yt)/(cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_240_81 = Coupling(name = 'UVGC_240_81',
                       value = {-1:'( (Ca*complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(Ca*complex(0,1)*G**2*yt)/(cmath.pi**2*cmath.sqrt(2)) ) + (Ca*complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*Ca*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (Ca*complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (Ca*complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (Ca*complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_241_82 = Coupling(name = 'UVGC_241_82',
                       value = {-1:'( (complex(0,1)*G**2*Sa*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*Sa*yt)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*Sa*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*Sa*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*Sa*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*Sa*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*Sa*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

