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
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Obs/run_11_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'SMS Decomposition' : [
    {
        'ID' : 1,
        'SMS' : '(PV > inv)',
        'Masses (GeV)' : [('inv', 2800.0)],
        'PIDs' : [('inv', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 21.9}
    },
    {
        'ID' : 2,
        'SMS' : '(PV > Y1(1)), (Y1(1) > xd,xd~)',
        'Masses (GeV)' : [('Y1', 2800.0), ('xd', 1.0), ('xd~', 1.0)],
        'PIDs' : [
            ('Y1', 5000001),
            ('xd', 5000521),
            ('xd~', -5000521)
        ],
        'Weights (fb)' : {'xsec 13.0 TeV': 21.9}
    },
    {
        'ID' : 3,
        'SMS' : '(PV > Y1(1)), (Y1(1) > q,q)',
        'Masses (GeV)' : [('Y1', 2800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 13.9}
    },
    {
        'ID' : 4,
        'SMS' : '(PV > Y1(1)), (Y1(1) > c,c)',
        'Masses (GeV)' : [('Y1', 2800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 4.65}
    },
    {
        'ID' : 5,
        'SMS' : '(PV > Y1(1)), (Y1(1) > t-,t+)',
        'Masses (GeV)' : [('Y1', 2800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 4.64}
    },
    {
        'ID' : 6,
        'SMS' : '(PV > Y1(1)), (Y1(1) > b,b)',
        'Masses (GeV)' : [('Y1', 2800.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 4.65}
    }
],
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 18.58155,
        'upper limit (fb)' : 49.7499,
        'expected upper limit (fb)' : 27.7742,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 2800.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.3734992,
        'r_expected' : 0.669022,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 18.581549454569156}
    }
],
'Total xsec for missing topologies (fb)' : 31.16832,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 21.87794,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.645387,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.644988,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 49.74987,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 21.87794,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 18.58155,
        'SMS' : 'PV > (jet,jet)',
        'SMS IDs' : [3, 4]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.645387,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 4.644988,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}