# Excalibur-Project

The Excalibur Project is a document processing and question generation system that processes PDF documents, stores extracted content in a vector database, and generates relevant questions based on user queries. In addition to these capabilities, the system includes features for schedule creation, data analysis, data training, and prediction—providing comprehensive tools to extract insights, predict student succes, and generate customized schedules based on document content

## Features
- Schedule Creation
- Data Analysis
- Data Prediction
- Data visualization
- PDF text extraction and cleaning
- Document embedding generation
- Vector database storage using Weaviate
- Question generation using T5 model
- Streamlit web interface

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/CalinCezar/Excalibur-Project.git
```

2. Navigate to the project directory

```bash
cd Excalibur-Project
```

3. There find the `.env.template ` file and dublicate it

Open the `.env` file and replace the placeholder value with your actual key

4. Run docker container for Weaviate

```bash
docker-compose up
```

5. Create a virtual environemnt

```bash
python3 -m venv venv
```

6. Activate the virtual environment
for Linux/Mac
```bash
source venv/bin/activate

```
for Windows
```bash
venv\Scripts\activate

```
7. Install the dependencies

```bash
pip install -r requirements.txt
```

8. Build the application

```bash
pip install -e .[dev]
```

9. Run the application

```bash
streamlit run app.py
```

10. Navigate to the following URL in your browser and check the documentation and interact with the API

```
http://localhost:8501
```

11. Additionally, you can run the tox check with the following command

```bash
tox
```

Happy coding! 🎄✨🎁
