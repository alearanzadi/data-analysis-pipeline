from adquisition import load_data
from clean import clean_data





def main():
    data = load_data('./fertility_rate.csv')
    data = clean_data(data)
    print(data)

if __name__ == '__main__': 
    main()