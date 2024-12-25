# Excalibur-Project
AI project for educational purposes
## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/CalinCezar/Excalibur-Project.git
```

2. Navigate to the project directory

```bash
cd Excalibur-Project
```
3. Create a virtual environemnt

```bash
docker-compose up
```

4. Create a virtual environemnt

```bash
python3 -m venv venv
```

5. Activate the virtual environment
for Linux/Mac
```bash
source venv/bin/activate

```
for Windows
```bash
source venv\Scripts\activate

```
6. Install the dependencies

```bash
pip install -r requirements.txt
```

7. Build the application

```bash
pip install -e .[dev]
```

8. Build the application

```bash
streamlit run ui/app.py
```

9. Navigate to the following URL in your browser and check the documentation and interact with the API

```
http://localhost:8501
```

10. Additionally, you can run the tox check with the following command

```bash
tox
```