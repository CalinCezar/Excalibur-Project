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
pip install .

```

8. Run the application

```bash
streamlit run app.py
```

9. Navigate to the following URL in your browser and check the documentation and interact with the API

```
http://localhost:8501
```

10. Additionally, you can run the tox check with the following command

```bash
tox
```

Happy coding! 🎄✨🎁
