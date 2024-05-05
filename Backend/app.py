from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
import json
from g4f.client import Client

app = Flask(__name__)
CORS(app) 
client = Client()

#path links
ibm_sections_file="C:/Users/Owner/Filings_Analysis/assignment/public/Data/keywords_ibm_sectionwise.json"
mc_sections_file="C:/Users/Owner/Filings_Analysis/assignment/public/Data/keywords_mc_sectionwise.json"
ibm_entire_file="C:/Users/Owner/Filings_Analysis/assignment/public/Data/keywords_ibm_entire.json"
mc_entire_file="C:/Users/Owner/Filings_Analysis/assignment/public/Data/keywords_mc_entire.json"

def generate_response(message):
    # Use the completion endpoint of the GPT API
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )

    response = ""
    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content:
                response += chunk.choices[0].delta.content
    return response

@app.route('/api/analyze', methods=['GET', 'POST'])
def analyze():
    data = request.get_json()
    selected_method = data.get('method')
    selected_section = data.get('section')
    selected_year=data.get('year')
    selected_company=data.get('company')

    #read data from file
    with open(ibm_sections_file, 'r') as file:
        ibm_sections = json.load(file)

    with open(ibm_entire_file, 'r') as file:
        ibm_entire = json.load(file)

    with open(mc_sections_file, 'r') as file:
        mc_sections = json.load(file)

    with open(mc_entire_file, 'r') as file:
        mc_entire = json.load(file)

    print(selected_method,selected_company,selected_section,selected_year)
    # Summarization of Sections
    if selected_method=='Summarization':
        if selected_section=='Item 1. Business Overview':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    # print(item['Year'],str(selected_year).strip(),item['Year']==str(selected_year).strip())
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 1. Business Risk Factors':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 1. Business Cyber Security':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 2. Properties':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["property"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["property"])})
        elif selected_section=='Item 3. Legal Proceedings':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["legal proceedings"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["legal proceedings"])})
        elif selected_section=='Item 5. Market Registrant':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('extract numerical data and store it in dictionary format. Dont give code. Only give dictionery. Directly give the output.'+ item["market registrant"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text in textual format. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('extract numerical data and store it in dictionary format. Only give dictionery. Dont give code. Directly give the output.'+ item["market registrant"])})
        elif selected_section=='Item 15. Exhibit Financial Statement Schedule':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text in textual format. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"])})
        elif selected_section=='Entire Filing':
            if selected_company=='Mastercard':
                year_array=mc_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    print(year)
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ mc_entire[idx])})
            else:
                year_array=ibm_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Summarize the text. Dont give code. Directly give the output.'+ ibm_entire[idx])})
            
    #topic modelling
    elif selected_method=='Topic Modelling':
        if selected_section=='Item 1. Business Overview':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 1. Business Risk Factors':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling on the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling on the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 1. Business Cyber Security':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling on the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling on the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"])})
        elif selected_section=='Item 2. Properties':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["property"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["property"])})
        elif selected_section=='Item 3. Legal Proceedings':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["legal proceedings"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["legal proceedings"])})
        elif selected_section=='Item 5. Market Registrant':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('extract numerical data and store it in dictionary format. Dont give code. Directly give the output.'+ item["market registrant"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('extract numerical data and store it in dictionary format. Dont give code. Directly give the output.'+ item["market registrant"])})
        elif selected_section=='Item 15. Exhibit Financial Statement Schedule':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"])})
        elif selected_section=='Entire Filing':
            if selected_company=='Mastercard':
                year_array=mc_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ mc_entire[idx])})
            else:
                year_array=ibm_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Perform topic modelling. Dont give code. Directly give the output.'+ ibm_entire[idx])})
            
    #sentiment analysis
    elif selected_method=='Sentiment Analysis':
        if selected_section=='Item 1. Business Overview':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c]'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["Business"])})
        elif selected_section=='Item 1. Business Risk Factors':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis on the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis on the risk factors mentioned in the text. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["Business"])})
        elif selected_section=='Item 1. Business Cyber Security':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis on the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["Business"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis on the cyber security information mentioned in the text. Dont give code. Directly give the output.'+ item["Business"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["Business"])})
        elif selected_section=='Item 2. Properties':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["property"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["property"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["property"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["property"])})
        elif selected_section=='Item 3. Legal Proceedings':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["legal proceedings"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["legal proceedings"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["legal proceedings"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["legal proceedings"])})
        elif selected_section=='Item 5. Market Registrant':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["market registrant"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["market registrant"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["market registrant"])})
        elif selected_section=='Item 15. Exhibit Financial Statement Schedule':
            if selected_company=='Mastercard':
                for item in mc_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["exhibit financial statement schedule"])})
            else:
                for item in ibm_sections:
                    if (item['Year']).strip()==str(selected_year).strip():
                        return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ item["exhibit financial statement schedule"]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ item["exhibit financial statement schedule"])})
        elif selected_section=='Entire Filing':
            if selected_company=='Mastercard':
                year_array=mc_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ mc_entire[idx]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ mc_entire[idx])})
            else:
                year_array=ibm_entire[-1]
                year_arr_updated=[]
                for year in year_array:
                    year_arr_updated.append(int(year.strip()))
                idx=year_arr_updated.index(selected_year)
                return jsonify({'message': generate_response('Perform Sentiment Analysis. Dont give code. Directly give the output.'+ ibm_entire[idx]),'visualization_data':generate_response('give percentage of positive, negative and neutral sentiments from the data in list format.Dont give code. Directly give the output only list of numbers like [a,b,c].'+ ibm_entire[idx])})

    return jsonify({
        'message': 'Some error occured',
    })

if __name__ == '__main__':
    app.run(debug=True)
