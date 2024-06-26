# PDF to Word Converter

Convert PDF files to Word documents effortlessly with this web application built using Flask and MongoDB.

## Features

- Upload PDF files and convert them to Word (docx) format.
- Store converted Word documents along with user details (name and mobile number) in a MongoDB database.
- Simple and intuitive user interface.
- Easy setup and deployment.

## Installation

1. Clone the repository:

2. Install dependencies:


3. Set up MongoDB:

   - Create a MongoDB Atlas account (or use an existing one).
   - Create a cluster and obtain the connection string.
   - Replace the MongoDB connection string in `app.py` with your own connection string.

4. Run the application:


Access the application at `http://localhost:5000` in your web browser.

## Usage

1. Open the application in your web browser.
2. Fill in your name and mobile number.
3. Upload a PDF file using the provided form.
4. Click the "Convert" button to convert the PDF to a Word document.
5. The converted Word document will be stored in the database along with your details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

