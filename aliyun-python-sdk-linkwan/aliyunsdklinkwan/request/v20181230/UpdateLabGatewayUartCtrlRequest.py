# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateLabGatewayUartCtrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'UpdateLabGatewayUartCtrl','linkwan')
		self.set_protocol_type('https');

	def get_GwEui(self):
		return self.get_body_params().get('GwEui')

	def set_GwEui(self,GwEui):
		self.add_body_params('GwEui', GwEui)

	def get_Enabled(self):
		return self.get_body_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_body_params('Enabled', Enabled)