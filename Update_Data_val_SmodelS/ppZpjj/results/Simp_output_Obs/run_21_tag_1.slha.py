smodelsOutput = {
'OutputStatus' : {
    'sigmacut' : 0.001,
    'minmassgap' : 50,
    'maxcond' : 0.2,
    'ncpus' : 1,
    'model' : 'smodels.share.models.ppZpjj',
    'promptwidth' : 1e-11,
    'stablewidth' : 1e-25,
    'eraseprompt' : 'spin,eCharge,colordim',
    'checkinput' : True,
    'doinvisible' : True,
    'docompress' : True,
    'computestatistics' : True,
    'testcoverage' : True,
    'combinesrs' : False,
    'reportallsrs' : False,
    'experimentalfeatures' : False,
    'file status' : 1,
    'decomposition status' : 1,
    'warnings' : 'Input file ok',
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Obs/run_21_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'SMS Decomposition' : [
    {
        'ID' : 1,
        'SMS' : '(PV > inv)',
        'Masses (GeV)' : [('inv', 3800.0)],
        'PIDs' : [('inv', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 5.97}
    },
    {
        'ID' : 2,
        'SMS' : '(PV > Y1(1)), (Y1(1) > xd,xd~)',
        'Masses (GeV)' : [('Y1', 3800.0), ('xd', 1.0), ('xd~', 1.0)],
        'PIDs' : [
            ('Y1', 5000001),
            ('xd', 5000521),
            ('xd~', -5000521)
        ],
        'Weights (fb)' : {'xsec 13.0 TeV': 5.97}
    },
    {
        'ID' : 3,
        'SMS' : '(PV > Y1(1)), (Y1(1) > q,q)',
        'Masses (GeV)' : [('Y1', 3800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 9.81}
    },
    {
        'ID' : 4,
        'SMS' : '(PV > Y1(1)), (Y1(1) > c,c)',
        'Masses (GeV)' : [('Y1', 3800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 3.27}
    },
    {
        'ID' : 5,
        'SMS' : '(PV > Y1(1)), (Y1(1) > t-,t+)',
        'Masses (GeV)' : [('Y1', 3800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 3.27}
    },
    {
        'ID' : 6,
        'SMS' : '(PV > Y1(1)), (Y1(1) > b,b)',
        'Masses (GeV)' : [('Y1', 3800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 3.27}
    }
],
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 13.08484,
        'upper limit (fb)' : 25.5942,
        'expected upper limit (fb)' : 13.032,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 3800.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.5112423,
        'r_expected' : 1.004055,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 13.084838316987835}
    }
],
'Total xsec for missing topologies (fb)' : 12.50932,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.966988,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 3.27121,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 3.271125,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 25.59416,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 13.08484,
        'SMS' : 'PV > (jet,jet)',
        'SMS IDs' : [3, 4]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 5.966988,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 3.27121,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 3.271125,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}