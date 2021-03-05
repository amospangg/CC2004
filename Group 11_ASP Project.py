import matplotlib.pyplot as plt
import numpy as np

def main():
    import pandas as pd
    countries = pd.read_csv('IMVA.csv') # This is to read the datafile.
    countries['Israel'] = pd.to_numeric(countries['Israel'], errors='coerce').fillna(0) # This is to turn all Israel NaN to 0

    # These codes are to sum up the data from each country.
    visitors_country = [np.sum(countries['Brunei Darussalam']), np.sum(countries['Indonesia']),
                        np.sum(countries['Malaysia']), np.sum(countries['Myanmar']), np.sum(countries['Philippines']),
                        np.sum(countries['Thailand']), np.sum(countries['Vietnam']), np.sum(countries['China']),
                        np.sum(countries['Hong Kong SAR']), np.sum(countries['Taiwan']), np.sum(countries['Japan']),
                        np.sum(countries['South Korea']), np.sum(countries['Bangladesh']), np.sum(countries['India']),
                        np.sum(countries['Pakistan']), np.sum(countries['Sri Lanka']), np.sum(countries['Iran']),
                        np.sum(countries['Israel']), np.sum(countries['Kuwait']), np.sum(countries['Saudi Arabia']),
                        np.sum(countries['United Arab Emirates'])]
    # This is to array the summed up data
    visitors = np.array(visitors_country)

    import pandas as pd
    # We put all the new data into a new dataframe
    data = {'Country': ['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines',
                        'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan',
                        'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran',
                        'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates'],
            'Visitors': [visitors[0], visitors[1], visitors[2], visitors[3], visitors[4], visitors[5], visitors[6],
                         visitors[7], visitors[8], visitors[9], visitors[10], visitors[11], visitors[12], visitors[13],
                         visitors[14], visitors[15], visitors[16], visitors[17], visitors[18], visitors[19],
                         visitors[20]]}
    df = pd.DataFrame(data)

    # Sorts out the data from highest to lowest
    df.sort_values(by=['Visitors'], inplace=True, ascending=True)

    # This is to plot the graph for All Countries
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 5))
    plt.ticklabel_format(style='plain')
    plt.xticks(range(len(df['Visitors'])), df['Country'], rotation=30, ha='right')
    plt.xlabel('Countries')
    plt.ylabel('Visitors')
    plt.title('All countries visitors over a ten year period')
    plt.bar(range(len(df['Visitors'])), df['Visitors'])

    plt.show()

    # Takes the top 3 countries data
    top3 = df.tail(3)
    # Resets the index of the top 3 countries
    top3 = top3.reset_index(drop=True)

    # Plots out the graph for the top 3 countries
    import matplotlib.pyplot as plt
    plt.ticklabel_format(style='plain')
    plt.xticks(range(len(top3['Visitors'])), top3['Country'])
    plt.xlabel('Countries')
    plt.ylabel('Visitors')
    plt.title('Top 3 countries visitors over a ten year period')
    plt.bar(range(len(top3['Visitors'])), top3['Visitors'])

    plt.show()

if __name__ == '__main__':
    main()

# Unit Test