from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = 'Data_Run2016'
config.General.requestName = 'JetHT_Run2016F_PromptReco_v1_MINIAOD'
config.section_('JobType')
config.JobType.psetName = '../qg_tag_flat-data-cfg_miniAOD.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.outputFiles = ['OUTFILENAME']
config.section_('Data')
config.Data.inputDataset = '/JetHT/Run2016F-PromptReco-v1/MINIAOD'
config.Data.unitsPerJob = 100 #without '' since it must be an int
config.Data.splitting = 'LumiBased'
config.Data.publication = False
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_254833_13TeV_PromptReco_Collisions15_JSON.txt'
config.Data.lumiMask = 'Json/Cert_271036-278808_13TeV_PromptReco_Collisions16_JSON_NoL1T_19Aug16.txt'
#config.Data.runRange = '254833-254833'#'208306-238354' # '193093-194075'                             
config.Data.outLFNDirBase = '/store/user/abat/Run2016/Data2016'
#config.Data.outLFNDirBase = '/store/user/santanas/rootTrees/Run2015B_JetHT_10June2015DCSJson_JECV5_5a70fc3/'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_IT_Rome'
