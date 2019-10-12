
hostcreate = """# Add a kvm host
$ kcli create host kvm -H 192.168.1.6 twix

# Add a aws host
$ kcli create host aws --access_key_id xxx  --access_key_secret xxx  -k KEYPAIR mypair -r eu-west-3 myaws

# Add a gcp host
$ kcli create host gcp --credentials ~/.kcli/xx.json --project myproject-209909 --zone us-central1-b mygcp

# Add a ovirt host
$ kcli create host ovirt -c mycluster -d mydatacenter -H 192.168.1.2 -u admin@internal -p pass -o org1 --pool x myovirt

# Add a vsphere host
$ kcli create host vsphere -c mycluster -d mydatacenter -H 192.168.1.3 -u admin@xxx.es -p pass mysphere

# Add a openstack host
$ kcli create host openstack --auth-url http://10.19.114.91:5000/v3 -u admin -p pass --project myproject myosp

# Add a kubevirt host using existing k8s credentials
$ kcli create host kubevirt mykubevirt
"""

_list = """# Get list of vms
$ kcli list vm

# Get list of products
$ kcli list product

# Get list of clients/hosts
$ kcli list host
"""

plancreate = """# Create a plan named ocp311 from a file
$ kcli create plan -f multi.yml ocp311

# Do the same but customize some parameters
$ kcli create plan -f multi.yml -P masters=1 -P nodes=2 -P crio=true

# Create a plan from a remote url, customizing some parameters
$ kcli create plan -u https://github.com/karmab/kcli-plans/blob/master/kubernetes/kubernetes.yml -P masters=3
"""

planinfo = """# Get info from a local plan file
$ kcli info plan -f multi.yml

# Get info of a plan with a remote url
$ kcli info plan -u https://github.com/karmab/kcli-plans/blob/master/kubernetes/kubernetes.yml
"""

productinfo = """# Get info from product kubernetes
$ kcli info product kubernetes
"""

repocreate = """# Create a product repo from karmab samples repo
$ kcli create repo -u https://github.com/karmab/kcli-plans karmab
"""

vmcreate = """# create a centos vm from image centos7 with a random name
$ kcli create vm -i centos7

# create a centos vm named myvm customizing its memory and cpus
$ kcli create vm -i centos7 -P memory=4096 -P numcpus=4

# pass disks, networks and even cmds
$ kcli create vm -i CentOS-7-x86_64-GenericCloud.qcow2 -P disks=[10,20] -P nets=[default] -P cmds=[yum -y install nc]

# create a vm from a custom profile
$ kcli create vm -p myprofile myvm
"""

vmexport = """# export vm myvm with a specific name for the generated image
$ kcli export -i myimage vmyvm
"""
