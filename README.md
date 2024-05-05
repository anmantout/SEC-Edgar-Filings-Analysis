## SEC-Edgar-Filings-Analysis
The project utilizes textual analysis techniques to extract valuable insights from SEC-EDGAR filings. By parsing through the extensive textual content of these filings, including annual reports (Form 10-K) the system identifies key information. Leveraging natural language processing (NLP) algorithms, we extract and analyze textual data to uncover trends, patterns, and sentiments, providing stakeholders with actionable intelligence for informed decision-making. This approach enables investors, analysts, and regulators to gain deeper understanding and valuable insights from the vast amount of textual data available in SEC filings, enhancing transparency, and facilitating better risk management and investment strategies. This project do various textual analyses along with visualization like:
- Summarization of the filings
- Topic Modelling
- Sentiment analysis
For details on the benefits of the specific insights derived from SEC filings, please refer to the [User Benefits of Specific Insights](#user-benefits-of-specific-insights) section.

## Tech Stack

- **Frontend**: React JS- React's extensive ecosystem of libraries and community support provides access to a wide range of tools and resources for frontend development.
- **UI Library**: React Bootstrap- React Bootstrap provides a set of pre-designed components and styles that are easy to integrate into React applications, reducing development time and effort.
- **Backend**: Python, Flask- Flask's simplicity and flexibility make it well-suited for prototyping and rapid development, allowing to focus on implementing business logic and API endpoints efficiently.
- **LLM**: GPT 3.5- GPT (Generative Pre-trained Transformer) is a state-of-the-art natural language processing model that has been pre-trained on vast amounts of text data, enabling it to understand and generate human-like text. GPT's transformer architecture allows it to capture complex patterns and relationships in textual data, making it well-suited for tasks such as text summarization, sentiment analysis, and information extraction.
- **Data Visualization**: Chart.js- Chart.js is a lightweight and versatile JavaScript library for creating interactive and customizable charts and graphs.

## Flowchart of Methodology
![Screenshot 2024-05-05 131205](https://github.com/anmantout/SEC-Edgar-Filings-Analysis/assets/147123118/8a6e2b78-c3a1-40cc-9fa8-92a9b2e3ddfe)

## User Benefits of Specific Insights

1. **Summarization of Filings**:
   - Saves time by providing concise and relevant information from lengthy SEC-EDGAR filings.
   - Enables users to quickly grasp key points without reading through the entire document.

2. **Topic Modelling**:
   - Helps users understand main themes and topics discussed within SEC-EDGAR filings.
   - Categorizes content into distinct topics, providing insights into company focus areas such as financial performance, risk factors, and regulatory compliance.

3. **Sentiment Analysis**:
   - Gauges overall sentiment expressed in SEC-EDGAR filings, indicating confidence, optimism, or concerns regarding the policies.
   - Influences decision-making processes such as investment decisions, risk assessment, and strategic planning.

## Working
Videos are uploaded on the link: https://drive.google.com/drive/folders/1afX7X5q8uB0nSHoUnboLzhyJoGxwjfkf?usp=sharing 
Visualization files are present in frontend folder and analysis using GPT LLM is in backend/app.py 

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/sec-edgar-analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sec-edgar-analysis
    ```

3. Install dependencies using npm or yarn:

    ```bash
    npm install
    # or
    yarn install
    ```

## Running the Application

1. Start the React frontend:

    ```bash
    npm start
    # or
    yarn start
    ```

2. Start the Flask backend:

    ```bash
    cd backend
    flask run
    ```

3. Access the application in your web browser at `http://localhost:3000`.

## Usage

Once the application is running, you can interact with it in your web browser. Enter the desired SEC-EDGAR filing or company name to analyze, and the application will provide insights such as summarization, topic modeling, and sentiment analysis based on the provided filing data.

