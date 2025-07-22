import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am Ajay Singh, a certified Data Analyst. I have experience working with Power BI, Zoho Analytics, "
           "and SQL for data visualization and analysis. I also completed an internship at Null Class Pvt. Ltd., "
           "where I worked on Twitter data analytics and created interactive dashboards.")
engine.runAndWait()