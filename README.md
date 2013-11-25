## WiserTogether Patton Openshift Cartridge
### powered by OpenShift Cartridge Development Kit 

For the latest on creating cartridges, read the [Cartridge Writer's Guide](https://github.com/openshift/origin-server/blob/master/node/README.writing_cartridges.md)


To deploy a Patton-based application named APPNAME, using the PAAS skeleton as a base, use the RHC command

rhc app create -n wisertogether --from-code https://github.com/WiserTogether/paas-skeleton.git APPNAME http://pattoncdk-wisertogether.rhcloud.com/manifest/master 




