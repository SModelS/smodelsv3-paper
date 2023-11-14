# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 28, 2023)
# Date: Tue 14 Nov 2023 15:12:04


from object_library import all_decays, Decay
import particles as P


Decay_Sd = Decay(name = 'Decay_Sd',
                 particle = P.Sd,
                 partial_widths = {(P.h,P.h):'((36*Ca**4*lam1**2*Sa**2*vev**2 - 24*Ca**4*lam1*lam3*Sa**2*vev**2 + 4*Ca**4*lam3**2*Sa**2*vev**2 + 12*Ca**2*lam1*lam3*Sa**4*vev**2 - 4*Ca**2*lam3**2*Sa**4*vev**2 + lam3**2*Sa**6*vev**2 + 12*Ca**5*lam1*lam3*Sa*vev*vev2 - 4*Ca**5*lam3**2*Sa*vev*vev2 + 72*Ca**3*lam1*lam2*Sa**3*vev*vev2 - 24*Ca**3*lam1*lam3*Sa**3*vev*vev2 - 24*Ca**3*lam2*lam3*Sa**3*vev*vev2 + 10*Ca**3*lam3**2*Sa**3*vev*vev2 + 12*Ca*lam2*lam3*Sa**5*vev*vev2 - 4*Ca*lam3**2*Sa**5*vev*vev2 + Ca**6*lam3**2*vev2**2 + 12*Ca**4*lam2*lam3*Sa**2*vev2**2 - 4*Ca**4*lam3**2*Sa**2*vev2**2 + 36*Ca**2*lam2**2*Sa**4*vev2**2 - 24*Ca**2*lam2*lam3*Sa**4*vev2**2 + 4*Ca**2*lam3**2*Sa**4*vev2**2)*cmath.sqrt(-4*Mh**2*MSd**2 + MSd**4))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.chi,P.chi):'((-4*Ca**2*Mchi**2*ychi**2 + Ca**2*MSd**2*ychi**2)*cmath.sqrt(-4*Mchi**2*MSd**2 + MSd**4))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((MSd**2*Sa**2*ytau**2 - 4*MTA**2*Sa**2*ytau**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MTA**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.t,P.t__tilde__):'((3*MSd**2*Sa**2*yt**2 - 12*MT**2*Sa**2*yt**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MT**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ee**4*Sa**2*vev**2)/(4.*sw**4) + (ee**4*MSd**4*Sa**2*vev**2)/(16.*MW**4*sw**4) - (ee**4*MSd**2*Sa**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MSd**4 - 4*MSd**2*MW**2))/(16.*cmath.pi*abs(MSd)**3)',
                                   (P.Z,P.Z):'(((9*ee**4*Sa**2*vev**2)/2. + (3*ee**4*MSd**4*Sa**2*vev**2)/(8.*MZ**4) - (3*ee**4*MSd**2*Sa**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*Sa**2*vev**2)/(4.*sw**4) + (cw**4*ee**4*MSd**4*Sa**2*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MSd**2*Sa**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*Sa**2*vev**2)/sw**2 + (cw**2*ee**4*MSd**4*Sa**2*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MSd**2*Sa**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*Sa**2*sw**2*vev**2)/cw**2 + (ee**4*MSd**4*Sa**2*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MSd**2*Sa**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*Sa**2*sw**4*vev**2)/(4.*cw**4) + (ee**4*MSd**4*Sa**2*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MSd**2*Sa**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MSd**4 - 4*MSd**2*MZ**2))/(32.*cmath.pi*abs(MSd)**3)',
                                   (P.Zp,P.Zp):'((192*Ca**2*gchi**4*gZp**4*vev2**2 + (16*Ca**2*gchi**4*gZp**4*MSd**4*vev2**2)/MZp**4 - (64*Ca**2*gchi**4*gZp**4*MSd**2*vev2**2)/MZp**2)*cmath.sqrt(MSd**4 - 4*MSd**2*MZp**2))/(32.*cmath.pi*abs(MSd)**3)'})

Decay_h = Decay(name = 'Decay_h',
                particle = P.h,
                partial_widths = {(P.Sd,P.Sd):'((Ca**6*lam3**2*vev**2 + 12*Ca**4*lam1*lam3*Sa**2*vev**2 - 4*Ca**4*lam3**2*Sa**2*vev**2 + 36*Ca**2*lam1**2*Sa**4*vev**2 - 24*Ca**2*lam1*lam3*Sa**4*vev**2 + 4*Ca**2*lam3**2*Sa**4*vev**2 - 12*Ca**5*lam2*lam3*Sa*vev*vev2 + 4*Ca**5*lam3**2*Sa*vev*vev2 - 72*Ca**3*lam1*lam2*Sa**3*vev*vev2 + 24*Ca**3*lam1*lam3*Sa**3*vev*vev2 + 24*Ca**3*lam2*lam3*Sa**3*vev*vev2 - 10*Ca**3*lam3**2*Sa**3*vev*vev2 - 12*Ca*lam1*lam3*Sa**5*vev*vev2 + 4*Ca*lam3**2*Sa**5*vev*vev2 + 36*Ca**4*lam2**2*Sa**2*vev2**2 - 24*Ca**4*lam2*lam3*Sa**2*vev2**2 + 4*Ca**4*lam3**2*Sa**2*vev2**2 + 12*Ca**2*lam2*lam3*Sa**4*vev2**2 - 4*Ca**2*lam3**2*Sa**4*vev2**2 + lam3**2*Sa**6*vev2**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MSd**2))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.chi,P.chi):'((-4*Mchi**2*Sa**2*ychi**2 + Mh**2*Sa**2*ychi**2)*cmath.sqrt(-4*Mchi**2*Mh**2 + Mh**4))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((Ca**2*Mh**2*ytau**2 - 4*Ca**2*MTA**2*ytau**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MTA**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.t,P.t__tilde__):'((3*Ca**2*Mh**2*yt**2 - 12*Ca**2*MT**2*yt**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MT**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*Ca**2*ee**4*vev**2)/(4.*sw**4) + (Ca**2*ee**4*Mh**4*vev**2)/(16.*MW**4*sw**4) - (Ca**2*ee**4*Mh**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(Mh**4 - 4*Mh**2*MW**2))/(16.*cmath.pi*abs(Mh)**3)',
                                  (P.Z,P.Z):'(((9*Ca**2*ee**4*vev**2)/2. + (3*Ca**2*ee**4*Mh**4*vev**2)/(8.*MZ**4) - (3*Ca**2*ee**4*Mh**2*vev**2)/(2.*MZ**2) + (3*Ca**2*cw**4*ee**4*vev**2)/(4.*sw**4) + (Ca**2*cw**4*ee**4*Mh**4*vev**2)/(16.*MZ**4*sw**4) - (Ca**2*cw**4*ee**4*Mh**2*vev**2)/(4.*MZ**2*sw**4) + (3*Ca**2*cw**2*ee**4*vev**2)/sw**2 + (Ca**2*cw**2*ee**4*Mh**4*vev**2)/(4.*MZ**4*sw**2) - (Ca**2*cw**2*ee**4*Mh**2*vev**2)/(MZ**2*sw**2) + (3*Ca**2*ee**4*sw**2*vev**2)/cw**2 + (Ca**2*ee**4*Mh**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (Ca**2*ee**4*Mh**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*Ca**2*ee**4*sw**4*vev**2)/(4.*cw**4) + (Ca**2*ee**4*Mh**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (Ca**2*ee**4*Mh**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(Mh**4 - 4*Mh**2*MZ**2))/(32.*cmath.pi*abs(Mh)**3)',
                                  (P.Zp,P.Zp):'((192*gchi**4*gZp**4*Sa**2*vev2**2 + (16*gchi**4*gZp**4*Mh**4*Sa**2*vev2**2)/MZp**4 - (64*gchi**4*gZp**4*Mh**2*Sa**2*vev2**2)/MZp**2)*cmath.sqrt(Mh**4 - 4*Mh**2*MZp**2))/(32.*cmath.pi*abs(Mh)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_Zp = Decay(name = 'Decay_Zp',
                 particle = P.Zp,
                 partial_widths = {(P.u,P.u__tilde__):'(MZp**2*(6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.c,P.c__tilde__):'(MZp**2*(6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.t,P.t__tilde__):'((-6*gqL**2*gZp**2*MT**2 + 36*gqL*gqR*gZp**2*MT**2 - 6*gqR**2*gZp**2*MT**2 + 6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2)*cmath.sqrt(-4*MT**2*MZp**2 + MZp**4))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.d,P.d__tilde__):'(MZp**2*(6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.s,P.s__tilde__):'(MZp**2*(6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.b,P.b__tilde__):'(MZp**2*(6*gqL**2*gZp**2*MZp**2 + 6*gqR**2*gZp**2*MZp**2))/(48.*cmath.pi*abs(MZp)**3)',
                                   (P.chi,P.chi):'((-16*gchi**2*Mchi**2 + 4*gchi**2*MZp**2)*cmath.sqrt(-4*Mchi**2*MZp**2 + MZp**4))/(96.*cmath.pi*abs(MZp)**3)'})

