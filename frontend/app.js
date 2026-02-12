const peraWallet = new PeraWalletConnect();
let walletAddress = null;

async function connectWallet() {
  try {
    const accounts = await peraWallet.connect();
    walletAddress = accounts[0];

    document.getElementById("status").innerText =
      "Wallet connected: " + walletAddress;
  } catch (error) {
    console.log(error);
    alert("Wallet connection cancelled");
  }
}

function buyTicket() {
  if (!walletAddress) {
    alert("Please connect wallet first");
    return;
  }
  alert("Next step: NFT ticket minting");
}

function verifyTicket() {
  if (!walletAddress) {
    alert("Please connect wallet first");
    return;
  }
  alert("Next step: ticket verification");
}
