# ChatGPT-Bitcoin-Analyzer
This is a Streamlit web application that uses the OpenAI GPT-3.5 model to analyze live cryptocurrency prices, specifically focusing on Bitcoin. The application fetches the historical price data of Bitcoin for the last 7 days from a RapidAPI endpoint and then uses the GPT-3.5 model to generate a technical analysis based on that price data. The analysis includes Price Overview, Moving Averages, Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), and advice on whether to buy or sell.

![Untitled](https://github.com/tanmay-guptaa/ChatGPT-Bitcoin-Analyzer/assets/119430497/c2a217dd-9b83-4dab-b2ad-ac1484fbf9bc)


**Requirements**

To run this application, you need the following:
1. API Key for OpenAI GPT-3.5 model.
2. API Key for the RapidAPI endpoint to fetch cryptocurrency price data.


**Usage**
1. Clone this repository to your local machine.
2. Install the required Python libraries (OpenAI, requests, json, and Streamlit) if you haven't already.
3. Replace the placeholders for the API keys in the code with your actual keys.
4. Run the Streamlit application using the following command:
   ```bash
   streamlit run main.py
   ```
5. The web application will open in your default browser. Click the "Analyze" button to initiate the analysis.
6. The application will fetch the Bitcoin prices, create a user prompt for the GPT-3.5 model, and display the generated analysis in a 
   text area on the web page.

Please note that the application uses the GPT-3.5 model from OpenAI to generate the analysis. Make sure to follow the terms and conditions of the API providers.


**Contributing**

Contributions to this project are welcome and encouraged! If you have any improvements or new features to add, feel free to fork the repository and submit a pull request.
