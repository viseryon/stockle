from yahooquery import Ticker


sp100_tickers = {
    'AAPL': {'Name': 'Apple', 'Sector': 'Information Technology'},
    'ABBV': {'Name': 'AbbVie', 'Sector': 'Health Care'},
    'ABT': {'Name': 'Abbott', 'Sector': 'Health Care'},
    'ACN': {'Name': 'Accenture', 'Sector': 'Information Technology'},
    'ADBE': {'Name': 'Adobe', 'Sector': 'Information Technology'},
    'AIG': {'Name': 'American International Group', 'Sector': 'Financials'},
    'AMD': {'Name': 'AMD', 'Sector': 'Information Technology'},
    'AMGN': {'Name': 'Amgen', 'Sector': 'Health Care'},
    'AMT': {'Name': 'American Tower', 'Sector': 'Real Estate'},
    'AMZN': {'Name': 'Amazon', 'Sector': 'Consumer Discretionary'},
    'AVGO': {'Name': 'Broadcom', 'Sector': 'Information Technology'},
    'AXP': {'Name': 'American Express', 'Sector': 'Financials'},
    'BA': {'Name': 'Boeing', 'Sector': 'Industrials'},
    'BAC': {'Name': 'Bank of America', 'Sector': 'Financials'},
    'BK': {'Name': 'BNY Mellon', 'Sector': 'Financials'},
    'BKNG': {'Name': 'Booking Holdings', 'Sector': 'Consumer Discretionary'},
    'BLK': {'Name': 'BlackRock', 'Sector': 'Financials'},
    'BMY': {'Name': 'Bristol Myers Squibb', 'Sector': 'Health Care'},
    'BRK.B': {'Name': 'Berkshire Hathaway', 'Sector': 'Financials'},
    'C': {'Name': 'Citigroup', 'Sector': 'Financials'},
    'CAT': {'Name': 'Caterpillar', 'Sector': 'Industrials'},
    'CHTR': {'Name': 'Charter Communications', 'Sector': 'Communication Services'},
    'CL': {'Name': 'Colgate-Palmolive', 'Sector': 'Consumer Staples'},
    'CMCSA': {'Name': 'Comcast', 'Sector': 'Communication Services'},
    'COF': {'Name': 'Capital One', 'Sector': 'Financials'},
    'COP': {'Name': 'ConocoPhillips', 'Sector': 'Energy'},
    'COST': {'Name': 'Costco', 'Sector': 'Consumer Staples'},
    'CRM': {'Name': 'Salesforce', 'Sector': 'Information Technology'},
    'CSCO': {'Name': 'Cisco', 'Sector': 'Information Technology'},
    'CVS': {'Name': 'CVS Health', 'Sector': 'Health Care'},
    'CVX': {'Name': 'Chevron', 'Sector': 'Energy'},
    'DHR': {'Name': 'Danaher', 'Sector': 'Health Care'},
    'DIS': {'Name': 'Disney', 'Sector': 'Communication Services'},
    'DOW': {'Name': 'Dow', 'Sector': 'Materials'},
    'DUK': {'Name': 'Duke Energy', 'Sector': 'Utilities'},
    'EMR': {'Name': 'Emerson', 'Sector': 'Industrials'},
    'EXC': {'Name': 'Exelon', 'Sector': 'Utilities'},
    'F': {'Name': 'Ford', 'Sector': 'Consumer Discretionary'},
    'FDX': {'Name': 'FedEx', 'Sector': 'Industrials'},
    'GD': {'Name': 'General Dynamics', 'Sector': 'Industrials'},
    'GE': {'Name': 'GE', 'Sector': 'Industrials'},
    'GILD': {'Name': 'Gilead', 'Sector': 'Health Care'},
    'GM': {'Name': 'GM', 'Sector': 'Consumer Discretionary'},
    'GOOG': {'Name': 'Alphabet (Class C)', 'Sector': 'Communication Services'},
    'GOOGL': {'Name': 'Alphabet (Class A)', 'Sector': 'Communication Services'},
    'GS': {'Name': 'Goldman Sachs', 'Sector': 'Financials'},
    'HD': {'Name': 'Home Depot', 'Sector': 'Consumer Discretionary'},
    'HON': {'Name': 'Honeywell', 'Sector': 'Industrials'},
    'IBM': {'Name': 'IBM', 'Sector': 'Information Technology'},
    'INTC': {'Name': 'Intel', 'Sector': 'Information Technology'},
    'JNJ': {'Name': 'Johnson & Johnson', 'Sector': 'Health Care'},
    'JPM': {'Name': 'JPMorgan Chase', 'Sector': 'Financials'},
    'KHC': {'Name': 'Kraft Heinz', 'Sector': 'Consumer Staples'},
    'KO': {'Name': 'Coca-Cola', 'Sector': 'Consumer Staples'},
    'LIN': {'Name': 'Linde', 'Sector': 'Materials'},
    'LLY': {'Name': 'Lilly', 'Sector': 'Health Care'},
    'LMT': {'Name': 'Lockheed Martin', 'Sector': 'Industrials'},
    'LOW': {'Name': "Lowe's", 'Sector': 'Consumer Discretionary'},
    'MA': {'Name': 'Mastercard', 'Sector': 'Information Technology'},
    'MCD': {'Name': "McDonald's", 'Sector': 'Consumer Discretionary'},
    'MDLZ': {'Name': 'Mondelēz International', 'Sector': 'Consumer Staples'},
    'MDT': {'Name': 'Medtronic', 'Sector': 'Health Care'},
    'MET': {'Name': 'MetLife', 'Sector': 'Financials'},
    'META': {'Name': 'Meta', 'Sector': 'Communication Services'},
    'MMM': {'Name': '3M', 'Sector': 'Industrials'},
    'MO': {'Name': 'Altria', 'Sector': 'Consumer Staples'},
    'MRK': {'Name': 'Merck', 'Sector': 'Health Care'},
    'MS': {'Name': 'Morgan Stanley', 'Sector': 'Financials'},
    'MSFT': {'Name': 'Microsoft', 'Sector': 'Information Technology'},
    'NEE': {'Name': 'NextEra Energy', 'Sector': 'Utilities'},
    'NFLX': {'Name': 'Netflix', 'Sector': 'Communication Services'},
    'NKE': {'Name': 'Nike', 'Sector': 'Consumer Discretionary'},
    'NVDA': {'Name': 'Nvidia', 'Sector': 'Information Technology'},
    'ORCL': {'Name': 'Oracle', 'Sector': 'Information Technology'},
    'PEP': {'Name': 'PepsiCo', 'Sector': 'Consumer Staples'},
    'PFE': {'Name': 'Pfizer', 'Sector': 'Health Care'},
    'PG': {'Name': 'Procter & Gamble', 'Sector': 'Consumer Staples'},
    'PM': {'Name': 'Philip Morris International', 'Sector': 'Consumer Staples'},
    'PYPL': {'Name': 'PayPal', 'Sector': 'Information Technology'},
    'QCOM': {'Name': 'Qualcomm', 'Sector': 'Information Technology'},
    'RTX': {'Name': 'Raytheon Technologies', 'Sector': 'Industrials'},
    'SBUX': {'Name': 'Starbucks', 'Sector': 'Consumer Discretionary'},
    'SCHW': {'Name': 'Charles Schwab', 'Sector': 'Financials'},
    'SO': {'Name': 'Southern Company', 'Sector': 'Utilities'},
    'SPG': {'Name': 'Simon', 'Sector': 'Real Estate'},
    'T': {'Name': 'AT&T', 'Sector': 'Communication Services'},
    'TGT': {'Name': 'Target', 'Sector': 'Consumer Discretionary'},
    'TMO': {'Name': 'Thermo Fisher Scientific', 'Sector': 'Health Care'},
    'TMUS': {'Name': 'T-Mobile', 'Sector': 'Communication Services'},
    'TSLA': {'Name': 'Tesla', 'Sector': 'Consumer Discretionary'},
    'TXN': {'Name': 'Texas Instruments', 'Sector': 'Information Technology'},
    'UNH': {'Name': 'UnitedHealth Group', 'Sector': 'Health Care'},
    'UNP': {'Name': 'Union Pacific', 'Sector': 'Industrials'},
    'UPS': {'Name': 'United Parcel Service', 'Sector': 'Industrials'},
    'USB': {'Name': 'U.S. Bank', 'Sector': 'Financials'},
    'V': {'Name': 'Visa', 'Sector': 'Information Technology'},
    'VZ': {'Name': 'Verizon', 'Sector': 'Communication Services'},
    'WBA': {'Name': 'Walgreens Boots Alliance', 'Sector': 'Consumer Staples'},
    'WFC': {'Name': 'Wells Fargo', 'Sector': 'Financials'},
    'WMT': {'Name': 'Walmart', 'Sector': 'Consumer Staples'},
    'XOM': {'Name': 'ExxonMobil', 'Sector': 'Energy'}
}

