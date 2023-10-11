"""
.. module:: ppZpjj  
   :synopsis: Defines the BSM particles to be used. Properties not defined here and defined by the LHE or SLHA input file (such as masses, width and BRs) are automatically added later.

.. moduleauthor:: Yoxara Villamziar <yoxarasv@gmail.com>

"""

from smodels.base.particle import Particle, MultiParticle

#label='Zprime
#Zprime = Particle(label='Zprime', isSM=False, pdg=9900032, eCharge = 0, colordim = 1, spin = 1, _isInvisible=False)
#Y1_particle = Particle(label='Y1', isSM=False, pdg=5000001, eCharge=0, colordim=1, spin=1, _isInvisible=False)
#xd_particle = Particle(label='xd', isSM=False, pdg=5000521, eCharge=0, colordim=1, spin=0.5, _isInvisible=True)

#Y1 = MultiParticle('Y1', [Y1_particle, Y1_particle.chargeConjugate('Y1')])
#xd = MultiParticle('xd', [xd_particle, xd_particle.chargeConjugate('xd')])

#BSMList = [Y1, xd]

Y1 = Particle(label='Y1', isSM=False, pdg=5000001, eCharge=0, colordim=1, spin=1, _isInvisible=False)

xd_particle = Particle(label='xd', isSM=False, pdg=5000521, eCharge=0, colordim=1, spin=0.5, _isInvisible=True)

xd_antiparticle = Particle(label='xd~', isSM=False, pdg=-5000521, eCharge=0, colordim=1, spin=0.5, _isInvisible=True)

BSMList = [Y1, xd_particle, xd_antiparticle]



#BSMparticleList = MultiParticle('BSM', BSMList)
