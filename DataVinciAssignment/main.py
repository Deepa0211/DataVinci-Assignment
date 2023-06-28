# Import statements
import yfinance as yf  # to access yahoo finance API
import datetime as dt
import pandas as pd
import plotly.graph_objects as gra_obj  # to use graph object module of plotly

# Function to extract data
def extract_history(ticker, start_date,end_date):
    try: # for handling exceptions
        data = yf.download(ticker, start=start_date, end=end_date) # Downloading historical data

        # Only extracting necessary columns
        data = data[["Open",
                     "Close",
                     "High",
                     "Low",
                     "Volume"]]
        return data

    except Exception as e:
        print("Error Occurred: ", str(e))
        return None

# Specifying the arguments
ticker = "DABUR.NS"
start_date = dt.datetime(2022, 6, 23)
end_date = dt.datetime(2023, 6, 23)

# Calling function extract_history
f_data = extract_history(ticker, start_date, end_date)
if f_data is not None:
    # table get printed
    print(f_data)

    # Calculate average daily trading volume
    avg_volume = f_data["Volume"].mean()
    print("Average Daily Trading Volume:", avg_volume)

    # Creating Candlestick chart for extracted data
    fig = gra_obj.Figure(data=[gra_obj.Candlestick(x=f_data.index,
                                         open=f_data["Open"],
                                         high=f_data["High"],
                                         low=f_data["Low"],
                                         close=f_data["Close"])])

    # Designing the chart layout
    fig.update_layout(title="Candlestick Chart for One year financial data of Dabur India Limited listed on NSE",
                      xaxis_title="Date",
                      yaxis_title="Price",
                      xaxis_rangeslider_visible=False)

    # Show the chart
    fig.show()





