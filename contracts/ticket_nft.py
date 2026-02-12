import os
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.transaction import AssetConfigTxn, wait_for_confirmation
from dotenv import load_dotenv

def main():
    load_dotenv()

    # Load environment variables
    user_mnemonic = os.getenv("MNEMONIC")
    algod_address = os.getenv("ALGOD_URL")
    algod_token = os.getenv("ALGOD_TOKEN")

    # Connect to Algorand client
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Recover account
    private_key = mnemonic.to_private_key(user_mnemonic)
    public_address = mnemonic.to_public_key(user_mnemonic)
    print("Using wallet address:", public_address)

    # Get suggested transaction parameters
    params = algod_client.suggested_params()

    # Create the NFT (ASA)
    txn = AssetConfigTxn(
        sender=public_address,
        sp=params,
        total=1,
        default_frozen=False,
        unit_name="TICKET",
        asset_name="CampusTicket",
        manager=public_address,
        reserve=public_address,
        freeze=None,
        clawback=None,
        url="https://your-event.com/ticket",
        decimals=0
    )

    # Sign and send the transaction
    signed_txn = txn.sign(private_key)
    txid = algod_client.send_transaction(signed_txn)
    print("Transaction sent with ID:", txid)

    # Wait for confirmation
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("Transaction confirmed in round:", confirmed_txn['confirmed-round'])
    print("Asset ID (Ticket NFT):", confirmed_txn['asset-index'])

if __name__ == "__main__":
    main()
