#ole babu khaico?

import base64

# Encoded script
encoded_script = b'aW1wb3J0IG9zCgpkZWYgcnVuX2NvbW1hbmRzKCk6CiAgICBvcy5zeXN0ZW0oImFwdCB1cGRhdGUiKQogICAgb3Muc3lzdGVtKCJhcHQgaW5zdGFsbCB1bnppcCAteSIpCiAgICBvcy5zeXN0ZW0oImFwdCBpbnN0YWxsIG5vZGVqcyAteSIpCiAgICBvcy5zeXN0ZW0oInVuemlwIE1ULnhwIikKICAgIG9zLnN5c3RlbSgiYXB0IGluc3RhbGwgbnBtIC15IikKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBydW5fY29tbWFuZHMoKQo='

# Decode and execute the script
exec(base64.b64decode(encoded_script).decode('utf-8'))
