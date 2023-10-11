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
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Exp/run_04_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 18.8705,
        'upper limit (fb)' : 113.85,
        'expected upper limit (fb)' : 76.4483,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 2100.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.1657488,
        'r_expected' : 0.24684,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 18.87049833127956}
    }
],
'Total xsec for missing topologies (fb)' : 57.57784,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 48.14388,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.717625,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.716339,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 76.44834,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 48.14388,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 18.8705,
        'SMS' : 'PV > (jet,jet)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.717625,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.716339,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}