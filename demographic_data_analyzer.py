import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer el archivo CSV
    df = pd.read_csv("adult.data.csv")

    # 1. Recuento de cada raza
    race_count = df['race'].value_counts()

    # 2. Promedio de edad de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje de personas con Bachelors
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1)

    # 4. Educación avanzada y salario
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. Porcentaje que ganan >50K según educación
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] /
                                   df[higher_education].shape[0]) * 100, 1)

    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] /
                                  df[lower_education].shape[0]) * 100, 1)

    # 6. Mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentaje de personas que trabajan mínimas horas y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
                             num_min_workers.shape[0]) * 100, 1)

    # 8. País con mayor % de personas >50K
    country_earning = (df[df['salary'] == '>50K']['native-country']
                       .value_counts() / df['native-country'].value_counts() * 100)
    highest_earning_country = country_earning.idxmax()
    highest_earning_country_percentage = round(country_earning.max(), 1)

    # 9. Ocupación más común de los ricos en India
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
                         ['occupation'].value_counts().idxmax())

    # Mostrar resultados
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Higher education rich: {higher_education_rich}%")
        print(f"Lower education rich: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Retornar resultados como diccionario (para los tests automáticos)
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
