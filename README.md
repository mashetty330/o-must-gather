# O Must Gather (omg)

oc like tool that works with must-gather rather than OpenShift API

Important Note: This fork is an extension of original project and has feature specific to ODF must-gather which isn't available in the original project. So to avail these make sure you follow the exact steps mentioned below. 

![GitHub release (latest by date)](https://img.shields.io/github/v/release/kxr/o-must-gather)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/o-must-gather)
![GitHub](https://img.shields.io/github/license/kxr/o-must-gather?color=blue)

## Installation

Simply run:

    $ pip3 install git+https://github.com/mashetty330/o-must-gather.git@stable

## Usage

Point it to an extracted must-gather:

    $ omg use </path/to/must-gather/>

Or you can point directly to the file, omg will validate and uncompress it for you:

    $ omg use <must-gather-tar-file>

Use it like oc:

    # omg get clusterVersion
    # omg get clusterOperators
    # omg project openshift-ingress
    # omg get pods -o wide

ODF specific:
 # omg get scd ---> gets the full storage cluster details

## Additional Features


### `omg use`

- When run without any arguments i.e, just `omg use`, omg will show you the details of the currently selected
  must-gather. For example:

        # omg use ./must-gather.local.2723199189299891619
        Now using project "openshift-monitoring" on must-gather "/home/knaeem/Downloads/must-gather.local.2723199189299891619/quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-d7c882054a4528eda72e69a7988c5931b5a1643913b11bfd2575a78a8620808f"

        # omg use
        Current must-gather: /home/knaeem/Downloads/must-gather.local.2723199189299891619/quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-d7c882054a4528eda72e69a7988c5931b5a1643913b11bfd2575a78a8620808f
            Current Project: openshift-monitoring
            Cluster API URL: ['https://api.ocp4.aidemo.local:6443']
           Cluster Platform: ['oVirt']

- To facilitate users working with multiple must-gathers, you can now set the current working directory to be used as
  the must-gather path. In this case, simply switching the current working directory to the desired must-gather will be
  enough to start using that must-gather. To use this mode, simply run `omg use --cwd`. For example:

        # omg use --cwd
        Using your current working directory

        # cd /home/knaeem/Downloads/must-gather.local.2723199189299891619/quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-d7c882054a4528eda72e69a7988c5931b5a1643913b11bfd2575a78a8620808f

        # omg use
        Current must-gather: .
            Current Project: openshift-monitoring
            Cluster API URL: ['https://api.ocp4.aidemo.local:6443']
           Cluster Platform: ['oVirt']

        # cd /home/knaeem/Downloads/must-gather.local.7890185621691109993/quay-io-openshift-release-dev-ocp-v4-0-art-dev-sha256-549bd48582a9fa615b8728bc6e1d66f3a9c829f415d9ddd58f95eb978be50274

        # omg use
        Current must-gather: .
            Current Project: openshift-monitoring
            Cluster API URL: ['https://api.ocpprod.example.com:6443']
           Cluster Platform: ['None']

- You can now point the omg command to a file and it will uncompress it for you, but **only** if is a valid file. What is a 
  valid file?:
  - It is a tar file, we use tarfile module to validate that, not just by extension.
  - It have only one root directory inside the tar file and the name starts with "must-gather".
  Once it match this criteria the file is uncompressed on the current directory and it move to the standard 'omg use' flow.




