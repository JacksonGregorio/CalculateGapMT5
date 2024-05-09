import pandas as pd

def find_high_numbers(df, n):
    return df['<SPREAD>'].nlargest(n)

def find_high_only(df):
    return df['<SPREAD>'].max()

def print_all_csv(df):
    print(df)

def find_high_gap(df):
    high_gap_rows = []
    sum_spread = 0
    previous_spread = df['<SPREAD>'].iloc[0]

    for index, row in df.iterrows():
        if row['<SPREAD>'] > previous_spread:
            high_gap_rows.append(row[['<DATE>', '<TIME>', '<SPREAD>']])
            sum_spread += row['<SPREAD>']
        previous_spread = row['<SPREAD>']

    print("valor do maior gap: ", sum_spread)
    print("gaps usados: ")
    for row in high_gap_rows:
        print(row)

def check_spread_gap(df):
    if '<SPREAD>' not in df.columns:
        print("Error: DataFrame does not have a '<SPREAD>' column.")
        return None, None

    max_sequence = []
    current_sequence = []
    previous_spread = df['<SPREAD>'].iloc[0]

    for spread in df['<SPREAD>'].iloc[1:]:
        if spread >= previous_spread:
            current_sequence.append(spread)
        else:
            if sum(current_sequence) > sum(max_sequence):
                max_sequence = current_sequence
            current_sequence = []
        previous_spread = spread

    if sum(current_sequence) > sum(max_sequence):
        max_sequence = current_sequence

    print(f'Maior soma de sequência: {sum(max_sequence)}')
    print(f'<SPREAD> values in the longest increasing sequence: {max_sequence}')

def main():
    df = pd.read_csv('csv/importmt5Virgula-1.csv')

    while True:
        choice = input("Digite de 1 a 5 ou sair: ")

        if choice == '1':
            n = int(input("Digite o numero de valores a retorna: "))
            result = find_high_numbers(df, n)
            print(result)
        elif choice == '2':
            result = find_high_only(df)
            print(result)
        elif choice == '3':
            print_all_csv(df)
        elif choice == '4':
            find_high_gap(df)
        elif choice == '5':
            check_spread_gap(df)
        elif choice.lower() == 'sair':
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()