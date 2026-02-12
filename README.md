# 🎟️ Decentralized Campus Event Ticketing

Welcome to the **future of campus events**! This project leverages the **Algorand Blockchain** to issue secure, verifiable, and tamper-proof event tickets as Non-Fungible Tokens (NFTs). Say goodbye to fake tickets, scalping, and lost entries.

## 🚀 Why This Project Rocks

Traditional ticketing systems are broken. They rely on centralized databases that can be hacked, and paper tickets that can be easily forged. **Decentralized Campus Event Ticketing** solves these problems by minting every ticket as a unique digital asset on the Algorand blockchain.

### ✨ Key Features

*   **Immutable Ownership**: Each ticket is an NFT (Algorand Standard Asset). Once you own it, it's yours. No one can take it away or duplicate it.
*   **Fraud-Proof Security**: The blockchain guarantees the authenticity of every ticket. Verification is instant and undeniable.
*   **Seamless Wallet Integration**: Connect easily with **Pera Wallet** to buy and store your tickets directly on your phone.
*   **Eco-Friendly Tech**: Built on **Algorand**, a carbon-negative blockchain known for its speed, low fees, and sustainability.
*   **Transparent Transactions**: All ticket sales and transfers are recorded on the public ledger, ensuring complete transparency.

## 🛠️ Technical Stack

This project is built using a modern, robust tech stack designed for reliability and ease of use:

*   **Blockchain**: [Algorand](https://algorand.com/) (Layer 1 Proof-of-Stake)
*   **Smart Contracts / SDK**: Python (`algosdk`) for asset management and transaction signing.
*   **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
*   **Wallet Connect**: Integrated with `@perawallet/connect` for secure user authentication.

## 🏁 Getting Started

Dive into the code and run the system yourself!

### Prerequisites
*   Python 3.x
*   Node.js (for frontend dependencies if expanded)
*   An Algorand Wallet (e.g., Pera Wallet) with some test ALGOs.

### Installation

1.  **Clone the Repo**
    ```bash
    git clone https://github.com/your-username/algorand-campus-ticketing.git
    cd algorand-campus-ticketing
    ```

2.  **Setup Backend**
    *   Install Python dependencies:
        ```bash
        pip install py-algorand-sdk python-dotenv
        ```
    *   Create a `.env` file in the root directory and add your wallet mnemonic and Algod credentials:
        ```env
        MNEMONIC="your 25 word mnemonic phrase here"
        ALGOD_URL="https://testnet-api.algonode.cloud"
        ALGOD_TOKEN=""
        ```

3.  **Mint a Ticket**
    *   Run the Python script to mint your first NFT ticket:
        ```bash
        python contracts/ticket_nft.py
        ```
    *   Check the console output for the **Asset ID** confirmed on the blockchain!

4.  **Run the Frontend**
    *   Simply open `frontend/index.html` in your browser.
    *   Click **Connect Wallet** to link your Pera Wallet.
    *   (Coming Soon) Interact with the Buy/Verify buttons to integrate with the smart contract!

## 🔮 Roadmap

*   [ ] **QR Code Generation**: Generate a unique QR code for each ticket for easy scanning at the venue.
*   [ ] **Marketplace**: Allow students to securely resell tickets if they can't attend.
*   [ ] **Mobile App**: A dedicated mobile app for smoother entry.

---

Built with ❤️ for **Hackspiration'26**. Let's revolutionize campus events!
