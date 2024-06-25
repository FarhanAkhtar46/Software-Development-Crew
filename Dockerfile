# # Use the Python 3.11 slim base image
# FROM python:3.11.7

# # Set the working directory in the container
# WORKDIR /app

# COPY requirements.txt ./

# # Install Python dependencies from requirements file
# RUN pip install -r requirements.txt

# COPY . /app

# # This tells Docker to listen on port 80 at runtime. Port 80 is the standard port for HTTP.
# EXPOSE 8501

# # # This command creates a .streamlit directory in the home directory of the container.
# # RUN mkdir ~/.streamlit

# # # This copies your Streamlit configuration file into the .streamlit directory you just created.
# # RUN cp config.toml ~/.streamlit/config.toml

# # # Similar to the previous step, this copies your Streamlit credentials file into the .streamlit directory.
# # # RUN cp credentials.toml ~/.streamlit/credentials.toml

# # # This sets the default command for the container to run the app with Streamlit.
# # ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# # This command tells Streamlit to run your app.py script when the container starts.
# CMD ["python","-m", "streamlit", "run","app.py"]


FROM python:3.11
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py