smodelsOutput = {
'OutputStatus' : {
    'sigmacut' : 0.001,
    'minmassgap' : 50,
    'maxcond' : 0.2,
    'ncpus' : 1,
    'model' : 'smodels.share.models.ppZpjj',
    'checkinput' : True,
    'doinvisible' : True,
    'docompress' : True,
    'computestatistics' : True,
    'testcoverage' : True,
    'combinesrs' : False,
    'file status' : 1,
    'decomposition status' : 1,
    'warnings' : 'Input file ok',
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Exp/run_09_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 10.4592,
        'upper limit (fb)' : 45.076,
        'expected upper limit (fb)' : 36.1819,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 2600.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.2320347,
        'r_expected' : 0.2890726,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 10.459197661397047}
    }
],
'Total xsec for missing topologies (fb)' : 25.72265,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 20.49336,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.614799,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.614497,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 36.18185,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 20.49336,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 10.4592,
        'SMS' : 'PV > (jet,jet)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.614799,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.614497,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}