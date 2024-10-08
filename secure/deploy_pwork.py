from beaker import client, localnet

from app_pwork_ import app, update_state

app.build().export("./artifacts")

accounts = localnet.kmd.get_accounts()
sender = accounts[0]

app_client = client.ApplicationClient(
    client=localnet.get_algod_client(),
    app=app,
    sender=sender.address,
    signer=sender.signer_new,
)

app_client.create()

return_value = app_client.call(
    update_state, actual="Open", assevered="Ant", payed="Ant"
).return_value
print(return_value)
