# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Wed 6 Sep 2023 09:08:25


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
               couplings = {(0,0,0):C.R2GC_216_55,(0,0,1):C.R2GC_218_58,(0,1,0):C.R2GC_219_59,(0,1,1):C.R2GC_219_60,(0,3,0):C.R2GC_219_59,(0,3,1):C.R2GC_221_62,(0,5,0):C.R2GC_216_55,(0,5,1):C.R2GC_217_57,(0,6,0):C.R2GC_216_55,(0,6,1):C.R2GC_216_56,(0,7,0):C.R2GC_219_59,(0,7,1):C.R2GC_220_61,(0,2,1):C.R2GC_182_35,(0,4,1):C.R2GC_181_34})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_185_40,(2,0,1):C.R2GC_185_41,(0,0,0):C.R2GC_185_40,(0,0,1):C.R2GC_185_41,(6,0,0):C.R2GC_188_45,(6,0,1):C.R2GC_226_68,(4,0,0):C.R2GC_183_36,(4,0,1):C.R2GC_183_37,(3,0,0):C.R2GC_183_36,(3,0,1):C.R2GC_183_37,(8,0,0):C.R2GC_184_38,(8,0,1):C.R2GC_184_39,(7,0,0):C.R2GC_189_46,(7,0,1):C.R2GC_225_67,(5,0,0):C.R2GC_183_36,(5,0,1):C.R2GC_183_37,(1,0,0):C.R2GC_183_36,(1,0,1):C.R2GC_183_37,(11,0,0):C.R2GC_187_43,(11,0,1):C.R2GC_187_44,(10,0,0):C.R2GC_187_43,(10,0,1):C.R2GC_187_44,(9,0,1):C.R2GC_186_42,(2,1,0):C.R2GC_185_40,(2,1,1):C.R2GC_185_41,(0,1,0):C.R2GC_185_40,(0,1,1):C.R2GC_185_41,(4,1,0):C.R2GC_183_36,(4,1,1):C.R2GC_183_37,(3,1,0):C.R2GC_183_36,(3,1,1):C.R2GC_183_37,(8,1,0):C.R2GC_184_38,(8,1,1):C.R2GC_225_67,(6,1,0):C.R2GC_222_63,(6,1,1):C.R2GC_222_64,(7,1,0):C.R2GC_189_46,(7,1,1):C.R2GC_184_39,(5,1,0):C.R2GC_183_36,(5,1,1):C.R2GC_183_37,(1,1,0):C.R2GC_183_36,(1,1,1):C.R2GC_183_37,(11,1,0):C.R2GC_187_43,(11,1,1):C.R2GC_187_44,(10,1,0):C.R2GC_187_43,(10,1,1):C.R2GC_187_44,(9,1,1):C.R2GC_186_42,(2,2,0):C.R2GC_185_40,(2,2,1):C.R2GC_185_41,(0,2,0):C.R2GC_185_40,(0,2,1):C.R2GC_185_41,(4,2,0):C.R2GC_183_36,(4,2,1):C.R2GC_183_37,(3,2,0):C.R2GC_183_36,(3,2,1):C.R2GC_183_37,(8,2,0):C.R2GC_184_38,(8,2,1):C.R2GC_223_66,(6,2,0):C.R2GC_188_45,(7,2,0):C.R2GC_223_65,(7,2,1):C.R2GC_223_66,(5,2,0):C.R2GC_183_36,(5,2,1):C.R2GC_183_37,(1,2,0):C.R2GC_183_36,(1,2,1):C.R2GC_183_37,(11,2,0):C.R2GC_187_43,(11,2,1):C.R2GC_187_44,(10,2,0):C.R2GC_187_43,(10,2,1):C.R2GC_187_44,(9,2,1):C.R2GC_186_42})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_237_70})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_238_71})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_239_72})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_240_73})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Sd ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_241_74})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_195_50})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_195_50})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_195_50})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_191_48})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_191_48})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_191_48})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_193_49})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_212_51})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_165_32,(0,1,0):C.R2GC_142_11})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_165_32,(0,1,0):C.R2GC_142_11})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_165_32,(0,1,0):C.R2GC_142_11})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_164_31,(0,1,0):C.R2GC_139_10})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_164_31,(0,1,0):C.R2GC_139_10})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_164_31,(0,1,0):C.R2GC_139_10})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_8,(0,1,0):C.R2GC_138_9})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_190_47})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_190_47})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_233_69,(0,2,0):C.R2GC_233_69,(0,1,0):C.R2GC_190_47,(0,3,0):C.R2GC_190_47})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_190_47})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_190_47})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_190_47})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_215_54,(0,1,2):C.R2GC_130_1,(0,2,0):C.R2GC_214_52,(0,2,1):C.R2GC_214_53})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_131_2})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_132_3})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.Zp, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_158_20,(0,1,0):C.R2GC_158_20,(0,2,0):C.R2GC_158_20})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Zp ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_155_16,(0,0,1):C.R2GC_155_17,(0,1,0):C.R2GC_155_16,(0,1,1):C.R2GC_155_17,(0,2,0):C.R2GC_155_16,(0,2,1):C.R2GC_155_17})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_162_27,(0,0,1):C.R2GC_162_28,(0,1,0):C.R2GC_162_27,(0,1,1):C.R2GC_162_28,(0,2,0):C.R2GC_162_27,(0,2,1):C.R2GC_162_28})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Zp ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_157_19,(0,1,0):C.R2GC_156_18,(0,2,0):C.R2GC_156_18,(0,3,0):C.R2GC_156_18})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_168_33,(0,1,0):C.R2GC_168_33,(0,2,0):C.R2GC_168_33})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_159_21,(0,0,1):C.R2GC_159_22,(0,1,0):C.R2GC_159_21,(0,1,1):C.R2GC_159_22,(0,2,0):C.R2GC_159_21,(0,2,1):C.R2GC_159_22})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_163_29,(0,0,1):C.R2GC_163_30,(0,1,0):C.R2GC_163_29,(0,1,1):C.R2GC_163_30,(0,2,0):C.R2GC_163_29,(0,2,1):C.R2GC_163_30})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_153_12,(0,0,1):C.R2GC_153_13,(0,1,0):C.R2GC_153_12,(0,1,1):C.R2GC_153_13,(0,2,0):C.R2GC_153_12,(0,2,1):C.R2GC_153_13})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_161_25,(1,0,1):C.R2GC_161_26,(0,1,0):C.R2GC_160_23,(0,1,1):C.R2GC_160_24,(0,2,0):C.R2GC_160_23,(0,2,1):C.R2GC_160_24,(0,3,0):C.R2GC_160_23,(0,3,1):C.R2GC_160_24})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_154_14,(0,0,1):C.R2GC_154_15,(0,1,0):C.R2GC_154_14,(0,1,1):C.R2GC_154_15,(0,2,0):C.R2GC_154_14,(0,2,1):C.R2GC_154_15})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_134_5})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_133_4})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_133_4})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_6})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_136_7})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_216_34,(0,0,1):C.UVGC_218_39,(0,0,2):C.UVGC_218_40,(0,0,3):C.UVGC_216_36,(0,1,0):C.UVGC_219_41,(0,1,1):C.UVGC_219_42,(0,1,3):C.UVGC_219_43,(0,3,0):C.UVGC_219_41,(0,3,1):C.UVGC_221_46,(0,3,2):C.UVGC_221_47,(0,3,3):C.UVGC_219_43,(0,5,0):C.UVGC_216_34,(0,5,1):C.UVGC_217_37,(0,5,2):C.UVGC_217_38,(0,5,3):C.UVGC_216_36,(0,7,0):C.UVGC_216_34,(0,7,1):C.UVGC_216_35,(0,7,2):C.UVGC_182_8,(0,7,3):C.UVGC_216_36,(0,8,0):C.UVGC_219_41,(0,8,1):C.UVGC_220_44,(0,8,2):C.UVGC_220_45,(0,8,3):C.UVGC_219_43,(0,2,1):C.UVGC_182_7,(0,2,2):C.UVGC_182_8,(0,4,1):C.UVGC_181_5,(0,4,2):C.UVGC_181_6,(0,6,1):C.UVGC_170_1})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_184_12,(2,0,3):C.UVGC_184_11,(0,0,2):C.UVGC_184_12,(0,0,3):C.UVGC_184_11,(6,0,1):C.UVGC_225_56,(6,0,2):C.UVGC_226_60,(6,0,3):C.UVGC_226_61,(6,0,4):C.UVGC_225_59,(4,0,2):C.UVGC_183_9,(4,0,3):C.UVGC_183_10,(3,0,2):C.UVGC_183_9,(3,0,3):C.UVGC_183_10,(8,0,2):C.UVGC_184_11,(8,0,3):C.UVGC_184_12,(7,0,1):C.UVGC_225_56,(7,0,2):C.UVGC_225_57,(7,0,3):C.UVGC_225_58,(7,0,4):C.UVGC_225_59,(5,0,2):C.UVGC_183_9,(5,0,3):C.UVGC_183_10,(1,0,2):C.UVGC_183_9,(1,0,3):C.UVGC_183_10,(11,0,2):C.UVGC_187_15,(11,0,3):C.UVGC_187_16,(10,0,2):C.UVGC_187_15,(10,0,3):C.UVGC_187_16,(9,0,2):C.UVGC_186_13,(9,0,3):C.UVGC_186_14,(2,1,2):C.UVGC_184_12,(2,1,3):C.UVGC_184_11,(0,1,2):C.UVGC_184_12,(0,1,3):C.UVGC_184_11,(4,1,2):C.UVGC_183_9,(4,1,3):C.UVGC_183_10,(3,1,2):C.UVGC_183_9,(3,1,3):C.UVGC_183_10,(8,1,1):C.UVGC_227_62,(8,1,2):C.UVGC_225_57,(8,1,3):C.UVGC_227_63,(8,1,4):C.UVGC_227_64,(6,1,2):C.UVGC_222_48,(6,1,3):C.UVGC_222_49,(6,1,4):C.UVGC_222_50,(7,1,0):C.UVGC_188_17,(7,1,2):C.UVGC_184_11,(7,1,3):C.UVGC_189_18,(5,1,2):C.UVGC_183_9,(5,1,3):C.UVGC_183_10,(1,1,2):C.UVGC_183_9,(1,1,3):C.UVGC_183_10,(11,1,2):C.UVGC_187_15,(11,1,3):C.UVGC_187_16,(10,1,2):C.UVGC_187_15,(10,1,3):C.UVGC_187_16,(9,1,2):C.UVGC_186_13,(9,1,3):C.UVGC_186_14,(2,2,2):C.UVGC_184_12,(2,2,3):C.UVGC_184_11,(0,2,2):C.UVGC_184_12,(0,2,3):C.UVGC_184_11,(4,2,2):C.UVGC_183_9,(4,2,3):C.UVGC_183_10,(3,2,2):C.UVGC_183_9,(3,2,3):C.UVGC_183_10,(8,2,1):C.UVGC_224_53,(8,2,2):C.UVGC_223_51,(8,2,3):C.UVGC_224_54,(8,2,4):C.UVGC_224_55,(6,2,0):C.UVGC_188_17,(6,2,3):C.UVGC_186_13,(7,2,2):C.UVGC_223_51,(7,2,3):C.UVGC_223_52,(7,2,4):C.UVGC_222_50,(5,2,2):C.UVGC_183_9,(5,2,3):C.UVGC_183_10,(1,2,2):C.UVGC_183_9,(1,2,3):C.UVGC_183_10,(11,2,2):C.UVGC_187_15,(11,2,3):C.UVGC_187_16,(10,2,2):C.UVGC_187_15,(10,2,3):C.UVGC_187_16,(9,2,2):C.UVGC_186_13,(9,2,3):C.UVGC_186_14})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_237_74,(0,0,2):C.UVGC_237_75,(0,0,1):C.UVGC_237_76})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_238_77,(0,0,2):C.UVGC_238_78,(0,0,1):C.UVGC_238_79})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_239_80})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_240_81})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_241_82})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_195_27,(0,1,0):C.UVGC_174_4,(0,2,0):C.UVGC_174_4})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_195_27,(0,1,0):C.UVGC_174_4,(0,2,0):C.UVGC_174_4})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_195_27,(0,1,0):C.UVGC_229_66,(0,2,0):C.UVGC_229_66})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_191_20,(0,1,0):C.UVGC_172_3,(0,2,0):C.UVGC_172_3})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_191_20,(0,1,0):C.UVGC_172_3,(0,2,0):C.UVGC_172_3})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_191_20,(0,1,0):C.UVGC_172_3,(0,2,0):C.UVGC_172_3})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,1):C.UVGC_192_22,(0,1,2):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,3):C.UVGC_192_25,(0,2,0):C.UVGC_192_21,(0,2,1):C.UVGC_192_22,(0,2,2):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,3):C.UVGC_192_25})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,2):C.UVGC_192_22,(0,1,3):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,1):C.UVGC_192_25,(0,2,0):C.UVGC_192_21,(0,2,2):C.UVGC_192_22,(0,2,3):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,1):C.UVGC_192_25})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,1):C.UVGC_192_22,(0,1,2):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,3):C.UVGC_230_67,(0,2,0):C.UVGC_192_21,(0,2,1):C.UVGC_192_22,(0,2,2):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,3):C.UVGC_230_67})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,2):C.UVGC_192_22,(0,1,3):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,1):C.UVGC_192_25,(0,2,0):C.UVGC_192_21,(0,2,2):C.UVGC_192_22,(0,2,3):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,1):C.UVGC_192_25})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,1):C.UVGC_192_22,(0,1,2):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,3):C.UVGC_192_25,(0,2,0):C.UVGC_192_21,(0,2,1):C.UVGC_192_22,(0,2,2):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,3):C.UVGC_192_25})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_193_26,(0,1,0):C.UVGC_192_21,(0,1,2):C.UVGC_192_22,(0,1,3):C.UVGC_192_23,(0,1,4):C.UVGC_192_24,(0,1,1):C.UVGC_192_25,(0,2,0):C.UVGC_192_21,(0,2,2):C.UVGC_192_22,(0,2,3):C.UVGC_192_23,(0,2,4):C.UVGC_192_24,(0,2,1):C.UVGC_192_25})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,1):C.UVGC_212_29})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,1):C.UVGC_212_29})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,2):C.UVGC_234_71,(0,0,1):C.UVGC_212_29})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,1):C.UVGC_212_29})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,1):C.UVGC_212_29})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_212_28,(0,0,2):C.UVGC_234_71,(0,0,1):C.UVGC_212_29})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_235_72,(0,1,0):C.UVGC_236_73})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_231_68,(0,1,0):C.UVGC_232_69})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_190_19,(0,1,0):C.UVGC_171_2,(0,2,0):C.UVGC_171_2})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_190_19,(0,1,0):C.UVGC_171_2,(0,2,0):C.UVGC_171_2})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_233_70,(0,2,0):C.UVGC_233_70,(0,1,0):C.UVGC_228_65,(0,3,0):C.UVGC_228_65})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_190_19,(0,1,0):C.UVGC_171_2,(0,2,0):C.UVGC_171_2})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_190_19,(0,1,0):C.UVGC_171_2,(0,2,0):C.UVGC_171_2})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_190_19,(0,1,0):C.UVGC_171_2,(0,2,0):C.UVGC_171_2})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_215_31,(0,0,1):C.UVGC_215_32,(0,0,2):C.UVGC_215_33,(0,1,2):C.UVGC_214_30})

