# WebScraperFilter

WebScraperFilter is a Python project that utilizes web scraping techniques, particularly using the requests and BeautifulSoup libraries, to collect data from a target website. It then provides a web interface built with Streamlit for users to filter products based on price and ratings.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/AdArSh-1101/WebScraperFilter.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit web application:

    ```bash
    streamlit run Untitled.py
    ```

4. Access the Streamlit web interface in your browser. You can filter products by specifying price and rating ranges.

## How it works

1. **Web Scraping**: The project uses the `requests` library to send HTTP requests to the target website (in this case, [https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops)) and `BeautifulSoup` for parsing the HTML content of the webpage to extract relevant data such as product name, price, description, and rating. This scraping functionality is implemented in `Untitled.ipynb`.

2. **Data Output**: After scraping, the collected data is stored in CSV format in the file `output.csv`.

3. **Streamlit Application**: The Streamlit application is implemented in `Untitled.py`. This Python script provides a user-friendly web interface for filtering the scraped data based on price and ratings, and displays the filtered results.

## Requirements

- Python 3.x
- Streamlit
- requests
- BeautifulSoup

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

