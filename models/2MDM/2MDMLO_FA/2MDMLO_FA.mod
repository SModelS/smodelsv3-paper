(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)
(*                                                                             *)
(*         This file has been automatically generated by FeynRules.            *)
(*                                                                             *)
(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)


FR$ModelInformation={
  ModelName->"2MDM",
  Authors -> {"Yoxara Villamizar"},
  Emails -> {"yoxarasv@sprace,org.br"},
  Date -> "08.04.2022",
  Version -> "1",
  URLs -> ""};

FR$ClassesTranslation={};

FR$InteractionOrderPerturbativeExpansion={{QCD, 0}, {QED, 0}, {NP, 0}};

FR$GoldstoneList={S[2], S[3], S[5]};

(*     Declared indices    *)

IndexRange[ Index[Gluon] ] = NoUnfold[ Range[ 8 ] ]

IndexRange[ Index[SU2W] ] = Range[ 3 ]

IndexRange[ Index[Generation] ] = Range[ 3 ]

IndexRange[ Index[Colour] ] = NoUnfold[ Range[ 3 ] ]

IndexRange[ Index[SU2D] ] = Range[ 2 ]

(*     Declared particles    *)

M$ClassesDescription = {
V[1] == {
    SelfConjugate -> True,
    PropagatorLabel -> "a",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> 0,
    Indices -> {} },

V[2] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Z",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {} },

V[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorLabel -> "W",
    PropagatorType -> Sine,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

V[4] == {
    SelfConjugate -> True,
    Indices -> {Index[Gluon]},
    PropagatorLabel -> "G",
    PropagatorType -> Cycles,
    PropagatorArrow -> None,
    Mass -> 0 },

U[1] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uA",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0,
    Indices -> {} },

U[2] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uZ",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MZ,
    Indices -> {} },

U[31] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, Q},
    PropagatorLabel -> "uWp",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

U[32] == {
    SelfConjugate -> False,
    QuantumNumbers -> {GhostNumber, -Q},
    PropagatorLabel -> "uWm",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MW,
    Indices -> {} },

U[4] == {
    SelfConjugate -> False,
    Indices -> {Index[Gluon]},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uG",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> 0 },

V[5] == {
    SelfConjugate -> True,
    Indices -> {},
    PropagatorLabel -> "Zp",
    PropagatorType -> Sine,
    PropagatorArrow -> None,
    Mass -> MZp },

U[5] == {
    SelfConjugate -> False,
    Indices -> {},
    QuantumNumbers -> {GhostNumber},
    PropagatorLabel -> "uZp",
    PropagatorType -> GhostDash,
    PropagatorArrow -> Forward,
    Mass -> MZp },

F[1] == {
    Indices -> {Index[Generation]},
    SelfConjugate -> False,
    QuantumNumbers -> {LeptonNumber},
    PropagatorLabel -> "v",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> 0 },

F[2] == {
    Indices -> {Index[Generation]},
    SelfConjugate -> False,
    QuantumNumbers -> {-Q, LeptonNumber},
    PropagatorLabel -> "l",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Ml },

F[3] == {
    Indices -> {Index[Generation], Index[Colour]},
    SelfConjugate -> False,
    QuantumNumbers -> {(2*Q)/3},
    PropagatorLabel -> "uq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Mu },

F[4] == {
    Indices -> {Index[Generation], Index[Colour]},
    SelfConjugate -> False,
    QuantumNumbers -> {-Q/3},
    PropagatorLabel -> "dq",
    PropagatorType -> Straight,
    PropagatorArrow -> Forward,
    Mass -> Md },

S[1] == {
    SelfConjugate -> True,
    PropagatorLabel -> "h",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> Mh,
    Indices -> {} },

S[2] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Go",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MZ,
    Indices -> {} },

S[3] == {
    SelfConjugate -> False,
    QuantumNumbers -> {Q},
    PropagatorLabel -> "GP",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MW,
    Indices -> {} },

S[4] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Sd",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MSd,
    Indices -> {} },

S[5] == {
    SelfConjugate -> True,
    PropagatorLabel -> "Phip",
    PropagatorType -> ScalarDash,
    PropagatorArrow -> None,
    Mass -> MZp,
    Indices -> {} },

