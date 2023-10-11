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
    'input file' : '/home/yoxara/2MDM/Update_Data_val_SmodelS/ppZpjj/slhaFiles/xsec_ppZp_CMS_Obs/run_28_tag_1.slha',
    'database version' : '3.0.0-beta',
    'smodels version' : '3.0.0-beta'
},
'SMS Decomposition' : [
    {
        'ID' : 1,
        'SMS' : '(PV > inv)',
        'Masses (GeV)' : [('inv', 4500.0)],
        'PIDs' : [('inv', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 2.85}
    },
    {
        'ID' : 2,
        'SMS' : '(PV > Y1(1)), (Y1(1) > xd,xd~)',
        'Masses (GeV)' : [('Y1', 4500.0), ('xd', 1.0), ('xd~', 1.0)],
        'PIDs' : [
            ('Y1', 5000001),
            ('xd', 5000521),
            ('xd~', -5000521)
        ],
        'Weights (fb)' : {'xsec 13.0 TeV': 2.85}
    },
    {
        'ID' : 3,
        'SMS' : '(PV > Y1(1)), (Y1(1) > q,q)',
        'Masses (GeV)' : [('Y1', 4500.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 8.84}
    },
    {
        'ID' : 4,
        'SMS' : '(PV > Y1(1)), (Y1(1) > c,c)',
        'Masses (GeV)' : [('Y1', 4500.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 2.95}
    },
    {
        'ID' : 5,
        'SMS' : '(PV > Y1(1)), (Y1(1) > t-,t+)',
        'Masses (GeV)' : [('Y1', 4500.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 2.95}
    },
    {
        'ID' : 6,
        'SMS' : '(PV > Y1(1)), (Y1(1) > b,b)',
        'Masses (GeV)' : [('Y1', 4500.0)],
        'PIDs' : [('Y1', 5000001)],
        'Weights (fb)' : {'xsec 13.0 TeV': 2.95}
    }
],
'ExptRes' : [
    {
        'maxcond' : 0.0,
        'theory prediction (fb)' : 11.78718,
        'upper limit (fb)' : 20.5267,
        'expected upper limit (fb)' : 17.3274,
        'TxNames' : ['TRV1qq'],
        'Mass (GeV)' : [('Y1', 4500.0)],
        'AnalysisID' : 'CMS-EXO-19-012',
        'DataSetID' : None,
        'AnalysisSqrts (TeV)' : 13.0,
        'lumi (fb-1)' : 137.0,
        'dataType' : 'upperLimit',
        'r' : 0.5742365,
        'r_expected' : 0.6802625,
        'Width (GeV)' : [('Y1', inf)],
        'TxNames weights (fb)' : {'TRV1qq': 11.78717980398944}
    }
],
'Total xsec for missing topologies (fb)' : 8.739506,
'missing topologies' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.946795,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.946758,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.845953,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    }
],
'Total xsec for missing topologies with displaced decays (fb)' : 0.0,
'missing topologies with displaced decays' : [],
'Total xsec for missing topologies with prompt decays (fb)' : 20.52669,
'missing topologies with prompt decays' : [
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 11.78718,
        'SMS' : 'PV > (jet,jet)',
        'SMS IDs' : [3, 4]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.946795,
        'SMS' : 'PV > (b,b)',
        'SMS IDs' : [6]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.946758,
        'SMS' : 'PV > (t,t)',
        'SMS IDs' : [5]
    },
    {
        'sqrts (TeV)' : 13.0,
        'weight (fb)' : 2.845953,
        'SMS' : 'PV > (MET)',
        'SMS IDs' : [1]
    }
],
'Total xsec for topologies outside the grid (fb)' : 0.0,
'topologies outside the grid' : []
}