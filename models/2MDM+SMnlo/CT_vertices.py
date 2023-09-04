# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Fri 25 Aug 2023 00:07:37


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
               couplings = {(0,0,0):C.R2GC_229_76,(0,0,1):C.R2GC_231_79,(0,1,0):C.R2GC_232_80,(0,1,1):C.R2GC_232_81,(0,3,0):C.R2GC_232_80,(0,3,1):C.R2GC_234_83,(0,5,0):C.R2GC_229_76,(0,5,1):C.R2GC_230_78,(0,6,0):C.R2GC_229_76,(0,6,1):C.R2GC_229_77,(0,7,0):C.R2GC_232_80,(0,7,1):C.R2GC_233_82,(0,2,1):C.R2GC_175_44,(0,4,1):C.R2GC_174_43})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_178_49,(2,0,1):C.R2GC_178_50,(0,0,0):C.R2GC_178_49,(0,0,1):C.R2GC_178_50,(6,0,0):C.R2GC_181_54,(6,0,1):C.R2GC_239_89,(4,0,0):C.R2GC_176_45,(4,0,1):C.R2GC_176_46,(3,0,0):C.R2GC_176_45,(3,0,1):C.R2GC_176_46,(8,0,0):C.R2GC_177_47,(8,0,1):C.R2GC_177_48,(7,0,0):C.R2GC_182_55,(7,0,1):C.R2GC_238_88,(5,0,0):C.R2GC_176_45,(5,0,1):C.R2GC_176_46,(1,0,0):C.R2GC_176_45,(1,0,1):C.R2GC_176_46,(11,0,0):C.R2GC_180_52,(11,0,1):C.R2GC_180_53,(10,0,0):C.R2GC_180_52,(10,0,1):C.R2GC_180_53,(9,0,1):C.R2GC_179_51,(2,1,0):C.R2GC_178_49,(2,1,1):C.R2GC_178_50,(0,1,0):C.R2GC_178_49,(0,1,1):C.R2GC_178_50,(4,1,0):C.R2GC_176_45,(4,1,1):C.R2GC_176_46,(3,1,0):C.R2GC_176_45,(3,1,1):C.R2GC_176_46,(8,1,0):C.R2GC_177_47,(8,1,1):C.R2GC_238_88,(6,1,0):C.R2GC_235_84,(6,1,1):C.R2GC_235_85,(7,1,0):C.R2GC_182_55,(7,1,1):C.R2GC_177_48,(5,1,0):C.R2GC_176_45,(5,1,1):C.R2GC_176_46,(1,1,0):C.R2GC_176_45,(1,1,1):C.R2GC_176_46,(11,1,0):C.R2GC_180_52,(11,1,1):C.R2GC_180_53,(10,1,0):C.R2GC_180_52,(10,1,1):C.R2GC_180_53,(9,1,1):C.R2GC_179_51,(2,2,0):C.R2GC_178_49,(2,2,1):C.R2GC_178_50,(0,2,0):C.R2GC_178_49,(0,2,1):C.R2GC_178_50,(4,2,0):C.R2GC_176_45,(4,2,1):C.R2GC_176_46,(3,2,0):C.R2GC_176_45,(3,2,1):C.R2GC_176_46,(8,2,0):C.R2GC_177_47,(8,2,1):C.R2GC_236_87,(6,2,0):C.R2GC_181_54,(7,2,0):C.R2GC_236_86,(7,2,1):C.R2GC_236_87,(5,2,0):C.R2GC_176_45,(5,2,1):C.R2GC_176_46,(1,2,0):C.R2GC_176_45,(1,2,1):C.R2GC_176_46,(11,2,0):C.R2GC_180_52,(11,2,1):C.R2GC_180_53,(10,2,0):C.R2GC_180_52,(10,2,1):C.R2GC_180_53,(9,2,1):C.R2GC_179_51})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_250_93,(0,1,0):C.R2GC_251_94})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_224_70})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_225_71})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_226_72})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_252_95,(0,1,0):C.R2GC_249_92})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_253_96})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_254_97})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_255_98})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_187_60})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_187_60})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_187_60})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_183_56})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_183_56})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_183_56})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_184_57})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_213_65})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_211_63})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_246_91})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_214_66})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_212_64})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_246_91})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_155_35,(0,1,0):C.R2GC_134_1})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_155_35,(0,1,0):C.R2GC_134_1})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_155_35,(0,1,0):C.R2GC_134_1})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_36,(0,1,0):C.R2GC_135_2})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_156_36,(0,1,0):C.R2GC_135_2})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_36,(0,1,0):C.R2GC_135_2})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_185_58})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_186_59})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_186_59})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_245_90,(0,2,0):C.R2GC_245_90,(0,1,0):C.R2GC_186_59,(0,3,0):C.R2GC_186_59})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_186_59})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_186_59})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_221_69,(0,2,0):C.R2GC_221_69,(0,1,0):C.R2GC_186_59,(0,3,0):C.R2GC_186_59})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_228_75,(0,1,0):C.R2GC_138_3,(0,1,3):C.R2GC_138_4,(0,2,1):C.R2GC_227_73,(0,2,2):C.R2GC_227_74})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_216_68})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_210_62})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_215_67})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_209_61})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_5,(0,0,1):C.R2GC_139_6})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_140_7,(0,0,1):C.R2GC_140_8})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.Zp, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_149_24,(0,1,0):C.R2GC_149_24,(0,2,0):C.R2GC_149_24})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_153_31,(0,0,1):C.R2GC_153_32,(0,1,0):C.R2GC_153_31,(0,1,1):C.R2GC_153_32,(0,2,0):C.R2GC_153_31,(0,2,1):C.R2GC_153_32})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Zp ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_147_21,(0,0,1):C.R2GC_147_22,(0,1,0):C.R2GC_147_21,(0,1,1):C.R2GC_147_22,(0,2,0):C.R2GC_147_21,(0,2,1):C.R2GC_147_22})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Zp ],
                color = [ 'd(1,2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_148_23,(0,1,0):C.R2GC_148_23,(0,2,0):C.R2GC_148_23})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_160_38,(0,0,1):C.R2GC_160_39,(0,0,2):C.R2GC_160_40,(0,0,3):C.R2GC_160_41,(0,0,4):C.R2GC_160_42,(0,1,0):C.R2GC_160_38,(0,1,1):C.R2GC_160_39,(0,1,2):C.R2GC_160_40,(0,1,3):C.R2GC_160_41,(0,1,4):C.R2GC_160_42,(0,2,0):C.R2GC_160_38,(0,2,1):C.R2GC_160_39,(0,2,2):C.R2GC_160_40,(0,2,3):C.R2GC_160_41,(0,2,4):C.R2GC_160_42})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_150_25,(0,0,1):C.R2GC_150_26,(0,1,0):C.R2GC_150_25,(0,1,1):C.R2GC_150_26,(0,2,0):C.R2GC_150_25,(0,2,1):C.R2GC_150_26})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_154_33,(0,0,1):C.R2GC_154_34,(0,1,0):C.R2GC_154_33,(0,1,1):C.R2GC_154_34,(0,2,0):C.R2GC_154_33,(0,2,1):C.R2GC_154_34})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_17,(0,0,1):C.R2GC_145_18,(0,1,0):C.R2GC_145_17,(0,1,1):C.R2GC_145_18,(0,2,0):C.R2GC_145_17,(0,2,1):C.R2GC_145_18})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_152_29,(1,0,1):C.R2GC_152_30,(0,1,0):C.R2GC_151_27,(0,1,1):C.R2GC_151_28,(0,2,0):C.R2GC_151_27,(0,2,1):C.R2GC_151_28,(0,3,0):C.R2GC_151_27,(0,3,1):C.R2GC_151_28})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_146_19,(0,0,1):C.R2GC_146_20,(0,1,0):C.R2GC_146_19,(0,1,1):C.R2GC_146_20,(0,2,0):C.R2GC_146_19,(0,2,1):C.R2GC_146_20})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.H1, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_142_11,(0,0,1):C.R2GC_142_12})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_141_9,(0,0,1):C.R2GC_141_10})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_158_37})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.H1, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_143_13,(0,0,1):C.R2GC_143_14})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.g, P.H2, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_15,(0,0,1):C.R2GC_144_16})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_229_63,(0,0,1):C.UVGC_229_64,(0,0,2):C.UVGC_231_69,(0,0,3):C.UVGC_231_70,(0,0,4):C.UVGC_229_66,(0,1,0):C.UVGC_232_71,(0,1,1):C.UVGC_232_72,(0,1,2):C.UVGC_232_73,(0,1,4):C.UVGC_232_74,(0,3,0):C.UVGC_232_71,(0,3,1):C.UVGC_232_72,(0,3,2):C.UVGC_234_77,(0,3,3):C.UVGC_234_78,(0,3,4):C.UVGC_232_74,(0,5,0):C.UVGC_229_63,(0,5,1):C.UVGC_229_64,(0,5,2):C.UVGC_230_67,(0,5,3):C.UVGC_230_68,(0,5,4):C.UVGC_229_66,(0,7,0):C.UVGC_229_63,(0,7,1):C.UVGC_229_64,(0,7,2):C.UVGC_229_65,(0,7,3):C.UVGC_175_9,(0,7,4):C.UVGC_229_66,(0,8,0):C.UVGC_232_71,(0,8,1):C.UVGC_232_72,(0,8,2):C.UVGC_233_75,(0,8,3):C.UVGC_233_76,(0,8,4):C.UVGC_232_74,(0,2,2):C.UVGC_175_8,(0,2,3):C.UVGC_175_9,(0,4,2):C.UVGC_174_6,(0,4,3):C.UVGC_174_7,(0,6,2):C.UVGC_161_1})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_177_13,(2,0,4):C.UVGC_177_12,(0,0,3):C.UVGC_177_13,(0,0,4):C.UVGC_177_12,(6,0,0):C.UVGC_238_89,(6,0,2):C.UVGC_238_90,(6,0,3):C.UVGC_239_94,(6,0,4):C.UVGC_239_95,(6,0,5):C.UVGC_238_93,(4,0,3):C.UVGC_176_10,(4,0,4):C.UVGC_176_11,(3,0,3):C.UVGC_176_10,(3,0,4):C.UVGC_176_11,(8,0,3):C.UVGC_177_12,(8,0,4):C.UVGC_177_13,(7,0,0):C.UVGC_238_89,(7,0,2):C.UVGC_238_90,(7,0,3):C.UVGC_238_91,(7,0,4):C.UVGC_238_92,(7,0,5):C.UVGC_238_93,(5,0,3):C.UVGC_176_10,(5,0,4):C.UVGC_176_11,(1,0,3):C.UVGC_176_10,(1,0,4):C.UVGC_176_11,(11,0,3):C.UVGC_180_16,(11,0,4):C.UVGC_180_17,(10,0,3):C.UVGC_180_16,(10,0,4):C.UVGC_180_17,(9,0,3):C.UVGC_179_14,(9,0,4):C.UVGC_179_15,(2,1,3):C.UVGC_177_13,(2,1,4):C.UVGC_177_12,(0,1,3):C.UVGC_177_13,(0,1,4):C.UVGC_177_12,(4,1,3):C.UVGC_176_10,(4,1,4):C.UVGC_176_11,(3,1,3):C.UVGC_176_10,(3,1,4):C.UVGC_176_11,(8,1,0):C.UVGC_240_96,(8,1,2):C.UVGC_240_97,(8,1,3):C.UVGC_238_91,(8,1,4):C.UVGC_240_98,(8,1,5):C.UVGC_240_99,(6,1,0):C.UVGC_235_79,(6,1,3):C.UVGC_235_80,(6,1,4):C.UVGC_235_81,(6,1,5):C.UVGC_235_82,(7,1,1):C.UVGC_181_18,(7,1,3):C.UVGC_177_12,(7,1,4):C.UVGC_182_19,(5,1,3):C.UVGC_176_10,(5,1,4):C.UVGC_176_11,(1,1,3):C.UVGC_176_10,(1,1,4):C.UVGC_176_11,(11,1,3):C.UVGC_180_16,(11,1,4):C.UVGC_180_17,(10,1,3):C.UVGC_180_16,(10,1,4):C.UVGC_180_17,(9,1,3):C.UVGC_179_14,(9,1,4):C.UVGC_179_15,(2,2,3):C.UVGC_177_13,(2,2,4):C.UVGC_177_12,(0,2,3):C.UVGC_177_13,(0,2,4):C.UVGC_177_12,(4,2,3):C.UVGC_176_10,(4,2,4):C.UVGC_176_11,(3,2,3):C.UVGC_176_10,(3,2,4):C.UVGC_176_11,(8,2,0):C.UVGC_237_85,(8,2,2):C.UVGC_237_86,(8,2,3):C.UVGC_236_83,(8,2,4):C.UVGC_237_87,(8,2,5):C.UVGC_237_88,(6,2,1):C.UVGC_181_18,(6,2,4):C.UVGC_179_14,(7,2,0):C.UVGC_235_79,(7,2,3):C.UVGC_236_83,(7,2,4):C.UVGC_236_84,(7,2,5):C.UVGC_235_82,(5,2,3):C.UVGC_176_10,(5,2,4):C.UVGC_176_11,(1,2,3):C.UVGC_176_10,(1,2,4):C.UVGC_176_11,(11,2,3):C.UVGC_180_16,(11,2,4):C.UVGC_180_17,(10,2,3):C.UVGC_180_16,(10,2,4):C.UVGC_180_17,(9,2,3):C.UVGC_179_14,(9,2,4):C.UVGC_179_15})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_250_113,(0,0,2):C.UVGC_250_114,(0,0,1):C.UVGC_250_115,(0,1,0):C.UVGC_251_116,(0,1,2):C.UVGC_251_117,(0,1,1):C.UVGC_251_118})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_224_54})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_225_55})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_226_56})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_252_119,(0,0,2):C.UVGC_252_120,(0,0,1):C.UVGC_252_121,(0,1,0):C.UVGC_249_110,(0,1,2):C.UVGC_249_111,(0,1,1):C.UVGC_249_112})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_253_122})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_254_123})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_255_124})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_187_24,(0,1,0):C.UVGC_163_3,(0,2,0):C.UVGC_163_3})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_187_24,(0,1,0):C.UVGC_163_3,(0,2,0):C.UVGC_163_3})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_187_24,(0,1,0):C.UVGC_242_101,(0,2,0):C.UVGC_242_101})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_183_20,(0,1,0):C.UVGC_166_5,(0,2,0):C.UVGC_166_5})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_183_20,(0,1,0):C.UVGC_166_5,(0,2,0):C.UVGC_166_5})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_183_20,(0,1,0):C.UVGC_218_48,(0,2,0):C.UVGC_218_48})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,1):C.UVGC_188_26,(0,1,2):C.UVGC_188_27,(0,1,3):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,4):C.UVGC_188_30,(0,2,0):C.UVGC_188_25,(0,2,1):C.UVGC_188_26,(0,2,2):C.UVGC_188_27,(0,2,3):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,4):C.UVGC_188_30})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,1):C.UVGC_188_26,(0,1,3):C.UVGC_188_27,(0,1,4):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,2):C.UVGC_188_30,(0,2,0):C.UVGC_188_25,(0,2,1):C.UVGC_188_26,(0,2,3):C.UVGC_188_27,(0,2,4):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,2):C.UVGC_188_30})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,1):C.UVGC_188_26,(0,1,2):C.UVGC_188_27,(0,1,3):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,4):C.UVGC_243_102,(0,2,0):C.UVGC_188_25,(0,2,1):C.UVGC_188_26,(0,2,2):C.UVGC_188_27,(0,2,3):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,4):C.UVGC_243_102})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,1):C.UVGC_188_26,(0,1,3):C.UVGC_188_27,(0,1,4):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,2):C.UVGC_188_30,(0,2,0):C.UVGC_188_25,(0,2,1):C.UVGC_188_26,(0,2,3):C.UVGC_188_27,(0,2,4):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,2):C.UVGC_188_30})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,1):C.UVGC_188_26,(0,1,2):C.UVGC_188_27,(0,1,3):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,4):C.UVGC_188_30,(0,2,0):C.UVGC_188_25,(0,2,1):C.UVGC_188_26,(0,2,2):C.UVGC_188_27,(0,2,3):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,4):C.UVGC_188_30})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_184_21,(0,1,0):C.UVGC_188_25,(0,1,2):C.UVGC_188_26,(0,1,3):C.UVGC_188_27,(0,1,4):C.UVGC_188_28,(0,1,5):C.UVGC_188_29,(0,1,1):C.UVGC_219_49,(0,2,0):C.UVGC_188_25,(0,2,2):C.UVGC_188_26,(0,2,3):C.UVGC_188_27,(0,2,4):C.UVGC_188_28,(0,2,5):C.UVGC_188_29,(0,2,1):C.UVGC_219_49})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_213_39,(0,0,1):C.UVGC_213_40})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_211_35,(0,0,1):C.UVGC_211_36})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_246_105,(0,0,2):C.UVGC_246_106,(0,0,1):C.UVGC_246_107})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_214_41,(0,0,1):C.UVGC_214_42})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_212_37,(0,0,1):C.UVGC_212_38})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_246_105,(0,0,2):C.UVGC_246_106,(0,0,1):C.UVGC_246_107})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_247_108,(0,1,0):C.UVGC_248_109})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_222_52,(0,1,0):C.UVGC_223_53})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_164_4,(0,2,0):C.UVGC_164_4})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_164_4,(0,2,0):C.UVGC_164_4})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_244_103,(0,2,0):C.UVGC_244_103})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_164_4,(0,2,0):C.UVGC_164_4})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_164_4,(0,2,0):C.UVGC_164_4})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_185_22,(0,1,0):C.UVGC_220_50,(0,2,0):C.UVGC_220_50})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_186_23,(0,1,0):C.UVGC_162_2,(0,2,0):C.UVGC_162_2})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_186_23,(0,1,0):C.UVGC_162_2,(0,2,0):C.UVGC_162_2})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_245_104,(0,2,0):C.UVGC_245_104,(0,1,0):C.UVGC_241_100,(0,3,0):C.UVGC_241_100})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_186_23,(0,1,0):C.UVGC_162_2,(0,2,0):C.UVGC_162_2})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_186_23,(0,1,0):C.UVGC_162_2,(0,2,0):C.UVGC_162_2})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_221_51,(0,2,0):C.UVGC_221_51,(0,1,0):C.UVGC_217_47,(0,3,0):C.UVGC_217_47})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_228_59,(0,0,1):C.UVGC_228_60,(0,0,2):C.UVGC_228_61,(0,0,3):C.UVGC_228_62,(0,1,0):C.UVGC_227_57,(0,1,3):C.UVGC_227_58})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_216_45,(0,0,1):C.UVGC_216_46})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_210_33,(0,0,0):C.UVGC_210_34})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_215_43,(0,0,1):C.UVGC_215_44})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_209_31,(0,0,0):C.UVGC_209_32})

