
import os
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.transaction import AssetTransferTxn, wait_for_confirmation
from dotenv import load_dotenv

def main():
    load_dotenv()

    user_mnemonic = os.getenv("MNEMONIC")
    algod_address = os.getenv("ALGOD_URL")
    algod_token = os.getenv("ALGOD_TOKEN")
    asset_id = int(os.getenv("TICKET_ASSET_ID"))

    algod_client = algod.AlgodClient(algod_token, algod_address)

    private_key = mnemonic.to_private_key(user_mnemonic)
    public_address = mnemonic.to_public_key(user_mnemonic)
    print("Using gatekeeper wallet:", public_address)

    user_address = input("Enter attendee wallet address: ")
    account_info = algod_client.account_info(user_address)
    assets = account_info.get('assets', [])

    has_ticket = any(asset['asset-id'] == asset_id and asset['amount'] > 0 for asset in assets)

    if not has_ticket:
        print("❌ Ticket not found or already used.")
        return

    print("✅ Ticket verified. Burning ticket...")

    params = algod_client.suggested_params()
    txn = AssetTransferTxn(
        sender=user_address,
        sp=params,
        receiver="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ",
        amt=1,
        index=asset_id
    )

    signed_txn = txn.sign(private_key)
    txid = algod_client.send_transaction(signed_txn)
    print("Transaction sent. ID:", txid)

    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("🎟️ Ticket burned. Entry granted.")

if __name__ == "__main__":
    main()