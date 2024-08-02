# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Fri 2 Aug 2024 17:01:18


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_244_65,(0,0,1):C.R2GC_246_68,(0,1,0):C.R2GC_252_69,(0,1,1):C.R2GC_252_70,(0,3,0):C.R2GC_252_69,(0,3,1):C.R2GC_254_72,(0,5,0):C.R2GC_244_65,(0,5,1):C.R2GC_245_67,(0,6,0):C.R2GC_244_65,(0,6,1):C.R2GC_244_66,(0,7,0):C.R2GC_252_69,(0,7,1):C.R2GC_253_71,(0,2,1):C.R2GC_201_40,(0,4,1):C.R2GC_200_39})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_204_45,(2,0,1):C.R2GC_204_46,(0,0,0):C.R2GC_204_45,(0,0,1):C.R2GC_204_46,(6,0,0):C.R2GC_207_50,(6,0,1):C.R2GC_259_78,(4,0,0):C.R2GC_202_41,(4,0,1):C.R2GC_202_42,(3,0,0):C.R2GC_202_41,(3,0,1):C.R2GC_202_42,(8,0,0):C.R2GC_203_43,(8,0,1):C.R2GC_203_44,(7,0,0):C.R2GC_208_51,(7,0,1):C.R2GC_258_77,(5,0,0):C.R2GC_202_41,(5,0,1):C.R2GC_202_42,(1,0,0):C.R2GC_202_41,(1,0,1):C.R2GC_202_42,(11,0,0):C.R2GC_206_48,(11,0,1):C.R2GC_206_49,(10,0,0):C.R2GC_206_48,(10,0,1):C.R2GC_206_49,(9,0,1):C.R2GC_205_47,(2,1,0):C.R2GC_204_45,(2,1,1):C.R2GC_204_46,(0,1,0):C.R2GC_204_45,(0,1,1):C.R2GC_204_46,(4,1,0):C.R2GC_202_41,(4,1,1):C.R2GC_202_42,(3,1,0):C.R2GC_202_41,(3,1,1):C.R2GC_202_42,(8,1,0):C.R2GC_203_43,(8,1,1):C.R2GC_258_77,(6,1,0):C.R2GC_255_73,(6,1,1):C.R2GC_255_74,(7,1,0):C.R2GC_208_51,(7,1,1):C.R2GC_203_44,(5,1,0):C.R2GC_202_41,(5,1,1):C.R2GC_202_42,(1,1,0):C.R2GC_202_41,(1,1,1):C.R2GC_202_42,(11,1,0):C.R2GC_206_48,(11,1,1):C.R2GC_206_49,(10,1,0):C.R2GC_206_48,(10,1,1):C.R2GC_206_49,(9,1,1):C.R2GC_205_47,(2,2,0):C.R2GC_204_45,(2,2,1):C.R2GC_204_46,(0,2,0):C.R2GC_204_45,(0,2,1):C.R2GC_204_46,(4,2,0):C.R2GC_202_41,(4,2,1):C.R2GC_202_42,(3,2,0):C.R2GC_202_41,(3,2,1):C.R2GC_202_42,(8,2,0):C.R2GC_203_43,(8,2,1):C.R2GC_256_76,(6,2,0):C.R2GC_207_50,(7,2,0):C.R2GC_256_75,(7,2,1):C.R2GC_256_76,(5,2,0):C.R2GC_202_41,(5,2,1):C.R2GC_202_42,(1,2,0):C.R2GC_202_41,(1,2,1):C.R2GC_202_42,(11,2,0):C.R2GC_206_48,(11,2,1):C.R2GC_206_49,(10,2,0):C.R2GC_206_48,(10,2,1):C.R2GC_206_49,(9,2,1):C.R2GC_205_47})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_270_81,(0,1,0):C.R2GC_271_82})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_239_59})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_240_60})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Sd ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_241_61})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_272_83,(0,1,0):C.R2GC_269_80})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_274_85})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_275_86})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_213_56})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_213_56})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_213_56})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_209_52})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_209_52})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_209_52})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_210_53})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_231_57})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_181_35,(0,1,0):C.R2GC_160_1})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_181_35,(0,1,0):C.R2GC_160_1})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_181_35,(0,1,0):C.R2GC_160_1})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_182_36,(0,1,0):C.R2GC_161_2})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_182_36,(0,1,0):C.R2GC_161_2})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_182_36,(0,1,0):C.R2GC_161_2})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_211_54})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_212_55})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_55})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_264_79,(0,2,0):C.R2GC_264_79,(0,1,0):C.R2GC_212_55,(0,3,0):C.R2GC_212_55})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_212_55})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_212_55})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_235_58,(0,2,0):C.R2GC_235_58,(0,1,0):C.R2GC_212_55,(0,3,0):C.R2GC_212_55})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_243_64,(0,1,0):C.R2GC_164_3,(0,1,3):C.R2GC_164_4,(0,2,1):C.R2GC_242_62,(0,2,2):C.R2GC_242_63})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_165_5,(0,0,1):C.R2GC_165_6})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_166_7,(0,0,1):C.R2GC_166_8})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.Zp, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_175_24,(0,1,0):C.R2GC_175_24,(0,2,0):C.R2GC_175_24})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_179_31,(0,0,1):C.R2GC_179_32,(0,1,0):C.R2GC_179_31,(0,1,1):C.R2GC_179_32,(0,2,0):C.R2GC_179_31,(0,2,1):C.R2GC_179_32})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Zp ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_173_21,(0,0,1):C.R2GC_173_22,(0,1,0):C.R2GC_173_21,(0,1,1):C.R2GC_173_22,(0,2,0):C.R2GC_173_21,(0,2,1):C.R2GC_173_22})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Zp ],
                color = [ 'd(1,2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_174_23,(0,1,0):C.R2GC_174_23,(0,2,0):C.R2GC_174_23})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_185_38,(0,1,0):C.R2GC_185_38,(0,2,0):C.R2GC_185_38})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_176_25,(0,0,1):C.R2GC_176_26,(0,1,0):C.R2GC_176_25,(0,1,1):C.R2GC_176_26,(0,2,0):C.R2GC_176_25,(0,2,1):C.R2GC_176_26})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_180_33,(0,0,1):C.R2GC_180_34,(0,1,0):C.R2GC_180_33,(0,1,1):C.R2GC_180_34,(0,2,0):C.R2GC_180_33,(0,2,1):C.R2GC_180_34})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_171_17,(0,0,1):C.R2GC_171_18,(0,1,0):C.R2GC_171_17,(0,1,1):C.R2GC_171_18,(0,2,0):C.R2GC_171_17,(0,2,1):C.R2GC_171_18})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_178_29,(1,0,1):C.R2GC_178_30,(0,1,0):C.R2GC_177_27,(0,1,1):C.R2GC_177_28,(0,2,0):C.R2GC_177_27,(0,2,1):C.R2GC_177_28,(0,3,0):C.R2GC_177_27,(0,3,1):C.R2GC_177_28})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_172_19,(0,0,1):C.R2GC_172_20,(0,1,0):C.R2GC_172_19,(0,1,1):C.R2GC_172_20,(0,2,0):C.R2GC_172_19,(0,2,1):C.R2GC_172_20})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_168_11,(0,0,1):C.R2GC_168_12})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_167_9,(0,0,1):C.R2GC_167_10})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_184_37})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_169_13,(0,0,1):C.R2GC_169_14})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_15,(0,0,1):C.R2GC_170_16})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_244_42,(0,0,1):C.UVGC_244_43,(0,0,2):C.UVGC_246_48,(0,0,3):C.UVGC_246_49,(0,0,4):C.UVGC_244_45,(0,1,0):C.UVGC_252_57,(0,1,1):C.UVGC_252_58,(0,1,2):C.UVGC_252_59,(0,1,4):C.UVGC_252_60,(0,3,0):C.UVGC_252_57,(0,3,1):C.UVGC_252_58,(0,3,2):C.UVGC_254_63,(0,3,3):C.UVGC_254_64,(0,3,4):C.UVGC_252_60,(0,5,0):C.UVGC_244_42,(0,5,1):C.UVGC_244_43,(0,5,2):C.UVGC_245_46,(0,5,3):C.UVGC_245_47,(0,5,4):C.UVGC_244_45,(0,7,0):C.UVGC_244_42,(0,7,1):C.UVGC_244_43,(0,7,2):C.UVGC_244_44,(0,7,3):C.UVGC_201_9,(0,7,4):C.UVGC_244_45,(0,8,0):C.UVGC_252_57,(0,8,1):C.UVGC_252_58,(0,8,2):C.UVGC_253_61,(0,8,3):C.UVGC_253_62,(0,8,4):C.UVGC_252_60,(0,2,2):C.UVGC_201_8,(0,2,3):C.UVGC_201_9,(0,4,2):C.UVGC_200_6,(0,4,3):C.UVGC_200_7,(0,6,2):C.UVGC_187_1})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_203_13,(2,0,4):C.UVGC_203_12,(0,0,3):C.UVGC_203_13,(0,0,4):C.UVGC_203_12,(6,0,0):C.UVGC_258_75,(6,0,2):C.UVGC_258_76,(6,0,3):C.UVGC_259_80,(6,0,4):C.UVGC_259_81,(6,0,5):C.UVGC_258_79,(4,0,3):C.UVGC_202_10,(4,0,4):C.UVGC_202_11,(3,0,3):C.UVGC_202_10,(3,0,4):C.UVGC_202_11,(8,0,3):C.UVGC_203_12,(8,0,4):C.UVGC_203_13,(7,0,0):C.UVGC_258_75,(7,0,2):C.UVGC_258_76,(7,0,3):C.UVGC_258_77,(7,0,4):C.UVGC_258_78,(7,0,5):C.UVGC_258_79,(5,0,3):C.UVGC_202_10,(5,0,4):C.UVGC_202_11,(1,0,3):C.UVGC_202_10,(1,0,4):C.UVGC_202_11,(11,0,3):C.UVGC_206_16,(11,0,4):C.UVGC_206_17,(10,0,3):C.UVGC_206_16,(10,0,4):C.UVGC_206_17,(9,0,3):C.UVGC_205_14,(9,0,4):C.UVGC_205_15,(2,1,3):C.UVGC_203_13,(2,1,4):C.UVGC_203_12,(0,1,3):C.UVGC_203_13,(0,1,4):C.UVGC_203_12,(4,1,3):C.UVGC_202_10,(4,1,4):C.UVGC_202_11,(3,1,3):C.UVGC_202_10,(3,1,4):C.UVGC_202_11,(8,1,0):C.UVGC_260_82,(8,1,2):C.UVGC_260_83,(8,1,3):C.UVGC_258_77,(8,1,4):C.UVGC_260_84,(8,1,5):C.UVGC_260_85,(6,1,0):C.UVGC_255_65,(6,1,3):C.UVGC_255_66,(6,1,4):C.UVGC_255_67,(6,1,5):C.UVGC_255_68,(7,1,1):C.UVGC_207_18,(7,1,3):C.UVGC_203_12,(7,1,4):C.UVGC_208_19,(5,1,3):C.UVGC_202_10,(5,1,4):C.UVGC_202_11,(1,1,3):C.UVGC_202_10,(1,1,4):C.UVGC_202_11,(11,1,3):C.UVGC_206_16,(11,1,4):C.UVGC_206_17,(10,1,3):C.UVGC_206_16,(10,1,4):C.UVGC_206_17,(9,1,3):C.UVGC_205_14,(9,1,4):C.UVGC_205_15,(2,2,3):C.UVGC_203_13,(2,2,4):C.UVGC_203_12,(0,2,3):C.UVGC_203_13,(0,2,4):C.UVGC_203_12,(4,2,3):C.UVGC_202_10,(4,2,4):C.UVGC_202_11,(3,2,3):C.UVGC_202_10,(3,2,4):C.UVGC_202_11,(8,2,0):C.UVGC_257_71,(8,2,2):C.UVGC_257_72,(8,2,3):C.UVGC_256_69,(8,2,4):C.UVGC_257_73,(8,2,5):C.UVGC_257_74,(6,2,1):C.UVGC_207_18,(6,2,4):C.UVGC_205_14,(7,2,0):C.UVGC_255_65,(7,2,3):C.UVGC_256_69,(7,2,4):C.UVGC_256_70,(7,2,5):C.UVGC_255_68,(5,2,3):C.UVGC_202_10,(5,2,4):C.UVGC_202_11,(1,2,3):C.UVGC_202_10,(1,2,4):C.UVGC_202_11,(11,2,3):C.UVGC_206_16,(11,2,4):C.UVGC_206_17,(10,2,3):C.UVGC_206_16,(10,2,4):C.UVGC_206_17,(9,2,3):C.UVGC_205_14,(9,2,4):C.UVGC_205_15})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_270_98,(0,0,2):C.UVGC_270_99,(0,0,1):C.UVGC_270_100,(0,1,0):C.UVGC_271_101,(0,1,2):C.UVGC_271_102,(0,1,1):C.UVGC_271_103})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_239_33})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_240_34})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_241_35})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_272_104,(0,0,2):C.UVGC_272_105,(0,0,1):C.UVGC_272_106,(0,1,0):C.UVGC_269_95,(0,1,2):C.UVGC_269_96,(0,1,1):C.UVGC_269_97})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_273_107})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_274_108})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_275_109})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_213_24,(0,1,0):C.UVGC_189_3,(0,2,0):C.UVGC_189_3})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_213_24,(0,1,0):C.UVGC_189_3,(0,2,0):C.UVGC_189_3})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_213_24,(0,1,0):C.UVGC_262_87,(0,2,0):C.UVGC_262_87})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_209_20,(0,1,0):C.UVGC_192_5,(0,2,0):C.UVGC_192_5})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_209_20,(0,1,0):C.UVGC_192_5,(0,2,0):C.UVGC_192_5})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_209_20,(0,1,0):C.UVGC_234_28,(0,2,0):C.UVGC_234_28})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,1):C.UVGC_247_51,(0,1,2):C.UVGC_247_52,(0,1,3):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,4):C.UVGC_247_55,(0,2,0):C.UVGC_247_50,(0,2,1):C.UVGC_247_51,(0,2,2):C.UVGC_247_52,(0,2,3):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,4):C.UVGC_247_55})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,1):C.UVGC_247_51,(0,1,3):C.UVGC_247_52,(0,1,4):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,2):C.UVGC_247_55,(0,2,0):C.UVGC_247_50,(0,2,1):C.UVGC_247_51,(0,2,3):C.UVGC_247_52,(0,2,4):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,2):C.UVGC_247_55})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,1):C.UVGC_247_51,(0,1,2):C.UVGC_247_52,(0,1,3):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,4):C.UVGC_263_88,(0,2,0):C.UVGC_247_50,(0,2,1):C.UVGC_247_51,(0,2,2):C.UVGC_247_52,(0,2,3):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,4):C.UVGC_263_88})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,1):C.UVGC_247_51,(0,1,3):C.UVGC_247_52,(0,1,4):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,2):C.UVGC_247_55,(0,2,0):C.UVGC_247_50,(0,2,1):C.UVGC_247_51,(0,2,3):C.UVGC_247_52,(0,2,4):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,2):C.UVGC_247_55})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,1):C.UVGC_247_51,(0,1,2):C.UVGC_247_52,(0,1,3):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,4):C.UVGC_247_55,(0,2,0):C.UVGC_247_50,(0,2,1):C.UVGC_247_51,(0,2,2):C.UVGC_247_52,(0,2,3):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,4):C.UVGC_247_55})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_210_21,(0,1,0):C.UVGC_247_50,(0,1,2):C.UVGC_247_51,(0,1,3):C.UVGC_247_52,(0,1,4):C.UVGC_247_53,(0,1,5):C.UVGC_247_54,(0,1,1):C.UVGC_251_56,(0,2,0):C.UVGC_247_50,(0,2,2):C.UVGC_247_51,(0,2,3):C.UVGC_247_52,(0,2,4):C.UVGC_247_53,(0,2,5):C.UVGC_247_54,(0,2,1):C.UVGC_251_56})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_231_25,(0,0,1):C.UVGC_231_26})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_231_25,(0,0,1):C.UVGC_231_26})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_266_91,(0,0,2):C.UVGC_266_92,(0,0,1):C.UVGC_231_26})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_231_25,(0,0,1):C.UVGC_231_26})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_231_25,(0,0,1):C.UVGC_231_26})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_266_91,(0,0,2):C.UVGC_266_92,(0,0,1):C.UVGC_231_26})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_267_93,(0,1,0):C.UVGC_268_94})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_237_31,(0,1,0):C.UVGC_238_32})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_190_4,(0,2,0):C.UVGC_190_4})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_190_4,(0,2,0):C.UVGC_190_4})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_265_90,(0,2,0):C.UVGC_265_90})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_190_4,(0,2,0):C.UVGC_190_4})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_190_4,(0,2,0):C.UVGC_190_4})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_211_22,(0,1,0):C.UVGC_236_30,(0,2,0):C.UVGC_236_30})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_212_23,(0,1,0):C.UVGC_188_2,(0,2,0):C.UVGC_188_2})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_212_23,(0,1,0):C.UVGC_188_2,(0,2,0):C.UVGC_188_2})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_264_89,(0,2,0):C.UVGC_264_89,(0,1,0):C.UVGC_261_86,(0,3,0):C.UVGC_261_86})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_212_23,(0,1,0):C.UVGC_188_2,(0,2,0):C.UVGC_188_2})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_212_23,(0,1,0):C.UVGC_188_2,(0,2,0):C.UVGC_188_2})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_235_29,(0,2,0):C.UVGC_235_29,(0,1,0):C.UVGC_233_27,(0,3,0):C.UVGC_233_27})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_243_38,(0,0,1):C.UVGC_243_39,(0,0,2):C.UVGC_243_40,(0,0,3):C.UVGC_243_41,(0,1,0):C.UVGC_242_36,(0,1,3):C.UVGC_242_37})

