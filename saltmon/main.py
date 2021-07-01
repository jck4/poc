#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, Instance, Vpc
from infra import *

class Stack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        AwsProvider(self, 'Aws', region='us-east-1')
        for instance in instances:
            try:
                Vpc(self,instance.network,cidr_block="10.0.0.0/32")
            except:
                pass
                
                
app = App()
Stack(app, "test")
app.synth()
