# CSV Data Editor

A lightweight, web-based CSV editor built using Python and [Streamlit](https://streamlit.io/). This tool lets you easily upload, view, and edit CSV files in your browser. Perfect for quick data clean-up, analysis, or making minor adjustments without the need for a full spreadsheet application.

## Features

- **CSV Upload & Preview:** Load your CSV file with a simple file uploader and view its contents in a clean, interactive table.
- **Inline Editing:** Modify cell values directly in the table for fast data editing.
- **Data Export:** Download your updated CSV file once you’re done editing.
- **User-Friendly Interface:** An intuitive design that makes editing CSV data quick and straightforward.
- **Built with Streamlit:** Leverage the power of Python and Streamlit to create a dynamic web application.

## Installation

To run the CSV Data Editor locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sirnino/csv-data-editor.git
   cd csv-data-editor
   ```

2. **Set Up a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   Ensure you have Python 3.7+ installed, then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Launch the Streamlit app with:

   ```bash
   streamlit run main.py
   ```

   The app should now open in your default browser, or you can navigate to the provided local URL.

## Usage

1. **Open the Application:** Navigate to the URL where the app is running (e.g., [http://localhost:8501](http://localhost:8501)).
2. **Upload a CSV File:** Use the file uploader widget to select your CSV file.
3. **Edit Data:** Once loaded, click on any cell to edit its value.
4. **Download Changes:** After editing, use the provided download button to export the updated CSV file.

## Project Structure

The project structure might look like this:

```
csv-data-editor/
├── main.py             # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── utils/              # A folder containing files with utility methods
```

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Open a pull request.

Please ensure your code adheres to the project’s style guidelines and includes appropriate tests.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the framework that makes it easy to build and share data apps.
- Inspiration from the open-source community for creating simple yet powerful tools for data manipulation.