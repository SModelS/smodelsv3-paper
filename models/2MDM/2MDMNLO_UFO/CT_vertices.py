# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Tue 6 Aug 2024 18:03:01


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
               couplings = {(0,0,0):C.R2GC_350_134,(0,0,1):C.R2GC_352_137,(0,1,0):C.R2GC_358_138,(0,1,1):C.R2GC_358_139,(0,3,0):C.R2GC_358_138,(0,3,1):C.R2GC_360_141,(0,5,0):C.R2GC_350_134,(0,5,1):C.R2GC_351_136,(0,6,0):C.R2GC_350_134,(0,6,1):C.R2GC_350_135,(0,7,0):C.R2GC_358_138,(0,7,1):C.R2GC_359_140,(0,2,1):C.R2GC_259_72,(0,4,1):C.R2GC_258_71})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_262_77,(2,0,1):C.R2GC_262_78,(0,0,0):C.R2GC_262_77,(0,0,1):C.R2GC_262_78,(6,0,0):C.R2GC_265_82,(6,0,1):C.R2GC_366_147,(4,0,0):C.R2GC_260_73,(4,0,1):C.R2GC_260_74,(3,0,0):C.R2GC_260_73,(3,0,1):C.R2GC_260_74,(8,0,0):C.R2GC_261_75,(8,0,1):C.R2GC_261_76,(7,0,0):C.R2GC_266_83,(7,0,1):C.R2GC_364_146,(5,0,0):C.R2GC_260_73,(5,0,1):C.R2GC_260_74,(1,0,0):C.R2GC_260_73,(1,0,1):C.R2GC_260_74,(11,0,0):C.R2GC_264_80,(11,0,1):C.R2GC_264_81,(10,0,0):C.R2GC_264_80,(10,0,1):C.R2GC_264_81,(9,0,1):C.R2GC_263_79,(2,1,0):C.R2GC_262_77,(2,1,1):C.R2GC_262_78,(0,1,0):C.R2GC_262_77,(0,1,1):C.R2GC_262_78,(4,1,0):C.R2GC_260_73,(4,1,1):C.R2GC_260_74,(3,1,0):C.R2GC_260_73,(3,1,1):C.R2GC_260_74,(8,1,0):C.R2GC_261_75,(8,1,1):C.R2GC_364_146,(6,1,0):C.R2GC_362_143,(6,1,1):C.R2GC_362_144,(7,1,0):C.R2GC_266_83,(7,1,1):C.R2GC_261_76,(5,1,0):C.R2GC_260_73,(5,1,1):C.R2GC_260_74,(1,1,0):C.R2GC_260_73,(1,1,1):C.R2GC_260_74,(11,1,0):C.R2GC_264_80,(11,1,1):C.R2GC_264_81,(10,1,0):C.R2GC_264_80,(10,1,1):C.R2GC_264_81,(9,1,1):C.R2GC_263_79,(2,2,0):C.R2GC_262_77,(2,2,1):C.R2GC_262_78,(0,2,0):C.R2GC_262_77,(0,2,1):C.R2GC_262_78,(4,2,0):C.R2GC_260_73,(4,2,1):C.R2GC_260_74,(3,2,0):C.R2GC_260_73,(3,2,1):C.R2GC_260_74,(8,2,0):C.R2GC_261_75,(8,2,1):C.R2GC_361_142,(6,2,0):C.R2GC_265_82,(7,2,0):C.R2GC_363_145,(7,2,1):C.R2GC_361_142,(5,2,0):C.R2GC_260_73,(5,2,1):C.R2GC_260_74,(1,2,0):C.R2GC_260_73,(1,2,1):C.R2GC_260_74,(11,2,0):C.R2GC_264_80,(11,2,1):C.R2GC_264_81,(10,2,0):C.R2GC_264_80,(10,2,1):C.R2GC_264_81,(9,2,1):C.R2GC_263_79})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_384_159,(0,1,0):C.R2GC_385_160})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_317_110,(0,1,0):C.R2GC_316_109})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_387_162,(0,1,0):C.R2GC_388_163})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_332_120,(0,1,0):C.R2GC_331_119})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_346_129,(0,1,0):C.R2GC_347_130})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_311_104})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_326_114})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_291_92})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_313_106})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_328_116})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_292_93})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_314_107})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_329_117})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_293_94})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_379_154,(0,1,0):C.R2GC_376_151})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_380_155,(0,1,0):C.R2GC_377_152})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_310_103,(0,1,0):C.R2GC_312_105})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_325_113,(0,1,0):C.R2GC_327_115})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_342_125,(0,1,0):C.R2GC_340_123})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_378_153})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_300_98})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_341_124})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_381_156})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_301_99})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_343_126})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_382_157})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_302_100})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_344_127})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_270_87})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_270_87})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_270_87})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_84})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_267_84})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_267_84})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_268_85})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_372_149})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_373_150})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_307_102})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_322_112})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_337_122})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_383_158})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_315_108})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_386_161})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_330_118})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_345_128})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_298_96,(0,1,0):C.R2GC_299_97})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_298_96,(0,1,0):C.R2GC_299_97})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_298_96,(0,1,0):C.R2GC_299_97})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_289_90,(0,1,0):C.R2GC_290_91})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_289_90,(0,1,0):C.R2GC_290_91})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_289_90,(0,1,0):C.R2GC_290_91})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_269_86})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_370_148,(0,2,0):C.R2GC_370_148,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_296_95,(0,2,0):C.R2GC_296_95,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_335_121,(0,2,0):C.R2GC_335_121,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_305_101,(0,2,0):C.R2GC_305_101,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_320_111,(0,2,0):C.R2GC_320_111,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_287_89,(0,2,0):C.R2GC_287_89,(0,1,0):C.R2GC_285_88,(0,3,0):C.R2GC_285_88})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,4):C.R2GC_349_133,(0,1,0):C.R2GC_240_5,(0,1,2):C.R2GC_240_6,(0,1,3):C.R2GC_240_7,(0,1,5):C.R2GC_240_8,(0,1,6):C.R2GC_240_9,(0,1,7):C.R2GC_240_10,(0,2,1):C.R2GC_348_131,(0,2,4):C.R2GC_348_132})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.g, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_249_25,(0,0,1):C.R2GC_249_26,(0,0,2):C.R2GC_249_27,(0,0,3):C.R2GC_249_28,(0,0,4):C.R2GC_249_29,(0,0,5):C.R2GC_249_30})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_250_31,(0,0,1):C.R2GC_250_32,(0,0,2):C.R2GC_250_33,(0,0,3):C.R2GC_250_34,(0,0,4):C.R2GC_250_35,(0,0,5):C.R2GC_250_36})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.Zp, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_243_14,(0,1,0):C.R2GC_243_14,(0,2,0):C.R2GC_243_14})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Zp ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_247_21,(0,0,1):C.R2GC_247_22,(0,1,0):C.R2GC_247_21,(0,1,1):C.R2GC_247_22,(0,2,0):C.R2GC_247_21,(0,2,1):C.R2GC_247_22})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Zp ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_241_11,(0,0,1):C.R2GC_241_12,(0,1,0):C.R2GC_241_11,(0,1,1):C.R2GC_241_12,(0,2,0):C.R2GC_241_11,(0,2,1):C.R2GC_241_12})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Zp ],
                color = [ 'd(1,2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_242_13,(0,1,0):C.R2GC_242_13,(0,2,0):C.R2GC_242_13})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_244_15,(0,0,1):C.R2GC_244_16,(0,1,0):C.R2GC_244_15,(0,1,1):C.R2GC_244_16,(0,2,0):C.R2GC_244_15,(0,2,1):C.R2GC_244_16})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_248_23,(0,0,1):C.R2GC_248_24,(0,1,0):C.R2GC_248_23,(0,1,1):C.R2GC_248_24,(0,2,0):C.R2GC_248_23,(0,2,1):C.R2GC_248_24})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_255_61,(0,0,1):C.R2GC_255_62,(0,0,2):C.R2GC_255_63,(0,0,3):C.R2GC_255_64,(0,0,4):C.R2GC_255_65,(0,1,0):C.R2GC_255_61,(0,1,1):C.R2GC_255_62,(0,1,2):C.R2GC_255_63,(0,1,3):C.R2GC_255_64,(0,1,4):C.R2GC_255_65,(0,2,0):C.R2GC_255_61,(0,2,1):C.R2GC_255_62,(0,2,2):C.R2GC_255_63,(0,2,3):C.R2GC_255_64,(0,2,4):C.R2GC_255_65})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_238_1,(0,0,1):C.R2GC_238_2,(0,1,0):C.R2GC_238_1,(0,1,1):C.R2GC_238_2,(0,2,0):C.R2GC_238_1,(0,2,1):C.R2GC_238_2})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_246_19,(1,0,1):C.R2GC_246_20,(0,1,0):C.R2GC_245_17,(0,1,1):C.R2GC_245_18,(0,2,0):C.R2GC_245_17,(0,2,1):C.R2GC_245_18,(0,3,0):C.R2GC_245_17,(0,3,1):C.R2GC_245_18})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_239_3,(0,0,1):C.R2GC_239_4,(0,1,0):C.R2GC_239_3,(0,1,1):C.R2GC_239_4,(0,2,0):C.R2GC_239_3,(0,2,1):C.R2GC_239_4})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_252_43,(0,0,1):C.R2GC_252_44,(0,0,2):C.R2GC_252_45,(0,0,3):C.R2GC_252_46,(0,0,4):C.R2GC_252_47,(0,0,5):C.R2GC_252_48})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_251_37,(0,0,1):C.R2GC_251_38,(0,0,2):C.R2GC_251_39,(0,0,3):C.R2GC_251_40,(0,0,4):C.R2GC_251_41,(0,0,5):C.R2GC_251_42})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_256_66,(0,0,1):C.R2GC_256_67,(0,0,2):C.R2GC_256_68,(0,0,3):C.R2GC_256_69,(0,0,4):C.R2GC_256_70})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.g, P.h, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_253_49,(0,0,1):C.R2GC_253_50,(0,0,2):C.R2GC_253_51,(0,0,3):C.R2GC_253_52,(0,0,4):C.R2GC_253_53,(0,0,5):C.R2GC_253_54})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.g, P.g, P.Sd, P.Sd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_254_55,(0,0,1):C.R2GC_254_56,(0,0,2):C.R2GC_254_57,(0,0,3):C.R2GC_254_58,(0,0,4):C.R2GC_254_59,(0,0,5):C.R2GC_254_60})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_350_133,(0,0,1):C.UVGC_350_134,(0,0,2):C.UVGC_350_135,(0,0,3):C.UVGC_352_142,(0,0,4):C.UVGC_352_143,(0,0,5):C.UVGC_350_137,(0,0,6):C.UVGC_350_138,(0,0,7):C.UVGC_350_139,(0,1,0):C.UVGC_358_157,(0,1,1):C.UVGC_358_158,(0,1,2):C.UVGC_358_159,(0,1,3):C.UVGC_358_160,(0,1,5):C.UVGC_358_161,(0,1,6):C.UVGC_358_162,(0,1,7):C.UVGC_358_163,(0,3,0):C.UVGC_358_157,(0,3,1):C.UVGC_358_158,(0,3,2):C.UVGC_358_159,(0,3,3):C.UVGC_360_166,(0,3,4):C.UVGC_360_167,(0,3,5):C.UVGC_358_161,(0,3,6):C.UVGC_358_162,(0,3,7):C.UVGC_358_163,(0,5,0):C.UVGC_350_133,(0,5,1):C.UVGC_350_134,(0,5,2):C.UVGC_350_135,(0,5,3):C.UVGC_351_140,(0,5,4):C.UVGC_351_141,(0,5,5):C.UVGC_350_137,(0,5,6):C.UVGC_350_138,(0,5,7):C.UVGC_350_139,(0,7,0):C.UVGC_350_133,(0,7,1):C.UVGC_350_134,(0,7,2):C.UVGC_350_135,(0,7,3):C.UVGC_350_136,(0,7,4):C.UVGC_259_5,(0,7,5):C.UVGC_350_137,(0,7,6):C.UVGC_350_138,(0,7,7):C.UVGC_350_139,(0,8,0):C.UVGC_358_157,(0,8,1):C.UVGC_358_158,(0,8,2):C.UVGC_358_159,(0,8,3):C.UVGC_359_164,(0,8,4):C.UVGC_359_165,(0,8,5):C.UVGC_358_161,(0,8,6):C.UVGC_358_162,(0,8,7):C.UVGC_358_163,(0,2,3):C.UVGC_259_4,(0,2,4):C.UVGC_259_5,(0,4,3):C.UVGC_258_2,(0,4,4):C.UVGC_258_3,(0,6,3):C.UVGC_257_1})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,4):C.UVGC_261_9,(2,0,5):C.UVGC_261_8,(0,0,4):C.UVGC_261_9,(0,0,5):C.UVGC_261_8,(6,0,0):C.UVGC_365_193,(6,0,2):C.UVGC_365_194,(6,0,3):C.UVGC_365_195,(6,0,4):C.UVGC_366_200,(6,0,5):C.UVGC_366_201,(6,0,6):C.UVGC_365_197,(6,0,7):C.UVGC_365_198,(6,0,8):C.UVGC_365_199,(4,0,4):C.UVGC_260_6,(4,0,5):C.UVGC_260_7,(3,0,4):C.UVGC_260_6,(3,0,5):C.UVGC_260_7,(8,0,4):C.UVGC_261_8,(8,0,5):C.UVGC_261_9,(7,0,0):C.UVGC_365_193,(7,0,2):C.UVGC_365_194,(7,0,3):C.UVGC_365_195,(7,0,4):C.UVGC_364_188,(7,0,5):C.UVGC_365_196,(7,0,6):C.UVGC_365_197,(7,0,7):C.UVGC_365_198,(7,0,8):C.UVGC_365_199,(5,0,4):C.UVGC_260_6,(5,0,5):C.UVGC_260_7,(1,0,4):C.UVGC_260_6,(1,0,5):C.UVGC_260_7,(11,0,4):C.UVGC_264_12,(11,0,5):C.UVGC_264_13,(10,0,4):C.UVGC_264_12,(10,0,5):C.UVGC_264_13,(9,0,4):C.UVGC_263_10,(9,0,5):C.UVGC_263_11,(2,1,4):C.UVGC_261_9,(2,1,5):C.UVGC_261_8,(0,1,4):C.UVGC_261_9,(0,1,5):C.UVGC_261_8,(4,1,4):C.UVGC_260_6,(4,1,5):C.UVGC_260_7,(3,1,4):C.UVGC_260_6,(3,1,5):C.UVGC_260_7,(8,1,0):C.UVGC_364_185,(8,1,2):C.UVGC_364_186,(8,1,3):C.UVGC_364_187,(8,1,4):C.UVGC_364_188,(8,1,5):C.UVGC_364_189,(8,1,6):C.UVGC_364_190,(8,1,7):C.UVGC_364_191,(8,1,8):C.UVGC_364_192,(6,1,0):C.UVGC_362_176,(6,1,2):C.UVGC_362_177,(6,1,3):C.UVGC_362_178,(6,1,4):C.UVGC_362_179,(6,1,5):C.UVGC_362_180,(6,1,6):C.UVGC_362_181,(6,1,7):C.UVGC_362_182,(6,1,8):C.UVGC_362_183,(7,1,1):C.UVGC_265_14,(7,1,4):C.UVGC_261_8,(7,1,5):C.UVGC_266_15,(5,1,4):C.UVGC_260_6,(5,1,5):C.UVGC_260_7,(1,1,4):C.UVGC_260_6,(1,1,5):C.UVGC_260_7,(11,1,4):C.UVGC_264_12,(11,1,5):C.UVGC_264_13,(10,1,4):C.UVGC_264_12,(10,1,5):C.UVGC_264_13,(9,1,4):C.UVGC_263_10,(9,1,5):C.UVGC_263_11,(2,2,4):C.UVGC_261_9,(2,2,5):C.UVGC_261_8,(0,2,4):C.UVGC_261_9,(0,2,5):C.UVGC_261_8,(4,2,4):C.UVGC_260_6,(4,2,5):C.UVGC_260_7,(3,2,4):C.UVGC_260_6,(3,2,5):C.UVGC_260_7,(8,2,0):C.UVGC_361_168,(8,2,2):C.UVGC_361_169,(8,2,3):C.UVGC_361_170,(8,2,4):C.UVGC_361_171,(8,2,5):C.UVGC_361_172,(8,2,6):C.UVGC_361_173,(8,2,7):C.UVGC_361_174,(8,2,8):C.UVGC_361_175,(6,2,1):C.UVGC_265_14,(6,2,5):C.UVGC_263_10,(7,2,0):C.UVGC_362_176,(7,2,2):C.UVGC_362_177,(7,2,3):C.UVGC_362_178,(7,2,4):C.UVGC_361_171,(7,2,5):C.UVGC_363_184,(7,2,6):C.UVGC_362_181,(7,2,7):C.UVGC_362_182,(7,2,8):C.UVGC_362_183,(5,2,4):C.UVGC_260_6,(5,2,5):C.UVGC_260_7,(1,2,4):C.UVGC_260_6,(1,2,5):C.UVGC_260_7,(11,2,4):C.UVGC_264_12,(11,2,5):C.UVGC_264_13,(10,2,4):C.UVGC_264_12,(10,2,5):C.UVGC_264_13,(9,2,4):C.UVGC_263_10,(9,2,5):C.UVGC_263_11})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_384_233,(0,0,2):C.UVGC_384_234,(0,0,1):C.UVGC_384_235,(0,1,0):C.UVGC_385_236,(0,1,2):C.UVGC_385_237,(0,1,1):C.UVGC_385_238})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_317_62,(0,0,2):C.UVGC_317_63,(0,0,0):C.UVGC_317_64,(0,1,1):C.UVGC_316_59,(0,1,2):C.UVGC_316_60,(0,1,0):C.UVGC_316_61})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_387_242,(0,0,2):C.UVGC_387_243,(0,0,1):C.UVGC_387_244,(0,1,0):C.UVGC_388_245,(0,1,2):C.UVGC_388_246,(0,1,1):C.UVGC_388_247})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_332_89,(0,0,2):C.UVGC_332_90,(0,0,1):C.UVGC_332_91,(0,1,0):C.UVGC_331_86,(0,1,2):C.UVGC_331_87,(0,1,1):C.UVGC_331_88})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_346_113,(0,0,2):C.UVGC_346_114,(0,0,1):C.UVGC_346_115,(0,1,0):C.UVGC_347_116,(0,1,2):C.UVGC_347_117,(0,1,1):C.UVGC_347_118})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_311_50})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_326_77})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_291_26})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.h ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_313_54})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_328_81})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_292_27})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_314_55})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_329_82})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_293_28})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_379_222,(0,0,2):C.UVGC_379_223,(0,0,1):C.UVGC_379_224,(0,1,0):C.UVGC_376_215,(0,1,2):C.UVGC_376_216,(0,1,1):C.UVGC_376_217})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_380_225,(0,0,2):C.UVGC_380_226,(0,0,1):C.UVGC_380_227,(0,1,0):C.UVGC_377_218,(0,1,2):C.UVGC_377_219,(0,1,1):C.UVGC_377_220})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_310_47,(0,0,2):C.UVGC_310_48,(0,0,0):C.UVGC_310_49,(0,1,1):C.UVGC_312_51,(0,1,2):C.UVGC_312_52,(0,1,0):C.UVGC_312_53})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_325_74,(0,0,2):C.UVGC_325_75,(0,0,1):C.UVGC_325_76,(0,1,0):C.UVGC_327_78,(0,1,2):C.UVGC_327_79,(0,1,1):C.UVGC_327_80})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_342_105,(0,0,2):C.UVGC_342_106,(0,0,1):C.UVGC_342_107,(0,1,0):C.UVGC_340_101,(0,1,2):C.UVGC_340_102,(0,1,1):C.UVGC_340_103})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_378_221})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_300_35})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_341_104})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_381_228})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_301_36})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_343_108})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_382_229})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_302_37})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Sd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_344_109})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_270_19,(0,1,0):C.UVGC_368_203,(0,2,0):C.UVGC_368_203})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_270_19,(0,1,0):C.UVGC_295_30,(0,2,0):C.UVGC_295_30})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_270_19,(0,1,0):C.UVGC_334_93,(0,2,0):C.UVGC_334_93})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_267_16,(0,1,0):C.UVGC_304_39,(0,2,0):C.UVGC_304_39})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_267_16,(0,1,0):C.UVGC_319_66,(0,2,0):C.UVGC_319_66})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_267_16,(0,1,0):C.UVGC_286_21,(0,2,0):C.UVGC_286_21})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,1):C.UVGC_353_145,(0,1,2):C.UVGC_353_146,(0,1,3):C.UVGC_353_147,(0,1,4):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,5):C.UVGC_369_204,(0,2,0):C.UVGC_353_144,(0,2,1):C.UVGC_353_145,(0,2,2):C.UVGC_353_146,(0,2,3):C.UVGC_353_147,(0,2,4):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,5):C.UVGC_369_204})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,1):C.UVGC_353_145,(0,1,3):C.UVGC_353_146,(0,1,4):C.UVGC_353_147,(0,1,5):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,2):C.UVGC_354_153,(0,2,0):C.UVGC_353_144,(0,2,1):C.UVGC_353_145,(0,2,3):C.UVGC_353_146,(0,2,4):C.UVGC_353_147,(0,2,5):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,2):C.UVGC_354_153})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,1):C.UVGC_353_145,(0,1,2):C.UVGC_353_146,(0,1,3):C.UVGC_353_147,(0,1,4):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,5):C.UVGC_357_156,(0,2,0):C.UVGC_353_144,(0,2,1):C.UVGC_353_145,(0,2,2):C.UVGC_353_146,(0,2,3):C.UVGC_353_147,(0,2,4):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,5):C.UVGC_357_156})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,1):C.UVGC_353_145,(0,1,2):C.UVGC_353_146,(0,1,4):C.UVGC_353_147,(0,1,5):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,3):C.UVGC_355_154,(0,2,0):C.UVGC_353_144,(0,2,1):C.UVGC_353_145,(0,2,2):C.UVGC_353_146,(0,2,4):C.UVGC_353_147,(0,2,5):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,3):C.UVGC_355_154})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,1):C.UVGC_353_145,(0,1,2):C.UVGC_353_146,(0,1,3):C.UVGC_353_147,(0,1,4):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,5):C.UVGC_356_155,(0,2,0):C.UVGC_353_144,(0,2,1):C.UVGC_353_145,(0,2,2):C.UVGC_353_146,(0,2,3):C.UVGC_353_147,(0,2,4):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,5):C.UVGC_356_155})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_268_17,(0,1,0):C.UVGC_353_144,(0,1,2):C.UVGC_353_145,(0,1,3):C.UVGC_353_146,(0,1,4):C.UVGC_353_147,(0,1,5):C.UVGC_353_148,(0,1,6):C.UVGC_353_149,(0,1,7):C.UVGC_353_150,(0,1,8):C.UVGC_353_151,(0,1,1):C.UVGC_353_152,(0,2,0):C.UVGC_353_144,(0,2,2):C.UVGC_353_145,(0,2,3):C.UVGC_353_146,(0,2,4):C.UVGC_353_147,(0,2,5):C.UVGC_353_148,(0,2,6):C.UVGC_353_149,(0,2,7):C.UVGC_353_150,(0,2,8):C.UVGC_353_151,(0,2,1):C.UVGC_353_152})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_372_207,(0,0,2):C.UVGC_372_208,(0,0,1):C.UVGC_372_209})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_373_210,(0,0,2):C.UVGC_373_211,(0,0,1):C.UVGC_373_212})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_307_42,(0,0,2):C.UVGC_307_43,(0,0,0):C.UVGC_307_44})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_322_69,(0,0,2):C.UVGC_322_70,(0,0,1):C.UVGC_322_71})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_337_96,(0,0,2):C.UVGC_337_97,(0,0,1):C.UVGC_337_98})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_383_230,(0,0,2):C.UVGC_383_231,(0,0,1):C.UVGC_383_232})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_315_56,(0,0,2):C.UVGC_315_57,(0,0,0):C.UVGC_315_58})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_386_239,(0,0,2):C.UVGC_386_240,(0,0,1):C.UVGC_386_241})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_330_83,(0,0,2):C.UVGC_330_84,(0,0,1):C.UVGC_330_85})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_345_110,(0,0,2):C.UVGC_345_111,(0,0,1):C.UVGC_345_112})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_374_213,(0,1,0):C.UVGC_375_214})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_33,(0,1,0):C.UVGC_299_34})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_338_99,(0,1,0):C.UVGC_339_100})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_308_45,(0,1,0):C.UVGC_309_46})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_323_72,(0,1,0):C.UVGC_324_73})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_24,(0,1,0):C.UVGC_290_25})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_371_206,(0,2,0):C.UVGC_371_206})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_297_32,(0,2,0):C.UVGC_297_32})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_336_95,(0,2,0):C.UVGC_336_95})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_306_41,(0,2,0):C.UVGC_306_41})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_321_68,(0,2,0):C.UVGC_321_68})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Zp ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_269_18,(0,1,0):C.UVGC_288_23,(0,2,0):C.UVGC_288_23})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_370_205,(0,2,0):C.UVGC_370_205,(0,1,0):C.UVGC_367_202,(0,3,0):C.UVGC_367_202})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_296_31,(0,2,0):C.UVGC_296_31,(0,1,0):C.UVGC_294_29,(0,3,0):C.UVGC_294_29})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_335_94,(0,2,0):C.UVGC_335_94,(0,1,0):C.UVGC_333_92,(0,3,0):C.UVGC_333_92})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_305_40,(0,2,0):C.UVGC_305_40,(0,1,0):C.UVGC_303_38,(0,3,0):C.UVGC_303_38})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_320_67,(0,2,0):C.UVGC_320_67,(0,1,0):C.UVGC_318_65,(0,3,0):C.UVGC_318_65})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_287_22,(0,2,0):C.UVGC_287_22,(0,1,0):C.UVGC_285_20,(0,3,0):C.UVGC_285_20})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_349_125,(0,0,1):C.UVGC_349_126,(0,0,2):C.UVGC_349_127,(0,0,3):C.UVGC_349_128,(0,0,4):C.UVGC_349_129,(0,0,5):C.UVGC_349_130,(0,0,6):C.UVGC_349_131,(0,0,7):C.UVGC_349_132,(0,1,0):C.UVGC_348_119,(0,1,1):C.UVGC_348_120,(0,1,2):C.UVGC_348_121,(0,1,5):C.UVGC_348_122,(0,1,6):C.UVGC_348_123,(0,1,7):C.UVGC_348_124})

