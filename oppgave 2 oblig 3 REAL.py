import gspread as gs
import pandas as pd
import altair as alt

gc = gs.api_key("AIzaSyBKrUqkbU3gsEujXEh8N3uQTN7fM0Dpg3I")
sh = gc.open_by_key('1RYN0i4Zx_UETVuYacgaGfnFcv4l9zd9toQTTdkQkj7g')
wsh = sh.worksheet("barnehage1-2aar")
all_values = wsh.get_all_values()

for i, row in enumerate(all_values):
    if '2015' in row:
        header_row_index = i
        break

headers = all_values[header_row_index][1:10]  # Columns B to J
headers = [str(header).strip() for header in headers]

municipality_column_name = all_values[header_row_index][0].strip()
data = [row[0:10] for row in all_values[header_row_index + 1:]]
df = pd.DataFrame(data, columns=[municipality_column_name] + headers)

df.replace('.', pd.NA, inplace=True)
for column in headers:
    df[column] = pd.to_numeric(df[column], errors='coerce')

print("Column Names in DataFrame:", df.columns)
print("Data Preview:")
print(df.head())

df.fillna(0, inplace=True)

# 1. Bar Chart: Visualization for a specific year, e.g., 2023
if '2023' in df.columns:
    try:
        chart_2023 = alt.Chart(df).mark_bar().encode(
            x=alt.X(f'{municipality_column_name}:N', title='Municipality'),
            y=alt.Y('2023:Q', title='Percentage in 2023'),
            tooltip=[municipality_column_name, '2023']
        ).properties(
            title='Kindergarten Enrollment Percentage in 2023 by Municipality',
            width=8000,
            height=4000
        )
        chart_2023.save('kindergarten_percentage_2023.html')
        print("Bar chart saved as 'kindergarten_percentage_2023.html'.")
    except ValueError as e:
        print(f"Error while creating the bar chart: {e}")
else:
    print("Cannot create bar chart because the '2023' column is missing.")

# 2. Line Chart: Average Percentage Over the Years
if all(year in df.columns for year in headers):
    average_per_year = df[headers].mean().reset_index()
    average_per_year.columns = ['Year', 'Average_Percentage']

    try:
        line_chart = alt.Chart(average_per_year).mark_line(point=True).encode(
            x=alt.X('Year:N', title='Year'),
            y=alt.Y('Average_Percentage:Q', title='Average Percentage'),
            tooltip=['Year', 'Average_Percentage']
        ).properties(
            title='Average Percentage of Children Aged 1-2 in Kindergarten (2015-2023)',
            width=6000,
            height=4000
        )
        line_chart.save('average_percentage_over_years.html')
        print("Line chart saved as 'average_percentage_over_years.html'.")
    except ValueError as e:
        print(f"Error while creating the line chart: {e}")
else:
    print("Cannot create line chart because one or more year columns are missing.")

# 3. Heatmap: Municipality Percentages from 2015-2023
if all(year in df.columns for year in headers):
    df_melted = df.melt(id_vars=[municipality_column_name], value_vars=headers,
                        var_name='Year', value_name='Percentage')

    try:
        heatmap = alt.Chart(df_melted).mark_rect().encode(
            x=alt.X('Year:O', title='Year'),
            y=alt.Y(f'{municipality_column_name}:N', title='Municipality'),
            color=alt.Color('Percentage:Q', title='Enrollment Percentage'),
            tooltip=[municipality_column_name, 'Year', 'Percentage']
        ).properties(
            title='Heatmap of Kindergarten Enrollment Percentage (2015-2023)',
            width=8000,
            height=6000
        )
        heatmap.save('kindergarten_enrollment_heatmap.html')
        print("Heatmap saved as 'kindergarten_enrollment_heatmap.html'.")
    except ValueError as e:
        print(f"Error while creating the heatmap: {e}")
else:
    print("Cannot create heatmap because one or more year columns are missing.")

# Debugging: Verify DataFrame after Analysis
print("Final DataFrame Preview:")
print(df.head())

