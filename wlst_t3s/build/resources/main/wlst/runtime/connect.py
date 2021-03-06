###################################################################################################
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
###################################################################################################
import os
import java.lang.System as System
import java.io.FileInputStream as FileInputStream
import java.util.Properties as Properties

propFile="/tmp/wlst.properties"

if( os.path.isfile( propFile ) ):
   propFile = FileInputStream("/tmp/wlst.properties")
   prop = System.getProperties()
   prop.load( propFile )
   System.setProperties( prop )
   System.getProperties().list(System.out)
#End if

def connectToAdminServer():
    script = sys.argv.pop(0)
    user = sys.argv.pop(0)
    url = sys.argv.pop(0)
    password = os.getenv('DEPLOYIT_WLST_PASSWORD')
    print "Connecting to WebLogic %s as user %s" %(url, user)
    connect(user, password, url)


