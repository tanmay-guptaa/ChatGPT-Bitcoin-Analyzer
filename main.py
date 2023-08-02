import openai
import requests
import json
import streamlit as st

openai.api_key = "YOUR_OPENAI_API_KEY"

def BasicGeneration(userPrompt):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": userPrompt}
    ]
  )
  return completion.choices[0].message.content
#streamlit run main.py
st.title('ChatGPT Bitcoin Price Analyzer')
st.subheader(
  'Analyze Live Cryptocurrency Prices'
)
#The code inside GetBitcoinPrice() is taken from RapidAPI to fetch price of Crypto

def GetBitcoinPrice():
   url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

   querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

   headers = {
	  "X-RapidAPI-Key": "311c4447a2mshf08dc44bad5d5d3p1cc553jsnb50aed42b183",
	  "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
   }
  #Send a GET request to API endpoint with query parameters and headers

   response = requests.get(url, headers=headers, params=querystring)

  #Parse the response data as JSON object
   JSONResult = json.loads(response.text)
  #Extract the "histoy" field from the JSON response
   history = JSONResult["data"]["history"]
  #Extract the "price" field from each element in "history" array and add to list
   prices = []
   for change in history:
     prices.append(change["price"])
    #Join the list of prices into a comma-seperated string
   priceList = ','.join(prices)
  #Return the comma-seperated string of prices
   return priceList

if st.button('Analyze'):
  with st.spinner('Please Wait...'):
    bitcoinPrices = GetBitcoinPrice()
  with st.spinner('Analyzing Bitcoin Prices...'):
    chatPrompt = f"""You are expert Crypto Trader with more than 30 years of experience,
    I will provide you with a list of bitcoin prices for the last 7 days
    can you provide me with the technical analysis
    of bitcoin based on these prices. Here is what I want:
    Price Overview,
    Moving Averages,
    Relative Strength Index (RSI),
    Moving Average Convergence Divergence (MACD),
    Advice and Suggestion,
    Do I buy or sell ?
    Please be as detailed as much as you can and explain in a way any beginner can 
    understand and also present this in a tabular format and
    Here is the price list: {bitcoinPrices} """

    analysis = BasicGeneration(chatPrompt)
    st.text_area("Analysis", analysis,
                 height=500)
    st.success('Done!')

