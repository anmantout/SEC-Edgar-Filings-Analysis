import React, { useState } from 'react';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import Dropdown from 'react-bootstrap/Dropdown';
import axios from 'axios';
import DataVisualization from './Visualization';
import SentimentPieChart from './SentimentPieChart';

const Dashboard = () => {
    const [dropDownHeading1, setDropDownHeading1] = useState('Methods');
    const [dropDownHeading2, setDropDownHeading2] = useState('Sections');
    const [dropDownHeading3, setDropDownHeading3] = useState('Year');
    const [dropDownHeading4, setDropDownHeading4] = useState('Company');
    const [selectedMethod, setSelectedMethod] = useState('');
    const [selectedSection, setSelectedSection] = useState('');
    const [selectedYear, setSelectedYear] = useState('');
    const [selectedCompany, setSelectedCompany] = useState('');
    const [data, setData] = useState('');
    const [visualData, setVisualData]=useState('');
    const [visualDataforSentimentAnalysis, setVisualDataforSentimentAnalysis]=useState('');
    const [loading, setLoading] = useState(false); // State to manage loading status

    const handleDropdown1TitleChange = (newTitle) => {
        setDropDownHeading1(newTitle);
        setSelectedMethod(newTitle);
    };

    const handleDropdown2TitleChange = (newTitle) => {
        setDropDownHeading2(newTitle);
        setSelectedSection(newTitle);
    };

    const handleYearChange = (newTitle) => {
        setDropDownHeading3(newTitle);
        setSelectedYear(newTitle);
    };

    const handleCompanyChange = (newTitle) => {
        setDropDownHeading4(newTitle);
        setSelectedCompany(newTitle);
    };

    const handleSubmit = async () => {
        setLoading(true); // Set loading to true when submitting request
        try {
            const response = await axios.post('http://127.0.0.1:5000/api/analyze', {
                method: selectedMethod,
                section: selectedSection,
                year: selectedYear,
                company: selectedCompany
            });
            console.log(response.data.visualization_data);
            setData(response.data.message);
            if(response.data.visualization_data!='')
            {
                setVisualData(response.data.visualization_data);
                setVisualDataforSentimentAnalysis(JSON.parse(response.data.visualization_data));
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setLoading(false); // Set loading to false when request is complete
        }
    };

    const formattedData = {
        positive: visualDataforSentimentAnalysis[0],
        negative: visualDataforSentimentAnalysis[1],
        neutral: visualDataforSentimentAnalysis[2]
        }

    
    // if(visualDataforSentimentAnalysis!='')
    // {
    //     const numericalData = visualDataforSentimentAnalysis.match(/\d+/g);
    //     formattedData = {
    //     positive: numericalData[0],
    //     negative: numericalData[1],
    //     neutral: numericalData[2]
    //     }
    // }
    
    const handleTryAgain = () => {
        window.location.reload(); // Reload the page
    };

    return (
        <>
            <br />
            <h1 style={{ textAlign: 'center' }}>Dashboard</h1>
            <br />
            <hr />
            <br />
            <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-around' }}>
                <div>
                    <h5 style={{ textAlign: 'center' }}>Text Analysis Method</h5>
                    <DropdownButton id="dropdown-method" title={dropDownHeading1}>
                        <Dropdown.Item onClick={() => handleDropdown1TitleChange("Summarization")}>Summarization</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown1TitleChange("Topic Modelling")}>Topic Modelling</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown1TitleChange("Sentiment Analysis")}>Sentiment Analysis</Dropdown.Item>
                    </DropdownButton>
                </div>
                <div>
                    <h5>Select Filing Section</h5>
                    <DropdownButton id="dropdown-section" title={dropDownHeading2}>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 1. Business Overview")}>Business Overview</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 1. Business Risk Factors")}>Risk Factors</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 1. Business Cyber Security")}>Cyber Security</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 2. Properties")}>Item 2. Properties</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 3. Legal Proceedings")}>Item 3. Legal Proceedings</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 5. Market Registrant")}>Item 5. Market Registrant</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Item 15. Exhibit Financial Statement Schedule")}>Item 15. Exhibit Financial Statement Schedule</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleDropdown2TitleChange("Entire Filing")}>Entire Filing</Dropdown.Item>
                    </DropdownButton>
                </div>
                {/* set year */}
                <div>
                    <h5>Year</h5>
                    <DropdownButton id="dropdown-section" title={dropDownHeading3}>
                        {Array.from({length: 13}, (_, i) => {
                            const year = 2011 + i;
                            return (
                            <Dropdown.Item key={year} onClick={() => handleYearChange(year)}>
                                {year}
                            </Dropdown.Item>
                            );
                        })}
                    </DropdownButton>
                </div>
                <div>
                    <h5>Select Company</h5>
                    <DropdownButton id="dropdown-section" title={dropDownHeading4}>
                        <Dropdown.Item onClick={() => handleCompanyChange("IBM")}>IBM</Dropdown.Item>
                        <Dropdown.Item onClick={() => handleCompanyChange("Mastercard")}>Mastercard</Dropdown.Item>
                    </DropdownButton>
                </div>
            </div>
            <br />
            <div style={{ textAlign: 'center' }}>
                <Button variant="danger" onClick={handleSubmit}>Submit</Button>
            </div>
            <hr />
            <br />
            <div style={{ textAlign: 'center' }}>
                {/* Conditional rendering of loading symbol */}
                {loading && 
                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hourglass-split" viewBox="0 0 16 16">
                        <path d="M2.5 15a.5.5 0 1 1 0-1h1v-1a4.5 4.5 0 0 1 2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 3V2h-1a.5.5 0 0 1 0-1h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 .213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1zm2-13v1c0 .537.12 1.045.337 1.5h6.326c.216-.455.337-.963.337-1.5V2zm3 6.35c0 .701-.478 1.236-1.011 1.492A3.5 3.5 0 0 0 4.5 13s.866-1.299 3-1.48zm1 0v3.17c2.134.181 3 1.48 3 1.48a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351z"/>
                        </svg>
                    </div>}
            </div>
            <br />
            <div className='container'>
                {data}
                <br/>
                <Button variant="secondary" onClick={handleTryAgain}>Try Again</Button>
                <br/>
                {(dropDownHeading1=='Summarization' || dropDownHeading1=='Topic Modelling') && visualData!='' && visualData!==undefined &&
                    <div>
                        <br></br>
                        <hr></hr>
                        <h5>Data Visualization</h5>
                        <DataVisualization data={visualData} />
                        <br/>
                        <br/>
                        <Button variant="secondary" onClick={handleTryAgain}>Try Again</Button>
                    </div>
                }
                {dropDownHeading1=='Sentiment Analysis' && visualData!='' && visualData!==undefined &&
                    <div>
                        <br></br>
                        <hr></hr>
                        <h5>Data Visualization</h5>
                        <SentimentPieChart data={formattedData} />
                        <br/>
                        <br/>
                        <Button variant="secondary" onClick={handleTryAgain}>Try Again</Button>
                    </div>
                }
            </div>
        </>
    );
}

export default Dashboard;