TWITTER_URL = 'https://twitter.com/SliwinskiAlan'
GITHUB_URL = 'https://github.com/viseryon/stockle'
LINKEDIN_URL = 'https://www.linkedin.com/in/alan-sliwinski/'

CHART_LAYOUT = {'font': {'color': 'white'},
                'legend': {'tracegroupgap': 0},
                'margin': {'b': 25, 'l': 25, 'r': 25, 't': 25},
                'paper_bgcolor': '#1a1a1a',
                'plot_bgcolor': '#1a1a1a',
                'template': '...',
                'xaxis': {'anchor': 'y',
                          'domain': [0.0, 1.0],
                          'showgrid': False,
                          'title': {'text': ''}},
                'yaxis': {'anchor': 'x',
                          'domain': [0.0, 1.0],
                          'showgrid': False,
                          'title': {'text': ''}},
                'displayModeBar': False,
                'height': 600,
                'width': 600}


def all_tickers() -> dict:

    tickers = {
        'AAPL': {'Name': 'Apple', 'Sector': 'Information Technology'},
        'ABBV': {'Name': 'AbbVie', 'Sector': 'Health Care'},
        'ABT': {'Name': 'Abbott', 'Sector': 'Health Care'},
        'ACN': {'Name': 'Accenture', 'Sector': 'Information Technology'},
        'ADBE': {'Name': 'Adobe', 'Sector': 'Information Technology'},
        'AIG': {'Name': 'American International Group', 'Sector': 'Financials'},
        'AMD': {'Name': 'AMD', 'Sector': 'Information Technology'},
        'AMGN': {'Name': 'Amgen', 'Sector': 'Health Care'},
        'AMT': {'Name': 'American Tower', 'Sector': 'Real Estate'},
        'AMZN': {'Name': 'Amazon', 'Sector': 'Consumer Discretionary'},
        'AVGO': {'Name': 'Broadcom', 'Sector': 'Information Technology'},
        'AXP': {'Name': 'American Express', 'Sector': 'Financials'},
        'BA': {'Name': 'Boeing', 'Sector': 'Industrials'},
        'BAC': {'Name': 'Bank of America', 'Sector': 'Financials'},
        'BK': {'Name': 'BNY Mellon', 'Sector': 'Financials'},
        'BKNG': {'Name': 'Booking Holdings', 'Sector': 'Consumer Discretionary'},
        'BLK': {'Name': 'BlackRock', 'Sector': 'Financials'},
        'BMY': {'Name': 'Bristol Myers Squibb', 'Sector': 'Health Care'},
        'BRK.B': {'Name': 'Berkshire Hathaway', 'Sector': 'Financials'},
        'C': {'Name': 'Citigroup', 'Sector': 'Financials'},
        'CAT': {'Name': 'Caterpillar', 'Sector': 'Industrials'},
        'CHTR': {'Name': 'Charter Communications',
                 'Sector': 'Communication Services'},
        'CL': {'Name': 'Colgate-Palmolive', 'Sector': 'Consumer Staples'},
        'CMCSA': {'Name': 'Comcast', 'Sector': 'Communication Services'},
        'COF': {'Name': 'Capital One', 'Sector': 'Financials'},
        'COP': {'Name': 'ConocoPhillips', 'Sector': 'Energy'},
        'COST': {'Name': 'Costco', 'Sector': 'Consumer Staples'},
        'CRM': {'Name': 'Salesforce', 'Sector': 'Information Technology'},
        'CSCO': {'Name': 'Cisco', 'Sector': 'Information Technology'},
        'CVS': {'Name': 'CVS Health', 'Sector': 'Health Care'},
        'CVX': {'Name': 'Chevron', 'Sector': 'Energy'},
        'DHR': {'Name': 'Danaher', 'Sector': 'Health Care'},
        'DIS': {'Name': 'Disney', 'Sector': 'Communication Services'},
        'DOW': {'Name': 'Dow', 'Sector': 'Materials'},
        'DUK': {'Name': 'Duke Energy', 'Sector': 'Utilities'},
        'EMR': {'Name': 'Emerson', 'Sector': 'Industrials'},
        'EXC': {'Name': 'Exelon', 'Sector': 'Utilities'},
        'F': {'Name': 'Ford', 'Sector': 'Consumer Discretionary'},
        'FDX': {'Name': 'FedEx', 'Sector': 'Industrials'},
        'GD': {'Name': 'General Dynamics', 'Sector': 'Industrials'},
        'GE': {'Name': 'GE', 'Sector': 'Industrials'},
        'GILD': {'Name': 'Gilead', 'Sector': 'Health Care'},
        'GM': {'Name': 'GM', 'Sector': 'Consumer Discretionary'},
        'GOOG': {'Name': 'Alphabet (Class C)', 'Sector': 'Communication Services'},
        'GOOGL': {'Name': 'Alphabet (Class A)', 'Sector': 'Communication Services'},
        'GS': {'Name': 'Goldman Sachs', 'Sector': 'Financials'},
        'HD': {'Name': 'Home Depot', 'Sector': 'Consumer Discretionary'},
        'HON': {'Name': 'Honeywell', 'Sector': 'Industrials'},
        'IBM': {'Name': 'IBM', 'Sector': 'Information Technology'},
        'INTC': {'Name': 'Intel', 'Sector': 'Information Technology'},
        'JNJ': {'Name': 'Johnson & Johnson', 'Sector': 'Health Care'},
        'JPM': {'Name': 'JPMorgan Chase', 'Sector': 'Financials'},
        'KHC': {'Name': 'Kraft Heinz', 'Sector': 'Consumer Staples'},
        'KO': {'Name': 'Coca-Cola', 'Sector': 'Consumer Staples'},
        'LIN': {'Name': 'Linde', 'Sector': 'Materials'},
        'LLY': {'Name': 'Lilly', 'Sector': 'Health Care'},
        'LMT': {'Name': 'Lockheed Martin', 'Sector': 'Industrials'},
        'LOW': {'Name': "Lowe's", 'Sector': 'Consumer Discretionary'},
        'MA': {'Name': 'Mastercard', 'Sector': 'Information Technology'},
        'MCD': {'Name': "McDonald's", 'Sector': 'Consumer Discretionary'},
        'MDLZ': {'Name': 'Mondelēz International', 'Sector': 'Consumer Staples'},
        'MDT': {'Name': 'Medtronic', 'Sector': 'Health Care'},
        'MET': {'Name': 'MetLife', 'Sector': 'Financials'},
        'META': {'Name': 'Meta', 'Sector': 'Communication Services'},
        'MMM': {'Name': '3M', 'Sector': 'Industrials'},
        'MO': {'Name': 'Altria', 'Sector': 'Consumer Staples'},
        'MRK': {'Name': 'Merck', 'Sector': 'Health Care'},
        'MS': {'Name': 'Morgan Stanley', 'Sector': 'Financials'},
        'MSFT': {'Name': 'Microsoft', 'Sector': 'Information Technology'},
        'NEE': {'Name': 'NextEra Energy', 'Sector': 'Utilities'},
        'NFLX': {'Name': 'Netflix', 'Sector': 'Communication Services'},
        'NKE': {'Name': 'Nike', 'Sector': 'Consumer Discretionary'},
        'NVDA': {'Name': 'Nvidia', 'Sector': 'Information Technology'},
        'ORCL': {'Name': 'Oracle', 'Sector': 'Information Technology'},
        'PEP': {'Name': 'PepsiCo', 'Sector': 'Consumer Staples'},
        'PFE': {'Name': 'Pfizer', 'Sector': 'Health Care'},
        'PG': {'Name': 'Procter & Gamble', 'Sector': 'Consumer Staples'},
        'PM': {'Name': 'Philip Morris International', 'Sector': 'Consumer Staples'},
        'PYPL': {'Name': 'PayPal', 'Sector': 'Information Technology'},
        'QCOM': {'Name': 'Qualcomm', 'Sector': 'Information Technology'},
        'RTX': {'Name': 'Raytheon Technologies', 'Sector': 'Industrials'},
        'SBUX': {'Name': 'Starbucks', 'Sector': 'Consumer Discretionary'},
        'SCHW': {'Name': 'Charles Schwab', 'Sector': 'Financials'},
        'SO': {'Name': 'Southern Company', 'Sector': 'Utilities'},
        'SPG': {'Name': 'Simon', 'Sector': 'Real Estate'},
        'T': {'Name': 'AT&T', 'Sector': 'Communication Services'},
        'TGT': {'Name': 'Target', 'Sector': 'Consumer Discretionary'},
        'TMO': {'Name': 'Thermo Fisher Scientific', 'Sector': 'Health Care'},
        'TMUS': {'Name': 'T-Mobile', 'Sector': 'Communication Services'},
        'TSLA': {'Name': 'Tesla', 'Sector': 'Consumer Discretionary'},
        'TXN': {'Name': 'Texas Instruments', 'Sector': 'Information Technology'},
        'UNH': {'Name': 'UnitedHealth Group', 'Sector': 'Health Care'},
        'UNP': {'Name': 'Union Pacific', 'Sector': 'Industrials'},
        'UPS': {'Name': 'United Parcel Service', 'Sector': 'Industrials'},
        'USB': {'Name': 'U.S. Bank', 'Sector': 'Financials'},
        'V': {'Name': 'Visa', 'Sector': 'Information Technology'},
        'VZ': {'Name': 'Verizon', 'Sector': 'Communication Services'},
        'WBA': {'Name': 'Walgreens Boots Alliance', 'Sector': 'Consumer Staples'},
        'WFC': {'Name': 'Wells Fargo', 'Sector': 'Financials'},
        'WMT': {'Name': 'Walmart', 'Sector': 'Consumer Staples'},
        'XOM': {'Name': 'ExxonMobil', 'Sector': 'Energy'}
    }

    return tickers


def get_chart_data(stonk):

    h = stonk.history('6mo').droplevel('symbol')
    x = [date.strftime('%Y-%m-%d') for date in h.index]
    y = h['adjclose'].to_list()

    return x, y


def get_hints_data(stonk, ticker):

    data = stonk.all_modules[ticker]

    city = data['summaryProfile']['city']
    industry = data['summaryProfile']['industry']
    mkt_cap = data['summaryDetail']['marketCap']
    ceo = data['assetProfile']['companyOfficers'][0]['name']

    rev = 0
    for quarter in data['earnings']['financialsChart']['quarterly']:
        rev += quarter['revenue']

    mkt_cap = f'${mkt_cap / 1_000_000_000: .2f}B'
    rev = f'${rev / 1_000_000_000: .2f}B'

    # ceo = ceo.split(' ')[-1]

    return rev, city, industry, mkt_cap, ceo


def data_call(ticker):

    stonk = Ticker(ticker)

    x, y = get_chart_data(stonk)
    rev, city, industry, mkt_cap, ceo = get_hints_data(stonk, ticker)

    return x, y, rev, city, industry, mkt_cap, ceo


if __name__ == '__main__':
    pass