F[7] == {
    SelfConjugate -> True,
    PropagatorLabel -> "chi",
    PropagatorType -> Straight,
    PropagatorArrow -> None*PDG -> {9910012},
    Mass -> Mchi,
    Indices -> {} }
}


(*        Definitions       *)

GaugeXi[ V[1] ] = GaugeXi[A];
GaugeXi[ V[2] ] = GaugeXi[Z];
GaugeXi[ V[3] ] = GaugeXi[W];
GaugeXi[ V[4] ] = GaugeXi[G];
GaugeXi[ U[1] ] = GaugeXi[A];
GaugeXi[ U[2] ] = GaugeXi[Z];
GaugeXi[ U[31] ] = GaugeXi[W];
GaugeXi[ U[32] ] = GaugeXi[W];
GaugeXi[ U[4] ] = GaugeXi[G];
GaugeXi[ S[1] ] = 1;
GaugeXi[ S[2] ] = GaugeXi[Z];
GaugeXi[ S[3] ] = GaugeXi[W];

MZ[ ___ ] := MZ;
MW[ ___ ] := MW;
MZp[ ___ ] := MZp;
Ml[ 1 ] := Me;
Ml[ 2 ] := MMU;
Ml[ 3 ] := MTA;
Mu[ 1, _ ] := MU;
Mu[ 1 ] := MU;
Mu[ 2, _ ] := MC;
Mu[ 2 ] := MC;
Mu[ 3, _ ] := MT;
Mu[ 3 ] := MT;
Md[ 1, _ ] := MD;
Md[ 1 ] := MD;
Md[ 2, _ ] := MS;
Md[ 2 ] := MS;
Md[ 3, _ ] := MB;
Md[ 3 ] := MB;
Mh[ ___ ] := Mh;
MSd[ ___ ] := MSd;
Mchi[ ___ ] := Mchi;


TheLabel[ V[4, {__}] ] := TheLabel[V[4]];
TheLabel[ U[4, {__}] ] := TheLabel[U[4]];
TheLabel[ F[1, {1}] ] := "ve";
TheLabel[ F[1, {2}] ] := "vm";
TheLabel[ F[1, {3}] ] := "vt";
TheLabel[ F[2, {1}] ] := "e";
TheLabel[ F[2, {2}] ] := "mu";
TheLabel[ F[2, {3}] ] := "ta";
TheLabel[ F[3, {1, _}] ] := "u";
TheLabel[ F[3, {1}] ] := "u";
TheLabel[ F[3, {2, _}] ] := "c";
TheLabel[ F[3, {2}] ] := "c";
TheLabel[ F[3, {3, _}] ] := "t";
TheLabel[ F[3, {3}] ] := "t";
TheLabel[ F[4, {1, _}] ] := "d";
TheLabel[ F[4, {1}] ] := "d";
TheLabel[ F[4, {2, _}] ] := "s";
TheLabel[ F[4, {2}] ] := "s";
TheLabel[ F[4, {3, _}] ] := "b";
TheLabel[ F[4, {3}] ] := "b";


(*      Couplings (calculated by FeynRules)      *)

