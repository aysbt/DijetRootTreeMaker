from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.workArea = 'SignalRun2016'
config.General.requestName ='QstarToJJ_M9000_RunIISpring16MiniAODv2'

config.section_('JobType')
config.JobType.psetName = '../qg_tag_flat-MC-cfg_miniAOD.py'
config.JobType.pluginName = 'Analysis'
#config.JobType.outputFiles = 'crab3_QGTAG_Jun2015_MC_Analysis.root'

config.section_('Data')
config.Data.inputDataset ='/QstarToJJ_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
#config.Data.inputDataset ='/RSGravitonToQuarkQuark_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
#config.Data.inputDataset ='/RSGravitonToGluonGluon_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
#config.Data.inputDataset ='/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.publication = False
#config.Data.outLFNDirBase = '/store/user/abat/Run2016/QCDRun2016'
config.Data.outLFNDirBase = '/store/user/abat/Run2016/SignalRun2016/QQ'
config.section_('User')
config.section_('Site')

config.Site.storageSite ='T3_US_FNALLPC'
