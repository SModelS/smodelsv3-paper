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
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Exp/run_03_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 22.61375,
        'upper limit (fb)' : 150.961,
        'expected upper limit (fb)' : 92.9507,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 2000.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.1497986,
        'r_expected' : 0.2432876,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 22.613749595722837}
    }
],
'Total xsec for missing topologies (fb)' : 70.33699,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 59.03199,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.653437,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.651563,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 92.95074,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 59.03199,
        'SMS' : 'PV > (MET)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 22.61375,
        'SMS' : 'PV > (jet,jet)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.653437,
        'SMS' : 'PV > (b,b)'
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.651563,
        'SMS' : 'PV > (t,t)'
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}