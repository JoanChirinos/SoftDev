#Team Pupps -- Joan Chirinos, Susan Lin
#SoftDev pd08
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template, request, session, url_for, redirect
import urllib.request, json
app = Flask(__name__) #create instance of class Flask

@app.route('/')
def root():
    URL_STUB = 'http://api.population.io:80/1.0'

    countries = '/countries/'
    wpr = '/wp-rank/2001-03-02/male/United%20States/today/'
    life_expectancy = '/life-expectancy/total/male/United%20States/2001-03-02/'
    population = '/population/2001/United%20States/17/'
    mortality = '/mortality-distribution/United%20States/male/17y9m/today/'

    countries_response = urllib.request.urlopen(URL_STUB + countries)
    wpr_response = urllib.request.urlopen(URL_STUB + wpr)
    life_expectancy_response = urllib.request.urlopen(URL_STUB + life_expectancy)
    population_response = urllib.request.urlopen(URL_STUB + population)
    mortality_response =urllib.request.urlopen(URL_STUB + mortality)

    ARGUMENT_DICT = {}

    countries_dict = json.loads(countries_response.read())
    print('COUNTRIES DICT:\n{}\n\n\n\n'.format(countries_dict))
    ARGUMENT_DICT['countries'] = countries_dict['countries']

    wpr = json.loads(wpr_response.read())
    print('WPR DICT:\n{}\n\n\n\n'.format(wpr))
    ARGUMENT_DICT['wpr_sex'] = wpr['sex']
    ARGUMENT_DICT['wpr_country'] = wpr['country']
    ARGUMENT_DICT['wpr_dob'] = wpr['dob']
    ARGUMENT_DICT['wpr_rank'] = wpr['rank']

    le = json.loads(life_expectancy_response.read())
    print('LE DICT:\n{}\n\n\n\n'.format(le))
    ARGUMENT_DICT['le_sex'] = le['sex']
    ARGUMENT_DICT['le_country'] = le['country']
    ARGUMENT_DICT['le_dob'] = le['dob']
    ARGUMENT_DICT['le_le'] = le['total_life_expectancy']

    pop_dict = json.loads(population_response.read())[0]
    ARGUMENT_DICT['pop_dict'] = pop_dict
    print('POP DICT:\n{}\n\n\n\n'.format(pop_dict))

    mortality_dict = json.loads(mortality_response.read())
    mortality_list = mortality_dict['mortality_distribution']
    ARGUMENT_DICT['mortality_list'] = mortality_list
    ARGUMENT_DICT['m_age'] = '17y, 9m'
    ARGUMENT_DICT['m_country'] = 'United States'
    ARGUMENT_DICT['m_sex'] = 'Male'
    print('MORTALITY LIST:\n{}\n\n\n\n'.format(mortality_list))

    return render_template('base.html', **ARGUMENT_DICT)


if __name__ == '__main__':
    app.debug = True
    app.run()
