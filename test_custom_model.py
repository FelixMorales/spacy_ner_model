import spacy

nlp_ner = spacy.load('./model-best') 

test_text = '''The global crypto market capitalisation tumbled 3.60 percent over the last 24 hours to $2.18 trillion while the total trading volume fell 6.79 percent to $95.77 billion.

While DeFi ($15.16 billion) accounted for 15.83 percent of the trading volume, stablecoins ($75.16 billion) made up 78.48 percent. The market dominance of Bitcoin rose 0.29 percent to 40.45 percent today morning. Bitcoin is currently trading at $46,560.09.

As for major cryptocurrencies, Bitcoin tumbled 2.46 percent to trade at Rs 37,49,173 while Ethereum fell 4.48 percent at Rs 2,93,527.4. Cardano declined 7.25 percent to Rs 105.4. Avalanche fell 8.77 percent to Rs 8,048, Polkadot tumbled 7.53 percent at Rs 2,137.04 and Litecoin dipped 1.04 percent to Rs 11,725.33 over the last 24 hours. Tether rose 0.12 percent to trade at Rs 80.18.

Memecoin SHIB fell 5.61 percent while Dogecoin decreased 4.29 percent to trade at Rs 13.56. LUNA fell around 6.39 percent to Rs 6,579.55.

Ethereum-based metaverse game The Sandbox co-founder and operations chief Sebastien Borget viewed the metaverse as a digital nation, saying that it’s validating to see his team’s idea for a community-owned, user-customisable online game world embraced by more people.

RELATED STORIES
  2021: A Year Of NFT Craze 
  Elon Musk reveals who he thinks the mysterious Satoshi Nakamoto is 
  Crypto Learn: How to read Crypto Charts? 
“Every day, the map is different. There are new landowners and new communities that come and decide to build things next to each other. I feel like it's a digital nation—living and breathing. That's why it's exciting. It's culturally rich, it’s global, and it's accessible," he continued.

Per blockchain data site Glassnode, there are now 71,364,788 addresses holding some amount of Ethereum, the second-largest cryptocurrency by market capitalisation.

Meanwhile, a white hat hacker won a bug bounty. In early December, the person known as Leon Spacewalker on Twitter had helped Polygon avert a multibillion-dollar disaster. He reported an exploit in a critical Polygon smart contract that held more than nine billion MATIC tokens on Dec. 3, then worth around $20.2 billion. Core developers rushed a fix by Dec. 5. Spacewalker reportedly won a $2.2 million bug bounty, the blockchain network announced yesterday. '''

doc = nlp_ner(test_text)

for word in doc.ents:
    print(f'text: {word.text} - tag: {word.label_}')