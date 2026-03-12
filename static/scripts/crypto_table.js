async function updateTable() {
    const tbody = document.getElementById("table-body");
    const url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,tether,binancecoin,cardano,polkadot,xrp,uniswap,litecoin,chainlink,dogecoin,matic-network,solana,cosmos,tron,arbitrum,avalanche,bitcoin-cash,binance-usd,celo,chiliz,cryptonex,dai,dash,decentraland,ecomi,fantom,filecoin,hedera-hashgraph,huobi-token,mdex,neo,nexus,nexo,okb,paxos-standard,perpetual-protocol,quant-network,shiba-inu,terra-luna,theta-token,vechain,yfi-ii,zcash,bittorrent,curve-dao-token,curve-fi,cakecoin,digibyte,enjin-coin,harmony,kusama,loopring,maidsafecoin,near,omisego,pancakeswap,ren,serum,siacoin,stellar,telcoin,travala.com,uma,yearn-finance,zero-ex";

    try {
        // Fetch the data from the API
        const response = await fetch(url);

        // Check if CoinGecko blocked us (e.g., Rate Limit Exceeded)
        if (!response.ok) {
            throw new Error(`API Error: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();
        let html = "";

        data.forEach((coin) => {
            // SAFETY NET: If a coin is missing price data, default to 0 to prevent crashes
            const currentPrice = coin.current_price || 0;
            const priceChange = coin.price_change_percentage_24h || 0;

            html += `
                <tr>
                    <td>${coin.name} (${coin.symbol.toUpperCase()})</td>
                    <td><img src="${coin.image}" alt="${coin.symbol}" width="25"></td>
                    <td>$${currentPrice < 1 ? currentPrice.toFixed(7) : currentPrice.toFixed(2)}</td>
                    <td class="${priceChange < 0 ? 'red' : 'green'}">
                        ${priceChange > 0 ? '+' : ''}${priceChange.toFixed(2)}%
                    </td>
                </tr>
            `;
        });

        // Inject the generated HTML into the table
        tbody.innerHTML = html;

    } catch (error) {
        // If anything goes wrong, log it and show an error message in the table
        console.error("Failed to fetch coin data:", error);
        tbody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:red; padding: 20px;">Error loading data. You might be rate-limited by CoinGecko. Check the browser console (F12) for details.</td></tr>`;
    }
}

document.addEventListener("DOMContentLoaded", updateTable);