M$CouplingMatrices = {

C[ S[2] , S[2] , S[2] , S[2] ] == {{(-6*I)*lam1, 0}},

C[ S[2] , S[2] , S[3] , -S[3] ] == {{(-2*I)*lam1, 0}},

C[ S[3] , S[3] , -S[3] , -S[3] ] == {{(-4*I)*lam1, 0}},

C[ S[2] , S[2] , S[1] , S[1] ] == {{(-I)*(2*cosa^2*lam1 + lam3*sina^2), 0}},

C[ S[3] , -S[3] , S[1] , S[1] ] == {{(-I)*(2*cosa^2*lam1 + lam3*sina^2), 0}},

C[ S[1] , S[1] , S[1] , S[1] ] == {{(-6*I)*(cosa^4*lam1 + cosa^2*lam3*sina^2 + lam2*sina^4), 0}},

C[ S[2] , S[2] , S[5] , S[5] ] == {{(-I)*lam3, 0}},

C[ S[3] , -S[3] , S[5] , S[5] ] == {{(-I)*lam3, 0}},

C[ S[1] , S[1] , S[5] , S[5] ] == {{(-I)*(cosa^2*lam3 + 2*lam2*sina^2), 0}},

C[ S[5] , S[5] , S[5] , S[5] ] == {{(-6*I)*lam2, 0}},

C[ S[2] , S[2] , S[4] , S[4] ] == {{(-I)*(cosa^2*lam3 + 2*lam1*sina^2), 0}},

C[ S[3] , -S[3] , S[4] , S[4] ] == {{(-I)*(cosa^2*lam3 + 2*lam1*sina^2), 0}},

C[ S[1] , S[1] , S[4] , S[4] ] == {{(-I)*(cosa^4*lam3 + 2*cosa^2*(3*lam1 + 3*lam2 - 2*lam3)*sina^2 + lam3*sina^4), 0}},

C[ S[5] , S[5] , S[4] , S[4] ] == {{(-I)*(2*cosa^2*lam2 + lam3*sina^2), 0}},

C[ S[4] , S[4] , S[4] , S[4] ] == {{(-6*I)*(cosa^4*lam2 + cosa^2*lam3*sina^2 + lam1*sina^4), 0}},

C[ S[2] , S[2] , S[1] , S[4] ] == {{(-I)*cosa*(2*lam1 - lam3)*sina, 0}},

C[ S[3] , -S[3] , S[1] , S[4] ] == {{(-I)*cosa*(2*lam1 - lam3)*sina, 0}},

C[ S[1] , S[1] , S[1] , S[4] ] == {{(-3*I)*cosa*sina*(cosa^2*(2*lam1 - lam3) + (-2*lam2 + lam3)*sina^2), 0}},

C[ S[1] , S[5] , S[5] , S[4] ] == {{I*cosa*(2*lam2 - lam3)*sina, 0}},

C[ S[1] , S[4] , S[4] , S[4] ] == {{(3*I)*cosa*sina*(cosa^2*(2*lam2 - lam3) + (-2*lam1 + lam3)*sina^2), 0}},

C[ S[2] , S[2] , S[1] ] == {{(-2*I)*cosa*lam1*vev + I*lam3*sina*vev2, 0}},

C[ S[3] , -S[3] , S[1] ] == {{(-2*I)*cosa*lam1*vev + I*lam3*sina*vev2, 0}},

C[ S[1] , S[1] , S[1] ] == {{(-3*I)*(2*cosa^3*lam1*vev + cosa*lam3*sina^2*vev - cosa^2*lam3*sina*vev2 - 2*lam2*sina^3*vev2), 0}},

C[ S[1] , S[5] , S[5] ] == {{(-I)*(cosa*lam3*vev - 2*lam2*sina*vev2), 0}},

C[ S[1] , S[4] , S[4] ] == {{(-I)*(cosa^3*lam3*vev + 2*cosa*(3*lam1 - lam3)*sina^2*vev + 2*cosa^2*(-3*lam2 + lam3)*sina*vev2 - lam3*sina^3*vev2), 0}},

C[ S[2] , S[2] , S[4] ] == {{(-I)*(2*lam1*sina*vev + cosa*lam3*vev2), 0}},

C[ S[3] , -S[3] , S[4] ] == {{(-I)*(2*lam1*sina*vev + cosa*lam3*vev2), 0}},

C[ S[1] , S[1] , S[4] ] == {{(-I)*(2*cosa^2*(3*lam1 - lam3)*sina*vev + lam3*sina^3*vev + cosa^3*lam3*vev2 + 2*cosa*(3*lam2 - lam3)*sina^2*vev2), 0}},

C[ S[5] , S[5] , S[4] ] == {{(-I)*(lam3*sina*vev + 2*cosa*lam2*vev2), 0}},

C[ S[4] , S[4] , S[4] ] == {{(-3*I)*(cosa^2*lam3*sina*vev + 2*lam1*sina^3*vev + 2*cosa^3*lam2*vev2 + cosa*lam3*sina^2*vev2), 0}},

C[ S[3] , -S[3] , V[1] , V[1] ] == {{(2*I)*EL^2, 0}},

C[ S[3] , -S[3] , V[1] ] == {{(-I)*gc32, 0}, {I*gc32, 0}},

C[ -U[1] , U[32] , V[3] ] == {{I*gc33, 0}, {I*gc33, 0}, {0, 0}},

C[ -U[1] , U[31] , -V[3] ] == {{I*gc34, 0}, {I*gc34, 0}, {0, 0}},

C[ -S[3] , -U[32] , U[1] ] == {{(EL^2*vev)/(2*sw), 0}},

C[ -U[32] , U[1] , -V[3] ] == {{I*gc36, 0}, {I*gc36, 0}, {0, 0}},

C[ S[2] , -U[32] , U[32] ] == {{-(EL^2*vev)/(4*sw^2), 0}},

C[ S[1] , -U[32] , U[32] ] == {{((-I/4)*cosa*EL^2*vev)/sw^2, 0}},

C[ S[4] , -U[32] , U[32] ] == {{((-I/4)*EL^2*sina*vev)/sw^2, 0}},

C[ -U[32] , U[32] , V[1] ] == {{I*gc40, 0}, {I*gc40, 0}, {0, 0}},

C[ -U[32] , U[32] , V[2] ] == {{I*gc41, 0}, {I*gc41, 0}, {0, 0}},

C[ -S[3] , -U[32] , U[2] ] == {{(EL^2*(cw - sw)*(cw + sw)*vev)/(4*cw*sw^2), 0}},

C[ -U[32] , U[2] , -V[3] ] == {{I*gc43, 0}, {I*gc43, 0}, {0, 0}},

C[ S[3] , -U[31] , U[1] ] == {{-(EL^2*vev)/(2*sw), 0}},

C[ -U[31] , U[1] , V[3] ] == {{I*gc45, 0}, {I*gc45, 0}, {0, 0}},

C[ S[2] , -U[31] , U[31] ] == {{(EL^2*vev)/(4*sw^2), 0}},

C[ S[1] , -U[31] , U[31] ] == {{((-I/4)*cosa*EL^2*vev)/sw^2, 0}},

C[ S[4] , -U[31] , U[31] ] == {{((-I/4)*EL^2*sina*vev)/sw^2, 0}},

C[ -U[31] , U[31] , V[1] ] == {{I*gc49, 0}, {I*gc49, 0}, {0, 0}},

C[ -U[31] , U[31] , V[2] ] == {{I*gc50, 0}, {I*gc50, 0}, {0, 0}},

C[ S[3] , -U[31] , U[2] ] == {{-(EL^2*(cw - sw)*(cw + sw)*vev)/(4*cw*sw^2), 0}},

C[ -U[31] , U[2] , V[3] ] == {{I*gc52, 0}, {I*gc52, 0}, {0, 0}},

C[ S[3] , -U[2] , U[32] ] == {{(EL^2*(cw^2 + sw^2)*vev)/(4*cw*sw^2), 0}},

C[ -U[2] , U[32] , V[3] ] == {{I*gc54, 0}, {I*gc54, 0}, {0, 0}},

C[ -S[3] , -U[2] , U[31] ] == {{-(EL^2*(cw^2 + sw^2)*vev)/(4*cw*sw^2), 0}},

C[ -U[2] , U[31] , -V[3] ] == {{I*gc56, 0}, {I*gc56, 0}, {0, 0}},

C[ S[1] , -U[2] , U[2] ] == {{((-I/4)*cosa*EL^2*(cw^2 + sw^2)^2*vev)/(cw^2*sw^2), 0}},

C[ S[4] , -U[2] , U[2] ] == {{((-I/4)*EL^2*sina*(cw^2 + sw^2)^2*vev)/(cw^2*sw^2), 0}},

C[ -U[4, {e1x1}] , U[4, {e2x1}] , V[4, {e3x2}] ] == {{gc59*SUNF[e3x2, e1x1, e2x1], 0}, {gc59*SUNF[e3x2, e1x1, e2x1], 0}, {0, 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] ] == {{-(gc60*SUNF[e1x2, e2x2, e3x2]), 0}, {gc60*SUNF[e1x2, e2x2, e3x2], 0}, {gc60*SUNF[e1x2, e2x2, e3x2], 0}, {-(gc60*SUNF[e1x2, e2x2, e3x2]), 0}, {-(gc60*SUNF[e1x2, e2x2, e3x2]), 0}, {gc60*SUNF[e1x2, e2x2, e3x2], 0}},

C[ V[4, {e1x2}] , V[4, {e2x2}] , V[4, {e3x2}] , V[4, {e4x2}] ] == {{(-I)*gc61*(SUNF[e1x2, e2x2, e3x2, e4x2] + SUNF[e1x2, e3x2, e2x2, e4x2]), 0}, {I*gc61*(SUNF[e1x2, e2x2, e3x2, e4x2] - SUNF[e1x2, e4x2, e2x2, e3x2]), 0}, {I*gc61*(SUNF[e1x2, e3x2, e2x2, e4x2] + SUNF[e1x2, e4x2, e2x2, e3x2]), 0}},

C[ F[7] , F[7] , S[5] ] == {{gc62L, 0}, {gc62R, 0}},

C[ F[7] , F[7] , S[4] ] == {{I*gc63, 0}, {I*gc63, 0}},

C[ F[7] , F[7] , S[1] ] == {{I*gc64, 0}, {I*gc64, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , -S[3] ] == {{gc65L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc65R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[2] ] == {{gc66L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc66R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[1] ] == {{I*gc67L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc67R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[4] ] == {{I*gc68L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc68R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[2, {e1x2}] , F[1, {e2x2}] , -S[3] ] == {{gc69[e1x2, e2x2], 0}, {0, 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[2] ] == {{gc70L[e1x2, e2x2], 0}, {gc70R[e1x2, e2x2], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[1] ] == {{I*gc71L[e1x2, e2x2], 0}, {I*gc71R[e1x2, e2x2], 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , S[4] ] == {{I*gc72L[e1x2, e2x2], 0}, {I*gc72R[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , S[3] ] == {{gc73L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc73R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[2] ] == {{gc74L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {gc74R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[1] ] == {{I*gc75L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc75R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , S[4] ] == {{I*gc76L[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc76R[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ S[2] , -S[3] , V[1] , V[3] ] == {{((-I/2)*EL^2)/sw, 0}},

C[ -S[3] , S[1] , V[1] , V[3] ] == {{-(cosa*EL^2)/(2*sw), 0}},

C[ -S[3] , S[4] , V[1] , V[3] ] == {{-(EL^2*sina)/(2*sw), 0}},

C[ -S[3] , V[1] , V[3] ] == {{-(EL^2*vev)/(2*sw), 0}},

C[ S[2] , -S[3] , V[3] ] == {{(-I)*gc81, 0}, {I*gc81, 0}},

C[ -S[3] , S[1] , V[3] ] == {{-gc82, 0}, {gc82, 0}},

C[ -S[3] , S[4] , V[3] ] == {{-gc83, 0}, {gc83, 0}},

C[ V[1] , V[3] , -V[3] ] == {{(-I)*gc84, 0}, {I*gc84, 0}, {I*gc84, 0}, {(-I)*gc84, 0}, {(-I)*gc84, 0}, {I*gc84, 0}},

C[ S[2] , S[3] , V[1] , -V[3] ] == {{((-I/2)*EL^2)/sw, 0}},

C[ S[3] , S[1] , V[1] , -V[3] ] == {{(cosa*EL^2)/(2*sw), 0}},

C[ S[3] , S[4] , V[1] , -V[3] ] == {{(EL^2*sina)/(2*sw), 0}},

C[ S[3] , V[1] , -V[3] ] == {{(EL^2*vev)/(2*sw), 0}},

C[ S[2] , S[3] , -V[3] ] == {{(-I)*gc89, 0}, {I*gc89, 0}},

C[ S[3] , S[1] , -V[3] ] == {{-gc90, 0}, {gc90, 0}},

C[ S[3] , S[4] , -V[3] ] == {{-gc91, 0}, {gc91, 0}},

C[ S[2] , S[2] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[3] , -S[3] , V[3] , -V[3] ] == {{((I/2)*EL^2)/sw^2, 0}},

C[ S[1] , S[1] , V[3] , -V[3] ] == {{((I/2)*cosa^2*EL^2)/sw^2, 0}},

C[ S[1] , S[4] , V[3] , -V[3] ] == {{((I/2)*cosa*EL^2*sina)/sw^2, 0}},

C[ S[4] , S[4] , V[3] , -V[3] ] == {{((I/2)*EL^2*sina^2)/sw^2, 0}},

C[ S[1] , V[3] , -V[3] ] == {{((I/2)*cosa*EL^2*vev)/sw^2, 0}},

C[ S[4] , V[3] , -V[3] ] == {{((I/2)*EL^2*sina*vev)/sw^2, 0}},

C[ V[1] , V[1] , V[3] , -V[3] ] == {{(-I)*gc99, 0}, {(-I)*gc99, 0}, {(2*I)*gc99, 0}},

C[ V[3] , -V[3] , V[2] ] == {{(-I)*gc100, 0}, {I*gc100, 0}, {I*gc100, 0}, {(-I)*gc100, 0}, {(-I)*gc100, 0}, {I*gc100, 0}},

C[ V[3] , V[3] , -V[3] , -V[3] ] == {{(-I)*gc101, 0}, {(-I)*gc101, 0}, {(2*I)*gc101, 0}},

C[ -F[1, {e1x2}] , F[2, {e2x2}] , S[3] ] == {{0, 0}, {gc102R[e1x2, e2x2], 0}},

C[ S[3] , -S[3] , V[1] , V[2] ] == {{(I*EL^2*(cw - sw)*(cw + sw))/(cw*sw), 0}},

C[ S[2] , S[1] , V[2] ] == {{-gc104, 0}, {gc104, 0}},

C[ S[2] , S[4] , V[2] ] == {{-gc105, 0}, {gc105, 0}},

C[ S[3] , -S[3] , V[2] ] == {{(-I)*gc106, 0}, {I*gc106, 0}},

C[ S[2] , -S[3] , V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ -S[3] , S[1] , V[3] , V[2] ] == {{(cosa*EL^2)/(2*cw), 0}},

C[ -S[3] , S[4] , V[3] , V[2] ] == {{(EL^2*sina)/(2*cw), 0}},

C[ -S[3] , V[3] , V[2] ] == {{(EL^2*vev)/(2*cw), 0}},

C[ S[2] , S[3] , -V[3] , V[2] ] == {{((I/2)*EL^2)/cw, 0}},

C[ S[3] , S[1] , -V[3] , V[2] ] == {{-(cosa*EL^2)/(2*cw), 0}},

C[ S[3] , S[4] , -V[3] , V[2] ] == {{-(EL^2*sina)/(2*cw), 0}},

C[ S[3] , -V[3] , V[2] ] == {{-(EL^2*vev)/(2*cw), 0}},

C[ V[1] , V[3] , -V[3] , V[2] ] == {{(-2*I)*gc115, 0}, {I*gc115, 0}, {I*gc115, 0}},

C[ S[2] , S[2] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[3] , -S[3] , V[2] , V[2] ] == {{((I/2)*EL^2*(cw - sw)^2*(cw + sw)^2)/(cw^2*sw^2), 0}},

C[ S[1] , S[1] , V[2] , V[2] ] == {{((I/2)*cosa^2*EL^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[1] , S[4] , V[2] , V[2] ] == {{((I/2)*cosa*EL^2*sina*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[4] , S[4] , V[2] , V[2] ] == {{((I/2)*EL^2*sina^2*(cw^2 + sw^2)^2)/(cw^2*sw^2), 0}},

C[ S[1] , V[2] , V[2] ] == {{((I/2)*cosa*EL^2*(cw^2 + sw^2)^2*vev)/(cw^2*sw^2), 0}},

C[ S[4] , V[2] , V[2] ] == {{((I/2)*EL^2*sina*(cw^2 + sw^2)^2*vev)/(cw^2*sw^2), 0}},

C[ V[3] , -V[3] , V[2] , V[2] ] == {{(-I)*gc123, 0}, {(-I)*gc123, 0}, {(2*I)*gc123, 0}},

C[ S[1] , S[5] , V[5] ] == {{-gc124, 0}, {gc124, 0}},

C[ S[5] , S[4] , V[5] ] == {{-gc125, 0}, {gc125, 0}},

C[ S[5] , S[5] , V[5] , V[5] ] == {{(2*I)*gZp^2*QBphi^2, 0}},

C[ S[4] , S[4] , V[5] , V[5] ] == {{(2*I)*cosa^2*gZp^2*QBphi^2, 0}},

C[ S[1] , S[4] , V[5] , V[5] ] == {{(-2*I)*cosa*gZp^2*QBphi^2*sina, 0}},

C[ S[1] , S[1] , V[5] , V[5] ] == {{(2*I)*gZp^2*QBphi^2*sina^2, 0}},

C[ S[4] , V[5] , V[5] ] == {{(2*I)*cosa*gZp^2*QBphi^2*vev2, 0}},

C[ S[1] , V[5] , V[5] ] == {{(-2*I)*gZp^2*QBphi^2*sina*vev2, 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[1] ] == {{I*gc132*IndexDelta[e1x2, e2x2], 0}, {I*gc132*IndexDelta[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[1] ] == {{I*gc133*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc133*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[1] ] == {{I*gc134*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc134*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc135*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc135*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[4, {e3x2}] ] == {{I*gc136*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}, {I*gc136*IndexDelta[e1x2, e2x2]*SUNT[e3x2, e1x3, e2x3], 0}},

C[ -F[3, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[3] ] == {{I*gc137[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[4, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , -V[3] ] == {{I*gc138[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {0, 0}},

C[ -F[1, {e1x2}] , F[2, {e2x2}] , V[3] ] == {{I*gc139*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[2, {e1x2}] , F[1, {e2x2}] , -V[3] ] == {{I*gc140*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[2] ] == {{I*gc141L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc141R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[2] ] == {{I*gc142L*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc142R*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[1, {e1x2}] , F[1, {e2x2}] , V[2] ] == {{I*gc143*IndexDelta[e1x2, e2x2], 0}, {0, 0}},

C[ -F[2, {e1x2}] , F[2, {e2x2}] , V[2] ] == {{I*gc144L*IndexDelta[e1x2, e2x2], 0}, {I*gc144R*IndexDelta[e1x2, e2x2], 0}},

C[ -F[3, {e1x2, e1x3}] , F[3, {e2x2, e2x3}] , V[5] ] == {{I*gc145*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc145*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ -F[4, {e1x2, e1x3}] , F[4, {e2x2, e2x3}] , V[5] ] == {{I*gc146*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}, {I*gc146*IndexDelta[e1x2, e2x2]*IndexDelta[e1x3, e2x3], 0}},

C[ F[7] , F[7] , V[5] ] == {{I*gc147L, 0}, {I*gc147R, 0}}

}

(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)

(* Parameter replacement lists (These lists were created by FeynRules) *)

(* FA Couplings *)

M$FACouplings = {
     gc32 -> -EL,
     gc33 -> EL,
     gc34 -> -EL,
     gc36 -> EL,
     gc40 -> -EL,
     gc41 -> -((cw*EL)/sw),
     gc43 -> (cw*EL)/sw,
     gc45 -> -EL,
     gc49 -> EL,
     gc50 -> (cw*EL)/sw,
     gc52 -> -((cw*EL)/sw),
     gc54 -> (cw*EL)/sw,
     gc56 -> -((cw*EL)/sw),
     gc59 -> GS,
     gc60 -> -GS,
     gc61 -> -GS^2,
     gc62L -> ychi/Sqrt[2],
     gc62R -> -(ychi/Sqrt[2]),
     gc63 -> -((cosa*ychi)/Sqrt[2]),
     gc64 -> (sina*ychi)/Sqrt[2],
     gc65L[e1x2_, e2x2_] -> IndexSum[Conjugate[CKM[e2x2, Generation$1]]*Conjugate[yd[Generation$1, e1x2]], {Generation$1, 1, 3}],
     gc65R[e1x2_, e2x2_] -> -IndexSum[Conjugate[CKM[Generation$1, e1x2]]*yu[Generation$1, e2x2], {Generation$1, 1, 3}],
     gc66L[e1x2_, e2x2_] -> -(Conjugate[yd[e2x2, e1x2]]/Sqrt[2]),
     gc66R[e1x2_, e2x2_] -> yd[e1x2, e2x2]/Sqrt[2],
     gc67L[e1x2_, e2x2_] -> -((cosa*Conjugate[yd[e2x2, e1x2]])/Sqrt[2]),
     gc67R[e1x2_, e2x2_] -> -((cosa*yd[e1x2, e2x2])/Sqrt[2]),
     gc68L[e1x2_, e2x2_] -> -((sina*Conjugate[yd[e2x2, e1x2]])/Sqrt[2]),
     gc68R[e1x2_, e2x2_] -> -((sina*yd[e1x2, e2x2])/Sqrt[2]),
     gc69[e1x2_, e2x2_] -> Conjugate[yl[e2x2, e1x2]],
     gc70L[e1x2_, e2x2_] -> -(Conjugate[yl[e2x2, e1x2]]/Sqrt[2]),
     gc70R[e1x2_, e2x2_] -> yl[e1x2, e2x2]/Sqrt[2],
     gc71L[e1x2_, e2x2_] -> -((cosa*Conjugate[yl[e2x2, e1x2]])/Sqrt[2]),
     gc71R[e1x2_, e2x2_] -> -((cosa*yl[e1x2, e2x2])/Sqrt[2]),
     gc72L[e1x2_, e2x2_] -> -((sina*Conjugate[yl[e2x2, e1x2]])/Sqrt[2]),
     gc72R[e1x2_, e2x2_] -> -((sina*yl[e1x2, e2x2])/Sqrt[2]),
     gc73L[e1x2_, e2x2_] -> IndexSum[CKM[Generation$1, e2x2]*Conjugate[yu[Generation$1, e1x2]], {Generation$1, 1, 3}],
     gc73R[e1x2_, e2x2_] -> -IndexSum[CKM[e1x2, Generation$1]*yd[Generation$1, e2x2], {Generation$1, 1, 3}],
     gc74L[e1x2_, e2x2_] -> Conjugate[yu[e2x2, e1x2]]/Sqrt[2],
     gc74R[e1x2_, e2x2_] -> -(yu[e1x2, e2x2]/Sqrt[2]),
     gc75L[e1x2_, e2x2_] -> -((cosa*Conjugate[yu[e2x2, e1x2]])/Sqrt[2]),
     gc75R[e1x2_, e2x2_] -> -((cosa*yu[e1x2, e2x2])/Sqrt[2]),
     gc76L[e1x2_, e2x2_] -> -((sina*Conjugate[yu[e2x2, e1x2]])/Sqrt[2]),
     gc76R[e1x2_, e2x2_] -> -((sina*yu[e1x2, e2x2])/Sqrt[2]),
     gc81 -> EL/(2*sw),
     gc82 -> -(cosa*EL)/(2*sw),
     gc83 -> -(EL*sina)/(2*sw),
     gc84 -> EL,
     gc89 -> -EL/(2*sw),
     gc90 -> -(cosa*EL)/(2*sw),
     gc91 -> -(EL*sina)/(2*sw),
     gc99 -> -EL^2,
     gc100 -> (cw*EL)/sw,
     gc101 -> EL^2/sw^2,
     gc102R[e1x2_, e2x2_] -> -yl[e1x2, e2x2],
     gc104 -> -(cosa*EL*(cw^2 + sw^2))/(2*cw*sw),
     gc105 -> -(EL*sina*(cw^2 + sw^2))/(2*cw*sw),
     gc106 -> -(cw*EL)/(2*sw) + (EL*sw)/(2*cw),
     gc115 -> (cw*EL^2)/sw,
     gc123 -> -((cw^2*EL^2)/sw^2),
     gc124 -> gZp*QBphi*sina,
     gc125 -> cosa*gZp*QBphi,
     gc132 -> -EL,
     gc133 -> (2*EL)/3,
     gc134 -> -EL/3,
     gc135 -> GS,
     gc136 -> GS,
     gc137[e1x2_, e2x2_] -> (EL*CKM[e1x2, e2x2])/(Sqrt[2]*sw),
     gc138[e1x2_, e2x2_] -> (EL*Conjugate[CKM[e2x2, e1x2]])/(Sqrt[2]*sw),
     gc139 -> EL/(Sqrt[2]*sw),
     gc140 -> EL/(Sqrt[2]*sw),
     gc141L -> (cw*EL)/(2*sw) - (EL*sw)/(6*cw),
     gc141R -> (-2*EL*sw)/(3*cw),
     gc142L -> -(EL*(3*cw^2 + sw^2))/(6*cw*sw),
     gc142R -> (EL*sw)/(3*cw),
     gc143 -> (EL*(cw^2 + sw^2))/(2*cw*sw),
     gc144L -> -(EL*(cw^2 - sw^2))/(2*cw*sw),
     gc144R -> (EL*sw)/cw,
     gc145 -> gZp*QBq,
     gc146 -> gZp*QBq,
     gc147L -> gchi,
     gc147R -> -gchi};