gc = gs.api_key("AIzaSyBKrUqkbU3gsEujXEh8N3uQTN7fM0Dpg3I")
sh = gc.open_by_key('1RYN0i4Zx_UETVuYacgaGfnFcv4l9zd9toQTTdkQkj7g')
wsh = sh.worksheet("barnehage1-2aar")
all_values = wsh.get_all_values()

for i, row in enumerate(all_values):
    if '2015' in row:
        header_row_index = i
        break

# Extract headers
headers = all_values[header_row_index][1:10]  # Columns B to J
headers = [str(header).strip() for header in headers]

# Extract data from rows after headers
data = [row[1:10] for row in all_values[header_row_index + 1:]]

# Create DataFrame
df = pd.DataFrame(data, columns=headers)
df.insert(0, 'Kommune', [row[0] for row in all_values[header_row_index + 1:]])

# Replace '.' with NaN and convert numeric columns to appropriate types
df.replace('.', pd.NA, inplace=True)
for column in headers:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Filtrere vekk irrelevante rader fra DataFrame
df_filtered = df[df['Kommune'].notna() & ~df['Kommune'].str.contains('Database|Ekstern|Intern|region|Kilde|Statistisk|Kontakt|referansekode|Måleenhet|prosent|Målemetode|Offisiell|Sist endret', case=False, na=False)]
df_filtered = df_filtered.reset_index(drop=True)

# Debugging: Check the filtered data
print("Filtered DataFrame Preview:")
print(df_filtered.head())

df_filtered.fillna(float('inf'), inplace=True)

# Oppgave A: Hvilken kommune har hatt den høyeste prosenten av barn i ett- og to-årsalderen i barnehagen i 2023?
highest_2023 = df_filtered[df_filtered['2023'] == df_filtered['2023'][df_filtered['2023'] != float('inf')].max()]
print("\nTask A: Kommune med høyeste prosent i 2023:")
print(highest_2023[['Kommune', '2023']])

# Oppgave B: Hvilken kommune har hatt den laveste prosenten av barn i ett- og to-årsalderen i barnehagen i 2023?
lowest_2023 = df_filtered[df_filtered['2023'] == df_filtered['2023'][df_filtered['2023'] != float('inf')].min()]
print("\nTask B: Kommune med laveste prosent i 2023:")
print(lowest_2023[['Kommune', '2023']])

# Oppgave C: Hvilken kommune har den høyeste gjennomsnittlige prosenten av barn i ett- og to-årsalderen fra 2015 til 2023?
df_filtered['Average_2015_2023'] = df_filtered[headers].replace(float('inf'), pd.NA).mean(axis=1).round(1)
highest_avg = df_filtered[df_filtered['Average_2015_2023'] == df_filtered['Average_2015_2023'].max()]
print("\nTask C: Kommune med høyeste gjennomsnittlige prosent fra 2015 til 2023:")
print(highest_avg[['Kommune', 'Average_2015_2023']])

# Oppgave D: Hvilken kommune har den laveste gjennomsnittlige prosent av barn i ett- og to-årsalderen fra 2015 til 2023?
lowest_avg = df_filtered[df_filtered['Average_2015_2023'] == df_filtered['Average_2015_2023'].min()]
print("\nTask D: Kommune med laveste gjennomsnittlige prosent fra 2015 til 2023:")
print(lowest_avg[['Kommune', 'Average_2015_2023']])

# Oppgave F: Hva er den gjennomsnittlige prosenten for alle kommuner fra et spesifikt år mellom 2015 og 2023?
year = input("\nOppgi et år mellom 2015 og 2023 for å finne gjennomsnittet for alle kommuner: ")
if year in headers:
    average_for_year = df_filtered[year].replace(float('inf'), pd.NA).mean().round(1)
    print(f"Gjennomsnittlig prosent for alle kommuner i {year}: {average_for_year}%")
else:
    print(f"Feil: Året {year} finnes ikke i dataene. Vennligst velg et år mellom 2015 og 2023.")